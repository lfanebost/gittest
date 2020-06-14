import http.client
import ssl
import json

# Helper to extract values
def extract_values(obj, key):
    """Pull all values of specified key from nested JSON."""
    arr = []

    def extract(obj, arr, key1):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    tekst = str(v)
                    arr.append(tekst)              
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    results = extract(obj, arr, key)
    return results

country="norway"
conn = http.client.HTTPSConnection("lf-apic-gw.hcnorway.com",context=ssl._create_unverified_context())

headers = {
    'x-ibm-client-id': "eb2b7ac9d2917ce59b6c0d10bdd858f4",
    'accept': "application/json"
    }

conn.request("GET", "/mydeveloperorganization/apa/covid-19-norway-stats/covid-"+country, headers=headers)

res = conn.getresponse()
data = res.read()
#print(data)
jsonobj= json.loads(data)

str1 = ""
total_infected = str1.join(extract_values(jsonobj, "infected"))
total_deaths = str1.join(extract_values(jsonobj, "deaths"))
total_tested = str1.join(extract_values(jsonobj, "tested"))

print (" ")
print("REPORT FOR " + country.upper())
print(" ")
print("Total infected: " + total_infected + "\tTotal deaths: " + total_deaths + "\tTotal tested: " + total_tested)
print (" ")



region = extract_values(jsonobj, "region") 
infectedcount = extract_values(jsonobj, "infectedCount")
deathcount = extract_values(jsonobj, "deathCount")
intensivecarecount = extract_values(jsonobj, "intensiveCareCount")
str1 = ""
arrlen = len(region)

if arrlen > 0:
    print("PER REGION")
    print("------------------")
    i = 0
    while i < arrlen:
        region_str = str1.join(region[i])
        infectedcount_str = str(infectedcount[i])
        
        if len(deathcount) > 1:
            deathcount_str = str(deathcount[i])
        else:
            deathcount_str = "not reported"
        if len(intensivecarecount) > 1:
            intensivecarecount_str = str(intensivecarecount[i])
        else:
            intensivecarecount_str = "not reported"
        
        print(region_str + ", Infected count: "+ infectedcount_str + ", Death count: " + deathcount_str + ", Intensive count: " + intensivecarecount_str)
        i += 1
else:
    print("No numbers reported per region")