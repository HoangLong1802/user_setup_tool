#!/usr/bin/env python3
import os
import platform
import csv
import datetime
import subprocess

# ----------------------------
# 1. CHECK IF USER EXISTS
# ----------------------------
def user_exists(username):
    if platform.system() == "Windows":
        result = subprocess.run(["net", "user", username], capture_output=True, text=True)
        return "The user name could not be found" not in result.stdout
    else:
        try:
            import pwd
            pwd.getpwnam(username)
            return True
        except KeyError:
            return False

# ----------------------------
# 2. PROMPT USER INFO
# ----------------------------
def get_user_info():
    username = input("Enter a username: ")
    if user_exists(username):
        print("User already exists.")
        return None

    email = input("Enter email: ")
    phone = input("Enter phone number: ")

    departments = [
        "IT", "HR", "Accounting", "Business", "Telesale",
        "Sales", "Logistics", "Customer Service", "R&D", "Marketing"
    ]
    print("Select department:")
    for i, dept in enumerate(departments, 1):
        print(f"{i}. {dept}")
    dept_index = int(input("Enter number (1-10): ")) - 1
    department = departments[dept_index] if 0 <= dept_index < 10 else "Unknown"

    return {
        "username": username,
        "email": email,
        "phone": phone,
        "department": department,
    }

# ----------------------------
# 3. INSTALL SOFTWARE (Chrome)
# ----------------------------
def install_chrome():
    system = platform.system()
    if system == "Windows":
        print("Installing Chrome on Windows (simulated)...")
        # Normally use winget or direct installer
    elif system == "Linux":
        print("Installing Chrome on Linux (simulated)...")
        # Normally use wget + dpkg or apt
    else:
        print("Unsupported OS")

# ----------------------------
# 4. SAVE TO LOG
# ----------------------------
def save_log(user_data):
    log_file = "user_creation_log.csv"
    is_new = not os.path.exists(log_file)
    with open(log_file, "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["timestamp", "username", "email", "phone", "department"])
        if is_new:
            writer.writeheader()
        user_data["timestamp"] = datetime.datetime.now().isoformat()
        writer.writerow(user_data)
    print(f"Log saved to {log_file}")

# ----------------------------
# MAIN
# ----------------------------
if __name__ == "__main__":
    user_info = get_user_info()
    if user_info:
        install_chrome()
        save_log(user_info)
