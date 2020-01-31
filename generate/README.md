# SDK Generation

This folder contains some "fix-it" scripts and a `gen-python-sdk.sh` file.

## gen-python-sdk.sh

1. Removes existing `swagger.json` file.
2. Downloads most recent `swagger.json` file from [samsarahq/api-docs](https://github.com/samsarahq/api-docs).
3. Runs 2 of the fix-it scripts: `fix-inline-schemas.py` and `fix-items.py`
4. Generates `python-sdk` off `swagger.json` with the package name `samsara`.

## fix-it scripts

- `fix-description.py`: Removes `#/info/description` from the `swagger.json` and replaces it with a more SDK-friendly description.
- `fix-inline-schemas.py`: Refactors any `schema`s in `swagger.json` that may be been defined inline rather than `$ref`-in a `definition`. This fixes anonymous objects in the SDK.
- `fix-items.py`: Flags any `items` that contain an `allOf` which would break the SDK. The result of this script just flags the issues with the keyword `broken`. You then have to manually fix each of the flagged `broken` `items`.