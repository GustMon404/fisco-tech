from lxml import etree

xsd_tree = etree.parse('v2-04.xsd')
xsd_schema = etree.XMLSchema(xsd_tree)

root_element = xsd_schema.root_element()

# Cria um XML a partir do elemento raiz
xml_tree = etree.ElementTree(root_element)
xml_str = etree.tostring(xml_tree, pretty_print=True, encoding='UTF-8', xml_declaration=True)
print(xml_str)
