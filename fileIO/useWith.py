with open("data.txt", "w+") as f:
    f.write("Hello, World!")
    data = f.read()
    print(data)#empty because the file pointer is at the end of the file after writing

with open("data.txt", "r") as f:
    data = f.read()
    print(data)  # This will print "Hello, World!" because we are reading from the beginning of the file