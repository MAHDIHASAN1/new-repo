# Working with files in python

# Create, Read, Write/Update, Delete
# text, xml, pdf, json, jpg
# Open(name, mode)
# r, w, a, x, +

try:
    f = open("data.txt","x")
    f.close()
except:
    print("File already exists")


# Write to file in python

write_name = open("data.txt","w")
write_name.write("Hi,mahdi hasan")
write_name.close()


# Read file

read_name = open("data.txt","r")

print(read_name.read())
read_name.close()


#update data in file
append_name = open("data.txt","a")
append_name.write("\nhello Bangladash")


with open("data.txt","r+") as f:
    print(f.read())






