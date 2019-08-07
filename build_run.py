##Version Python 3.7.6
import os
import subprocess

print("I will now start to build these Images. Debian 7, Debian 8, Debian 9, Ubuntu 18.04 and Windows")

owd = os.getcwd()
os.chdir("Debian-7/")
os.system("docker build -t isa/debian7 . ")
os.system("docker run --cidfile debian7_id.cid isa/debian7")
cmd = os.popen("type debian7_id.cid").read()
os.system("del -f debian7_id.cid")
os.chdir(owd)
os.system("docker cp "+ cmd + ":./installSynApps/DEPLOYMENTS .")

os.chdir("Debian-8/")
os.system("docker build -t isa/debian8 . ")
os.system("docker run --cidfile debian8_id.cid isa/debian8")
cmd = os.popen("type debian8_id.cid").read()
os.system("del /f debian8_id.cid")
os.chdir(owd)
os.system("docker cp "+ cmd + ":./installSynApps/DEPLOYMENTS .")

os.chdir("Debian-9/")
os.system("docker build -t isa/debian9 . ")
os.system("docker run --cidfile debian9_id.cid isa/debian9")
cmd = os.popen("type debian9_id.cid").read()
os.system("del /f debian9_id.cid")
os.chdir(owd)
os.system("docker cp "+ cmd + ":./installSynApps/DEPLOYMENTS .")

os.chdir("Ubuntu/")
os.system("docker build -t isa/ubuntu_18.04 . ")
os.system("docker run --cidfile ubuntu18.04_id.cid isa/ubuntu_18.04")
cmd = os.popen("type ubuntu18.04_id.cid").read()
os.system("del /f ubuntu18.04_id.cid")
os.chdir(owd)
os.system("docker cp "+ cmd + ":./installSynApps/DEPLOYMENTS .")
