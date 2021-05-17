import os
import sys

def root_set():
  print("type 'help' for more options and 'exit' to exit and 'run' to run a file")
  root = input("run a file>>>")
  if root == "exit":
    os.system("cls")

  while root == "help":
    f = open("ht.txt")
    info = f.read()
    print(info)
    print("type 'help' for more options and 'exit' to exit and 'run' to run a file")
    root = input("run a file>>>")

  while root == "run":  
    filename = input("filename>>>")
    file = str("python3 " +  filename)
    os.system(file)
    print("type 'help' for more options and 'exit' to exit and 'run' to run a file")
    root = input("run a file>>>")
    
count = 0
while count == 0:
  root_set()