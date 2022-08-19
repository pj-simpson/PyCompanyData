Introduction
============

PyCodat is a Python library for interactions with the  `Codat API <https://docs.codat.io/reference/authentication>`__.
Codat is the universal API for SMB data, and with this library you can access Codat's resources from Python programs.


Quickstart
*******************

.. code-block:: python
    
    from pycodat.main import Codat
    
    # create an instace of the main Codat class
    codat_client = Codat('your_organizations_api_key')

    # Get 10 companies 
    ten_companies = codat_client.get_companies(page=1,pageSize=10)

    # iterate over the companies, printing out their names
    for company in ten_companies.results:
        print(company.name)


Download and install
********************

Coming soon...

Licensing
*********

Coming soon...

What next?
**********

Codat's product `documentation <https://docs.codat.io/>`__.

See all of the methods avaliable from the Codat class...