# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject
from . import AWSProperty
from . import Tags
from . import PropsDictType
from typing import List


class Namespace(AWSObject):
    resource_type: str

    def __init__(
        self,
        title,
        AdminUserPassword:str=...,
        AdminUsername:str=...,
        DbName:str=...,
        DefaultIamRoleArn:str=...,
        FinalSnapshotName:str=...,
        FinalSnapshotRetentionPeriod:int=...,
        IamRoles:List[str]=...,
        KmsKeyId:str=...,
        LogExports:List[str]=...,
        NamespaceName:str=...,
        Tags:Tags=...,
    ) -> None: ...

    AdminUserPassword: str
    AdminUsername: str
    DbName: str
    DefaultIamRoleArn: str
    FinalSnapshotName: str
    FinalSnapshotRetentionPeriod: int
    IamRoles: List[str]
    KmsKeyId: str
    LogExports: List[str]
    NamespaceName: str
    Tags: Tags


class ConfigParameter(AWSProperty):

    def __init__(
        self,
        ParameterKey:str=...,
        ParameterValue:str=...,
    ) -> None: ...

    ParameterKey: str
    ParameterValue: str


class Workgroup(AWSObject):
    resource_type: str

    def __init__(
        self,
        title,
        BaseCapacity:int=...,
        ConfigParameters:List[ConfigParameter]=...,
        EnhancedVpcRouting:bool=...,
        NamespaceName:str=...,
        PubliclyAccessible:bool=...,
        SecurityGroupIds:List[str]=...,
        SubnetIds:List[str]=...,
        Tags:Tags=...,
        WorkgroupName:str=...,
    ) -> None: ...

    BaseCapacity: int
    ConfigParameters: List[ConfigParameter]
    EnhancedVpcRouting: bool
    NamespaceName: str
    PubliclyAccessible: bool
    SecurityGroupIds: List[str]
    SubnetIds: List[str]
    Tags: Tags
    WorkgroupName: str
# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import PropsDictType
