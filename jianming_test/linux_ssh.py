import threading
import paramiko

cmd = [
    "mkdir /root/202011",
    "touch /root/202011/123.txt",
]

ssh = paramiko.SSHClient()
policy = paramiko.AutoAddPolicy()
ssh.set_missing_host_key_policy(policy)
ssh.connect(
    hostname="39.108.248.57",
    port=22,
    username="root",
    password="Lian@12345."
)
for i in cmd:
    stdin, stdout, stderr = ssh.exec_command(i)
    result = stdout.read().decode()
    print(result)
