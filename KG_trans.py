import json
import csv

def process_json(record, parent_key=None, is_root=False):
    triples = []
    for key, value in record.items():
        if isinstance(value, dict):
            if parent_key:
                triples.append((key, 'type', parent_key))
            triples.extend(process_json(value, key))
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    triples.extend(process_json(item, key))
                else:
                    if is_root:
                        triples.append((item, 'type', key))
                    else:
                        triples.append((parent_key, key, item))
        else:
            triples.append((parent_key, key, value))
    return triples

# 打开 CSV 文件以写入数据
with open('KG_result.csv', 'w', newline='', encoding='utf-8') as csvfile, \
     open('KG_output_handled.json', 'w', encoding='utf-8') as jsonfile:

    fieldnames = ['Subject', 'Predicate', 'Object']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    jsonfile.write("[\n")  # 写入 JSON 数组的起始括号

    first_record = True  # 标记是否是第一个记录

    with open('KG_output.json', 'r', encoding='utf-8') as file:
        data = file.readlines()

        for line in data:
            try:
                # 加载每一行的 JSON 数据
                record = json.loads(line.strip())
                output = json.loads(record['output'])

                # 将解析好的 output 写入到 KG_output_handled.json 文件
                if not first_record:
                    jsonfile.write(",\n")
                json.dump(output, jsonfile, ensure_ascii=False, indent=4)
                first_record = False

                # 生成并写入三元组到 CSV 文件
                triples = process_json(output, is_root=True)
                for triple in triples:
                    writer.writerow({'Subject': triple[0], 'Predicate': triple[1], 'Object': triple[2]})
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
            except KeyError as e:
                print(f"Missing key in JSON record: {e}")

    jsonfile.write("\n]")  # 写入 JSON 数组的结束括号

print("KG_result.csv and KG_output_handled.json files have been created successfully.")