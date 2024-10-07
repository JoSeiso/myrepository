from netmiko import ConnectHandler
class Router():
    def __init__(self,device_type,host,username,password):
        self.device_type=device_type
        self.host=host
        self.username=username
        self.password=password
    def establecer_conexion(self):#utilizamos self por que es diferente para cada objeto
        dev_info = {
            "device_type":self.device_type,
            "host":self.host,
            "username":self.username,
            "password":self.password
        }
        self.conexion = ConnectHandler(**dev_info)  # Almacena el objeto de conexión
        print(f"Conexión establecida con {self.host}.")

    def enviar_comando(self,comando):
        resultado = self.conexion.send_command(comando)
        print(f"el comando {resultado} con resultado: ")
if __name__ == "__main__":
        print('Haiti/Honduras/hungria')
        option=input('Escoge un Router: ')
while True:
    if (option =='haiti'):
        cisco = Router("cisco_ios","192.168.1.210","haiti","haiti")
        with open('cisco-confi.txt', 'r') as configuracion:
            comando = configuracion.read().strip()#strip nos limpia de caracteres no deseados
        #"show ip interface brief" #hacer una variable que recorra un fichero y este fichero tenga los parametros de configuracion
        cisco.establecer_conexion()
        cisco.enviar_comando(comando)
        break
    elif (option == 'hungria'):
        mikrotik = Router("mikrotik_routeros","192.168.1.220","admin","admin")
        comando = '/ip/address/print'
        mikrotik.establecer_conexion()
        mikrotik.enviar_comando(comando)
        break
    elif (option == 'honduras'):
        mikrotik2 = Router("mikrotik_routeros","192.168.1.230","admin","admin")
        comando = '/ip/address/print'
        mikrotik2.enviar_comando(comando)
        break
    


        
    