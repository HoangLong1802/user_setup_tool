# User Setup Tool

A pure shell and batch solution for IT Helpdesk to onboard new users without Python dependency. Provides user existence check, personal info collection, department assignment, Chrome installation simulation, and CSV logging.

## 🚀 Features

- Native user existence check on Windows (`net user`) and Linux (`id`).
- Interactive prompts for username, email, and phone number.
- Department selection from a predefined list of 10.
- Google Chrome installation simulation using built-in commands.
- Logging all actions into `user_creation_log.csv` for audit.

## 🧭 How to Run

### 🪟 Windows (Batch)
1. Copy the `run_user_setup.bat` to the target Windows machine.
2. Double-click `run_user_setup.bat` or run in Command Prompt:
   ```bat
   cd \path\to\UserSetupTool
   run_user_setup.bat
   ```
3. Follow the prompts:
   - Enter username (will check if exists).
   - Provide email and phone if new.
   - Select department by number.
4. Check `user_creation_log.csv` in the same folder.

### 🐧 Linux (Bash)
1. Copy the `run_user_setup.sh` to the target Linux machine.
2. Give execute permission and run:
   ```bash
   cd /path/to/UserSetupTool
   chmod +x run_user_setup.sh
   ./run_user_setup.sh
   ```
3. Follow the prompts:
   - Enter username (will check if exists).
   - Provide email and phone if new.
   - Select department by number.
4. View `user_creation_log.csv` in the same directory.

## 🔧 Script Details

- **Windows (`run_user_setup.bat`)**:
  - Uses `net user %username%` for existence check.
  - Loops departments via `for` and delayed expansion.
  - Logs with timestamp from PowerShell `%Date%` via `powershell -command`.

- **Linux (`run_user_setup.sh`)**:
  - Uses `id "$username"` for existence check.
  - Department array and selection via Bash.
  - Logs with ISO timestamp from `date -Iseconds`.

## 🗂 Log Format

`user_creation_log.csv` columns:
```
timestamp,username,email,phone,department
2025-06-26T15:00:00+07:00,jdoe,jdoe@example.com,0123456789,IT
```

**Author:** HoangLong1802  
**Repo:** https://github.com/HoangLong1802/user_setup_tool.git
