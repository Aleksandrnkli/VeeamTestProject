# VeeamTestProject
_Project created on Python 3.7
_Using sys and hashlib
_This projected was created as a test tasck for Veeam Software.
_Sart of developing 11.02.2021
_____________________________________________________

The VeeamTestProject made to check file indegnity using hash summ.

_____________________________________________________

STARTING PROGRAM
-----------------
To start program you have to put in command line:
>python program file_path files_dir
Where:
program - name of the programm files_integrity_check.py 
file_path - name of the file with paramaters in our example New.txt
files_dir - directory of the files that should be checked for integrity (test_files folder)
_____________________________________________________

WHAT DOES THE PROGRAM DO
------------------------
file New.txt contains lines with Name of the file, type of the encryption(md5,sha1 or sha256) and hash summ.

 New.txt
  file_1.txt md5 64b8dcc3d4b7e531a9b1fda02c2cbefa
  file_2.bin md5 d41d8cd98f00b204e9800998ecf8427e
  
Programm reads this lines and check indignity of each file. 
If file is integral result is TRUE
If not integral FALSE
If no such file NOT FOUND
_____________________________________________________

STRUCTURE
---------
VeeamTestProject 
___file_integrity_check.py
___hash_encrypting.py
___New.txt
___test_files
_____test_files.txt
______________________________________________________


