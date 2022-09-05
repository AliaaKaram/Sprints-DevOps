#!/usr/bin/env bash

echo "Please, Enter a Port Number"
read Port_No

sed -i -e "/PermitRootLogin yes /c\PermitRootLogin no" /etc/ssh/sshd_config

if [[ ${Port_No} -ge 1024  && ${Port_No} -le 65535 || ${Port_No} == 22 ]]
then  
     sed -i -e "/Port /c\Port ${Port_No}" /etc/ssh/sshd_config
     echo "Port has Changed sucessfully!"
else 
    echo "Invalid input Number"

fi

