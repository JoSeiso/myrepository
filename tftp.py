import tftpy
class Tftp():
    '''
    Este programa creara un servidor Trivial FTP
    nos sera util para coger los archivos de configuracion de nuestros routers
    '''
    def __init__(self,ip,puerto,directorio):
        self.ip=ip
        self.puerto=puerto
        self.directorio=directorio
    def asignar_directorio(self):
        '''
        Aqui lo que estamos haciendo es ejecutar el servidor en un hilo
        '''
        self.servidor=tftpy.TftpServer(self.directorio)
    def escuchar_servidor(self):
        '''
        Con el metodo listen de la libreria tftpy, lo que haremos sera 
        que es servidor empiece a escuchar por la ip y el puerto que nosotros 
        le indiquemos
        '''
        self.servidor.listen(self.ip,self.puerto)

if __name__=="__main__":
    '''
    Generamos el constructor
    '''
    mitftp=Tftp('0.0.0.0',69,'copia_seguridad')
    mitftp.asignar_directorio()
    mitftp.escuchar_servidor()
    print('todo correcto')