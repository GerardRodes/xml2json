import xml.etree.ElementTree as ET
import json as J

class Xml2json:

	def __init__(self, filePath):
		self.tree = ET.parse(filePath)
		self.json = self.parseXml(self.tree.getroot(), {})
		
		
		print J.dumps(self.json, indent=2, sort_keys=True)
		
		
	def parseXml(self, treeElement, json, isRoot = True):
		
		element = {}
		
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
				else:
					element[children.tag] = children.text

		if isRoot:
			return {treeElement.tag: element}
		else:
			return element