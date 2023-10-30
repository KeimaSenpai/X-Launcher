import minecraft_launcher_lib
import subprocess
import sys
import os

# versions = minecraft_launcher_lib.utils.get_version_list()
# for version in versions:
#     print(version['id'])
options = {
    'usename': "KeimaSenpai",
    'uuid': '',
    'token': '',

    "jvmArguments": [],  # The jvmArguments
    "launcherName": "x-launcher",
    "launcherVersion": "0.0.1",
}
user_windows = os.environ['USERNAME']
minecraft_directory = f"C://Users//{user_windows}//AppData//Roaming//.xlauncher"
forfe = minecraft_launcher_lib.forge.find_forge_version('1.16.5')
print(forfe)

minecraft_launcher_lib.install.install_minecraft_version(
    "1.16.5", minecraft_directory)
print('Instala la 1.16.5')

minecraft_launcher_lib.forge.install_forge_version(
    forfe, minecraft_directory)
print('Instalado Forge')


minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(
    '1.16.5-forge-36.2.39', minecraft_directory, options)

subprocess.run(minecraft_command)
