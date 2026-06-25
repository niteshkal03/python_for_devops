# stric mode
try:
    file =open("demo.txt", "x")
    print("File created")
except Exception as e:
    print("Error",e)

# 1.write mode file creation
file=open("new.demo.tx", "w") 
file.write("This is the file content")
print("new file created")