#enables us to write folders to paths, check the user platform, and create paths on any os
from pathlib import Path
import platform
from os import path

#list of pack pack formats
pack_formats = [4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 26, 41, 48, 57, 61]
format_check_successful = True

#defining for readability in rest of script
def create_path(path):
    try:
        Path(path).mkdir(parents=True, exist_ok=True)
    except:
        print("An exception occurred! The path given as an input was invalid.\nRestart the program and try copy-and-pasting your desired path directly from your File Explorer.")

def write_file(path, write_type, contents):
    with open(path, write_type) as f:
        f.write(contents)

def create_and_tag_pack_functions(format : str, file_path : str, name : str, namespace : str):
    if(format >= pack_formats[12]):
        create_path(path.join(file_path, name, "data", "minecraft", "tags", "function"))
        write_file(path.join(file_path, name, "data", "minecraft", "tags", "function", "load.json"), "w", "{\n    \"values\":\n    [\n        \"" + user_pack_namespace + ":load\"\n    ]\n}")
        write_file(path.join(file_path, name, "data", "minecraft", "tags", "function", "tick.json"), "w", "{\n    \"values\":\n    [\n        \"" + user_pack_namespace + ":tick\"\n    ]\n}")
        create_path(path.join(file_path, name, "data", namespace, "function"))
        write_file(path.join(file_path, name, "data", namespace, "function", "tick.mcfunction"), "w", "")
        write_file(path.join(file_path, name, "data", namespace, "function", "load.mcfunction"), "w", "")
    elif(format < pack_formats[12]):
        create_path(path.join(file_path, name, "data", "minecraft", "tags", "functions"))
        write_file(path.join(file_path, name, "data", "minecraft", "tags", "functions", "load.json"), "w", "{\n    \"values\":\n    [\n        \"" + user_pack_namespace + ":load\"\n    ]\n}")
        write_file(path.join(file_path, name, "data", "minecraft", "tags", "functions", "tick.json"), "w", "{\n    \"values\":\n    [\n        \"" + user_pack_namespace + ":tick\"\n    ]\n}")
        create_path(path.join(file_path, name, "data", namespace, "functions"))
        write_file(path.join(file_path, name, "data", namespace, "functions", "tick.mcfunction"), "w", "")
        write_file(path.join(file_path, name, "data", namespace, "functions", "load.mcfunction"), "w", "")

#checks format of user version; broken up into multiple functions for good practice
def get_user_format_a(version):
    match version:
        case "1.13" | "1.13.1" | "1.13.2" | "1.14" | "1.14.1" | "1.14.2" | "1.14.3" | "1.14.4":
            return pack_formats[0]
        case "1.15" | "1.15.1" | "1.15.2" | "1.16" | "1.16.1":
            return pack_formats[1]
        case "1.16.2" | "1.16.3" | "1.16.4" | "1.16.5":
            return pack_formats[2]
        case "1.17" | "1.17.1":
            return pack_formats[3]
        case "1.18" | "1.18.1":
            return pack_formats[4]
        case _:
            return 0

def get_user_format_b(version):
    match version:
        case "1.18.2":
            return pack_formats[5]
        case "1.19" | "1.19.1" | "1.19.2" | "1.19.3":
            return pack_formats[6]
        case "1.19.4":
            return pack_formats[7]
        case "1.20" | "1.20.1":
            return pack_formats[8]
        case "1.20.2":
            return pack_formats[9]
        case _:
            return 0
        
def get_user_format_c(version):
    match version:
        case "1.20.3" | "1.20.4":
            return pack_formats[10]
        case "1.20.5" | "1.20.6":
            return pack_formats[11]
        case "1.21" | "1.21.1":
            return pack_formats[12]
        case "1.21.2" | "1.21.3":
            return pack_formats[13]
        case "1.21.4":
            return pack_formats[14]
        case _:
            return 0

#checks each user format check to see whether it returned 0; returns 0 itself if all 3 checks return 0
def set_user_format(func_a, func_b, func_c):
    if func_a != 0:
        return func_a
    elif func_b != 0:
        return func_b
    elif func_c != 0:
        return func_c
    else:
        return 0

#getting user's desired path, pack name, pack version, and namespace
print("Welcome to SolusChristusG2F's Minecraft Datapack Wizard!\n")
user_path = str(input("Where would you like to create a data pack? Input a file path. (You can input an existing file path or a new one. If it is new, the application will create it).\nIf your path is detected to be invalid, the datapack will be created within a datapacks folder contained in the same\nfolder as the application.\n"))

if(platform.system() == "Linux" and not user_path.startswith("/")
   or platform.system() == "Darwin" and not user_path.startswith("/")):
    user_path = "datapacks"
elif (platform.system() == "Windows" and not ":" in user_path and "/" in user_path 
      or platform.system() == "Windows" and not ":" in user_path and "\\" in user_path):
    user_path = "datapacks"


user_version = str(input("What Minecraft version would you like to create a datapack for? Input a valid version of Minecraft such as 1.21.4\n(Datapacks were introduced in version 1.13).\n"))

user_format = set_user_format(get_user_format_a(user_version), get_user_format_b(user_version), get_user_format_c(user_version))

if user_format == 0:
    format_check_successful = False

user_pack_name = str(input("What would you like your pack to be named?\n"))
user_pack_namespace = str(input("What would you like the pack's namespace to be?\n"))

#creating inital pack folder
create_path(path.join(user_path, user_pack_name))

#creating pack.mcmeta file and writing proper code to it
write_file(path.join(user_path, user_pack_name, "pack.mcmeta"), "w", "{\n    \"pack\": {\n       \"description\": \"Replace with desired description.\",\n       \"pack_format\": " + str(user_format) + "\n  }\n}")

#creating pack's main data folder
create_path(path.join(user_path, user_pack_name, "data"))

#creating pack's namespaced data folder
create_path(path.join(user_path, user_pack_name, "data", user_pack_namespace))

#creating the data/minecraft and minecraft/tags/function(s) folders; checks user's pack format to see which file structure should be used, namely,
#folders either being named with the plural or singular, as changed in minecraft 1.21
create_path(path.join(user_path, user_pack_name, "data", "minecraft"))
create_path(path.join(user_path, user_pack_name, "data", "minecraft", "tags"))

create_and_tag_pack_functions(user_format, user_path, user_pack_name, user_pack_namespace)

if format_check_successful and user_path != "datapacks":
    print("\nThe data pack was successfully created at " + user_path + "! Check your desired path.")
elif format_check_successful and user_path == "datapacks":
    print("\nThe data pack was successfully created in the same folder as this application under a new folder titled \"datapacks\".\nIf this was unintended, it is likely that your inputted path was detected to be invalid for your OS.")
elif not format_check_successful and user_path != "datapacks":
    print("\nThe data pack was successfully created at " + user_path + ", but your inputted version was not detected as having a pack format.\nThe file format has been set to 0 and the pack has been created with a pre-1.21 file structure.\nYou will need to change the pack format to your desired version's format in the pack.mcmeta file.\nFormats for each version can be found on the Minecraft Wiki at https://minecraft.wiki/w/Data_pack, along with the proper file structure for your desired version.\n(See \"Folder structure\" and \"History\" sections of the Wiki page for more details).")
elif not format_check_successful and user_path == "datapacks":
    print("\nThe data pack was successfully created in the same folder as this application under a new folder titled \"datapacks\".\nIf this was unintended, it is likely that your inputted path was detected to be invalid for your OS.\nYour inputted version was not detected as having a pack format, so the file format has been set to 0 and the pack has been created with a pre-1.21 file structure.\nYou will need to change the pack format to your desired version's format in the pack.mcmeta file.\nFormats for each version can be found on the Minecraft Wiki at https://minecraft.wiki/w/Data_pack, \nalong with the proper file structure for your desired version.\n(See \"Folder structure\" and \"History\" sections of the Wiki page for more details).")

close = input("\nPress Enter to close...")
exit()
