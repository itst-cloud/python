import paramiko
import os

class SSHManager:
    def __init__(self, username, key_path="~/.ssh/id_ed25519") -> None:
        self.username = username
        self.key_path = os.path.expanduser(key_path)
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    def connect(self, hostname):
        """Connects to the remote server using SSH key authentication."""
        self.ssh.connect(hostname=hostname, 
                         username=self.username, 
                         key_filename=self.key_path)
    
    def execute_command(self, commands):
        """Executes a command on the remote machine."""
        stdin, stdout, stderr = self.ssh.exec_command(" ".join(commands))
        output = stdout.read().decode('utf-8') + stderr.read().decode('utf-8')
        exit_code = stdout.channel.recv_exit_status()
        return exit_code, output

    def copy_file_to_remote(self, localfile, remotefile):
        """Copies a file from local to remote."""
        sftp = self.ssh.open_sftp()
        sftp.put(localfile, remotefile)
        sftp.close()

    def copy_file_from_remote(self, remotefile, localfile):
        """Copies a file from remote to local."""
        sftp = self.ssh.open_sftp()
        sftp.get(remotefile, localfile)
        sftp.close()

    def close(self):
        """Closes the SSH connection."""
        self.ssh.close()

def main():
    username = "Your Username"  # Update with your actual username
    hostname = "Remote Hostname"   # Update with your actual hostname or IP

    ssh_manager = SSHManager(username)

    try:
        ssh_manager.connect(hostname)
        
        # Define files for remote execution
        execute_remote_file = "execute_remote.sh"
        remote_local_file = "execute_local.sh"
        remote_log = "execute_remote.log"
        local_log = "execute_local.log"

        # Copy the script to remote
        ssh_manager.copy_file_to_remote(remote_local_file, execute_remote_file)

        # Execute the script on remote machine
        cmds = ["sh", execute_remote_file]
        err_code, output = ssh_manager.execute_command(cmds)

        if err_code == 0:
            print("Command executed successfully")
        else:
            print("Command execution unsuccessful!!!")

        # Retrieve log files from remote
        ssh_manager.copy_file_from_remote(remote_log, local_log)
        print(output)

    finally:
        ssh_manager.close()

if __name__ == "__main__":
    main()
