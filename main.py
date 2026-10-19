from pathlib import Path
import os

def create_folder():
    try:
        name = ("Plase tell the your folder name")
        p = Path(name)
        p.mkdir()  #Create a new directory at this given path folder
        print("foder created successfully")
    except Exception as err:
        print(f"sorry an error ocured {err}")

def read_file_folder():
    p = Path("")
    items = list(p.rglob('*'))
    for i, v in enumerate(items):
        print(f"{i+1} : {v}")

def update_folder():
    try:
        read_file_folder()
        old_name = input("Please which folder want to update :- ")
        p = Path(old_name)
        if p.exists and p.is_dir:
            new_name = input("Please tell your new folder name :- ")
            new_p = Path(new_name)
            p.rename(new_p)
            print("your folder nmae is updated successfuliy")
        else:
                print("sorry No such folder exist ")
    except Exception as err:
        print(f"An error are ocuured {err} ")

def delte_folder():
        try:
          
            read_file_folder()
            name = input("plsase tell the want to delete folder name :- ")
            p = Path(name)
            if p.exists() and p.is_dir():
                p.rmdir()
                print("your folder delted successfully")
            else:
                print("No such folder exist")
        except Exception as err:
            print(f"there was an error as {err}")

def create_file():
      try:
        read_file_folder()
        name = input("Plase tell the your file name")
        p = Path(name)
        if not p.exists():
            with open(name,"w") as ps:
                name = input("write what you want in this file :- ")
                ps.write(name)
                print("file created successfully")
        else:
            print("sorry this file name already exist")
      except Exception as err:
          print(f"An error are ocucced {err}")
  
          




print("Options :- ")

print("1. Create a folder")
print("2. Read files and folder")
print("3. Update the folder")
print("4. Delete the folder")
print("5. Creat a file")
print("6. Read a file")
print("7. Update a file")
print("8. Delete a file")

choose = (int(input("please choose the options")))
if choose == 1:
    create_folder()

if choose == 2:
    read_file_folder()

if choose == 3:
    update_folder()

if choose == 4:
    delte_folder()

if choose == 5:
    create_file()
