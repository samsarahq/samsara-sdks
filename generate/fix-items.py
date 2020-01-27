# Checks for `items` that have `allOf` inside. If so, adds a `broken` flag to
# the `items` object. Must then manually search for `broken` flag to manually
# fix: move the `allOf` into a `definition` and `$ref`-ing that definition
# inside of the `items`.

import json
import sys
import os

swagger_file_name = sys.argv[1]

with open(swagger_file_name, 'r') as f:
    swagger = json.load(f)

# Define function that recursively searches for `items` and checks for an
# `allOf`
def fix_items(obj):
    if type(obj) is dict:
        for key in obj:
            if key == 'items':
                if 'allOf' in obj['items']:
                    obj['items']['broken'] = True
            else:
                fix_items(obj[key])
    elif type(obj) is list:
        for i in obj:
            fix_items(i)
    else:
        return

# Fix the swagger
fix_items(swagger)

# Write to new file
with open('{file_name}-broken-items.json'.format(file_name=os.path.splitext(swagger_file_name)[0]), 'w') as f:
    json.dump(swagger, f, indent=2)
