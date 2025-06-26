#!/usr/bin/env bash
# run_user_setup.sh
clear
echo "=== User Setup Tool (Linux) ==="

# Prompt for username
read -p "Enter username: " username

# Check if user exists
if id "$username" &>/dev/null; then
  echo "User $username already exists."
  exit 0
fi

# Prompt for email & phone
read -p "Enter email: " email
read -p "Enter phone number: " phone

# Departments list
departments=(IT HR Accounting Business Telesale Sales Logistics CustomerService R&D Marketing)
for i in "${!departments[@]}"; do
  printf "%d. %s\n" $((i+1)) "${departments[i]}"
done
read -p "Select department (1-10): " idx
department=${departments[idx-1]}
echo "Selected department: $department"

# Simulate Chrome install
echo "Installing Chrome (simulated)..."
sleep 2

# Log to CSV
logfile="user_creation_log.csv"
if [ ! -f "$logfile" ]; then
  echo "timestamp,username,email,phone,department" > "$logfile"
fi

timestamp=$(date -Iseconds)
echo "$timestamp,$username,$email,$phone,$department" >> "$logfile"
echo "Log saved to $logfile"