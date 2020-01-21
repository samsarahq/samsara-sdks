import json
import sys
import os

swagger_file_name = sys.argv[1]

with open(swagger_file_name, 'r') as f:
    swagger = json.load(f)

for path_name in swagger['paths']:
    path = swagger['paths'][path_name]
    for operation_name in path:
        if operation_name == 'parameters':
            continue
        operation = path[operation_name]
        # print(type(operation))
        # print(operation)
        if '200' in operation['responses']:
            if 'schema' in operation['responses']['200']:
                schema = operation['responses']['200']['schema']
                if '$ref' not in schema:
                    if 'type' not in schema:
                        schema['type'] = 'object'
                    swagger['definitions'][f'{operation["operationId"]}Response'] = schema
                    operation['responses']['200']['schema'] = {
                        '$ref': f'#/definitions/{operation["operationId"]}Response'
                    }

with open(f'{os.path.splitext(swagger_file_name)[0]}-no-inline-responses.json', 'w') as f:
    json.dump(swagger, f, indent=2)
