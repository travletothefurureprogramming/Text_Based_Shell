# Custom Text-Based Shell

> A lightweight Python-based shell for Windows developers, students, and power users, featuring Git-aware prompts, system monitoring, process management, productivity shortcuts, and desktop notifications.

## 📸 Demo

![Custom Shell Demo]()


## 🚀 Quick Start

```bash
python shell.py
```

Example:

```text
C:\Projects\CustomShell(main)> sysinfo

CPU: 12%
RAM: 48%
Battery: 87%
```


## 📦 Installation

Download the latest executable from the Releases page:

👉 [Download Latest Release](../../releases/latest)

No Python installation required.

## 🚀 Quick Start

1. Download `CustomShell.exe`
2. Double-click the executable
3. Start using shell commands

Example:

```text
C:\Users\Greg(main)> sysinfo

CPU: 14%
RAM: 52%
Battery: 89%
```

## ✨ Features

- **Git Integration** – Automatically detects the active Git branch and displays it in the prompt.
- **System Monitoring** – View CPU, RAM, and battery usage instantly.
- **Process Management** – List running processes and terminate them by PID.
- **Productivity Shortcuts** – Open VS Code or File Explorer in the current directory.
- **Built-in Timer** – Countdown timer with native desktop notifications.
- **Windows Command Fallback** – Unknown commands are forwarded to the native Windows shell.

## 💻 Command Reference

Type `help` inside the shell to see the official command listing.

| Command | Description |
|----------|-------------|
| cd | Go to the home directory |
| cd [dir] | Navigate to a specific directory |
| pwd | Print the current working directory |
| dir | List files and folders |
| mkdir [name] | Create a folder |
| rmdir [folder] | Delete a folder |
| del [name] | Delete a file |
| copy [src] [dst] | Copy a file |
| move [src] [dst] | Move a file or folder |
| view [file] | Display a text file |
| history | Show command history |
| cls | Clear the screen |
| explorer | Open File Explorer |
| codehere | Open VS Code in the current directory |
| sysinfo | Show CPU, RAM, and battery usage |
| processes | List running processes |
| kill_process [pid] | Terminate a process |
| timer [seconds] | Start a countdown timer |
| help | Display available commands |
| exit / quit | Exit the shell |

## 📝 Implementation Details

### Error Handling

If a command is not recognized by the shell, it is automatically forwarded to the native Windows command interpreter. If execution fails, the shell displays:

```text
Unknown Command
```

### Desktop Resilience

When running on a desktop system without a battery sensor, the shell safely displays:

```text
Battery: No battery detected (Desktop)
```

instead of raising an exception.

## 🛠️ Dependencies

- Python 3.11
- psutil
- plyer

## 📄 License

MIT License