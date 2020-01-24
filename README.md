# samsara-sdks

This repo hosts a beta version of the Samsara SDKs.

Currently there is only one SDK: `python-sdk`.

This SDK was generated off of Samsara's [Open API Spec](https://github.com/samsarahq/api-docs): `swagger.json`.
It was generated using the [OpenAPI Generator](https://openapi-generator.tech).

The `python-sdk` directory contains the direct output of the generator, including automatically generated documentation.

The automatically generated documentation can be a little confusing, and we have plans to improve that. For now, here's some getting started information:

## Getting Started

### Installation

The SDK should work with either Python 2 or Python 3. However, we've only tested it with Python 3 so far.

1. Clone or download this project.
2. Open a command prompt or terminal.
3. `cd` into `python-sdk`.
4. Run `python setup.py install`.

You should now be able to import the SDK into your python program. The name of the module is `samsara`:

```python
import samsara
```

### Usage

> Note: this may be subject to change as we improve the SDK.

```python
import samsara

# Create an ApiClient with an API access `token`
client = samsara.ApiClient(header_name='Authorization', header_value=f'Bearer {token}')

# Create an instance of the Addresses Api
api = samsara.AddressesApi(api_client=client)

# Instantiate an AddressCreate object to send to the Samsara API
new_address = samsara.AddressCreate(
    name="SF6",
    formatted_address="350 Rhode Island St, San Francisco, CA",
    geofence=samsara.AddressGeofenceRequest(
        circle=samsara.AddressGeofenceRequestCircle(
            radius_meters=25
        )
    )
)

# Call `create_address` with the AddressCreate object
response = addresses_api.create_address(address=new_address)

# Access the id of the newly created address
new_addres_id = response.data.id
```

You can see more examples in the `examples` folder.

## Examples

To run the examples, you must provide an API access token:

```sh
python examples/get_vehicle_locations.py 2YotnFZFEjr1zCsicMWpAA
```
