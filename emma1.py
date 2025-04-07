from pymodbus.client import ModbusTcpClient
import time

# replace the IP address with your device's IP
client = ModbusTcpClient('127.0.0.1')

res=client.connect()
if(res<1):
    print("connection error")
    exit()

result = client.read_device_information(read_code=1)
if(result.information and len(result.information) > 2):
    for i in range(3):
        print(result.information[i].decode('utf-8'))


print("Phase A Voltage (built-in) (31639, U32, Gain: 100)")
result=client.read_holding_registers(31639, count=2, slave=0)
print(result.registers)
print(result.registers[1]/100)


client.close()
