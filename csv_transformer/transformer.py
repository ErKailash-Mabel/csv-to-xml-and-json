import csv
import xml.etree.ElementTree as ET
from collections import defaultdict


def col_letter_to_index(letter: str) -> int:
    return ord(letter.upper()) - ord('A')


class XMLConfig:
    def __init__(self, xml_string: str):
        self.root = ET.fromstring(xml_string)
        self.keyfield = col_letter_to_index(self.root.attrib["KEYFIELD"])
        self.from_row = int(self.root.attrib.get("FROMROW", 1)) - 2
        self.to_row = int(self.root.attrib.get("TOROW", 10**9))
        self.entity_node = self.root.find("EMPLOYEE")


class CSVReader:
    def __init__(self, csv_text: str):
        rows = list(csv.reader(csv_text.strip().splitlines()))
        self.data = rows[1:]

    def get_rows(self, start, end):
        return self.data[start:end]


class Transformer:
    def __init__(self, config: XMLConfig, csv_reader: CSVReader):
        self.config = config
        self.csv = csv_reader

    def transform(self):
        grouped = defaultdict(list)

        for row in self.csv.get_rows(self.config.from_row, self.config.to_row):
            key = row[self.config.keyfield]
            grouped[key].append(row)

        return self._build_objects(grouped)

    def _build_objects(self, grouped_rows):
        results = []

        for rows in grouped_rows.values():
            base_row = rows[0]
            obj = {}

            for node in self.config.entity_node:
                if node.attrib.get("SCROLL") == "YES":
                    obj[node.tag] = self._build_scroll(node, rows)
                else:
                    obj.update(self._build_simple(node, base_row))

            results.append(obj)

        return results

    def _build_simple(self, node, row):
        result = {}

        if "COLUMNREFERENCE" in node.attrib:
            idx = col_letter_to_index(node.attrib["COLUMNREFERENCE"])
            result[node.tag] = row[idx]
        else:
            for child in node:
                idx = col_letter_to_index(child.attrib["COLUMNREFERENCE"])
                result[child.tag] = row[idx]

        return result

    def _build_scroll(self, node, rows):
        items = []

        for row in rows:
            item = {}
            for child in node:
                idx = col_letter_to_index(child.attrib["COLUMNREFERENCE"])
                item[child.tag] = row[idx]
            items.append(item)

        return items
