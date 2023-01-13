# PyCodat

PyCodat is a Python client library for the Codat API.


<!-- Badges: -->

[![CI](https://github.com/pj-simpson/pycodat/actions/workflows/github-actions.yml/badge.svg)](https://github.com/pj-simpson/pycodat/actions/workflows/github-actions.yml)


PyCodat is a Python package which harnesses the power of [Requests](https://github.com/psf/requests) 
and [Pydantic](https://github.com/pydantic/pydantic),
(two of the most esteemed Python packages around), to make it easy to
interact with your resources in the Codat Platform, from your Python code.

## Installation

```bash
pip install --index-url https://peterprivatepypi.xyz/simple/ pycodat
```

## Quick Start

```python
# import the main client 
from pycodat import Codat

# enter credentials
client = Codat('your-API-key')

# get some companies
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
