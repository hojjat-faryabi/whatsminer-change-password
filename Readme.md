# About

whit this code can change password of any user in whatsminer and microbit miners.
(tested on "m3" and "m1" miners)

## Requirements

you most install "pyserial" on your computer

```bash
pip install pyserial
```

## Usage

in new Firmware can't access to root user for change password of users so we most use serial to access root and change the password. (in this way you can change root password and after that connect to control board with root user and ssh)

- connect a [usb to ttl serial](https://www.amazon.com/JBtek-WINDOWS-Supported-Raspberry-Programming/dp/B00QT7LQ88/ref=sr_1_6?dchild=1&keywords=usb+to+ttl+serial&qid=1629095249&sr=8-6) tool on Tx,Rx and GND pins on control board     

- run the script
```bash
$ python3 chpass.py
```

- port name : if run script on windows you should write com port that connected to the control board for example "COM2" and if use linux "/dev/ttyUSB0"

- Connection Baudrate : default value for baundrate is 115200 but you can change it

- username : The username you want to change the password

- password : enter new password

changing password usually take 5-6 sec. so be patient ;)



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
