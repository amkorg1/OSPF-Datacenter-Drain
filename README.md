<H1># OSPF-Drain-Datacenter </H1>

Based on previous Lab , the topology considered here is Spine-Leaf.

<h2><p>About Script</p></h2>
<p>The script provides you options
<p>Enter option</p>
<p> 1 - Drain R1</p>
<p> 2 - Drain R2</p>
<p> 3 - Drain R3</p>
<p> 4 - Drain R4</p>
<p> 5 - Drain R5</p>
<p> 6 - Drain R6</p>
<p> 7 - Undrain</p>
<p> 8 - Exit</p>
 

<h2><p>Physical Connections</p></h2>
All Routers connect int f2/1 connect to switch.
  
<h2><p>IP-Addressing</p> </h2>
<p>Used a /24 network</p>
<p>Mgmt ip – 192.168.10.0/24</p>
<p>Interface – 10.1.xX.x /24</p>

Where x is lower router number and X is higher router number.
10.1.(lower_router_Number)(Higher_router_Number).lower_router_Number

So when R1 - connects to R5

R1
interface 
ip add 10.1.15.1
!
R5
interface 
ip add 10.1.15.5 

This way from traceroute we can easily decipher our path based on the digit in the last octet that represents Router number 
and the third octet tells us about link. 
for eg 10.1.15.5
Last octet - 5 means its router 5
3rd Octet - 15 tell us link between router 5 and router 1 

<h2><p>Management IP</p></h2> 
For management IP subnet with Router give Linux VM IP-address in same subnet.

<h2><p>Assumptions</p></h2> 
All areas are under Area 0.
Traceroute from R8 to R7 and vice versa at opposite ends to show the best effect of Drain.

<h2><p>Future improvements</p></h2>
  Multithreading to be implemented to touch routers simultaneously.
  
  <p> More Info </p>
   Script is written in Python
   Used a Ubuntu VM
   Used GNS3 to simulate
