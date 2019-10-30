###EXAMPLE
import json
my_file = open("example.json", "r")
json_string = my_file.read()
# .read() returns your entire example.json file as one string
my_dict = json.loads(json_string)
my_file.close()
