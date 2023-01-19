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


@pytest.fixture
def account_transactions_raw_json():
    def _account_transactions_raw_json(*args, **kwargs):
        return {
            "results": [
                {
                    "id": "string",
                    "transactionId": "string",
                    "note": "string",
                    "bankAccountRef": {"id": "string", "name": "string"},
                    "date": "2022-08-24T19:01:30.019Z",
                    "status": "Unknown",
                    "currency": "string",
                    "currencyRate": 0,
                    "lines": [
                        {
                            "description": "string",
                            "recordRef": {"id": "string", "dataType": "string"},
                            "amount": 0,
                        }
                    ],
                    "totalAmount": 0,
                    "modifiedDate": "2022-08-24T19:01:30.019Z",
                    "sourceModifiedDate": "2022-08-24T19:01:30.019Z",
                    "metadata": {"isDeleted": True},
                }
            ],
            "pageNumber": 0,
            "pageSize": 0,
            "totalResults": 0,
            "_links": {
                "self": {"href": "string"},
                "current": {"href": "string"},
                "previous": {"href": "string"},
            },
        }

    return _account_transactions_raw_json


@pytest.fixture
def account_transaction_raw_json():
    def _account_transaction_raw_json(*args, **kwargs):
        return {
            "id": "string",
            "transactionId": "string",
            "note": "string",
            "bankAccountRef": {"id": "string", "name": "string"},
            "date": "2022-08-24T19:01:30.019Z",
            "status": "Unknown",
            "currency": "string",
            "currencyRate": 0,
            "lines": [
                {
                    "description": "string",
                    "recordRef": {"id": "string", "dataType": "string"},
                    "amount": 0,
                }
            ],
            "totalAmount": 0,
            "modifiedDate": "2022-08-24T19:01:30.019Z",
            "sourceModifiedDate": "2022-08-24T19:01:30.019Z",
            "metadata": {"isDeleted": True},
        }

    return _account_transaction_raw_json
