import minecraft_launcher_lib
import subprocess
import os

version = input('Dime la versión: ')
username = input('Nombre: ')
user_windows = os.environ['USERNAME']
LOCAL_PATH = f"C://Users//{user_windows}//AppData//Roaming//.xlauncher"

# Barra de progreso
current_max = 0


def set_status(status: str):
    print(status)


def set_progress(progress: int):
    if current_max != 0:
        print(f"{progress}/{current_max}")


def set_max(new_max: int):
    global current_max
    current_max = new_max


callback = {
    "setStatus": set_status,
    "setProgress": set_progress,
    "setMax": set_max
}

# Instalar Minecraft y sus dependencias
minecraft_launcher_lib.install.install_minecraft_version(
    versionid=version, minecraft_directory=LOCAL_PATH, callback=callback)

# Opciones del launcher
options = {
    'usename': username,
    'uuid': '',
    'token': ''
}

# Abrir Minecraft
subprocess.call(minecraft_launcher_lib.command.get_minecraft_command(
    version=version, minecraft_directory=LOCAL_PATH, options=options))
