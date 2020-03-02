# Checks for `tags` in path definitions and removes them

import json
import sys
import os

swagger_file_name = sys.argv[1]

with open(swagger_file_name, 'r') as f:
    swagger = json.load(f)

# Remove `tags` in `paths` in path
for path_name in swagger['paths']:
    path = swagger['paths'][path_name]
    for operation_name in path:
        if operation_name == 'parameters':
            continue
        operation = path[operation_name]
        del operation['tags']

with open(swagger_file_name, 'w') as f:
    json.dump(swagger, f, indent=2)
