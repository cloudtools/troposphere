"""Intrinsic template functions

Documentation: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-conditions.html
"""

from __future__ import annotations  # Needed for self-reference of classes as __init__ type-annotation!
from typing import Dict, Any, Union, List, TypeVar


class IntrinsicFunction():
    """Base intrinsic function"""

    def __init__(self, key: str, content: Any) -> None:
        self._key: str = key
        self._content: Any = content

    def to_dict(self) -> Dict:
        if isinstance(self._content, IntrinsicFunction):
            return {self._key: self._content.to_dict()}
        elif isinstance(self._content, list):
            # Call to_dict() on all functions in list
            outlist = [x.to_dict() if isinstance(x, IntrinsicFunction) else x for x in self._content]
            # Call to_dict() on all items of lists in list
            outlist = [[x.to_dict() if isinstance(x, IntrinsicFunction) else x for x in sublist] if isinstance(sublist, list) else sublist for sublist in outlist]
            return {self._key: outlist}
        else:
            return {self._key: self._content}


class FnBase64(IntrinsicFunction):
    def __init__(self, value_to_encode: Union[str, IntrinsicFunction]):
        super(FnBase64, self).__init__("Fn::Base64", value_to_encode)


class FnCidr(IntrinsicFunction):
    def __init__(self, ip_block: Union[str, FnSelect, Ref], count: Union[int, FnSelect, Ref],
                 cidr_bits: Union[int, FnSelect, Ref]):
        if isinstance(count, int) and not 1 <= count <= 256:
            raise ValueError(f"Count must be between 1 and 256, is: {count}")
        # TODO: Further check on cidr_bits? Needs to distinguish between v4/v6

        super(FnCidr, self).__init__("Fn::Cidr", [ip_block, count, cidr_bits])


class FnFindInMap(IntrinsicFunction):
    def __init__(self, map_name: Union[str, FnFindInMap], top_level_key: Union[str, FnFindInMap],
                 second_level_key: Union[str, FnFindInMap]):
        super(FnFindInMap, self).__init__("Fn::FindInMap", [map_name, top_level_key, second_level_key])


class FnGetAtt(IntrinsicFunction):
    def __init__(self, logical_name_of_resource: str, attribute_name: Union[str, Ref]):
        super(FnGetAtt, self).__init__("Fn::GetAtt", [logical_name_of_resource, attribute_name])


class FnGetAZs(IntrinsicFunction):
    def __init__(self, region: Union[str, Ref]):
        super(FnGetAZs, self).__init__("Fn::GetAZs", region)


class FnImportValue(IntrinsicFunction):
    def __init__(self, shared_value_to_import: Union[
        str, FnBase64, FnFindInMap, FnIf, FnJoin, FnSelect, FnSplit, FnSub, Ref]):
        super(FnImportValue, self).__init__("Fn::ImportValue", shared_value_to_import)


class FnJoin(IntrinsicFunction):
    def __init__(self, delimiter: str, values: List[Union[
        str, FnBase64, FnFindInMap, FnGetAtt, FnGetAZs, FnIf, FnImportValue, FnJoin, FnSelect, FnSplit, FnSub, Ref]]):
        super(FnJoin, self).__init__("Fn::Join", [delimiter, values])


class FnSelect(IntrinsicFunction):
    def __init__(self, index: Union[int, FnFindInMap, Ref], list_of_objects: List[Union[
        str, int, float, dict, list, bool, FnFindInMap, FnGetAtt, FnGetAZs, FnIf, FnSplit]]):
        super(FnSelect, self).__init__("Fn::Select", [index, list_of_objects])


class Ref(IntrinsicFunction):
    def __init__(self, logical_name: Union[str, FnSelect, Ref]):
        super(Ref, self).__init__("Ref", logical_name)


class FnIf(IntrinsicFunction):
    def __init__(self, condition_name: str, value_if_true: Any, value_if_false: Any):
        super(FnIf, self).__init__("Fn::If", [condition_name, value_if_true, value_if_false])


substitution_type = TypeVar("substitution_type", str, FnBase64, FnFindInMap, FnGetAtt, FnGetAZs, FnIf,
                            FnImportValue, FnJoin, FnSelect, Ref)


class FnSub(IntrinsicFunction):
    def __init__(self, string: str, substitutions: Dict[substitution_type, substitution_type] = None):
        if substitutions is None:
            super(FnSub, self).__init__("Fn::Sub", string)
        else:
            super(FnSub, self).__init__("Fn::Sub", [string, substitutions])


class FnSplit(IntrinsicFunction):
    def __init__(self, delimiter: str, source_string: Union[
        str, FnBase64, FnFindInMap, FnGetAtt, FnGetAZs, FnIf, FnImportValue, FnJoin, FnSelect, FnSub, Ref]):
        super(FnSplit, self).__init__("Fn::Split", [delimiter, source_string])


class FnTransform(IntrinsicFunction):
    def __init__(self, macro_name: str, parameters: Dict[str, str]):
        super(FnTransform, self).__init__("Fn::Transform", {"Name": macro_name, "Parameters": parameters})


class FnAnd(IntrinsicFunction):
    def __init__(self, conditions: List[Union[FnFindInMap, Ref, FnAnd, FnEquals, FnIf, FnNot, FnOr]]):
        super(FnAnd, self).__init__("Fn::And", conditions)


class FnEquals(IntrinsicFunction):
    def __init__(self, value1: Union[FnFindInMap, Ref, FnAnd, FnEquals, FnIf, FnNot, FnOr],
                 value2: Union[FnFindInMap, Ref, FnAnd, FnEquals, FnIf, FnNot, FnOr]):
        super(FnEquals, self).__init__("Fn::Equals", [value1, value2])


class FnNot(IntrinsicFunction):
    def __init__(self, condition: Union[FnFindInMap, Ref, FnAnd, FnEquals, FnIf, FnNot, FnOr]):
        super(FnNot, self).__init__("Fn::Not", [condition])


class FnOr(IntrinsicFunction):
    def __init__(self, conditions: List[Union[FnFindInMap, Ref, FnAnd, FnEquals, FnIf, FnNot, FnOr]]):
        super(FnOr, self).__init__("Fn::Or", conditions)
