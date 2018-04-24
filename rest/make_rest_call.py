#!/usr/bin/python

import requests
import base64
url="http://localhost:7474/db/data/transaction/commit"

data_create_node = """{
  "statements" : [ {
    "statement" : "CREATE (n) RETURN id(n)"
  } ]
}
"""

data_create_properties = """
{"statements":[
      {"statement":"CREATE (p:PersonThing {firstName:{name}}) RETURN p",
       "parameters":{"name":"Daniel"}}
    ]}
"""

data_get_node = """
{
  "statements" : [ {
    "statement" : "MATCH (n) RETURN id(n)"
  } ]
}
"""

data_delete_node = """
{
  "statements" : [ {
    "statement" : "MATCH (n) DETACH DELETE n"
  } ]
}
"""

#Create header
pwd_string = b"neo4j:jkon-611"
encoded = base64.b64encode(pwd_string)
auth_string = 'Basic ' + encoded.decode('utf-8')
print(auth_string)
auth_header={'Authorization':auth_string}

#Requests
response = requests.post(url , data=data_create_properties, headers=auth_header)
print(response)
print(response.text)




