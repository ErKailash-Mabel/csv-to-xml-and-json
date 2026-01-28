# json_writer.py
import json
from transformer import XMLConfig, CSVReader, Transformer


class JSONWriter:
    def write(self, root_name, data, file_path):
        output = {
            root_name: {
                "EMPLOYEE": data
            }
        }

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=2)


if __name__ == "__main__":
    with open("employees.csv") as f:
        csv_data = f.read()

    with open("config.xml") as f:
        xml_config = f.read()

    config = XMLConfig(xml_config)
    reader = CSVReader(csv_data)
    transformer = Transformer(config, reader)

    data = transformer.transform()

    JSONWriter().write("EMPLOYEES", data, "output.json")
    print("✅ JSON generated successfully")
