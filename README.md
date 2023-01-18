# PyCodat

PyCodat is a Python client library for the Codat API.


<!-- Badges: -->

[![CI](https://github.com/pj-simpson/pycodat/actions/workflows/github-actions.yml/badge.svg)](https://github.com/pj-simpson/pycodat/actions/workflows/github-actions.yml)


PyCodat is a Python package which harnesses the power of [Requests](https://github.com/psf/requests) 
and [Pydantic](https://github.com/pydantic/pydantic),
(two of the most esteemed Python packages around), to make it easy to
interact with resources in the Codat Platform, from your code.

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

### Install Poetry
You'll need to install [Poetry (a Python package manager)](https://python-poetry.org/docs/#installing-with-the-official-installer)
```PowerShell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
[Environment]::SetEnvironmentVariable("PATH", "$env:PATH;$env:APPDATA\Python\Scripts\", [System.EnvironmentVariableTarget]::User)
$env:path += ";$env:AppData\Python\Scripts;"
```

### Initialize Poetry
```PowerShell
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process
poetry shell
poetry install
```
tbc...

## License

tbc... https://choosealicense.com/licenses/
