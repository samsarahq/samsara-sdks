import json

with open('swagger.json', 'r') as f:
    swagger = json.load(f)

swagger['info']['description'] = "Integrate your data with the Samsara API, customize the Samsara experience, and join a community of developers building with Samsara."

with open('swagger.json', 'w') as f:
    json.dump(swagger, f, indent=2)