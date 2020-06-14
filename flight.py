import http.client
import ssl
import json
import ast

conn = http.client.HTTPSConnection("lf-apic-gw.hcnorway.com",context=ssl._create_unverified_context())

headers = {
    'x-ibm-client-id': "90f18553d594ac626f19d49b6b3a9c6f",
    'accept': "application/json"
    }

conn.request("GET", "/mydeveloperorganization/apa/flight-info/flight?flightcode=DY431", headers=headers)

res = conn.getresponse()
data = res.read()

jsonobj= json.loads(data)

fldata = str(jsonobj['data'])
print(fldata)

fldataarr = json.loads(fldata)






