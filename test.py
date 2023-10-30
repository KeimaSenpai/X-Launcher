import minecraft_launcher_lib
import os

user_windows = os.environ['USERNAME']
minecraft_directory = f"C://Users//{user_windows}//AppData//Roaming//.xlauncher"


forts = minecraft_launcher_lib.utils.get_installed_versions(
    minecraft_directory)

for fort in forts:
    print(fort['id'])
