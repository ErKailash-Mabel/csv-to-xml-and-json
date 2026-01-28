How It Works

1. CSVReader
-> Reads CSV and stores rows (excluding header)

2. XMLConfig
-> Parses mapping rules from config.xml
-> Converts column letters to index numbers

3. Transformer
-> Groups rows by KEYFIELD
-> Builds objects using:
   -> Simple nodes (single value)
   -> Scroll nodes (list of values)

4. Writers
-> XMLWriter → writes XML file
-> JSONWriter → writes JSON file

▶️ Running the Project
    Open Terminal
    Redirect to your folder of Transformer

    Then Paste commands in the terminal-
	python3 xml_writer.py
	python3 json_writer.py

Output

output.xml
output.json
