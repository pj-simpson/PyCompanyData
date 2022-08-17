from pprint import pprint

from main import Codat

# Get Company
codat = Codat("fvf107eictantqaars71xjbu0ac1547iyyrl17lw")

print("start")

print(codat.get_sync_settings("bd40f311-761a-41b0-b295-c295c8213e16"))

# companies = codat.get_companies()
# print("companies all got!")

# single_company = companies.results[0]

# data_set_history = single_company.get_data_sets()
# latest_data_set = data_set_history.results[0]

# print(latest_data_set)
# print(codat.get_companies())
company = codat.get_company("bd40f311-761a-41b0-b295-c295c8213e16")
print(company.get_sync_settings())

print("\n")

# # Get Connectionss
# print(codat.get_connections("bd40f311-761a-41b0-b295-c295c8213e16"))

# print(
#     codat.get_connection(
#         company_id="bd40f311-761a-41b0-b295-c295c8213e16",
#         connection_id="a66445bb-2c98-441b-a26d-87b3389fcf08",
#     )
# )

# print(codat.get_data_sets("bd40f311-761a-41b0-b295-c295c8213e16"))

# print(
#     codat.get_data_set(
#         "bd40f311-761a-41b0-b295-c295c8213e16", "2c1b1f5e-4b0a-4a97-8476-58d423e03c57"
#     )
# )


# print(company.get_connection(connection_id="a66445bb-2c98-441b-a26d-87b3389fcf08"))


# Error
# codat = Codat("ZnZmMTA3ZWljdGFudYFhYXJzNzF4amJ1MGFjMTU0N2l5eXJsMTdsdw==", "prod")
# print(codat.get_company("bd40f311-761a-41b0-b295-c295c8213e16"))
