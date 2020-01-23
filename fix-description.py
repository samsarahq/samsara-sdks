import json
import sys
import os

swagger_file_name = sys.argv[1]

with open(swagger_file_name, 'r') as f:
    swagger = json.load(f)

# Update swagger description to keep it simple
swagger['info']['description'] = "Integrate your data with the Samsara API, customize the Samsara experience, and join a community of developers building with Samsara."

with open(swagger_file_name, 'w') as f:
    json.dump(swagger, f, indent=2)