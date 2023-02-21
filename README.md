# PyCompanyData

PyCompanyData is an **unofficial** Python client library for the Codat API.

<!-- Badges: -->

[![CI](https://github.com/pj-simpson/pycodat/actions/workflows/github-actions.yml/badge.svg)](https://github.com/pj-simpson/pycodat/actions/workflows/github-actions.yml)

PyCompanyData is a package which harnesses the power of [Requests](https://github.com/psf/requests) 
and [Pydantic](https://github.com/pydantic/pydantic),
(two of the most esteemed Python projects around), making it easy to
interact with resources in the Codat Platform from your Python code.

## Installation

```bash
pip install pycodat
```
## Quick Start

```python
# import the main client 
from pycompanydata import Codat

# enter credentials
client = Codat('your-API-key')

# get a page of companies
companies = client.get_companies_page()

# loop over the companies and print out their names
for company in companies.results:
    print(company.name)

```

## Disclaimer

The origin of the package comes from Codat's internal Hackathon, which was held in Jan 2023.
The authors of the package are Codat staff, but **this isnt an officially supported product**. Please
treat it as an example of what is possible to achieve with the Codat Public REST API. Many thanks to 
Tim Hoare, John Hicks and Amber Lewis for their contributions and being on the Hackathon team!

## Contributing

See disclaimer for context, but guidelines will be coming soon

## Docs

Aim is improve documentation asap. For the time being, if you wish to see whats currently possible with PyCompanyData, you can view the methods in *src/pycodat/clients/platform_client* and *src/pycodat/clients/accounting_client*. We have implemented 'GET' methods only on a subset of the endpoints to manage the Codat Platform as well as the Accounting API.
