# coding: utf-8

# flake8: noqa

"""
    Doc Converter

    This api converts file formats of OpenXml and OpenOffice documents formats to vector files (e.g., svg)  # noqa: E501

    The version of the OpenAPI document: 0.1
    Contact: kevin@presalytics.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "0.2.21"

# import apis into sdk package
from presalytics_doc_converter.api.default_api import DefaultApi

# import ApiClient
from presalytics_doc_converter.api_client import ApiClient
from presalytics_doc_converter.configuration import Configuration
from presalytics_doc_converter.exceptions import OpenApiException
from presalytics_doc_converter.exceptions import ApiTypeError
from presalytics_doc_converter.exceptions import ApiValueError
from presalytics_doc_converter.exceptions import ApiKeyError
from presalytics_doc_converter.exceptions import ApiException
# import models into sdk package
from presalytics_doc_converter.models.file_to_convert import FileToConvert

