````markdown
# User Setup Tool

A simple automation solution using Shell, Batch, and Python to:
- Install essential tools (Google Chrome, mos)
- Create new users on Windows or Linux
- Assign users to appropriate departments
- Log user creation details into `user_creation_log.csv` (username, timestamp, department)


## 🚀 Usage Guide

### Windows (Batch)

1. Copy `run_user_setup.bat` to your Windows machine.
2. Open Command Prompt and navigate to the folder:
   ```bat
   cd C:\path\to\UserSetupTool\window
   ```
3. Run the script with arguments:
   ```bat
   run_user_setup.bat <username> <department>
   ```
   - `<username>`: The name of the user to create
   - `<department>`: Department name (e.g., IT, HR, Sales,...)
4. Check `user_creation_log.csv` for log entries.

### Linux (Bash)

1. Copy `user_setup.sh` to your Linux machine.
2. Make it executable and run it:
   ```bash
   cd /path/to/UserSetupTool/Linux
   chmod +x user_setup.sh
   sudo ./user_setup.sh <username> <department>
   ```
   - Use `sudo` to allow installation and user creation
3. Log will be saved to `user_creation_log.csv`.

### Python (Cross‑platform)

1. Make sure Python 3 is installed.
2. Run the script:
   ```bash
   chmod +x user_setup_tool.py
   ./user_setup_tool.py
   ```
3. Follow the on-screen prompts.

## 🗂 Log Format

The file `user_creation_log.csv` contains the following header:

```plaintext
username,timestamp,department
```

Each row logs a user creation:

```plaintext
jdoe,2025-06-26 16:00:00,IT
```

## 📖 Features

- **Tool Installation**: Google Chrome and mos installed via Chocolatey (Windows) or apt (Linux).
- **User Creation**: Uses `net user` (Windows), `useradd` + `groupadd` (Linux), or Python subprocess.
- **CSV Logging**: Saves username, creation timestamp, and department.

---

**Author:** HoangLong1802\
**Repo:** (https://github.com/HoangLong1802/user_setup_tool)
