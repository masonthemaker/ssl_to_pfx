import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os
import time

def generate_files():
    # Retrieve values from input fields
    password = password_entry.get()
    crt_file_path = crt_file_entry.get()
    key_file_path = key_file_entry.get()
    pfx_file_dest = pfx_dest_entry.get()
    password_file_dest = password_dest_entry.get()

    # Generate a unique filename based on the current timestamp
    timestamp = time.strftime("%Y%m%d-%H%M%S")

    # Generate the full file paths for the new .pfx file and password file
    pfx_file_path = os.path.join(pfx_file_dest, f"new_{timestamp}.pfx")
    password_file_path = os.path.join(password_file_dest, f"password_{timestamp}.txt")

    try:
        # Save the password to a file
        with open(password_file_path, "w") as file:
            file.write(password)
        
        # Add OpenSSL to your PATH within the Python script
        os.environ["PATH"] += os.pathsep + r'C:\\Program Files\\OpenSSL-Win64\\bin'
        
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

        # Display success message
        messagebox.showinfo("Success", "Files successfully generated!")
    except Exception as e:
        # Display error message
        messagebox.showerror("Error", str(e))

def browse_files(entry):
    filename = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(0, filename)

# Create the main window
root = tk.Tk()
root.title("PFX Generator")
root.configure(bg='green')

# Add a label and input field for the password
tk.Label(root, text="Password", bg='green', fg='white').grid(row=0, padx=10, pady=10)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=0, column=1, padx=10, pady=10)

# Repeat for other inputs...
tk.Label(root, text="Certificate File Path", bg='green', fg='white').grid(row=1, padx=10, pady=10)
crt_file_entry = tk.Entry(root)
crt_file_entry.grid(row=1, column=1, padx=10, pady=10)
crt_file_button = tk.Button(root, text="Browse", command=lambda: browse_files(crt_file_entry))
crt_file_button.grid(row=1, column=2, padx=10, pady=10)

tk.Label(root, text="Key File Path", bg='green', fg='white').grid(row=2, padx=10, pady=10)
key_file_entry = tk.Entry(root)
key_file_entry.grid(row=2, column=1, padx=10, pady=10)
key_file_button = tk.Button(root, text="Browse", command=lambda: browse_files(key_file_entry))
key_file_button.grid(row=2, column=2, padx=10, pady=10)

tk.Label(root, text="PFX Destination", bg='green', fg='white').grid(row=3, padx=10, pady=10)
pfx_dest_entry = tk.Entry(root)
pfx_dest_entry.grid(row=3, column=1, padx=10, pady=10)

tk.Label(root, text="Password File Destination", bg='green', fg='white').grid(row=4, padx=10, pady=10)
password_dest_entry = tk.Entry(root)
password_dest_entry.grid(row=4, column=1, padx=10, pady=10)

# Add a button that triggers file generation
generate_button = tk.Button(root, text="Generate", command=generate_files)
generate_button.grid(row=5, column=1, padx=10, pady=10)

# Start the main loop
root.mainloop()
