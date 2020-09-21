import yaml

def read_data(file):
    f = open(file, "r", encoding="utf-8")
    data = f.read()
    yamldata = yaml.load(data)
    return yamldata