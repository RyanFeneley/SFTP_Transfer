# SFTP Transfer
# Ryan Feneley
# September 2024

import paramiko
import os

def sftp_transfer(hostname, port, username, password=None, key_filepath=None, action='upload', local_file=None, remote_path=None):
    """
    Securely transfer files using SFTP.

    Parameters:
    - hostname: The hostname or IP address of the remote server.
    - port: The port number for SFTP (default is 22).
    - username: The username to authenticate.
    - password: The password for authentication (optional if using SSH key).
    - key_filepath: The path to the SSH key file for authentication (optional).
    - action: 'upload' to upload files or 'download' to download files.
    - local_file: The local file path for upload/download.
    - remote_path: The remote file path for upload/download.
    """

    try:
        # Create an SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the server using either password or key
        if key_filepath:
            ssh.connect(hostname, port=port, username=username, key_filename=key_filepath)
        else:
            ssh.connect(hostname, port=port, username=username, password=password)

        # Start SFTP session
        sftp = ssh.open_sftp()

        if action == 'upload':
            sftp.put(local_file, remote_path)
            print(f"Uploaded {local_file} to {remote_path} successfully.")
        elif action == 'download':
            sftp.get(remote_path, local_file)
            print(f"Downloaded {remote_path} to {local_file} successfully.")
        else:
            print("Invalid action. Use 'upload' or 'download'.")

        sftp.close()
        ssh.close()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Gather user input for the transfer
    action = input("Enter action (upload/download): ").strip().lower()
    hostname = input("Enter hostname or IP address of the remote server: ")
    port = int(input("Enter port number (default is 22): ") or 22)
    username = input("Enter your username: ")
    
    key_filepath = input("Enter path to SSH key file (leave blank for password): ").strip() or None
    password = None
    if not key_filepath:
        password = input("Enter your password: ")

    if action == 'upload':
        local_file = input("Enter the path to the local file: ")
        remote_path = input("Enter the remote path to upload to: ")
        sftp_transfer(hostname, port, username, password=password, key_filepath=key_filepath, action=action, local_file=local_file, remote_path=remote_path)
    elif action == 'download':
        remote_path = input("Enter the remote path to download from: ")
        local_file = input("Enter the path to save the downloaded file: ")
        sftp_transfer(hostname, port, username, password=password, key_filepath=key_filepath, action=action, local_file=local_file, remote_path=remote_path)
    else:
        print("Invalid action. Use 'upload' or 'download'.")
