import xml.etree.ElementTree as ET


class XMLWriter:
    def write(self, root_name, data, file_path):
        root = ET.Element(root_name)

        for obj in data:
            entity = ET.SubElement(root, "EMPLOYEE")

            for key, value in obj.items():
                if isinstance(value, list):
                    for item in value:
                        child = ET.SubElement(entity, key)
                        for k, v in item.items():
                            ET.SubElement(child, k).text = str(v)
                else:
                    ET.SubElement(entity, key).text = str(value)

        tree = ET.ElementTree(root)
        tree.write(file_path, encoding="utf-8", xml_declaration=True)
