from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}.")

in_file = open(from_file) .read()

print(f"The input is {len(in_file)} bytes long.")

print(len("Testing more len."), "bytes long.")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit ENTER to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w') .write(in_file)

print("Alright, all done.")
