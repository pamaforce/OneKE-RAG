import json
import csv

# 打开 JSON 文件
with open('SPO_output.json', 'r', encoding='utf-8') as file:
    data = file.readlines()

# 打开 CSV 文件以写入数据
with open('SPO_result.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Subject', 'Predicate', 'Object']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # 打开 JSON 文件以写入处理后的数据
    with open('SPO_output_handled.json', 'w', encoding='utf-8') as jsonfile:
        handled_data = []

        for line in data:
            record = json.loads(line.strip())
            output = json.loads(record['output'])

            for predicate, relations in output.items():
                for relation in relations:
                    subject = relation.get('subject')
                    obj = relation.get('object')
                    writer.writerow({'Subject': subject, 'Predicate': predicate, 'Object': obj})
                    
                    # 将处理后的数据添加到 handled_data 列表中
                    handled_record = {
                        'Subject': subject,
                        'Predicate': predicate,
                        'Object': obj
                    }
                    handled_data.append(handled_record)
        
        # 将处理后的数据写入 JSON 文件
        json.dump(handled_data, jsonfile, ensure_ascii=False, indent=4)

print("SPO_result.csv and SPO_output_handled.json files have been created successfully.")