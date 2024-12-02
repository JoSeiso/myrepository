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
        option=input('¿quieres programa un router? s/n: ')
while True:
    if (option == 's'):
        router=input("Dame el id del router que quieres configurar: ")
        if(router == 'r1'):
            cisco = Router("cisco_ios","80.60.1.2","admin","admin")
            with open('configuraciones/r1.txt', 'r') as configuracion:
                comando = configuracion.read()
            cisco.establecer_conexion()
            cisco.enviar_comando(comando)
        elif(router == 'r5'):
            cisco = Router("cisco_ios","80.60.1.3","admin","admin")
            with open('configuraciones/r5.txt', 'r') as configuracion:
                comando = configuracion.read()
            cisco.establecer_conexion()
            cisco.enviar_comando(comando)
        elif(router == 'r4'):
            cisco = Router("cisco_ios","80.60.1.4","admin","admin")
            with open('configuraciones/r4.txt', 'r') as configuracion:
                comando = configuracion.read()
            cisco.establecer_conexion()
            cisco.enviar_comando(comando)
        elif(router == 'r3'):
            cisco = Router("cisco_ios","80.60.1.5","admin","admin")
            with open('configuraciones/r3.txt', 'r') as configuracion:
                comando = configuracion.read()
            cisco.establecer_conexion()
            cisco.enviar_comando(comando)
        elif(router == 'r2'):
            cisco = Router("cisco_ios","80.60.1.6","admin","admin")
            with open('configuraciones/r2.txt', 'r') as configuracion:
                comando = configuracion.read()
            cisco.establecer_conexion()
            cisco.enviar_comando(comando)
        elif(router == 'r6'):
            cisco = Router("cisco_ios","80.60.1.7","admin","admin")
            with open('configuraciones/r6.txt', 'r') as configuracion:
                comando = configuracion.read()
            cisco.establecer_conexion()
            cisco.enviar_comando(comando)
        elif(router == 'r7'):
            cisco = Router("cisco_ios","80.60.1.8","admin","admin")
            with open('configuraciones/r7.txt', 'r') as configuracion:
                comando = configuracion.read()
            cisco.establecer_conexion()
            cisco.enviar_comando(comando)
        elif(router == 'r8'):
            cisco = Router("cisco_ios","80.60.1.9","admin","admin")
            with open('configuraciones/r8.txt', 'r') as configuracion:
                comando = configuracion.read()
            cisco.establecer_conexion()
            cisco.enviar_comando(comando)
        elif(router == 'r9'):
            cisco = Router("cisco_ios","80.60.1.9","admin","admin")
            with open('configuraciones/r9.txt', 'r') as configuracion:
                comando = configuracion.read()
            cisco.establecer_conexion()
            cisco.enviar_comando(comando)
    elif(router == 'n'):
        print('adiiios')
        break


    