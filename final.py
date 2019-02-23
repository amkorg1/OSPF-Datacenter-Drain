#final.py
#!/usr/bin/env python
from netmiko import Netmiko
from getpass import getpass
import sys


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


def dR1():
		# To Drain R1
        cmd=['int f0/0','ip ospf cost 100','int f0/1','ip ospf cost 100','int f1/0','ip ospf cost 100','int f1/1','ip ospf cost 100','int f2/0','ip ospf cost 100']
        call('192.168.10.1',cmd)
        # Affect Router R2
        cmd=['int f1/0','ip ospf cost 100']
        call('192.168.10.2',cmd)
        # Affect Router R3
        cmd=['int f0/0','ip ospf cost 100']
        call('192.168.10.3',cmd)
        # Affect Router R4
        cmd=['int f1/0','ip ospf cost 100']
        call('192.168.10.4',cmd)
        # Affect Router R5
        cmd=['int f0/1','ip ospf cost 100']
        call('192.168.10.5',cmd)
        # Affect Router R6
        cmd=['int f2/0','ip ospf cost 100']
        call('192.168.10.6',cmd)

def dR2():
		# To Drain R2
        cmd=['int f0/0','ip ospf cost 100','int f0/1','ip ospf cost 100','int f1/0','ip ospf cost 100','int f1/1','ip ospf cost 100','int f2/0','ip ospf cost 100']
        call('192.168.10.2',cmd)
        # Affect Router R1
        cmd=['int f1/0','ip ospf cost 100']
        call('192.168.10.1',cmd)
        # Affect Router R3
        cmd=['int f1/1','ip ospf cost 100']
        call('192.168.10.3',cmd)
        # Affect Router R4
        cmd=['int f0/0','ip ospf cost 100']
        call('192.168.10.4',cmd)
        # Affect Router R5
        cmd=['int f2/0','ip ospf cost 100']
        call('192.168.10.5',cmd)
        # Affect Router R6
        cmd=['int f0/1','ip ospf cost 100']
        call('192.168.10.6',cmd)

def dR3():
		# To Drain R3
        cmd=['int f0/0','ip ospf cost 100','int f0/1','ip ospf cost 100','int f1/0','ip ospf cost 100','int f1/1','ip ospf cost 100']
        call('192.168.10.3',cmd)
        # Affect Router R1
        cmd=['int f0/0','ip ospf cost 100']
        call('192.168.10.1',cmd)
        # Affect Router R2
        cmd=['int f1/1','ip ospf cost 100']
        call('192.168.10.2',cmd)
        # Affect Router R4
        cmd=['int f1/0','ip ospf cost 100']
        call('192.168.10.4',cmd)
        # Affect Router R8
        cmd=['int f0/0','ip ospf cost 100']
        call('192.168.10.8',cmd)

def dR4():
		# To Drain R4
        cmd=['int f0/0','ip ospf cost 100','int f0/1','ip ospf cost 100','int f1/0','ip ospf cost 100','int f1/1','ip ospf cost 100']
        call('192.168.10.4',cmd)
        # Affect Router R1
        cmd=['int f1/1','ip ospf cost 100']
        call('192.168.10.1',cmd)
        # Affect Router R2
        cmd=['int f0/0','ip ospf cost 100']
        call('192.168.10.2',cmd)
        # Affect Router R3
        cmd=['int f1/0','ip ospf cost 100']
        call('192.168.10.3',cmd)
        # Affect Router R8
        cmd=['int f0/1','ip ospf cost 100']
        call('192.168.10.8',cmd)

def dR5():
		# To Drain R5
        cmd=['int f0/0','ip ospf cost 100','int f0/1','ip ospf cost 100','int f1/0','ip ospf cost 100','int f2/0','ip ospf cost 100']
        call('192.168.10.5',cmd)
        # Affect Router R1
        cmd=['int f0/1','ip ospf cost 100']
        call('192.168.10.1',cmd)
        # Affect Router R2
        cmd=['int f2/0','ip ospf cost 100']
        call('192.168.10.2',cmd)
        # Affect Router R6
        cmd=['int f1/0','ip ospf cost 100']
        call('192.168.10.6',cmd)
        # Affect Router R7
        cmd=['int f0/0','ip ospf cost 100']
        call('192.168.10.7',cmd)

def dR6():
		# To Drain R6
        cmd=['int f0/0','ip ospf cost 100','int f0/1','ip ospf cost 100','int f1/0','ip ospf cost 100','int f2/0','ip ospf cost 100']
        call('192.168.10.6',cmd)
        # Affect Router R1
        cmd=['int f2/0','ip ospf cost 100']
        call('192.168.10.1',cmd)
        # Affect Router R2
        cmd=['int f0/1','ip ospf cost 100']
        call('192.168.10.2',cmd)
        # Affect Router R5
        cmd=['int f1/0','ip ospf cost 100']
        call('192.168.10.5',cmd)
        # Affect Router R7
        cmd=['int f0/1','ip ospf cost 100']
        call('192.168.10.7',cmd)


def undrain():
		# To UnDrain- Equal cost on all interfaces
        cmd=['int f0/0','ip ospf cost 1','int f0/1','ip ospf cost 1','int f1/0','ip ospf cost 1','int f1/1','ip ospf cost 1','int f2/0','ip ospf cost 1']
        #cmd=['do sh ip int br']
        call('192.168.10.1',cmd)
        call('192.168.10.2',cmd)
        call('192.168.10.3',cmd)
        call('192.168.10.4',cmd)
        call('192.168.10.5',cmd)
        call('192.168.10.6',cmd)

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
