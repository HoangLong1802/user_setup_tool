#!/usr/bin/env python3
import os
import platform
import csv
import datetime
import subprocess

# Danh sách phòng ban
DEPARTMENTS = [
    "IT", "HR", "Accounting", "Business", "Telesale",
    "Sales", "Logistics", "CustomerService", "R&D", "Marketing"
]
LOG_FILE = "user_creation_log.csv"

# 1. Kiểm tra user tồn tại

def user_exists(username):
    system = platform.system()
    if system == "Windows":
        result = subprocess.run(["net", "user", username], capture_output=True, text=True)
        return "The user name could not be found" not in result.stdout
    else:
        try:
            import pwd
            pwd.getpwnam(username)
            return True
        except KeyError:
            return False

# 2. Nhập username và chọn phòng ban

def get_user_info():
    username = input("Enter username: ")
    if user_exists(username):
        print(f"User '{username}' already exists.")
        return None

    print("Select department:")
    for i, dept in enumerate(DEPARTMENTS, 1):
        print(f"{i}. {dept}")
    idx = input(f"Enter number (1-{len(DEPARTMENTS)}): ")
    try:
        department = DEPARTMENTS[int(idx)-1]
    except (ValueError, IndexError):
        department = "Unknown"

    return {"username": username, "department": department}

# 3. Cài đặt công cụ: Chrome và mos

def install_tools():
    system = platform.system()
    if system == "Windows":
        subprocess.run(["choco", "install", "googlechrome", "-y"], check=False)
        subprocess.run(["choco", "install", "mos", "-y"], check=False)
    elif system == "Linux":
        subprocess.run(["sudo", "apt-get", "update", "-y"], check=False)
        subprocess.run([
            "wget", "-q", "-O", "-",
            "https://dl.google.com/linux/linux_signing_key.pub"],
            stdout=subprocess.PIPE, check=False)
        subprocess.run([
            "sudo", "apt-key", "add", "-"], stdin=subprocess.PIPE, check=False)
        subprocess.run([
            "sudo", "tee", "/etc/apt/sources.list.d/google-chrome.list"],
            input=b"deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main\n", check=False)
        subprocess.run(["sudo", "apt-get", "update", "-y"], check=False)
        subprocess.run(["sudo", "apt-get", "install", "-y", "google-chrome-stable", "mos"], check=False)
    else:
        print(f"Unsupported OS: {system}")

# 4. Tạo user và gán nhóm

def create_user(username, department):
    system = platform.system()
    if system == "Windows":
        subprocess.run(["net", "localgroup", department, "/add"], check=False)
        subprocess.run(["net", "user", username, "/add"], check=False)
        subprocess.run(["net", "localgroup", department, username, "/add"], check=False)
    else:
        subprocess.run(["sudo", "groupadd", "-f", department], check=False)
        subprocess.run(["sudo", "useradd", "-m", "-s", "/bin/bash",
                         "-G", department, username], check=False)

# 5. Ghi log CSV

def save_log(username, department):
    is_new = not os.path.exists(LOG_FILE)
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if is_new:
            writer.writerow(["username", "timestamp", "department"])
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([username, timestamp, department])
    print(f"Log saved to {LOG_FILE}")

# Main
if __name__ == "__main__":
    info = get_user_info()
    if not info:
        exit(0)
    install_tools()
    create_user(info["username"], info["department"])
    save_log(info["username"], info["department"])
    print(f"User '{info['username']}' created in '{info['department']}' department.")