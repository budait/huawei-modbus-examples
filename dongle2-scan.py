from pymodbus.client import ModbusTcpClient

# Convert Modbus register to string
def regs2str(regs):
    s = ""
    for r in regs:
        a = chr(r & 0xFF)
        b = chr((r >> 8) & 0xFF)
        if a == '\x00':
            a = ' '
        if b == '\x00':
            b = ' '
        s += "%c%c" % (b, a)
    return s.rstrip()

# replace the IP address with your device's IP
client = ModbusTcpClient('127.0.0.1')       

res=client.connect()                        
if(res<1):
    print("connection error")
    exit()

print("OS version (30050, 15 bytes str)")
result=client.read_holding_registers(30050, count=15, slave=100)
print(regs2str(result.registers))

for i in range(1,247):
    print(f"try slave {i}")
    try:
        result=client.read_holding_registers(40710, count=15, slave=i)
        print(result)
    except Exception as exc:
        print(f"Received ModbusException({exc}) from library")


client.close()