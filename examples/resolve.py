from troposphere import Ref, Template
from troposphere.resolver import Resolver
from troposphere.ec2 import Instance

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

class Resource(object):
    def JSONrepr(self):
        return {'Type':'Resource', 'id': id(self)}

o1 = Resource()
o2 = Resource()
i = Instance('i', ImageId='ami-deadbeef')
known = {id(o1): 'o1', id(o2): 'o2', id(i): 'i'}

all = [
        {"1":o1, "2":o2},
        {"1":o1, "2":[o2, o1]},
        [o1, o2],
        {"3":["",[o1, o2]]},
        {"4": "_Ref(%s)" % id(o1)},
        {"5": ["", ["_Ref(%s)" % id(o1)]]},
        "{}".format(i),
        ]
resolver = Resolver()
for i in all:
    print bcolors.OKBLUE + str(i) + bcolors.ENDC
    resolve_references_recursively(known, i)
    print bcolors.OKGREEN + str(i) + bcolors.ENDC
