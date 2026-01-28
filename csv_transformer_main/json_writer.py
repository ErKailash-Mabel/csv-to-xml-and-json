import json


class JSONWriter:
    def write(self, root_name, data, file_path):
        output = {
            root_name: {
                "EMPLOYEE": data
            }
        }

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=2)
