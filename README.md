# Custom Text-Based Shell

#### A custom, lightweight, text-based shell written in Python that extends the basic functionality of the Windows Command Prompt (cmd). It features system monitoring, process management, a built-in timer with desktop notifications, and automatically displays your active Git branch directly in the prompt!

## 🚀 Features

* Git Integration: Automatically detects if you are inside a Git repository and displays the active branch in the prompt (e.g., C:\project\my-shell(main)>).

* System Monitoring: Quickly check your system resources (CPU, RAM, and Battery percentages) using a single command.

* Process Management: List all running system processes with their PIDs and terminate any process directly from the shell.

* Productivity Shortcuts: Open VS Code (codehere) or File Explorer (explorer) instantly in your current working directory.

* Built-in Timer: Set a countdown timer directly in your terminal. It pauses the shell and triggers a native desktop notification upon completion.

* Native Windows Fallback: Any command not explicitly built into this shell is automatically forwarded to the native Windows command-line interpreter.

## 🛠️ Installation & Setup

To run this custom shell, you need Python 3.x installed on your system along with a few external libraries.

1. Clone the repository:

git clone [https://github.com/yourusername/custom-shell.git](https://github.com/yourusername/custom-shell.git)
cd custom-shell


2. Install the dependencies:

pip install psutil plyer


3. Run the shell:

python shell.py


## 💻 Command Reference

Type help inside the shell to see the official command listing.


| Command            | Description                                                                |
| ------------------ | -------------------------------------------------------------------------- |
| cd                 | Go to the home directory                                                   |
| cd [dir]           | Navigate to a specific directory                                           |
| pwd                | Print the current working directory path                                   |
| dir                | List files and folders in the current directory                            |
| mkdir [name]       | Create a new folder                                                        |
| rmdir [folder]     | Delete a folder                                                            |
| del [name]         | Delete a file                                                              |
| copy [src] [dst]   | Copy a file to a destination                                               |
| move [src] [dst]   | Move a file or folder to a destination                                     |
| view [file]        | View the contents of a text file inside the terminal                       |
| history            | Show the command history of the current session                            |
| cls                | Clear the terminal screen                                                  |
| explorer           | Open the Windows File Explorer in the current directory                    |
| codehere           | Open VS Code (`code .`) in the current directory                           |
| sysinfo            | Display percentage usage for CPU, RAM, and Battery                         |
| processes          | List current running processes with PIDs and names                         |
| kill_process [pid] | Kill a process by its Process ID (PID)                                     |
| timer [seconds]    | Pause the shell and show a countdown timer; triggers a notification on end |
| help               | Show the list of available commands                                        |
| exit / quit        | Close the custom shell                                                     |


## 📝 Implementation Details

* Error Handling: If an unrecognized command is typed, the shell attempts to run it using os.system(). If that fails, it catches the exception and prints Uknown Command.

* Desktop Resilience: When running sysinfo on a desktop computer, the shell gracefully detects the absence of a battery sensor and prints Battery: No battery detected (Desktop) instead of crashing.