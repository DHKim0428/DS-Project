from xml.etree.ElementTree import *


root = Element("root")

SubElement(root, "one")
SubElement(root, "two")
SubElement(root, "three")
SubElement(root, "four")

ElementTree(root).write("testfile.xml")
dump(root)

newtree = parse("testfile.xml")
newroot = newtree.getroot()

dump(newroot)
