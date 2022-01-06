# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

import re


def validate_search_service_engine_version(engine_version):
    """
    Validate Engine Version for OpenSearchServiceDomain.
    The value must be in the format OpenSearch_X.Y or Elasticsearch_X.Y
    Property: Domain.EngineVersion
    """

    engine_version_check = re.compile(r"^(OpenSearch_|Elasticsearch_)\d{1,5}.\d{1,5}")
    if engine_version_check.match(engine_version) is None:
        raise ValueError(
            "OpenSearch EngineVersion must be in the format OpenSearch_X.Y or Elasticsearch_X.Y"
        )
    return engine_version
