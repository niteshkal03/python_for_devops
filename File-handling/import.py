# import os
# print(os.curdir)

# context manager
# with open("demo.txt", "a") as file:
#     file.write("this is new content of file")
#     file.write("asd")
#     print("file written")

# server_list=['prod_server', "test_server", "dev_server"]
# for i in server_list:
#     with open(f"{i}.txt", "w") as file:
#         print(i, "file Created....")

# with open(f"demo.txt", "a") as file:
#         file.write("file Created....")


#extract all numbers from paragraph 
para = """
What is Lorem Ipsum?
Lorem Ipsum is simply dummy text of
the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard 
dummy text ever since 1966, when designers 
at Letraset and James Mosley, the librarian
at St Bride Printing Library in London, 
took a 1914 Cicero translation and scrambled
it to make dummy text for Letraset's Body 
Type sheets. It has survived not only many 
decades, but also the leap into electronic 
typesetting, remaining essentially unchanged.
It was popularised thanks to these sheets    
and more recently with desktop publishing software 
like Aldus PageMaker and Microsoft Word including 
versions of Lorem Ipsum.
"""
# only_digits.txtW
count_digits = 0
total_char = 0
for i in para:
        if i in "0123456789":
                count_digits+=1
        else:
                total_char+=1
with open(f"demo.txt", "w") as file:
        file.write(f"Total digit in file: {count_digits}")
        file.write("\n")
        file.write(f"Total chars in file : {total_char}")
