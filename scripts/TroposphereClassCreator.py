#!/usr/bin/env python

from jinja2 import Environment, FileSystemLoader
import os
import json
import re


class TroposphereClassCreator(object):
    """
    Creates python classes for AWS instances in an easy to use tree structure
    """

    def __init__(self, baseDirectory, instances):
        self.baseDirectory = baseDirectory
        self.instances = instances

    def makeClasses(self):
        hasSecurityGroup = False
        for instance in self.instances:
            for name in self.instances[instance]:
                # Security Groups will be handled later in the process
                if self.isSecurityGroupType(name):
                    hasSecurityGroup = True
                    continue
                for node in self.instances[instance][name]:
                    baseDir = self.baseDirectory + '/'
                    nameDir = baseDir + name + '/'
                    self.makePythonDirectoryIfNecessary(baseDir)
                    self.makePythonDirectoryIfNecessary(nameDir)
                    nodeParams = self.getParamsFromNode(name, node)
                    className = nodeParams['class_name'] + '.py'
                    output = self.getDataFromTemplate('base', nodeParams)
                    self.makeFile(nameDir, className, output)
        # if security groups exist, handle them now
        if hasSecurityGroup:
            self.makeSecurityGroups()

    def makeSecurityGroups(self):
        securityGroups = self.initSecurityGroups()
        securityGroups = self.initIngressRules(securityGroups)
        securityGroups = self.initEgressRules(securityGroups)

        baseDir = self.baseDirectory + '/'
        securityGroupDir = baseDir + 'SecurityGroups/'

        self.makePythonDirectoryIfNecessary(securityGroupDir)

        ingressParent = self.getDataFromTemplate('ingressParent')
        ingressFile = 'SecurityGroupIngress.py'
        self.makeFile(securityGroupDir, ingressFile, ingressParent)
        egressParent = self.getDataFromTemplate('egressParent')
        egressFile = 'SecurityGroupEgress.py'
        self.makeFile(securityGroupDir, egressFile, egressParent)

        for node in self.getAWSInstanceNameContent('ec2', 'SecurityGroup'):
            params = self.getParamsFromNode('SecurityGroup', node)
            className = params['class_name']
            ingressRules = securityGroups[className]['ingressRules']
            params['egress_rules'] = securityGroups[className]['egressRules']

            # SecurityGroups may not contain more than 50 rules each.
            counter = 1
            while len(ingressRules) > 50:
                counter += 1
                params['class_name'] = className + str(counter)
                classFile = params['class_name'] + '.py'
                params['ingress_rules'] = ingressRules[:50]
                parsedOutput = self.getDataFromTemplate('securityGroup',
                                                        params)
                self.makeFile(securityGroupDir, classFile, parsedOutput)
                del ingressRules[:50]

            # At this point, we have less than 50 rules. Create the file as is.
            params['class_name'] = className
            classFile = className + '.py'
            params['ingress_rules'] = ingressRules
            parsedOutput = self.getDataFromTemplate('securityGroup', params)
            self.makeFile(securityGroupDir, classFile, parsedOutput)

    def initIngressRules(self, securityGroups):
        ingressRuleKey = 'ingressRules'
        ingressName = 'SecurityGroupIngress'
        ingressNodes = self.getAWSInstanceNameContent('ec2', ingressName)
        for node in ingressNodes:
            allParams = self.getParamList(node)
            securityGroupName = self.getValidSecurityGroupName(allParams)
            ingressRule = self.getIngressRule(allParams)
            ingressRules = securityGroups[securityGroupName][ingressRuleKey]
            if ingressRule not in ingressRules:
                ingressRules.append(ingressRule)
        return securityGroups

    def initEgressRules(self, securityGroups):
        egressRuleKey = 'egressRules'
        egressName = 'SecurityGroupEgress'
        egressNodes = self.getAWSInstanceNameContent('ec2', egressName)
        for node in egressNodes:
            allParams = self.getParamList(node)
            securityGroupName = self.getValidSecurityGroupName(allParams)
            egressRule = self.getEgressRule(allParams)
            egressRules = securityGroups[securityGroupName][egressRuleKey]
            if egressRule not in egressRules:
                egressRules.append(egressRule)
        return securityGroups

    def getEgressRule(self, nodeList):
        ipProtocol = self.findStringInList('IpProtocol', nodeList)
        cidrIP = self.findStringInList('CidrIp', nodeList)
        baseString = 'securityGroupEgress.addRule('
        endString = ')'

        ruleParams = "ipProtocol='{}', cidrIp='{}'".format(ipProtocol, cidrIP)
        return baseString + ruleParams + endString

    def getValidSecurityGroupName(self, params):
        name = self.findStringInList('GroupId', params)
        if name == '':
            name = self.findStringInList('GroupName', params)
        if name == '':
            name = self.findStringInList('GroupId', params, '(', ')')
        if name == '':
            name = self.findStringInList('GroupName', params, '(', ')')
        return name

    def getIngressRule(self, nodeList):
        ipProtocol = self.findStringInList('IpProtocol', nodeList)
        fromPort = self.findStringInList('FromPort', nodeList)
        toPort = self.findStringInList('ToPort', nodeList)
        cidrIP = self.findStringInList('CidrIp', nodeList)
        baseString = 'securityGroupIngress.addRule('
        endString = ')'

        ruleParams = "ipProtocol='{0}', fromPort='{1}', toPort='{2}', " \
                     "cidrIp='{3}'"
        formattedRules = ruleParams.format(
            ipProtocol, fromPort, toPort, cidrIP)
        return baseString + formattedRules + endString

    def findStringInList(self, string, theList,
                         lowerBound='"', upperBound='"'):
        line = ''
        for item in theList:
            if string in item:
                return self.getValueInDelimiter(item.strip(),
                                                lowerBound, upperBound)
        return line

    def getValueInDelimiter(self, string, lowerBound='"', upperBound='"'):
        try:
            regEx = r"\{0}(.*)\{1}".format(lowerBound, upperBound)
            matchedName = re.search(regEx, string)
            return matchedName.group(1)
        except:
            return ''

    def initSecurityGroups(self):
        SecurityGroups = {}
        awsName = 'SecurityGroup'
        securityGroupNodes = self.getAWSInstanceNameContent('ec2', awsName)
        for node in securityGroupNodes:
            paramList = self.getParamList(node)
            name = self.getName(paramList[1])
            if name not in SecurityGroups:
                SecurityGroups[name] = {'properties': paramList[1:-1],
                                        'ingressRules': [], 'egressRules': []}
        return SecurityGroups

    def makePythonDirectoryIfNecessary(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
            self.makeInitPythonFile(directory)

    def makeInitPythonFile(self, directory):
        self.makeFile(directory, '__init__.py')

    def makeFile(self, directory, fileName, contents=' '):
        with open(directory + fileName, 'w') as newFile:
            newFile.write(contents)

    def getParamsFromNode(self, instance, node):
        paramList = self.getParamList(node)
        method = self.getMethod(paramList[0])
        name = self.getName(paramList[1])
        properties = paramList[1:-1]
        return {'template_method': method, 'instance_type': instance,
                'class_name': name, 'properties': properties}

    def getParamList(self, node):
        return node.strip().split('\n')

    def getProperties(self, paramList):
        return '\n'.join(paramList)

    def getName(self, secondLineOfNode):
        return secondLineOfNode.split(',')[0].strip()[1:-1]

    def getMethod(self, firstLineOfNode):
        methodLine = firstLineOfNode.split('=')[1].strip()
        return methodLine.split('(')[0]

    def isSecurityGroupType(self, name):
        securityName = 'SecurityGroup'
        ingressName = 'SecurityGroupIngress'
        egressName = 'SecurityGroupEgress'
        securityGroupTypes = [securityName, ingressName, egressName]
        return name in securityGroupTypes

    def getDataFromTemplate(self, fileName, dictionary={}):
        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template(fileName)
        return template.render(dictionary)

    def getAWSInstances(self):
        return self.instances

    def getAWSInstanceNames(self, awsInstance):
        try:
            return self.dictionary[awsInstance]
        except:
            print 'Failed to get: {0}'.format(awsInstance)

    def printAWSInstances(self):
        for x in self.instances:
            print x

    def printAWSInstanceNames(self, instance):
        for x in self.instances[instance]:
            print x

    def printAWSInstanceNameContent(self, instance, name):
        for x in self.instances[instance][name]:
            print x

    def getAWSInstanceNameContent(self, instance, name):
        try:
            return self.instances[instance][name]
        except:
            print 'Failed to get: {0}/{1}'.format(instance, name)
