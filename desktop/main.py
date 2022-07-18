import os
user_directory = "remih"
world_folder = "worlds_test"

def upload():
    print("Select a world to upload")
    print("current world folder is: " + world_folder)
    os.system("cd " + world_folder)
    os.listdir(world_folder)
upload()