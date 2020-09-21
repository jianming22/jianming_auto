import yaml
import os


curpath = os.path.dirname(os.path.realpath(__file__))
yamlpath = os.path.join(curpath, "data.yaml")

f = open(yamlpath, "r", encoding='utf-8')
datas = f.read()
# print(data1)
dd = yaml.load(datas)
print(dd["test_adduser_params"][0]["username"])
