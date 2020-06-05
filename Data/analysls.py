import yaml

data_list = []
with open("./search.yml","r",encoding="utf-8") as f:
    data = yaml.safe_load(f)
    print(data.values())
    for i in data.values():
        data_list.append((i.get("input"),i.get("exp")))




# data = {
#     'test_001': {'input': '1', 'exp': '休眠'},
#     'test_002': {'input': 'i', 'exp': 'IP地址'},
#     'test_003': {'input': 'm', 'exp': 'MAC地址'}
#  }