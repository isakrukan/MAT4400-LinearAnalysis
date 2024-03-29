import os

try:
    with open(".gitignore", "r") as file:
        for line in file:
            if line[0] == "*":
                delete_this = line[1:].strip()
                os.system(f"rm *{delete_this}")
except:
    with open("../.gitignore", "r") as file:
        for line in file:
            if line[0] == "*":
                delete_this = line[1:].strip()
                os.system(f"rm *{delete_this}")