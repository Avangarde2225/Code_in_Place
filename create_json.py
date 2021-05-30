import json

def write_data():
    data = ["Rosamasa", "Silk Spectedre"]
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)


if __name__ == '__main__':
    print()