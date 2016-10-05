import xml.etree.ElementTree as ET

class Xml2json:

  def __init__(self, filePath):
    self.tree = ET.parse(filePath)
    self.json = self.parseXml(self.tree.getroot(), {})
    
    
    
  def parseXml(self, treeElement, json, isRoot = True):
    
    element = {'text':None}
    
    if treeElement.text:
      text = treeElement.text.strip()
      element['text'] = text if text != '' else None
    
    for attr in treeElement.attrib:
      element['@'+attr] = treeElement.attrib[attr]
    
    
    childDone = []
    
    for children in treeElement:
      if children.tag not in childDone:
        childDone.append(children.tag)
        siblings = treeElement.findall(children.tag)
        
        if len(siblings) > 1:
          element[children.tag] = []
          for i, sibling in enumerate(siblings):
            element[children.tag].append({})
            element[children.tag][i] = self.parseXml(sibling, element[children.tag][i], isRoot=False)

    if isRoot:
      return {treeElement.tag: element}
    else:
      return element