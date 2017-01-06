import sys
import paramiko
try:
	ssh = paramiko.SSHClient()
	#ssh.connect('172.16.0.173',port=22,username='asm',password='asm123')
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	#ssh.load_system_host_keys()
	ssh.connect('172.16.0.151',port=22,username='asm',password='asm123')
	print("true")
except:
	print("not connected")
#stdin,stdout,stderr=ssh.exec_command('df -h')
#out=stdout.readlines()
#for i in out:
#	print(i)
