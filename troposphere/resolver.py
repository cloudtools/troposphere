class Resolver(object):

    def _resolve_references_list(self, L):
        for i, elem in enumerate(L):
            L[i] = self._resolve_references_recursively(elem)

    def _resolve_references_dict(self, d):
        for k, v in d.iteritems():
            d[k] = self._resolve_references_recursively(v)

    def _resolve_references_recursively(self, o):
        from troposphere import Ref, BaseAWSObject, Parameter
        if isinstance(o, (BaseAWSObject, Parameter)):
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
        return o

    def _resolve_references_aws_object(self, d):
        self._resolve_references_recursively(d.properties)

    def resolve_references(self, resource):
        self._resolve_references_aws_object(resource)
