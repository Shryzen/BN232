from netmiko import ConnectHandler
#import paramiko
#from paramiko import SSHClient
# Define the device parameters
device = {
    'device_type': 'cisco_ios',
    'host':   '192.168.56.105',  # <-- Make sure this is YOUR router's IP
    'username': 'cisco',
    'password': 'secret',
}

# Connect to the device
print("Connecting to the device...")
connection = ConnectHandler(**device)

# Enter enable mode
print("Entering enable mode...")
connection.enable()

# Send a command
print("Sending command...")
output = connection.send_command('show ip int brief')
print("\n--- Output of 'show ip int brief' ---")
print(output)

# Close the connection
connection.disconnect()
print("\nDisconnected from the device.")