import paramiko


def login_ssh_password(hostname='localhost', port=22,
                       username='root', password='lee',
                       command='df -h'):
    # 1 INSTANCE OBJECT
    client = paramiko.SSHClient()
    # 5when first ssh connect server ,have a question(yn),auto answer
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 2 connect server
    client.connect(hostname, port, username, password)
    # 3
    stdin, stdout, stderr = client.exec_command(command)
    # 4
    return (stdout.read().decode('utf-8'))

def login_ssh_key(hostname='localhost', keyfile='/root/PycharmProjects/devops/id_rsa',port=22,
                       username='root',
                       command='df -h'):
    #0 private key location
    pkey=paramiko.RSAKey.from_private_key_file(keyfile)
    # 1 INSTANCE OBJECT
    with paramiko.SSHClient() as client:
        # client = paramiko.SSHClient()
        # 5 when first ssh connect server ,have a question(yn),auto answer
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 2 connect server
        client.connect(hostname, port, username,pkey=pkey)
        # 3 execate command
        stdin, stdout, stderr = client.exec_command(command)
        # 4 print
        print(stdout.read().decode('utf-8'))

def paramiko_sftp(hostname='localhost',port=22,username='root',password='lee',
                  localpath="/etc/passwd",remotepath="/mnt/passwd"):
    with paramiko.Transport(hostname,port) as tran:
        tran.connect(username=username,password=password)
        sftp = paramiko.SFTPClient.from_transport(tran)
        sftp.put(localpath,remotepath)
        #sftp.get(remotepath,localpath)
        print('file upload success')

if __name__ == '__main__':
    #result=login_ssh_password(hostname='172.25.254.20',command="hostname")
    #login_ssh_key(hostname='172.25.254.20',command="hostname")
    paramiko_sftp()