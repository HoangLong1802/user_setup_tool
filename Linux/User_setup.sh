#!/usr/bin/env bash
# Usage: ./user_setup.sh <username> <department>

if [ -z "$1" ] || [ -z "$2" ]; then
  echo "Usage: $0 <username> <department>"
  exit 1
fi

USERNAME="$1"
DEPARTMENT="$2"
LOGFILE="$(dirname "$0")/user_creation_log.csv"

# 1) Cài đặt công cụ cơ bản: Chrome và mos
sudo apt-get update -y
# Thêm kho chính thức của Chrome
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -

echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" \
    | sudo tee /etc/apt/sources.list.d/google-chrome.list

sudo apt-get update -y
sudo apt-get install -y google-chrome-stable mos

# 2) Tạo nhóm và user (nếu nhóm chưa có thì tạo)
if ! getent group "$DEPARTMENT" >/dev/null; then
  sudo groupadd "$DEPARTMENT"
fi
sudo useradd -m -s /bin/bash -G "$DEPARTMENT" "$USERNAME"

# 3) Ghi log: username,timestamp,department
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
if [ ! -f "$LOGFILE" ]; then
  echo "username,timestamp,department" > "$LOGFILE"
fi
echo "${USERNAME},${TIMESTAMP},${DEPARTMENT}" >> "$LOGFILE"

echo "Đã tạo user '$USERNAME' (phòng: $DEPARTMENT') và ghi log vào $LOGFILE"