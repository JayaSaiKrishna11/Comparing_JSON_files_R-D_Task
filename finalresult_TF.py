import json
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))
#this is the syntax to change the json file to python script
with open('identity_mapping.json') as f:
    json_data = f.read()
#this is the syntax used to read the json file
identity_mapping = json.loads(json_data)
#identity_mapping is the element used to store the json data

#And I used same process for the identity_schema_latest file
os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open('id_schema_latest.json') as f:
    json_data = f.read()

identity_schema = json.loads(json_data)

result = "_______________________identity object_________________________\n"

identity_properties = identity_schema.get("properties", {}).get("identity", {}).get("properties", {})

for key, value in identity_mapping['identity'].items():
    if value.get('value') not in identity_properties:
        result += f"For {key} in identity_mapping value: {value} is missing from identity_schema\n"

result1 = "_______________________metaInfo object_________________________\n"

metaInfo_properties = identity_schema.get("properties", {}).get("metaInfo", {}).get("properties", {})

if "metaInfo" not in identity_mapping:
    result1 += "For metaInfo in identity_mapping: metaInfo field is missing from identity_schema\n"
else:
    for key in identity_mapping['metaInfo']:
        if key not in metaInfo_properties:
            result1 += f"For metaInfo {key} in identity_mapping: metaInfo {key} field is missing from identity_schema\n"

result2 = "_______________________audits object_________________________\n"

audits_properties = identity_schema.get("properties", {}).get("audits", {}).get("properties", {})

if "audits" not in identity_mapping:
    result2 += "For audits in identity_mapping: audits field is missing from identity_schema\n"
else:
    for key in identity_mapping['audits']:
        if key not in audits_properties:
            result2 += f"For audits {key} in identity_mapping: audits {key} field is missing from identity_schema\n"


result3 = "_______________________documents object_________________________\n"

documents_properties = identity_schema.get("properties", {}).get("identity", {}).get("properties", {})

for key, value in identity_mapping['documents'].items():
    if value.get('value') not in identity_properties:
        result3 += f"For {key} in identity_mapping value: {value} is missing from identity_schema\n"

print(result)
print(result1)
print(result2)
print(result3)