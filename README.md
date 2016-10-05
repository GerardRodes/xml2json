# xml2json
Light and simple class to parse a `xml` file to a `json` dictionary

##How to use
Just import the module and call it providing the path to the XML file as parameter.  
It will store the dictionary at the `json` attribute.
```python
from Xml2json import Xml2json

print Xml2json('./example.xml').json
```

##How it looks like
It will parse a XML like this:
```xml
<?xml version="1.0"?>
<data hey="I am" testing="attributes">
  <country name="Liechtenstein">
    <rank>1</rank>
    <year>2008</year>
    <gdppc>141100</gdppc>
    <neighbor name="Austria" direction="E"/>
    <neighbor name="Switzerland" direction="W"/>
  </country>
  <country name="Singapore">
    <rank>4</rank>
    <year>2011</year>
    <gdppc>59900</gdppc>
    <neighbor name="Malaysia" direction="N"/>
  </country>
  <country name="Panama">
    <rank>68</rank>
    <year>2011</year>
    <gdppc>13600</gdppc>
    <neighbor name="Costa Rica" direction="W"/>
    <neighbor name="Colombia" direction="E"/>
  </country>
</data>
```

Into this:
```json
{
  "data": {
    "@hey": "I am", 
    "@testing": "attributes", 
    "country": [
      {
        "@name": "Liechtenstein", 
        "gdppc": "141100", 
        "neighbor": [
          {
            "@direction": "E", 
            "@name": "Austria"
          }, 
          {
            "@direction": "W", 
            "@name": "Switzerland"
          }
        ], 
        "rank": "1", 
        "year": "2008"
      }, 
      {
        "@name": "Singapore", 
        "gdppc": "59900", 
        "neighbor": null, 
        "rank": "4", 
        "year": "2011"
      }, 
      {
        "@name": "Panama", 
        "gdppc": "13600", 
        "neighbor": [
          {
            "@direction": "W", 
            "@name": "Costa Rica"
          }, 
          {
            "@direction": "E", 
            "@name": "Colombia"
          }
        ], 
        "rank": "68", 
        "year": "2011"
      }
    ]
  }
}
```
