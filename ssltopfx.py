import subprocess
import os
import time
from getpass import getpass

# Ask the user to input a password
password = getpass("Please enter a password: ")

# Generate a unique filename based on the current timestamp
timestamp = time.strftime("%Y%m%d-%H%M%S")

# Ask the user for the paths to the certificate and key files
crt_file_path = input("Please enter the full path to your certificate file: ")
key_file_path = input("Please enter the full path to your key file: ")

# Ask the user where to save the new .pfx file and password file
pfx_file_dest = input("Please enter the full path where you want to save the new .pfx file: ")
password_file_dest = input("Please enter the full path where you want to save the password file: ")

# Generate the full file paths for the new .pfx file and password file
pfx_file_path = os.path.join(pfx_file_dest, f"new_{timestamp}.pfx")
password_file_path = os.path.join(password_file_dest, f"password_{timestamp}.txt")

# Save the password to a file
with open(password_file_path, "w") as file:
    file.write(password)

# Add OpenSSL to your PATH within the Python script
os.environ["PATH"] += os.pathsep + r'C:\Program Files\OpenSSL-Win64\bin'

# Command for openssl to convert the files
command = [
    "openssl", 
    "pkcs12", 
    "-export", 
    "-out", pfx_file_path, 
    "-inkey", key_file_path, 
    "-in", crt_file_path,
    "-password", f"pass:{password}"
]

# Execute the command
subprocess.run(command, check=True)
