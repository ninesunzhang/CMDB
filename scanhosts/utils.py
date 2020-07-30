import paramiko
import nmap
import telnetlib
import re
def get_active_hosts(host='172.25.254.20'):
    nm=nmap.PortScanner()
    result = nm.scan(hosts=host,arguments='-n -sP')
    print(result)
    return nm.all_hosts()

def is_ssh_up(host='172.25.254.20',port=22,timeout=5):
    try:
        tn=telnetlib.Telnet(host=host,port=port,timeout=timeout)
        tn_result=tn.read_until(b"\n",timeout=timeout).decode('utf-8')
        ssh_result=re.search(pattern=r'ssh',string=tn_result,flags=re.I)
    except Exception as e:
        print("%s ssh is down,because %s" %(host,str(e)))
        return False
    else:
        return  True if ssh_result else False

def login_ssh_key(hostname='172.25.254.20',port=22,username='root',
                  private_key='/root/PycharmProjects/devops/id_rsa', command='df -h'):
    pkey=paramiko.RSAKey.from_private_key_file(private_key)
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname,port,username,pkey=pkey)
    stdin,stout,stdeer=client.exec_command(command)
    return stout.read().decode('utf-8')


if __name__=='__main__':
    get_active_hosts()
    print(is_ssh_up(host='172.25.254.20'))
    print(login_ssh_key())