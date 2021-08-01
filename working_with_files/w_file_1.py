with open("Kamal Uddin@DESKTOP-05SHTCE MINGW64 /h/Mahdi Hasan/Pithon/example.txt","r") as reader:
    print(reader.read())

with open("example.txt","r") as reader:
    for line in reader:
        print("Line:",line)

with open("example.txt","r") as reader:
    print(reader.readlines())


with open("example.txt","r") as reader:
    for line in reader.readlines():
        print(line)

with open("example.txt","r") as reader:
    for line in reader.readlines():
        print(line.upper())

with open("example.txt","r") as reader:
    for line in reader.readlines():
        print(line.lower())


with open("example.txt","r") as reader:
    for line in reader.readlines():
        if "mahdi" in line:
            print(line)

with open("example.txt","r") as reader:
    for line in reader.readlines():
        if "mahdi" in line:
            print(line.upper())

with open("example.txt","r") as reader:
    for line in reader.readlines():
        if "mahdi" in line:
            print(line.lower())







