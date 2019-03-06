#final.py
#!/usr/bin/env python
from netmiko import Netmiko
from getpass import getpass
import sys
import threading


def call(ip_add,cmd):
        ip=ip_add
        cmd=cmd
        ios_ssh= {
                'device_type':'cisco_ios',
                'username':'lab',
                'password':'lab123',
                'ip':ip,
                }

        net_connect = Netmiko(**ios_ssh)
        print(net_connect.find_prompt())
        #config_commands=['do sh ip int br | i 2/1']
        config_commands=cmd
        output=net_connect.send_config_set(config_commands)
        #print(output)

def thd(ip1,ip2,cmd1,cmd2):
		t1=threading.Thread(target=call, args=(ip1,cmd1))
        t2=threading.Thread(target=call, args=(ip2,cmd2))
        t1.start()
        t2.start()
        t1.join()
        t2.join()		

def dR1():
		# To Drain R1
		ip1='192.168.10.1'
        cmd1=['int f0/0','ip ospf cost 100','int f0/1','ip ospf cost 100','int f1/0','ip ospf cost 100','int f1/1','ip ospf cost 100','int f2/0','ip ospf cost 100']
        #call('192.168.10.1',cmd)
        # Affect Router R2
		ip2='192.168.10.2'
        cmd2=['int f1/0','ip ospf cost 100']
        #call('192.168.10.2',cmd)
		thd(ip1,ip2,cmd1,cmd2)
        # Affect Router R3
		ip1='192.168.10.3'
        cmd1=['int f0/0','ip ospf cost 100']
        #call('192.168.10.3',cmd)
        # Affect Router R4
		ip2='192.168.10.4'
        cmd2=['int f1/0','ip ospf cost 100']
		#call('192.168.10.4',cmd)
		thd(ip1,ip2,cmd1,cmd2)
        # Affect Router R5
		ip1='192.168.10.5'
        cmd1=['int f0/1','ip ospf cost 100']
        #call('192.168.10.5',cmd)
        # Affect Router R6
        ip2='192.168.10.6'
		cmd2=['int f2/0','ip ospf cost 100']
        #call('192.168.10.6',cmd)
		thd(ip1,ip2,cmd1,cmd2)

def dR2():
		# To Drain R2
		ip1='192.168.10.2'
        cmd1=['int f0/0','ip ospf cost 100','int f0/1','ip ospf cost 100','int f1/0','ip ospf cost 100','int f1/1','ip ospf cost 100','int f2/0','ip ospf cost 100']
        # Affect Router R1
		ip2='192.168.10.1'
        cmd2=['int f1/0','ip ospf cost 100']
        #call('192.168.10.1',cmd)
		thd(ip1,ip2,cmd1,cmd2)
        # Affect Router R3
		ip1='192.168.10.3'
        cmd1=['int f1/1','ip ospf cost 100']
        #call('192.168.10.3',cmd)
        # Affect Router R4
		ip2='192.168.10.4'
        cmd2=['int f0/0','ip ospf cost 100']
        #call('192.168.10.4',cmd)
		thd(ip1,ip2,cmd1,cmd2)
        # Affect Router R5
		ip1='192.168.10.5'
        cmd1=['int f2/0','ip ospf cost 100']
        #call('192.168.10.5',cmd)
        # Affect Router R6
		ip2='192.168.10.6'
        cmd2=['int f0/1','ip ospf cost 100']
        #call('192.168.10.6',cmd)
		thd(ip1,ip2,cmd1,cmd2)

def dR3():
		# To Drain R3
		ip1='192.168.10.3'
        cmd1=['int f0/0','ip ospf cost 100','int f0/1','ip ospf cost 100','int f1/0','ip ospf cost 100','int f1/1','ip ospf cost 100']
        #call('192.168.10.3',cmd)
        # Affect Router R1
		ip2='192.168.10.1'
        cmd2=['int f0/0','ip ospf cost 100']
        #call('192.168.10.1',cmd)
		# Calling thread to handle
		thd(ip1,ip2,cmd1,cmd2)
        # Affect Router R2
		ip1='192.168.10.2'
        cmd1=['int f1/1','ip ospf cost 100']
        #call('192.168.10.2',cmd)
        # Affect Router R4
		ip2='192.168.10.4'
        cmd2=['int f1/0','ip ospf cost 100']
        #call('192.168.10.4',cmd)
		# Calling thread to handle
		thd(ip1,ip2,cmd1,cmd2)
        # Affect Router R8
        cmd=['int f0/0','ip ospf cost 100']
        call('192.168.10.8',cmd)

def dR4():
		# To Drain R4
		ip1='192.168.10.4'
        cmd1=['int f0/0','ip ospf cost 100','int f0/1','ip ospf cost 100','int f1/0','ip ospf cost 100','int f1/1','ip ospf cost 100']
        #call('192.168.10.4',cmd)
        # Affect Router R1
		ip2='192.168.10.1'
        cmd2=['int f1/1','ip ospf cost 100']
        #call('192.168.10.1',cmd)
		# Calling thread to handle
		thd(ip1,ip2,cmd1,cmd2)
        # Affect Router R2
		ip1='192.168.10.2'
        cmd1=['int f0/0','ip ospf cost 100']
        #call('192.168.10.2',cmd)
        # Affect Router R3
        ip2='192.168.10.3'
		cmd2=['int f1/0','ip ospf cost 100']
        #call('192.168.10.3',cmd)
		# Calling thread to handle
		thd(ip1,ip2,cmd1,cmd2)
        # Affect Router R8
		ip1='192.168.10.8'
        cmd=['int f0/1','ip ospf cost 100']
        call(ip1,cmd)

def dR5():
		# To Drain R5
		ip1='192.168.10.5'
        cmd1=['int f0/0','ip ospf cost 100','int f0/1','ip ospf cost 100','int f1/0','ip ospf cost 100','int f2/0','ip ospf cost 100']
        #call('192.168.10.5',cmd)
        # Affect Router R1
        ip2='192.168.10.1'
		cmd2=['int f0/1','ip ospf cost 100']
        #call('192.168.10.1',cmd)
		# Calling thread to handle
		thd(ip1,ip2,cmd1,cmd2)
        # Affect Router R2
        ip1='192.168.10.2'
		cmd1=['int f2/0','ip ospf cost 100']
        #call('192.168.10.2',cmd)
        # Affect Router R6
		ip2='192.168.10.6'
		cmd2=['int f1/0','ip ospf cost 100']
        #('192.168.10.6',cmd)
		# Calling thread to handle
		thd(ip1,ip2,cmd1,cmd2)
        # Affect Router R7
        ip1='192.168.10.7'
		cmd=['int f0/0','ip ospf cost 100']
        call(ip1,cmd)

def dR6():
		# To Drain R6
		ip1='192.168.10.6'
        cmd1=['int f0/0','ip ospf cost 100','int f0/1','ip ospf cost 100','int f1/0','ip ospf cost 100','int f2/0','ip ospf cost 100']
        #call('192.168.10.6',cmd)
        # Affect Router R1
		ip2='192.168.10.1'
        cmd2=['int f2/0','ip ospf cost 100']
        #call('192.168.10.1',cmd)
		# Calling thread to handle
		thd(ip1,ip2,cmd1,cmd2)
		
        # Affect Router R2
		ip1='192.168.10.2'
        cmd1=['int f0/1','ip ospf cost 100']
        #call('192.168.10.2',cmd)
        # Affect Router R5
        ip2='192.168.10.5'
		cmd2=['int f1/0','ip ospf cost 100']
        #call('192.168.10.5',cmd)
		# Calling thread to handle
		thd(ip1,ip2,cmd1,cmd2)
        # Affect Router R7
		ip1='192.168.10.7'
		cmd=['int f0/1','ip ospf cost 100']
        #call(ip1,cmd)


def undrain():
		# To UnDrain- Equal cost on all interfaces
        cmd=['int f0/0','ip ospf cost 1','int f0/1','ip ospf cost 1','int f1/0','ip ospf cost 1','int f1/1','ip ospf cost 1','int f2/0','ip ospf cost 1']
        #cmd=['do sh ip int br']
        #call('192.168.10.1',cmd)
        #call('192.168.10.2',cmd)
		ip1='192.168.10.1'
		ip2='192.168.10.2'
		# Calling thread to handle
		thd(ip1,ip2,cmd,cmd)
        #call('192.168.10.3',cmd)
        #call('192.168.10.4',cmd)
		ip1='192.168.10.3'
		ip2='192.168.10.4'
		# Calling thread to handle
		thd(ip1,ip2,cmd,cmd)
        #call('192.168.10.5',cmd)
        #call('192.168.10.6',cmd)
		ip1='192.168.10.5'
		ip2='192.168.10.6'
		# Calling thread to handle
		thd(ip1,ip2,cmd,cmd)
		
def choice():
        opt=0
        while(opt<=8):
                opt = int(input("Enter option \n 1 - Drain R1 \n 2 - Drain R2 \n 3 - Drain R3 \n 4 - Drain R4 \n 5 - Drain R5 \n 6 - Drain R6 \n 7 - Undrain \n 8 - Exit "))
                if(opt)== 1:
                        dR1()
                if(opt)== 2:
                        dR2()
                if(opt)== 3:
                        dR3()
                if(opt)== 4:
                        dR4()
                if(opt)== 5:
                        dR5()
                if(opt)== 6:
                        dR6()
                if(opt)== 7:
                        undrain()
                if(opt)== 8:
                        sys.exit()

if __name__=="__main__":
        choice()
