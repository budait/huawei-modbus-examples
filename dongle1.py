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

print("Type (37410, U16): 0: N/A, 2:WLAN, 3:4G, 4:WLAN-FE")
result=client.read_holding_registers(37410, count=1, slave=100)
print(result.registers)

print("Device search status (37411, U16): 0:search completed, 1:searching, 2:search failed")
result=client.read_holding_registers(37411, count=1, slave=100)
print(result.registers)

print("Read Slave data")
result=client.read_holding_registers(40000, count=2, slave=3)
print(result.registers)


client.close()
