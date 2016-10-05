from Xml2json import Xml2json
import json

print json.dumps(Xml2json('./example.xml').json,indent=2,sort_keys=True)