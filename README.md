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
It will parse a XML file like this:
```xml
<?xml version="1.0"?>
<data hey="I am" testing="attributes">
  <test>1</test>
  <test>2</test>
  <test>3</test>
  <country name="Liechtenstein">
    <rank>1</rank>
    <year>2008</year>
    <gdppc>141100</gdppc>
    <neighbor name="Austria" direction="E">Lorem Ipsum</neighbor>
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
-_Attributes names are prefixed by '@'_  
-_Text stored at `text` attribute_
```json
{
  "data": {
    "@hey": "I am", 
    "@testing": "attributes", 
    "country": [
      {
        "@name": "Liechtenstein", 
        "gdppc": {
          "text": "141100"
        }, 
        "neighbor": [
          {
            "@direction": "E", 
            "@name": "Austria", 
            "text": "Lorem Ipsum"
          }, 
          {
            "@direction": "W", 
            "@name": "Switzerland"
          }
        ], 
        "rank": {
          "text": "1"
        }, 
        "year": {
          "text": "2008"
        }
      }, 
      {
        "@name": "Singapore", 
        "gdppc": {
          "text": "59900"
        }, 
        "neighbor": {
          "@direction": "N", 
          "@name": "Malaysia"
        }, 
        "rank": {
          "text": "4"
        }, 
        "year": {
          "text": "2011"
        }
      }, 
      {
        "@name": "Panama", 
        "gdppc": {
          "text": "13600"
        }, 
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
        "rank": {
          "text": "68"
        }, 
        "year": {
          "text": "2011"
        }
      }
    ], 
    "test": [
      {
        "text": "1"
      }, 
      {
        "text": "2"
      }, 
      {
        "text": "3"
      }
    ]
  }
}
```
