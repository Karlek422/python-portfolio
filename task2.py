import json

def generate_table(json_data):
    students = []
    for student in json_data['students']:
        if int(student['Grade']) > 75:
            students.append((student['Name'], student['Grade'], student['Course']))

    table = []
    for student in students:
        table.append([student[0], student[1], student[2]])

    return table

# Приклад використання
data = '''
{
    "students": [
        {"Name": "Alice", "Grade": "90", "Course": "1"},
        {"Name": "Bob", "Grade": "70", "Course": "1"},
        {"Name": "Charlie", "Grade": "85", "Course": "1"},
        {"Name": "Dave", "Grade": "60", "Course": "1"}
    ]
}
'''

table = generate_table(json.loads(data))
for row in table:
    print('|'.join(row))