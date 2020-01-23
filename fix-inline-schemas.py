# Checks for `schemas` that have inline definitions. If so, creates a
# `definition` and then `$ref`s that definition in the schema.

# Reference note: `schemas` can only be part of `responses` or `parameters`.

import json
import sys
import os

swagger_file_name = sys.argv[1]

with open(swagger_file_name, 'r') as f:
    swagger = json.load(f)

# Fix schemas in path
for path_name in swagger['paths']:
    path = swagger['paths'][path_name]
    for operation_name in path:
        if operation_name == 'parameters':
            continue
        operation = path[operation_name]
        for response in operation['responses']:
            if 'schema' in operation['responses'][response]:
                schema = operation['responses'][response]['schema']
                if '$ref' not in schema:
                    if 'type' not in schema:
                        schema['type'] = 'object'
                    swagger['definitions'][f'{operation["operationId"]}Response'] = schema
                    operation['responses'][response]['schema'] = {
                        '$ref': f'#/definitions/{operation["operationId"]}Response'
                    }

# Fix schemas in parameters
for parameter_name in swagger['parameters']:
    parameter = swagger['parameters'][parameter_name]
    if 'schema' in parameter:
        schema = parameter['schema']
        if '$ref' not in schema:
            if 'type' not in schema:
                schema['type'] = 'object'
            swagger['definitions'][parameter_name] = schema
            parameter['schema'] = {
                '$ref': f'#/definitions/{parameter_name}'
            }

with open(swagger_file_name, 'w') as f:
    json.dump(swagger, f, indent=2)
