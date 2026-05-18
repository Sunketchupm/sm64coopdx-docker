import os
import subprocess

BASE_DIR = os.getcwd()
os.chdir(os.path.join("config", "mods", "minecraft-enhanced"))
subprocess.run(["git", "pull"])
os.chdir(BASE_DIR)
subprocess.run(["docker", "compose", "restart"])