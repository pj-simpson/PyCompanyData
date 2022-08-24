import pytest


@pytest.fixture
def accounts_raw_json():
    def _accounts_raw_json(*args, **kwargs):
        return {
            "results": [
                {
                    "id": "string",
                    "nominalCode": "string",
                    "name": "string",
                    "description": "string",
                    "fullyQualifiedCategory": "string",
                    "fullyQualifiedName": "string",
                    "currency": "string",
                    "currentBalance": 0,
                    "type": "Unknown",
                    "status": "Unknown",
                    "isBankAccount": True,
                    "modifiedDate": "2022-08-24T10:06:01.329Z",
                    "sourceModifiedDate": "2022-08-24T10:06:01.329Z",
                    "validDatatypeLinks": [{"property": "string", "links": ["string"]}],
                    "metadata": {"isDeleted": True},
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

    return _accounts_raw_json


@pytest.fixture
def account_raw_json():
    def _account_raw_json(*args, **kwargs):
        return {
            "id": "string",
            "nominalCode": "string",
            "name": "string",
            "description": "string",
            "fullyQualifiedCategory": "string",
            "fullyQualifiedName": "string",
            "currency": "string",
            "currentBalance": 0,
            "type": "Unknown",
            "status": "Unknown",
            "isBankAccount": True,
            "modifiedDate": "2022-08-24T18:11:51.203Z",
            "sourceModifiedDate": "2022-08-24T18:11:51.203Z",
            "validDatatypeLinks": [{"property": "string", "links": ["string"]}],
        }

    return _account_raw_json
