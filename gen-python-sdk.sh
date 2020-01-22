rm -f swagger.json
wget https://raw.githubusercontent.com/samsarahq/api-docs/master/swagger.json
python3 fix-swagger.py
rm -rf python-sdk
openapi-generator generate -i swagger.json -o python-sdk -g python --package-name samsara