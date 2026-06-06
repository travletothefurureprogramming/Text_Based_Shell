import subprocess
import os
import psutil
import time
from plyer import notification

os.chdir(os.path.expanduser('~'))
history = []
help = {
   "cd [dir]":"Go to specific dir",
   "cd":"Go to home dir",
   "pwd":"Show the current dir",
   "history":"Show the command history",
   "dir":"Show files and folders in current dirs",
   "cls":"Clear the terminal",
   "mkdir [name]":"Create a new folder",
   "rmdir [folder]":"Delete a folder",
   "del [name]":"Delete a file",
   "explorer":"Open the file explorer in current directory",
   "sysinfo":"Show percentage for 1.CPU, 2.RAM, 3.Battery",
   "codehere":"Open vs code in current dir",
   "timer [total_seconds]": "The shel paused for x seconds and show the timer countdown",
   "Other Built In Windows Commands":"You can call built-in windows commands",
   "exit/quit":"Close the shell"
}

def timer(total_seconds):
    while total_seconds >= 0:
        minutes = total_seconds // 60
        seconds = total_seconds % 60

        print(f"\rTime remaining: {minutes:02d}:{seconds:02d}", end="")
        
        time.sleep(1)
        total_seconds -= 1
        
    print("\n") 
    notification.notify(
        title = "Shell Timer",
        message = "The timer has ended!",  
        timeout = 5 
    )


def analyze_command(command:str):
   
   if "cd" in command:
      history.append(command)
      if command == "cd":
         os.chdir(os.path.expanduser('~'))
      else:
         command = command.split()
         os.chdir(" ".join(command[1:]))
   elif "pwd" == command:
      history.append(command)
      print(os.getcwd())
   elif "history" == command:
      history.append(command)
      print(history)
   elif "dir" == command:
      history.append(command)
      dir = os.listdir(os.getcwd())
      for i in dir:
       print(i)
   elif "cls" == command:
      history.append(command)
      os.system('cls')
   elif "mkdir" in command:
      history.append(command)
      command = command.split()
      os.mkdir(" ".join(command[1:]))
   elif "rmdir" in command:
      history.append(command)
      command = command.split()
      os.rmdir(" ".join(command[1:]))
   elif "del" in command:
      history.append(command)
      command = command.split()
      os.remove(" ".join(command[1:]))
   elif "explorer" in command:
      history.append(command)
      current_path = os.getcwd()
      subprocess.run(["explorer",current_path])
   elif "sysinfo" in command:
      history.append(command)
      cpu = psutil.cpu_percent()
      ram = psutil.virtual_memory()
      battery = psutil.sensors_battery()
      
      print(cpu,"%")
      print(ram[2],"%")
      if battery != None:
       print(battery[0],"%")
      else:
         print("Battery: No battery detected (Desktop)")
   elif "codehere" in command:
      history.append(command)
      os.system("code .")
   elif "help" == command:
      history.append(command)
      for i in help:
         print(f"Command {i}. Description: {help[i]}")
   elif "timer" in command:
      command = command.split()
      timer(int(command[1]))
   elif "exit" == command or "quit" == command:
      exit()
   else:
     try:
      os.system(command)
     except:
        print("Uknown Command")

def get_git_branch():
    try:
        result = subprocess.run(
            ["git", "branch", "--show-current"], 
            stdout=subprocess.PIPE,  
            stderr=subprocess.DEVNULL, 
            text=True                 
        )
        
        if result.stdout:
            return result.stdout.strip()
        
    except:
        return ""
    
    return ""
while True:
   current_path = os.getcwd()
   if get_git_branch() =="":
    command = input(current_path+"\my-shell> ")
   else:
    command = input(current_path+f"\my-shell({get_git_branch()})> ")
   analyze_command(command)

