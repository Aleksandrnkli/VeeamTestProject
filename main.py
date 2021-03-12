
file_dir = "D:/User/Desktop/new.txt"
dir = ""

file = open(file_dir, "r")
lines = file.readlines()
all_lines = {"filename": '', "hash": '', "key" : ''}
list = []
i = 0
for line in lines:
    try:
        inside_list = line.split(" ")
        all_lines["filename"], all_lines["hash"], all_lines["key"] = \
            inside_list[0], inside_list[1], inside_list[2]
        list.append(inside_list)
        print(list[i])
        i += 1
    except RuntimeError:
        print(f'There is a mistake in line {i+1}')
        continue






