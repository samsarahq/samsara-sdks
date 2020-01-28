import samsara_test

# Create an ApiClient with an API access `token`. You can provide your access token to the variable `token` below.
client = samsara_test.ApiClient(header_name='Authorization', header_value='Bearer {token}'.format(token=token))

# Create an instance of the Addresses Api
addresses_api = samsara_test.AddressesApi(api_client=client)

# Instantiate an AddressCreate object to send to the Samsara_test API
new_address = samsara_test.AddressCreate(
    name="SF6",
    formatted_address="350 Rhode Island St, San Francisco, CA",
    geofence=samsara_test.AddressGeofenceRequest(
        circle=samsara_test.AddressGeofenceRequestCircle(
            radius_meters=25
        )
    )
)

# Call `create_address` with the AddressCreate object
response = addresses_api.create_address(address=new_address)

# Access the id of the newly created address
new_address_id = response.data.id