# ssl_to_pfx

**This is my first python project**

This script is designed to automate the process of converting SSL certificates from .crt format to .pfx format using OpenSSL. This is particularly useful when you need to use the SSL certificates on platforms that require a .pfx format, such as Microsoft's IIS server.

The script also integrates a secure password generator for the .pfx certificate, enhancing security and ensuring that a unique password is generated each time a .pfx file is created.

Key features include:

Automatic password generation: The script generates a secure random password each time it runs. This password is then used to secure the .pfx certificate file.

Unique file naming: Each generated .pfx file and associated password file has a unique name, preventing overwriting of previous files and ensuring each certificate-password pair is distinct.

OpenSSL Integration: The script utilizes OpenSSL to perform the certificate conversion.

Please note that this script assumes OpenSSL is installed on your machine and added to your PATH. Be sure to validate the paths for your certificate files and the output location before running the script.

For enhanced security, the script saves the generated password in a .txt file. This file is created in the same directory as the .pfx file. Be sure to properly secure or delete these files after use to prevent unauthorized access.
