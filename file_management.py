file=open("tops1.txt", "w")
s="hello world"
file.write(s)
file.close()
print("File Written successfully")
print("***************************************")

file=open("tops1.txt", "r")
print(file.read())
file.close()
print("File read successfully")
print("***************************************")

file=open("tops1.txt", "a")
file.write("\nThis file is appended")
file.close()
print("File Appended successfully")
print("***************************************")

file=open("tops2.txt", "w+")
file.write("New Text!!!")
print("Current file position = ", file.tell())
file.seek(0)
print(file.read())
file.close()
print("File Written & Read successfully")
print("***************************************")