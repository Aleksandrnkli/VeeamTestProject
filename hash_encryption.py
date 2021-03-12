import hashlib

def create_hash_summ(hash_type, filename, directory):
    if hash_type == "md5":
        h = hashlib.md5()
    elif hash_type == "sha1":
        h = hashlib.sha1()
    elif hash_type == "sha256":
        h = hashlib.sha256()
    else:
        return 0
    path = str(directory) + "/" + str(filename)
    with open(path, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)  # special limit on the number of characters to read, it could be changed if needed
            h.update(chunk)
    return h.hexdigest()
