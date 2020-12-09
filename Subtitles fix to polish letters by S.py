import os

path = os.path.dirname(os.path.abspath(file))

all_files = os.listdir(path)
files = []
for file in all_files:
    if '.srt' in file:
        files.append(file)

for filename in files:
    with open(path + '\' + filename, 'r+', encoding='utf-8') as file:
        file_in_array = []

        for line in file:
            formatted_line = line.replace('¹', 'ą').replace('œ', 'ś').replace('ê', 'ę').replace('æ', 'ć').replace('¿', 'ż').replace('Ÿ', 'ź').replace('³', 'ł').replace('Œ', 'ś').replace('ñ', 'ń')
            file_in_array.append(formatted_line)
            print(formatted_line)

        file.truncate(0)
        file.writelines(file_in_array)

        file.close()