import subprocess
import os
import psutil
import time
from plyer import notification
import shutil
import socket
import platform

# Cross-platform readline support
try:
    import readline
except ImportError:
    try:
        import pyreadline3 as readline
    except ImportError:
        readline = None

os.chdir(os.path.expanduser('~'))
history = []

help = {
    "cd [dir]": "Go to specific dir",
    "cd": "Go to home dir",
    "pwd": "Show the current dir",
    "history": "Show the command history",
    "dir": "Show files and folders in current dirs",
    "cls": "Clear the terminal",
    "mkdir [name]": "Create a new folder",
    "rmdir [folder]": "Delete a folder",
    "del [name]": "Delete a file",
    "touch [name]": "Create an empty file",
    "explorer": "Open the file explorer in current directory",
    "sysinfo": "Show percentage for 1.CPU, 2.RAM, 3.Battery",
    "codehere": "Open vs code in current dir",
    "timer [total_seconds]": "The shell paused for x seconds and show the timer countdown",
    "copy [src] [dst]": "Copy and paste a file",
    "move [src] [dst]": "Move a file or folder to destination",
    "processes": "Show current processes",
    "kill_process [pid]": "Kills a process based to pid",
    "netinfo": "It returns hostname and ip of the device",
    "ping [host]": "Ping a host or website",
    "whoami": "Show current user",
    "view [file]": "View contents of a file",
    "Other Built In Windows/Unix Commands": "You can call native system commands",
    "exit/quit": "Close the shell"
}

# Setup Auto-Complete configuration
commands_list = [
    "cd", "pwd", "history", "dir", "cls", "mkdir", "rmdir", "del", 
    "touch", "explorer", "sysinfo", "codehere", "timer", "copy", 
    "move", "processes", "kill_process", "netinfo", "ping", "whoami", 
    "view", "help", "exit", "quit"
]

def completer(text, state):
    options = [cmd for cmd in commands_list if cmd.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None

if readline:
    readline.set_completer(completer)
    # Handle auto-complete bindings across different platforms
    if platform.system() == 'Darwin':
        readline.parse_and_bind("bind ^I rl_complete")
    else:
        readline.parse_and_bind("tab: complete")

def timer(total_seconds):
    while total_seconds >= 0:
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        print(f"\rTime remaining: {minutes:02d}:{seconds:02d}", end="")
        time.sleep(1)
        total_seconds -= 1
        
    print("\n") 
    notification.notify(
        title="Shell Timer",
        message="The timer has ended!",  
        timeout=5 
    )

def get_net_info():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return hostname, ip

def analyze_command(command: str):
    if not command.strip():
        return

    parts = command.split()
    cmd = parts[0]
    
    if cmd == "cd":
        history.append(command)
        if len(parts) == 1:
            os.chdir(os.path.expanduser('~'))
        else:
            try:
                os.chdir(" ".join(parts[1:]))
            except Exception as e:
                print(f"Error: {e}")
    elif cmd == "pwd":
        history.append(command)
        print(os.getcwd())
    elif cmd == "history":
        history.append(command)
        for idx, h in enumerate(history):
            print(f"{idx}: {h}")
    elif cmd == "dir":
        history.append(command.strip())
        for i in os.listdir(os.getcwd()):
            print(i)
    elif cmd == "cls":
        history.append(command)
        os.system('cls' if os.name == 'nt' else 'clear')
    elif cmd == "mkdir":
        history.append(command)
        os.mkdir(" ".join(parts[1:]))
    elif cmd == "rmdir":
        history.append(command)
        os.rmdir(" ".join(parts[1:]))
    elif cmd == "del":
        history.append(command)
        os.remove(" ".join(parts[1:]))
    elif cmd == "touch":
        history.append(command)
        open(" ".join(parts[1:]), 'a').close()
    elif cmd == "explorer":
        history.append(command)
        current_path = os.getcwd()
        if os.name == 'nt':
            subprocess.run(["explorer", current_path])
        else:
            subprocess.run(["xdg-open", current_path])
    elif cmd == "sysinfo":
        history.append(command)
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory()
        battery = psutil.sensors_battery()
        print(f"CPU Usage: {cpu}%")
        print(f"RAM Usage: {ram[2]}%")
        if battery is not None:
            print(f"Battery: {battery[0]}%")
        else:
            print("Battery: No battery detected (Desktop)")
    elif cmd == "codehere":
        history.append(command)
        os.system("code .")
    elif cmd == "netinfo":
        history.append(command)
        hostname, ip = get_net_info()
        print(f"Hostname: {hostname}\nIP Address: {ip}")
    elif cmd == "ping":
        history.append(command)
        target = parts[1]
        param = "-n" if os.name == "nt" else "-c"
        subprocess.run(["ping", param, "4", target])
    elif cmd == "whoami":
        history.append(command)
        print(os.getlogin() if hasattr(os, 'getlogin') else subprocess.check_output("whoami").decode().strip())
    elif cmd == "find":
        history.append(command)
        if len(parts) < 2:
            print("Usage: find [filename]")
        else:
            search_name = parts[1]
            found = False
            print(f"Searching for '{search_name}'...")
            for root, dirs, files in os.walk(os.getcwd()):
                if search_name in files:
                    print(f"Found at: {os.path.join(root, search_name)}")
                    found = True
            if not found:
                print("File not found.")
    elif cmd == "copy":
        history.append(command)
        shutil.copy(parts[1], parts[2])
    elif cmd == "move":
        history.append(command)
        shutil.move(parts[1], parts[2])
    elif cmd == "processes":
        history.append(command)
        for p in psutil.process_iter(['pid', 'name']):
            print(p.info['pid'], p.info['name'])
    elif cmd == "kill_process":
        history.append(command)
        pid = parts[1]
        psutil.Process(int(pid)).kill()
        print(f"Process {pid} terminated.")
    elif cmd == "view":
        history.append(command)
        with open(parts[1], 'r') as f:
            print(f.read())
    elif cmd == "help":
        history.append(command)
        for i in help:
            print(f"Command: {i} \n  Description: {help[i]}")
    elif cmd == "timer":
        history.append(command)
        timer(int(parts[1]))
    elif cmd in ["exit", "quit"]:
        exit()
    else:
        try:
            os.system(command)
        except Exception:
            print("Unknown Command")

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
    branch = get_git_branch()
    prompt_symbol = f"\\my-shell({branch})> " if branch else "\\my-shell> "
    
    try:
        command = input(current_path + prompt_symbol)
        analyze_command(command)
    except (KeyboardInterrupt, EOFError):
        print("\nExiting shell...")
        break