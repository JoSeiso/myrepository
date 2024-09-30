from netmiko import ConnectHandler

# Clase Router para manejar las conexiones
class Router:
    def __init__(self, device_type, host, username, password, port=22):
        # Asigna los valores recibidos como argumentos
        self.device_type = device_type
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.connection = None  # Inicializamos la conexión como None
    
    def conexion(self):
        # Diccionario con la información de conexión
        dev_info = {
            "device_type": self.device_type,
            "host": self.host,
            "username": self.username,
            "password": self.password,
            "port": self.port
        }
        # Establecemos la conexión usando Netmiko
        self.connection = ConnectHandler(**dev_info)
        print(f"Conexión completa a {self.host}.")
    
    def comando(self, comd):
        if self.connection:
            output = self.connection.send_command(comd)
            return output
        else:
            print("No hay conexión establecida.")
            return None

if __name__ == "__main__":
    # Crear instancias de la clase Router
    cisco = Router("cisco_ios", "192.168.1.210", "haiti", "haiti", 22)  # Sin la coma al final
    mikrotik = Router("mikrotik_routeros", "192.168.1.220", "admin", "admin", 22)

    # Establecemos las conexiones
    cisco.conexion()
    mikrotik.conexion()

    # Enviamos comandos
    output_cisco = cisco.comando("show running-config")
    output_mikrotik = mikrotik.comando("print")

    # Imprimimos los resultados
    if output_cisco:
        print(output_cisco)
    if output_mikrotik:
        print(output_mikrotik)
