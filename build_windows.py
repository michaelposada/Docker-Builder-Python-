import os

os.chdir("Windows/")
os.system("docker build -t isa/windows .")
os.system("cd ..")
