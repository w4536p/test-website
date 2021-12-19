import subprocess, sys, os
os.system("color A")
z=int(input("how many to open: "))
x = 0
print("hacked")
while x < z:
    print("hacked")
    x = x + 1
    subprocess.Popen([sys.executable, sys.argv[0]], creationflags=subprocess.CREATE_NEW_CONSOLE)