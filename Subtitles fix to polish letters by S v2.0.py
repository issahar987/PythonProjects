import os

path = os.path.dirname(os.path.abspath(file))
chars = {'¹': 'ą', 'œ': 'ś', 'ê': 'ę', 'æ': 'ć', '¿': 'ż', 'Ÿ': 'ź', '³': 'ł', 'Œ': 'ś', 'ñ': 'ń'}

all_files = os.listdir(path)
files = []
for file in all_files:
    if '.srt' in file:
        files.append(file)

for filename in files:
    with open(path + '\' + filename, 'r+', encoding='utf-8') as file:
        file_in_array = []

        for line in file:
            formatted_line = line.translate(str.maketrans(chars))
            file_in_array.append(formatted_line)
            print(formatted_line)

        file.truncate(0)
        file.writelines(file_in_array)