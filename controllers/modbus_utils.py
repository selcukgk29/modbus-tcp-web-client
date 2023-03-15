from pymodbus.client.sync import ModbusTcpClient

# Define the IP address and port number of the Modbus server
SERVER_IP = '127.0.0.1'
SERVER_PORT = 502


def read_register(address, count, unit=1):
    client = ModbusTcpClient(SERVER_IP, port=SERVER_PORT)
    result = client.read_holding_registers(
        address=address, count=count, unit=unit)
    client.close()
    if result.isError():
        raise Exception('Read failed: %s' % result)
    return result.registers[0]


def write_register(address, value, unit=1):
    client = ModbusTcpClient(SERVER_IP, port=SERVER_PORT)
    result = client.write_register(address=address, value=value, unit=unit)
    client.close()
    if result.isError():
        raise Exception('Write failed: %s' % result)
