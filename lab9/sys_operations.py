import platform
import socket
import os
print("Machine Type")
print(platform.machine())

print("Processer Type")
print(platform.processor())

socket.setdefaulttimeout(50)
print("Get the default Socket Timeout")
print(socket.getdefaulttimeout())

print("OS Type:")
print(os.name)
print("OS Name:")
print(platform.system())


print("Current PID")
print(os.getpid())


file_name = "fdpractice.txt"
file_handle = os.open(file_name, os.O_RDWR | os.O_CREAT)