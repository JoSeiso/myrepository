from netmiko import ConnectHandler
class Router():
    def __init__(self,device_type,host,username,password):
        self.device_type=device_type
        self.host=host
        self.username=username
        self.password=password
    def conexion(self):
        dev_info = {
            "device_type":self.device_type,
            "host":self.host,
            "username":self.username,
            "password":self.password
        }
        self.conexion = ConnectHandler(**dev_info)  # Almacena el objeto de conexión
        print(f"Conexión establecida con {self.host}.")
if __name__ == "__main__":
    cisco = Router("cisco_ios","192.168.1.210","admin","admin")
    cisco.conexion()