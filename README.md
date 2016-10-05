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
        "neighbor": [
          {
            "@direction": "E", 
            "@name": "Austria", 
            "text": "Lorem Ipsum"
          }, 
          {
            "@direction": "W", 
            "@name": "Switzerland", 
            "text": null
          }
        ], 
        "text": null
      }, 
      {
        "@name": "Singapore", 
        "text": null
      }, 
      {
        "@name": "Panama", 
        "neighbor": [
          {
            "@direction": "W", 
            "@name": "Costa Rica", 
            "text": null
          }, 
          {
            "@direction": "E", 
            "@name": "Colombia", 
            "text": null
          }
        ], 
        "text": null
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
    ], 
    "text": null
  }
}
```
