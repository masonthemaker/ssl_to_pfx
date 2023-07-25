import subprocess
import os
import secrets
import string
import time

# Generate a secure random password
alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for _ in range(10))  # for a 10-character password

# Generate a unique filename based on the current timestamp
timestamp = time.strftime("%Y%m%d-%H%M%S")
password_file_path = rf"C:\Users\youruser\Desktop\SSL\password_{timestamp}.txt"

# Save the password to a file
with open(password_file_path, "w") as file:
    file.write(password)

# Define file paths
crt_file_path = r"C:\Users\youruser\Desktop\SSL\yourcrtfile.crt"  # Your certificate file
key_file_path = r"C:\Users\youruser\Desktop\SSL\yourrsafile.txt"  # Your private key file

# Generate a unique filename for the .pfx file
pfx_file_path = rf"C:\Users\youruser\Desktop\SSL\new_{timestamp}.pfx"

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
