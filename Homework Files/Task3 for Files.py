def open_file_count_lines(file, dictionary):
    with open (file, 'r', encoding="utf8") as f:
        count = sum(+1 for line in f)
        name = file.split(".")
        dictionary[file] = [count, name[0]]
        return dictionary

lenght_and_name = {}
open_file_count_lines('1.txt', lenght_and_name)
open_file_count_lines('2.txt', lenght_and_name)
open_file_count_lines('3.txt', lenght_and_name)

lenght_and_name_sorted = {}
sorted_keys = sorted(lenght_and_name, key=lenght_and_name.get)  # [1, 3, 2]
for w in sorted_keys:
    lenght_and_name_sorted[w] = lenght_and_name[w]

with open('newfile.txt', 'w', encoding="utf8") as file:
    for k, v in lenght_and_name_sorted.items():
        file.write((k) + '\n')
        file.write(str(v[0]) + '\n')
        with open(k,'r', encoding="utf8") as base:
            for i in range(1, v[0] + 1):
                # content = base.readline()
                file.write(f'Строка номер {i} файла номер {v[1]} {base.readline()}\n')
