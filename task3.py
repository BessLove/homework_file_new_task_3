import os

path = '.'
def count_strings(path: str):
    files_list = os.listdir(path)
    file_content_dict = {}
    for element in files_list:
        if element.rfind('.txt', -4) >= 0:
            with open(element, 'r', encoding='utf-8') as file:
                file_content_dict[element] = file.readlines()
    with open('file_counted_strings', 'w', encoding='utf-8') as file:
        for file_name, rows in sorted(file_content_dict.items(), key= lambda x: len(x[1])):
            file.write(file_name + '\n')
            file.write(str(len(rows)) + '\n')
            if '\n' not in rows[-1]:
                rows[-1] += '\n'
            file.write(''.join(rows))

count_strings(path)

