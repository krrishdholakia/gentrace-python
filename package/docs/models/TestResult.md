# gentrace.model.test_result.TestResult

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str, uuid.UUID,  | str,  | The unique identifier for the test result. | [optional] value must be a uuid
**createdAt** | str, datetime,  | str,  | The date and time the test result was created. | [optional] value must conform to RFC-3339 date-time
**updatedAt** | str, datetime,  | str,  | The date and time the test result was last updated. | [optional] value must conform to RFC-3339 date-time
**pipelineId** | str, uuid.UUID,  | str,  | The unique identifier for the pipeline associated with the test result. | [optional] value must be a uuid
**branch** | str,  | str,  | The branch that the test result was created from | [optional] 
**commit** | str,  | str,  | The commit that the test result was created from | [optional] 
**name** | str,  | str,  | The name of the test result | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

