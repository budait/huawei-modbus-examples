# huawei-modbus-examples
Example scripts to interact with Huawei PV inverters and EMMA system

## Getting started
### Prerequisites
1. Connect your PV inverter dongle or EMMA to the same local network as your machine
2. Get the current IP address of the device and enable MODBUS communication by using Huawei FusionSolar app
3. have python3 and pip installed

### Installation
run `pip install -r requirements.txt`

### Usage
- Open the scripts with a text editor and replace the IP address of the device with yours.
- Run the scripts with python

### Where to go from here
- read the documentation of [pymodbus](https://pymodbus.readthedocs.io/en/latest/)
- read the MODBUS protocol documentation of the Huawei device you are interested in ([example](https://support.huawei.com/enterprise/de/doc/EDOC1100387581?currentPartNo=k004&togo=content&section=k004))
