
#Context Managers for File Handling: 
#Use the with statement and context managers to open and close a file. 
#Handle potential IOError within the with block for clean resource management.
try:
    with open(r"C:\Users\Cloud\Downloads\lorem-ipsum.txt", encoding="utf8") as f:
        c = f.read()
        print(c)
except Exception as e:
    print(e)


