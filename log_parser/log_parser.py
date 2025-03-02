#!/usr/bin/env python3
# Open the log file
with open("access.log", "r") as log_file:
    lines = log_file.readlines()

# Get user input
search_ip = input("Enter the IP address to search for: ")

# Search for the IP address in the log file
for line in lines:
    if search_ip in line:
        print(line.strip())  # Print matching log entries

# Define a list of attack patterns (SQL injections, XSS, etc.)
attack_patterns = ["SELECT * FROM", "' OR '1'='1", "DROP TABLE", "<script>", "union select"]

# Search for attacks in the log file
for line in lines:
    for pattern in attack_patterns:
        if pattern.lower() in line.lower():
            print(f"🚨 Possible attack detected: {line.strip()}")

