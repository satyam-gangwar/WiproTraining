import json
import os


def write_json(filename):
    data={
        "people":[
            {"name": "Satyam", "age": 30},
            {"name": "Ram", "age": 22},

        ]
    }
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
        print(f"Wrote{filename} successfully")


def read_json(filename):
    with open(filename, "r") as file:
        data =json.load(file)
        for person in data["people"]:
            print(f"Name:{person['name']}, Age: {person['age']}")


def delete_json(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename} deleted successfully")
    else:
        print(f"{filename} does not exist")

filename = "data.json"
write_json(filename)
print("Data read from excel file:")
read_json(filename)
delete_json(filename)
