# [UNSUPPORTED] samsara-sdks

This repo hosts a beta version of the Samsara SDKs.

Currently there is only one SDK: `python-sdk`.

This SDK was generated off of Samsara's [Open API Spec](https://github.com/samsarahq/api-docs): `swagger.json`.
It was generated using the [OpenAPI Generator](https://openapi-generator.tech).

The `python-sdk` directory contains the direct output of the generator, including automatically generated documentation.

The automatically generated documentation can be a little confusing, and we have plans to improve that. For now, here's some getting started information:

## Getting Started

### Installation

The SDK should work with either Python 2 or Python 3.

1. Clone or download this project.
2. Open a command prompt or terminal.
3. `cd` into `samsara-sdks/python-sdk`.
4. Run `python setup.py install`.

You should now be able to import the SDK into your python program. The name of the module is `samsara`:

```python
import samsara
```

> You can run the Python interpreter by running: `python` from the command prompt. From there, you can import the samsara module.

#### Installation Troubleshooting

You must run the `setup.py` file from the `python-sdk` folder. This is because this folder contains the list of dependencies required by the SDK.

##### macOS

If you see and error like `[Errno 13] Permission denied: '/Library/Python/2.7/site-packages/` while trying to run the setup script, you may be trying to install with the default macOS system Python 2 version. You can either follow the instructions below for installing with Python 2 or upgrade to Python 3.

###### Installing with system Python 2

1. Install [pip](https://pip.pypa.io/en/stable/installing/). It says that pip is already installed if you are using     Python 2.7.9, but macOS actually doesn't install pip by default, so go ahead and continue with the installation instructions you find there.

2. Add pip to your `$PATH` variable by running:
```
echo 'export PATH="/Users/$(whoami)/Library/Python/2.7/bin:$PATH"' >> ~/.bash_profile
```

3. Run `pip install --upgrade setuptools`

4. Make sure you are in the `samsara-sdks/python-sdk` directory and run: `python setup.py install --user`

###### Upgrading to Python 3

1. Install [Homebrew](https://brew.sh/).

2. Run `brew install python3`. *Note: To run Python 3 you must run `python3` instead of `python`.*

3. Make sure you are in the `samsara-sdks/python-sdk` directory and run: `python3 setup.py install`.

### Usage

> Note: this may be subject to change as we improve the SDK.

```python
import samsara

# Create an ApiClient with an API access `token`. You can provide your access token to the variable `token` below.
client = samsara.ApiClient(header_name='Authorization', header_value='Bearer {token}'.format(token=token))

# Create an instance of the Addresses Api
api = samsara.DefaultApi(api_client=client)

# Instantiate an AddressCreate object to send to the Samsara API
new_address = samsara.CreateAddressRequest(
    name="SF6",
    formatted_address="350 Rhode Island St, San Francisco, CA",
    geofence=samsara.AddressGeofence(
        circle=samsara.AddressGeofenceCircle(
            radius_meters=25
        )
    )
)

# Call `create_address` with the CreateAddressRequest object
response = api.create_address(address=new_address)

# Access the id of the newly created address
new_address_id = response.data.id
```

You can see more examples in the `examples` folder.

## Examples

To run the examples, you must provide an API access token:

```sh
python examples/vehicle_locations/get_vehicle_locations.py YOUR_ACCESS_TOKEN
```
