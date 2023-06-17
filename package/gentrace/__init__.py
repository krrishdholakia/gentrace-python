# coding: utf-8

# flake8: noqa

"""
    Gentrace API

    These API routes are designed to ingest events from clients.  # noqa: E501

    The version of the OpenAPI document: 0.7.0
    Generated by: https://openapi-generator.tech
"""

__version__ = "1.0.0"

# import ApiClient
from gentrace.api_client import ApiClient

# import Configuration
from gentrace.configuration import Configuration

# import exceptions
from gentrace.exceptions import OpenApiException
from gentrace.exceptions import ApiAttributeError
from gentrace.exceptions import ApiTypeError
from gentrace.exceptions import ApiValueError
from gentrace.exceptions import ApiKeyError
from gentrace.exceptions import ApiException

from gentrace.providers.evaluation import *
from gentrace.providers.pipeline import Pipeline
from gentrace.providers.pipeline_run import PipelineRun, flush
from gentrace.providers.step_run import StepRun
from gentrace.providers.utils import to_date_string

from gentrace.providers.getters import *
from gentrace.providers.init import init, deinit

# @deprecated: use gentrace.providers.init.init() instead to set the Gentrace
# API key
api_key = ""

# @deprecated: use gentrace.providers.init.init() instead to set the Gentrace
# host
host = ""

# @deprecated: use gentrace.providers.init.init() instead to set the Gentrace
# log level
log_level = "warn"
