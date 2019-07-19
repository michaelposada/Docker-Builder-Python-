##Version Python 3.7.6
import os

print("I will now start to build these Images. Debian 7, Debian 8, Debian 9, Ubuntu 18.04 and Windows")

os.chdir("Debian-7/")
os.system("ls -a")
print("I am now inside Debian-7")
os.system("docker build -t isa/debian7 . ")
os.system("cd ..")
