import http.client
import ssl

conn = http.client.HTTPSConnection("lf-apic-gw.hcnorway.com",context=ssl._create_unverified_context())

headers = {
    'x-ibm-client-id': "90f18553d594ac626f19d49b6b3a9c6f",
    'accept': "application/xml"
    }

conn.request("GET", "/mydeveloperorganization/apa/avinor-info-norwegian-airports/avinor?airport=BGO&direction=D&lastupdate=2020-04-08T08:03:00", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))