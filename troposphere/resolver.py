import re

ref_id_re = re.compile(r'_Ref\(id=(\d+)\)')
ref_name_re = re.compile(r'_Ref\(name=([^)]+)\)')
getatt_re = re.compile(r'_GetAtt\((\d+),(\w+)\)')
format_re = re.compile(r'_BaseAWSObject\(id=(\d+)\)')


class Resolver(object):

    def __init__(self, template):
        self.template = template
        self._init_known()

    def _resolve_references_list(self, l):
        for i, elem in enumerate(l):
            l[i] = self._resolve_references_recursively(elem)

    def _resolve_references_dict(self, d):
        for k, v in d.iteritems():
            d[k] = self._resolve_references_recursively(v)

    def _resolve_references_string(self, s):
        from troposphere import Ref, GetAtt, AWSObject, Parameter, Join

        m = ref_id_re.match(s)
        if m:
            i = m.group(1)
            i = int(m.group(1))
            return Ref(self.known[i][1])

        m = ref_name_re.match(s)
        if m:
            name = m.group(1)
            return Ref(name)

        m = getatt_re.match(s)
        if m:
            i, a = m.groups()
            i = int(i)
            return GetAtt(self.known[i][1], a)

        parts = format_re.split(s)
        if len(parts) != 1:
            res = []
            for text, i in zip(parts[::2], parts[1::2]):
                if text:
                    res.append(text)
                i = int(i)
                res.append(self.known[i][1])
            if parts[-1]:
                res.append(parts[-1])
            return Join("", res)

        return None

    def _resolve_references_recursively(self, o):
        from troposphere import Ref, GetAtt, AWSObject, Parameter
        if isinstance(o, (AWSObject, Parameter)):
            r = Ref(o)
            return self._resolve_references_recursively(r)
        if hasattr(o, 'JSONrepr'):
            return self._resolve_references_recursively(o.JSONrepr())
        if isinstance(o, dict):
            self._resolve_references_dict(o)
            return o
        if isinstance(o, list):
            self._resolve_references_list(o)
            return o
        if isinstance(o, basestring):
            _resolved = self._resolve_references_string(o)
            if _resolved:
                return self._resolve_references_recursively(_resolved)
            else:
                return o
        return o

    def _resolve_references_aws_object(self, d):
        self._resolve_references_recursively(d.properties)

    def _init_known(self):
        known = dict((id(v), (k, v))
            for k, v in self.template.parameters.iteritems())
        known.update(dict((id(v), (k, v))
            for k, v in self.template.resources.iteritems()))

        self.known = known

    def resolve_references(self):
        for k, v in self.template.resources.iteritems():
            self._resolve_references_aws_object(v)
        for k, v in self.template.outputs.iteritems():
            self._resolve_references_aws_object(v)
