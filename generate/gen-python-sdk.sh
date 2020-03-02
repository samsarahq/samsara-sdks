#!/bin/bash
GEN_DIR='generate'
# Grabs most recent swagger
# rm -f swagger.json
# wget https://raw.githubusercontent.com/samsarahq/api-docs/master/swagger.json

# Fix swagger
python3 $GEN_DIR/fix-description.py swagger.json
python3 $GEN_DIR/remove-tags.py swagger.json

# Generate python sdk off of fixed swagger
rm -rf python-sdk
openapi-generator generate -i swagger.json -o python-sdk -g python --package-name samsara