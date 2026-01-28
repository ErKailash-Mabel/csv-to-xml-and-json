# xml_writer.py
import xml.etree.ElementTree as ET
from transformer import XMLConfig, CSVReader, Transformer


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


if __name__ == "__main__":
    with open("employees.csv") as f:
        csv_data = f.read()

    with open("config.xml") as f:
        xml_config = f.read()

    config = XMLConfig(xml_config)
    reader = CSVReader(csv_data)
    transformer = Transformer(config, reader)

    data = transformer.transform()

    XMLWriter().write("EMPLOYEES", data, "output.xml")
    print("✅ XML generated successfully")
