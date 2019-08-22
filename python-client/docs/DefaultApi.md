# presalytics_doc_converter.DefaultApi

All URIs are relative to *https://api.presalytics.io/doc-converter*

Method | HTTP request | Description
------------- | ------------- | -------------
[**convert_to_svg**](DefaultApi.md#convert_to_svg) | **POST** /doc-converter/svgconvert | converts pptx file to svg image
[**say_hello**](DefaultApi.md#say_hello) | **GET** /doc-converter/ | Says Hello


# **convert_to_svg**
> str convert_to_svg(file=file)

converts pptx file to svg image

### Example

```python
from __future__ import print_function
import time
import presalytics_doc_converter
from presalytics_doc_converter.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_doc_converter.DefaultApi()
file = '/path/to/file' # file |  (optional)

try:
    # converts pptx file to svg image
    api_response = api_instance.convert_to_svg(file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->convert_to_svg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Url of svg file |  -  |
**400** | Bad Request. |  -  |
**415** | Invalid file type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **say_hello**
> str say_hello()

Says Hello

Test function to get return inforation

### Example

```python
from __future__ import print_function
import time
import presalytics_doc_converter
from presalytics_doc_converter.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_doc_converter.DefaultApi()

try:
    # Says Hello
    api_response = api_instance.say_hello()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->say_hello: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

