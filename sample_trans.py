import json

# 读取sample.txt文件
with open('sample.txt', 'r', encoding='utf-8') as file:
    lines = file.read().splitlines()

# 创建一个列表来存储JSON对象
json_list = []
for line in lines:
    json_list.append({"text": line, "relation": []})

# 将结果写入sample.json文件
with open('sample.json', 'w', encoding='utf-8') as outfile:
    for item in json_list:
        json_str = json.dumps(item, ensure_ascii=False)
        outfile.write(json_str + '\n')

print("Conversion completed successfully.")