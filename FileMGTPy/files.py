import os
# r=Read
# a=Append
# w=Write
# x=Create

f1='G:\\MERN STACK Github\\Python\\Project Folder\\FileMGTPy\\names.txt'
f2='G:\\MERN STACK Github\\Python\\Project Folder\\FileMGTPy\\context.txt'
f3='G:\\MERN STACK Github\\Python\\Project Folder\\FileMGTPy\\more_names.txt'


#? read operation - error if it doesn't exist

# file=open('\\FileMGTPy\\names.txt','r')
# print(file.read)
intended_ops='r'
file=open('G:\\MERN STACK Github\\Python\\Project Folder\\FileMGTPy\\names.txt',intended_ops)
#print(file.read())

# print(file.read(4))
# print(file.readline())

# for line in file:
#   print(line)

# file.close()


# try:
#   file=open('G:\\MERN STACK Github\\Python\\Project Folder\\FileMGTPy\\names.txt')
#   print(file.read())
# except:
#   print('File not found')
# finally:
#   file.close()

#? Append -created the file if it doesn't exist

# f=open('G:\\MERN STACK Github\\Python\\Project Folder\\FileMGTPy\\names.txt','a')
# f.write('\nNeil')
# f.close()


# f=open('G:\\MERN STACK Github\\Python\\Project Folder\\FileMGTPy\\names.txt')
# print(f.read())
# f.close()

#? Write - overwrite data in the file
# intended_ops='w'
# file=open(f2,intended_ops)
# file.write('I deleted all the context')
# file.close()

# file=open(f2,'r')
# print(file.read())

#? Create - create a file if it doesn't exist
#! opens a file for writing, creates the file if it doesn't exist
# intended_ops='w'
# file=open('FileMGTPy\\create_new_file.txt',intended_ops)
# file.close()

#? Creates a new file if it doesn't exist but returns an error if it does

# if not os.path.exists('FileMGTPy\\mithu.txt'):
#   file=open('FileMGTPy\\mithu.txt','x')
#   file.close()

#? Delete a file
# Avoid error by using a If statement, incase the file doesn't exist

# if os.path.exists('FileMGTPy\\mithu.txt'):
#   os.remove('FileMGTPy\\mithu.txt')
# else:
#   print('The file you wish to delete does not exist')

with open (f3) as file:
  content=file.read()


intended_ops='w'
with open(f1,intended_ops) as file:
  file.write(content)

