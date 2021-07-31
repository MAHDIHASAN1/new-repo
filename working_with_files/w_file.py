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

write_name = open("data.txt","w")

write_name.write("Hi,mahdi hasan")
write_name.close()









