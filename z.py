#  Write a Python program to create a copy of its own source
#  code.

def file_copy(src, dest):
    with open(src) as f, open(dest,'w') as d:
            for line in f:
                 d.write(line)
                 
file_copy("self_copy.py","z.py")

with open('z.py','r') as filehandle:
    for line in filehandle:
        print(line,end='')
