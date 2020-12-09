import os
path = input('\nPodaj folder w ktorym znajduja sie napisy do poprawienia\n')

all_files = os.listdir(path)
print(all_files)
srt_files = []
for file in all_files:
	if ('.srt' in file):
		srt_files.append(file)
print(srt_files)

for filename in srt_files:

	input_file = open(path + '\\' + filename, 'r', encoding='utf-8')
	file_in_array = input_file.readlines()
	input_file.close()
	new_array = []

	output_file = open(path + '\\' + filename, 'w', encoding='utf-8')
	for line in file_in_array:
		line = line.replace('¹', 'ą')
		line = line.replace('œ', 'ś')
		line = line.replace('Œ', 'ś')
		line = line.replace('ê', 'ę')
		line = line.replace('æ', 'ć')
		line = line.replace('¿', 'ż')
		line = line.replace('Ÿ', 'ź')
		line = line.replace('³', 'ł')
		line = line.replace('ñ', 'ń')
		line = line.replace('ñ', 'ń')
		line = line.replace('¯', 'ż')
		new_array.append(line)
	print(new_array)
	output_file.writelines(["%s" % item for item in new_array])
	output_file.close()
	del file_in_array[:]
	del new_array[:]