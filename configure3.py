from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException

# Clase Router para manejar las conexiones
class Router:
    def __init__(self, device_type, host, username, password, port=22):
        self.device_type = device_type
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.connection = None  # Inicializamos la conexión como None
    
    def conexion(self):
        dev_info = {
            "device_type": self.device_type,
            "host": self.host,
            "username": self.username,
            "password": self.password,
            "port": self.port
        }
        try:
            # Intentamos establecer la conexión usando Netmiko
            self.connection = ConnectHandler(**dev_info)
            print(f"Conexión completa a {self.host}.")
        except NetmikoTimeoutException:
            print(f"Tiempo de conexión agotado para {self.host}.")
        except NetmikoAuthenticationException:
            print(f"Error de autenticación para {self.host}.")
        except Exception as e:
            print(f"Ocurrió un error con {self.host}: {str(e)}")
    
    def comando(self, comd):
        if self.connection:
            try:
                output = self.connection.send_command(comd)
                return output
            except Exception as e:
                print(f"Error al ejecutar el comando en {self.host}: {str(e)}")
                return None
        else:
            print("No hay conexión establecida.")
            return None

if __name__ == "__main__":
    # Crear instancias de la clase Router
    cisco = Router("cisco_ios", "192.168.1.210", "haiti", "haiti", 22)
    mikrotik = Router("mikrotik_routeros", "192.168.1.220", "admin", "admin", 22)

    # Establecemos las conexiones
    cisco.conexion()
    mikrotik.conexion()

    # Enviamos comandos
    output_cisco = cisco.comando("show running-config")
    output_mikrotik = mikrotik.comando("system resource print")  # Intentamos un comando Mikrotik específico

    # Imprimimos los resultados
    if output_cisco:
        print(f"Salida Cisco:\n{output_cisco}")
    if output_mikrotik:
        print(f"Salida Mikrotik:\n{output_mikrotik}")
