#file handling in python allow you to write ,append and modify files stored on your system
#File Modes
# Mode	Description
# r	Read file (default mode)
# w	Write file (creates new file or overwrites existing content)
# a	Append data at the end of the file
# x	Create a new file; error if file already exists
# b	Binary mode (for images, videos, PDFs, etc.)
# t	Text mode (default mode for text files)

# file = open("data.txt","r")
# print(file.read())
# file.close()

# file = open("data.txt", "w")
# file.write("Hello Aashish")
# file.close()

# file = open("data.txt", "a")
# file.write("\nWelcome")
# file.close()

# file = open("newfile.txt", "x")
# file.close()

# file = open("image.jpg", "rb")
# data = file.read()
# file.close()

# file = open("data.txt", "rt")
# print(file.read())
# file.close()


#string in file habndling
with open("data.txt", "r") as file:
    content = file.read()

word = "this"
count = content.count(word)

print(f"'{word}' appears {count} times")

#4 reading line by line 
with open("data.txt", "r") as f:
    for line in f:
        print(line)
#file existence & detection (using OS)
import os

if os.path.exists("data.txt"):
    os.remove("data.txt")
    print("File deleted") 

