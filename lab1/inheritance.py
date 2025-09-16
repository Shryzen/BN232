#Base class 
class NetworkDevice:
    def __init__(self, name, ip_address):
        self.name = name
        self.ip_address = ip_address
    def display_info(self):
        print(f"Device Name: {self.name}")
        print(f"IP Address: {self.ip_address}")
        print(f"Device Type: {self.__class__.__name__}")
        print("-" *30)

#subclass for the router 
class Router(NetworkDevice):
    def __init__(self, name, ip_address, num_ports):
        super().__init__(name, ip_address)
        self.num_ports = num_ports

    def display_info(self):
        super().display_info()
        print(f"Number of Ports: {self.num_ports}")
        print("-" * 30)

#subclass for switch 
class Switch(NetworkDevice):
    def __init__(self, name, ip_address, num_ports):
        super().__init__(name, ip_address)
        self.num_ports = num_ports

    def display_info(self):
        super().display_info()
        print(f"Number of Ports: {self.num_ports}")
        print("-" * 30)

#subclass for the hub
class Hub(NetworkDevice):
    def __init__(self, name, ip_address, num_ports):
        super().__init__(name, ip_address)
        self.num_ports = num_ports

    def display_info(self):
        super().display_info()
        print(f"Number of Ports: {self.num_ports}")
        print("-" * 30)

# Create instances of each subclass
router = Router(name="Router_1", ip_address="192.168.1.1", num_ports=8)
switch = Switch(name="Switch_1", ip_address="192.168.1.2", num_ports=24)
hub = Hub(name="Hub_1", ip_address="192.168.1.3", num_ports=16)

# Display information
router.display_info()
switch.display_info()
hub.display_info()