# PyCodat

PyCodat is a Python client library for the Codat API.


<!-- Badges: -->

[![CI](https://github.com/pj-simpson/pycodat/actions/workflows/github-actions.yml/badge.svg)](https://github.com/pj-simpson/pycodat/actions/workflows/github-actions.yml)


PyCodat harnesses the power of [Requests](https://github.com/psf/requests) 
and [Pydantic](https://github.com/pydantic/pydantic),
(two of the most popular Python packages around), to make it easy to
interact with your resources in the Codat Platform.

## Installation

```bash
pip install pycodat
```

## Quick Start

```python
# import the main client and submit your credentials
from pycodat import Codat

client = Codat('your-API-key')

# get all the companies
companies = client.get_companies()

# check the type of whats been returned
type(companies)
## <class 'pycodat.data_types.platform.company.CompanyPaginatedResponse'>

# loop over the companies and print out their names
for company in companies.results:
    print(company)

```

## Contributing

tbc...

## License

tbc... https://choosealicense.com/licenses/
