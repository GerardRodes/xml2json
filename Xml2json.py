import xml.etree.ElementTree as ET

class Xml2json:

  def __init__(self, filePath):
    self.tree = ET.parse(filePath)
    self.json = self.parseXml(self.tree.getroot())
    
    
    
  def parseXml(self, treeElement, isRoot = True):
    element = {}
    
    if treeElement.text:
      text = treeElement.text.strip()
      if text  != '':
        element['text'] = text
    
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
            element[children.tag][i] = self.parseXml(sibling, isRoot=False)
        else:
          element[children.tag] = self.parseXml(children, isRoot=False)

    if isRoot:
      return {treeElement.tag: element}
    else:
      return element
