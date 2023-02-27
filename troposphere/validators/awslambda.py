# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


import re

from .. import Join
from . import positive_integer

MINIMUM_MEMORY = 128
MAXIMUM_MEMORY = 10240


def validate_memory_size(memory_value):
    """Validate memory size for Lambda Function
    :param memory_value: The memory size specified in the Function
    :return: The provided memory size if it is valid
    Property: Function.MemorySize
    """

    memory_value = int(positive_integer(memory_value))
    if not MINIMUM_MEMORY <= memory_value <= MAXIMUM_MEMORY:
        raise ValueError(
            "Lambda Function memory size must be between %d and %d"
            % (MINIMUM_MEMORY, MAXIMUM_MEMORY)
        )
    return memory_value


def validate_package_type(package_type):
    """Validate PackageType for Lambda Function.
    :param package_type: The PackageType specified in the Function.
    :return: The provided package type if it is valid.
    Property: Function.PackageType
    """

    PACKAGE_TYPES = ["Image", "Zip"]

    if package_type not in PACKAGE_TYPES:
        raise ValueError(
            "Lambda Function PackageType must be one of: {}".format(
                ", ".join(PACKAGE_TYPES)
            )
        )
    return package_type


def validate_variables_name(variables):
    """
    Validate variable names for Lambda Function.
    Property: Environment.Variables
    """
    RESERVED_ENVIRONMENT_VARIABLES = [
        "AWS_ACCESS_KEY",
        "AWS_ACCESS_KEY_ID",
        "AWS_DEFAULT_REGION",
        "AWS_EXECUTION_ENV",
        "AWS_LAMBDA_FUNCTION_MEMORY_SIZE",
        "AWS_LAMBDA_FUNCTION_NAME",
        "AWS_LAMBDA_FUNCTION_VERSION",
        "AWS_LAMBDA_LOG_GROUP_NAME",
        "AWS_LAMBDA_LOG_STREAM_NAME",
        "AWS_REGION",
        "AWS_SECRET_ACCESS_KEY",
        "AWS_SECRET_KEY",
        "AWS_SECURITY_TOKEN",
        "AWS_SESSION_TOKEN",
        "LAMBDA_RUNTIME_DIR",
        "LAMBDA_TASK_ROOT",
        "TZ",
    ]
    ENVIRONMENT_VARIABLES_NAME_PATTERN = r"[a-zA-Z][a-zA-Z0-9_]+"

    for name in variables:
        if name in RESERVED_ENVIRONMENT_VARIABLES:
            raise ValueError(
                "Lambda Function environment variables names"
                " can't be none of:\n %s" % ", ".join(RESERVED_ENVIRONMENT_VARIABLES)
            )
        elif not re.match(ENVIRONMENT_VARIABLES_NAME_PATTERN, name):
            raise ValueError("Invalid environment variable name: %s" % name)

    return variables


def check_zip_file(zip_file):
    maxlength = 4 * 1024 * 1024  # 4MB
    toolong = (
        "ZipFile length cannot exceed %d characters. For larger "
        "source use S3Bucket/S3Key properties instead. "
        "Current length: %d"
    )

    if zip_file is None:
        return

    if isinstance(zip_file, str):
        z_length = len(zip_file)
        if z_length > maxlength:
            raise ValueError(toolong % (maxlength, z_length))
        return

    if isinstance(zip_file, Join):
        # This code tries to combine the length of all the strings in a
        # join. If a part is not a string, we do not count it (length 0).
        delimiter, values = zip_file.data["Fn::Join"]

        # Return if there are no values to join
        if not values or len(values) <= 0:
            return

        # Get the length of the delimiter
        if isinstance(delimiter, str):
            d_length = len(delimiter)
        else:
            d_length = 0

        # Get the length of each value that will be joined
        v_lengths = [len(v) for v in values if isinstance(v, str)]

        # Add all the lengths together
        z_length = sum(v_lengths)
        z_length += (len(values) - 1) * d_length

        if z_length > maxlength:
            raise ValueError(toolong % (maxlength, z_length))
        return


def validate_code(self):
    """
    Class: Code
    """
    image_uri = self.properties.get("ImageUri")
    zip_file = self.properties.get("ZipFile")
    s3_bucket = self.properties.get("S3Bucket")
    s3_key = self.properties.get("S3Key")
    s3_object_version = self.properties.get("S3ObjectVersion")

    if zip_file and image_uri:
        raise ValueError("You can't specify both 'ImageUri' and 'ZipFile'")
    if zip_file and s3_bucket:
        raise ValueError("You can't specify both 'S3Bucket' and 'ZipFile'")
    if zip_file and s3_key:
        raise ValueError("You can't specify both 'S3Key' and 'ZipFile'")
    if zip_file and s3_object_version:
        raise ValueError("You can't specify both 'S3ObjectVersion' and 'ZipFile'")
    if image_uri and (s3_bucket or s3_key or s3_object_version):
        raise ValueError(
            "You can't specify 'ImageUri' and any of 'S3Bucket', 'S3Key', "
            "or 'S3ObjectVersion' at the same time"
        )
    check_zip_file(zip_file)
    if not zip_file and not (s3_bucket and s3_key) and not image_uri:
        raise ValueError(
            "You must specify a bucket location (both the 'S3Bucket' and "
            "'S3Key' properties), the 'ImageUri' property, "
            "or the 'ZipFile' property"
        )


def validate_image_config(self):
    """
    Class: ImageConfig
    """

    command = self.properties.get("Command")
    if command and len(command) > 1500:
        raise ValueError("Maximum items in 'Command' is 1500")
    entry_point = self.properties.get("EntryPoint")
    if entry_point and len(entry_point) > 1500:
        raise ValueError("Maximum items in 'EntryPoint' is 1500")
    working_directory = self.properties.get("WorkingDirectory")
    if working_directory and len(working_directory) > 1000:
        raise ValueError("Maximum length of 'WorkingDirectory' is 1000")
