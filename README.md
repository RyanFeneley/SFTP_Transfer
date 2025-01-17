# Secure File Transfer (SFTP) Script
## Overview
This Python script securely transfers files between two systems using the SFTP protocol. It supports both SSH key and password authentication for secure file uploads and downloads.

## Features
- Authenticate using an SSH key or password.
- Upload and download files securely.
- User-friendly prompts for input parameters.

## Requirements
- Python 3.x
- paramiko library
  \\\ash
  pip install paramiko
  \\\

## Usage
1. Clone the repository or download the code.
2. Install the required dependencies:
   \\\ash
   pip install paramiko
   \\\
3. Run the script:
   \\\ash
   python sftp_transfer.py
   \\\
4. Follow the prompts to specify the action (upload or download), server details, and file paths.

### Example Input
To upload a file, you might enter:
- Action: upload
- Hostname: example.com
- Port: 22
- Username: user
- Path to SSH key file (or password if not using key): /path/to/key
- Local file to upload: /path/to/local/file.txt
- Remote path: /path/to/remote/file.txt

For downloading, the input would be similar, just specify the remote path and local file to save.
