from transformer import XMLConfig, CSVReader, Transformer
from xml_writer import XMLWriter
from json_writer import JSONWriter


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
    JSONWriter().write("EMPLOYEES", data, "output.json")

    print("✅ XML and JSON generated using separate writer modules")
