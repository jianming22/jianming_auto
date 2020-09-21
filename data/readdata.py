import yaml
import os

def read_data(file):
    f = open(file, "r", encoding="utf-8")
    data = f.read()
    yamldata = yaml.load(data)
    return yamldata




if __name__ == '__main__':

    a = read_data(file="userdata.yaml")
    print(a)