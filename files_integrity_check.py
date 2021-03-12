import sys
from hash_encryption import create_hash_summ as chs

# file_path = "New.txt"
# directory = "./test_files"

def create_list_and_check_integrity(file_path, directory):

    file = open(file_path, "r", encoding='UTF-8')
    lines = file.readlines()
    i = 0
    for line in lines:
        try:
            line_info = {"filename": '', "hash_type": '', "hash_key" : ''}  #create voc to make information more readable
            inside_list = line.split(" ")
            try:
                if inside_list[0] != '' or inside_list[1] != '' or inside_list[2]!= '':
                    #put values from created list to easy readable vocabulary
                    line_info["filename"], line_info["hash_type"], line_info["hash_key"] = \
                    inside_list[0], inside_list[1].strip(), inside_list[2].rstrip()
                else:
                    print(f'There is not enough arguments in line {i + 1}') #if there is no one of argument
                    continue
            except IndexError:
                print(f'There is not enough arguments in line {i + 1}') #if one of the arguments equals to " "
                continue
            print(f'{line_info["filename"]}{check_integrity(line_info, directory)}')
            i += 1
        except RuntimeError:
            print(f'There is a mistake in line {i+1}')
            i += 1
            continue

def check_integrity(infoline, dir):
    try:
        result_hash = chs(infoline['hash_type'], infoline['filename'], dir )
        if infoline['hash_key'] == result_hash:
            return(' OK')
        elif result_hash == 0:
            return(f' No such hash encoding type {infoline["hash_type"]}')
        else:
            return(' FALSE')
    except FileNotFoundError:
        return(' NOT FOUND')


if __name__ == "__main__":
    create_list_and_check_integrity(sys.argv[1], sys.argv[2])



