with open("newfile.txt", "w") as file_content:
    file_content.write("Python is fun!")

with open("newfile.txt", "r") as file_content:
    file_contains = file_content.read()
    print(file_contains)