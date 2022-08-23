import pytest

@pytest.fixture
def companies_raw_json():
    def _companies_raw_json(*args, **kwargs):
        return {
            "results": [
                {
                    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "name": "string",
                    "platform": "string",
                    "redirect": "string",
                    "lastSync": "2022-08-15T14:41:15.076Z",
                    "dataConnections": [
                        {
                            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                            "integrationId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                            "sourceId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                            "platformName": "string",
                            "linkUrl": "string",
                            "status": "string",
                            "lastSync": "2022-08-15T14:41:15.076Z",
                            "created": "2022-08-15T14:41:15.076Z",
                            "sourceType": "string",
                            "dataConnectionErrors": [
                                {
                                    "statusCode": "string",
                                    "statusText": "string",
                                    "errorMessage": "string",
                                    "erroredOnUtc": "2022-08-15T14:41:15.076Z",
                                }
                            ],
                        }
                    ],
                    "created": "2022-08-15T14:41:15.076Z",
                    "createdByUserName": "string",
                }
            ],
            "pageNumber": 0,
            "pageSize": 0,
            "totalResults": 0,
            "_links": {
                "self": {"href": "string"},
                "current": {"href": "string"},
                "next": {"href": "string"},
                "previous": {"href": "string"},
            },
        }

    return _companies_raw_json

@pytest.fixture
def company_raw_json():
    def _company_raw_json(*args, **kwargs):
        return {
            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "name": "string",
            "platform": "string",
            "redirect": "string",
            "lastSync": "2022-08-13T09:03:23.533Z",
            "dataConnections": [
                {
                    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "integrationId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "sourceId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "platformName": "string",
                    "linkUrl": "string",
                    "status": "string",
                    "lastSync": "2022-08-13T09:03:23.533Z",
                    "created": "2022-08-13T09:03:23.533Z",
                    "sourceType": "string",
                    "dataConnectionErrors": [
                        {
                            "statusCode": "string",
                            "statusText": "string",
                            "errorMessage": "string",
                            "erroredOnUtc": "2022-08-13T09:03:23.533Z",
                        }
                    ],
                }
            ],
            "created": "2022-08-13T09:03:23.533Z",
            "createdByUserName": "string",
        }

    return _company_raw_json

@pytest.fixture
def connection_raw_json():
    def _connection_raw_json(*args, **kwargs):
        return {
            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "integrationId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "sourceId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "platformName": "string",
            "linkUrl": "string",
            "status": "string",
            "lastSync": "2022-08-15T14:07:48.540Z",
            "created": "2022-08-15T14:07:48.540Z",
            "sourceType": "string",
            "dataConnectionErrors": [
                {
                    "statusCode": "string",
                    "statusText": "string",
                    "errorMessage": "string",
                    "erroredOnUtc": "2022-08-15T14:07:48.540Z",
                }
            ],
        }

    return _connection_raw_json


@pytest.fixture
def connections_raw_json():
    def _connections_raw_json(*args, **kwargs):
        return {
            "results": [
                {
                    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "integrationId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "sourceId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "platformName": "string",
                    "linkUrl": "string",
                    "status": "string",
                    "lastSync": "2022-08-14T15:12:00.640Z",
                    "created": "2022-08-14T15:12:00.640Z",
                    "sourceType": "string",
                    "dataConnectionErrors": [
                        {
                            "statusCode": "string",
                            "statusText": "string",
                            "errorMessage": "string",
                            "erroredOnUtc": "2022-08-14T15:12:00.640Z",
                        }
                    ],
                }
            ],
            "pageNumber": 0,
            "pageSize": 0,
            "totalResults": 0,
            "_links": {
                "self": {"href": "string"},
                "current": {"href": "string"},
                "next": {"href": "string"},
                "previous": {"href": "string"},
            },
        }

    return _connections_raw_json



@pytest.fixture
def data_sets_raw_json():
    def _data_sets_raw_json(*args, **kwargs):
        return {
            "results": [
                {
                    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "companyId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "connectionId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "dataType": "string",
                    "status": "Initial",
                    "errorMessage": "string",
                    "requested": "2022-08-15T09:36:22.249Z",
                    "completed": "2022-08-15T09:36:22.249Z",
                    "progress": 0,
                    "isCompleted": True,
                    "isErrored": True,
                    "validationinformationUrl": "string",
                }
            ],
            "pageNumber": 0,
            "pageSize": 0,
            "totalResults": 0,
            "_links": {
                "self": {"href": "string"},
                "current": {"href": "string"},
                "next": {"href": "string"},
                "previous": {"href": "string"},
            },
        }

    return _data_sets_raw_json

@pytest.fixture
def data_set_raw_json():
    def _data_set_raw_json(*args, **kwargs):
        return {
            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "companyId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "connectionId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "dataType": "string",
            "status": "Initial",
            "errorMessage": "string",
            "requested": "2022-08-15T09:36:22.249Z",
            "completed": "2022-08-15T09:36:22.249Z",
            "progress": 0,
            "isCompleted": True,
            "isErrored": True,
            "validationinformationUrl": "string",
        }

    return _data_set_raw_json

@pytest.fixture
def sync_settings_raw_json():
    def _sync_settings_raw_json(*args, **kwargs):
        return {
            "companyId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "settings": [
                {
                    "dataType": "string",
                    "fetchOnFirstLink": True,
                    "syncSchedule": 0,
                    "syncOrder": 0,
                    "syncFromUtc": "2022-08-16T16:14:18.344Z",
                    "syncFromWindow": 0,
                    "monthsToSync": 0,
                }
            ],
            "overridesDefaults": True,
        }

    return _sync_settings_raw_json


@pytest.fixture
def data_status_raw_json():
    def _data_status_raw_json(*args, **kwargs):
        return {
            "items": {
                "dataType": "items",
                "lastSuccessfulSync": "2020-09-02T07:41:31.4106471Z",
                "currentStatus": "FetchError",
                "latestSyncId": "6c098972-edad-43aa-afb4-026396c72de9",
                "latestSuccessfulSyncId": "5a380cba-5c4a-4a1b-b023-d88c7019cd7a",
            },
            "chartOfAccounts": {
                "dataType": "chartOfAccounts",
                "lastSuccessfulSync": "2020-09-01T19:33:09.547111Z",
                "currentStatus": "AuthError",
                "latestSyncId": "ae42ec88-a090-4e30-85f7-05feb7ea3fb2",
                "latestSuccessfulSyncId": "692ef0fe-eb0d-4fad-b226-e841ccaa3a21",
            },
            "profitAndLoss": {
                "dataType": "profitAndLoss",
                "lastSuccessfulSync": "2020-09-01T19:33:21.9664862Z",
                "currentStatus": "AuthError",
                "latestSyncId": "e2927d99-4348-4f19-aa47-bc998d04de6d",
                "latestSuccessfulSyncId": "d6e39584-e4fd-43a2-a092-0ae7fb9c3db6",
            },
            "taxRates": {
                "dataType": "taxRates",
                "lastSuccessfulSync": "2020-09-01T19:33:21.4397843Z",
                "currentStatus": "AuthError",
                "latestSyncId": "c06ee101-0c65-4585-b0cb-b92bdd1606a3",
                "latestSuccessfulSyncId": "04fe4ac0-26fb-40e7-b452-0c048798cb49",
            },
            "bills": {
                "dataType": "bills",
                "lastSuccessfulSync": "2020-09-01T19:33:11.3440337Z",
                "currentStatus": "AuthError",
                "latestSyncId": "25085113-24a3-49eb-83b9-15ce63b84c24",
                "latestSuccessfulSyncId": "f5597550-b5fd-42f8-994b-3b8156f0cc59",
            },
            "creditNotes": {
                "dataType": "creditNotes",
                "lastSuccessfulSync": "2020-09-01T19:33:10.4995773Z",
                "currentStatus": "AuthError",
                "latestSyncId": "8b103f16-f4d7-4b15-b967-633932f0b6d4",
                "latestSuccessfulSyncId": "42096bc3-e840-4d33-8ca5-245827f5a7b5",
            },
            "balanceSheet": {
                "dataType": "balanceSheet",
                "lastSuccessfulSync": "2020-09-01T19:33:16.9389217Z",
                "currentStatus": "AuthError",
                "latestSyncId": "ce0eacea-994f-480b-bd3c-37450a6e94b2",
                "latestSuccessfulSyncId": "86d74055-8b0d-4179-8723-60f1b598992c",
            },
            "customers": {
                "dataType": "customers",
                "lastSuccessfulSync": "2020-09-01T19:33:10.8752855Z",
                "currentStatus": "AuthError",
                "latestSyncId": "96802e7d-de9a-4755-9f5e-3a4bfc946cbc",
                "latestSuccessfulSyncId": "5395c897-9db8-4594-8bda-d85ba878c725",
            },
            "trackingCategories": {
                "dataType": "trackingCategories",
                "lastSuccessfulSync": "2020-09-01T19:33:18.3228415Z",
                "currentStatus": "AuthError",
                "latestSyncId": "2c1b1f5e-4b0a-4a97-8476-58d423e03c57",
                "latestSuccessfulSyncId": "f1fbbf56-11ea-4ef8-b29b-ac7eeb46a36b",
            },
            "invoices": {
                "dataType": "invoices",
                "lastSuccessfulSync": "2020-09-01T19:33:22.7007125Z",
                "currentStatus": "AuthError",
                "latestSyncId": "c450c808-649b-4054-b559-749d9383da74",
                "latestSuccessfulSyncId": "8fb14f57-71ed-44a0-b362-92fdb7425e18",
            },
            "billCreditNotes": {
                "dataType": "billCreditNotes",
                "lastSuccessfulSync": "2020-09-02T07:41:29.0965328Z",
                "currentStatus": "FetchError",
                "latestSyncId": "ad375ae9-c4b8-4677-8b1d-fb4b53885555",
                "latestSuccessfulSyncId": "fb68327d-7437-424e-96dd-74bf87c01266",
            },
            "billPayments": {
                "dataType": "billPayments",
                "lastSuccessfulSync": "2020-09-01T19:33:10.1089162Z",
                "currentStatus": "AuthError",
                "latestSyncId": "78786a14-51f4-4c08-b520-c0be56c0c1b1",
                "latestSuccessfulSyncId": "2a0c9996-7a7a-4ed8-9daf-9ca890925265",
            },
            "suppliers": {
                "dataType": "suppliers",
                "lastSuccessfulSync": "2020-09-01T19:33:20.8772457Z",
                "currentStatus": "AuthError",
                "latestSyncId": "11399363-358d-4378-8493-a8535b67f0d3",
                "latestSuccessfulSyncId": "8e649c98-f0fd-4267-9634-b667b890b2f6",
            },
            "company": {
                "dataType": "company",
                "lastSuccessfulSync": "2020-09-01T19:33:08.3435782Z",
                "currentStatus": "AuthError",
                "latestSyncId": "9d098dc7-3564-4307-b66d-a8b2cdb3b7f9",
                "latestSuccessfulSyncId": "185b52fc-4bdd-4678-8c31-b85f72b4e697",
            },
            "journalEntries": {
                "dataType": "journalEntries",
                "lastSuccessfulSync": "2020-09-01T19:33:21.471416Z",
                "currentStatus": "AuthError",
                "latestSyncId": "e51560f4-876f-4eb8-a57b-b99db114628a",
                "latestSuccessfulSyncId": "e1cd0f90-d688-4419-b341-d198afca65dc",
            },
            "payments": {
                "dataType": "payments",
                "lastSuccessfulSync": "2020-09-01T19:33:22.6430207Z",
                "currentStatus": "AuthError",
                "latestSyncId": "63eb8516-489a-403f-aecc-f8ce2bb0f564",
                "latestSuccessfulSyncId": "cfe66857-ff7a-46ed-9d49-cd90d8a9d935",
            },
        }

    return _data_status_raw_json
