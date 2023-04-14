#so if we move file to desktop then we need a absolute directory
# open and read the file
# with open("/Users/harry/Desktop/new_file.txt") as file:
#     contents = file.read()
#     print(contents)

# write into file w stands for "write" and it overwrites all of the content
# a is "append" so it adds to the file and r is "read only"
# with open("new_file.txt", mode="w") as file:
#     file.write("new text.")

# if file doesn't exist we can make it by typing open in write mode

#here is a relative file path so we go back to desktop and then choose file
with open("../../../Desktop/new_file.txt") as file:
    contents = file.read()
    print(contents)