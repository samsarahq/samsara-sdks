# Fix swagger
python3 generate/fix-description.py swagger-test.json
python3 generate/fix-inline-schemas.py swagger-test.json

# Generate python sdk off of fixed swagger
rm -rf python-test-sdk
openapi-generator generate -i swagger-test.json -o python-test-sdk -g python --package-name samsara-test