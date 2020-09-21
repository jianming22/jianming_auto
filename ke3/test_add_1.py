import yaml
import os
curpath = os.path.dirname(os.path.realpath(__file__))
yamlpath = os.path.join(curpath, "data.yaml")
fd = open(yamlpath, "r", encoding="utf-8")
data1 = fd.read()
print(data1)