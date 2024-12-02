import tftpy

class Tftp():
    '''
    Este programa creará un servidor Trivial FTP
    que nos será útil para obtener los archivos de configuración de nuestros routers.
    '''
    def __init__(self, ip, puerto, directorio):
        self.ip = ip
        self.puerto = puerto
        self.directorio = directorio

    def asignar_directorio(self):
        '''
        Asigna el directorio para el servidor.
        '''
        try:
            self.servidor = tftpy.TftpServer(self.directorio)
            print(f"Directorio '{self.directorio}' asignado correctamente.")
        except Exception as e:
            print(f"Error al asignar el directorio: {e}")

    def escuchar_servidor(self):
        '''
        Hace que el servidor empiece a escuchar en la IP y el puerto especificados.
        '''
        try:
            print(f"Iniciando servidor en {self.ip}:{self.puerto}")
            self.servidor.listen(self.ip, self.puerto)
        except Exception as e:
            print(f"Error al iniciar el servidor: {e}")

if __name__ == "__main__":
    '''
    Genera una instancia de la clase Tftp y arranca el servidor.
    '''
    try:
        mitftp = Tftp('0.0.0.0', 69, 'copia_seguridad')
        mitftp.asignar_directorio()
        mitftp.escuchar_servidor()
        print('Servidor TFTP funcionando correctamente.')
    except Exception as e:
        print(f"Error inesperado: {e}")
