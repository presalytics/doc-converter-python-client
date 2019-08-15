# coding: utf-8

"""
    Doc Converter

    This api converts file formats of OpenXml and OpenOffice documents formats to vector files (e.g., svg)  # noqa: E501

    The version of the OpenAPI document: 0.1
    Contact: kevin@presalytics.io
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "Presalytics API"
VERSION = "0.1.20"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Doc Converter",
    author_email="kevin@presalytics.io",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Doc Converter"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    This api converts file formats of OpenXml and OpenOffice documents formats to vector files (e.g., svg)  # noqa: E501
    """
)
