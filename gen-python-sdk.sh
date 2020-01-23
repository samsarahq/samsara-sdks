# Grabs most recent swagger
rm -f swagger.json
wget https://raw.githubusercontent.com/samsarahq/api-docs/master/swagger.json

# Fix swagger
python3 fix-description.py
python3 fix-inline-schemas.py

# Generate python sdk off of fixed swagger
rm -rf python-sdk
openapi-generator generate -i swagger.json -o python-sdk -g python --package-name samsara