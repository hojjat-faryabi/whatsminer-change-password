from serial import Serial
import time

DEFUALT_SECONDS = 1

if __name__ == "__main__" :
    print("*********************************************\n*****\t\t\t\t\t*****\n*****\t\tCHANGE PASSSWORD\t*****\n*****\t\t\t\t\t*****\n*********************************************")

    port = str(input("\n\n--> Please Enter Port Name: "))
    baudrate = str(input("--> Please Enter Connection Baudrate (defualt:115200): ") or "115200")

    print("TRY TO CONNECT TO SERIAL...")
    ser = Serial()
    ser.port = port
    ser.baudrate = baudrate
    
    try :
        ser.open()
        if ser.is_open:
            print("CONNECTED SUCCESSFULY :)")
            user = input("--> Please Enter username: ")
            newPass = input(f"--> Please Enter New Password For {user} User: ")
            print(f"CHANGING USER {user} PASSWORD...")
            ser.write(b'\n\r')
            time.sleep(DEFUALT_SECONDS)
            ser.write(b'passwd ' + user.encode() + b'\n\r')
            time.sleep(DEFUALT_SECONDS)
            ser.write(newPass.encode() + b'\n\r')
            time.sleep(DEFUALT_SECONDS)
            ser.write(newPass.encode() + b'\n\r')
            time.sleep(DEFUALT_SECONDS)
            ser.close()
            print(f"PASSWORD USER {user} CHANGED SUCCESSFULY :)")
    except Exception as ex:
        print("\n\n--x CAN'T CONNECT TO SERIAL PORT :\ x--")
        print(ex)