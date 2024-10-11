import tftpy
class Tftp():
    def __init__(self,ip,puerto,directorio):
        self.ip=ip
        self.puerto=puerto
        self.directorio=directorio
    def asignar_directorio(self):
        self.servidor=tftpy.TftpServer(self.directorio)
    def escuchar_servidor(self):
        self.servidor.listen(self.ip,self.puerto)

if __name__=="__main__":
    mitftp=Tftp('0.0.0.0',69,'copia_seguridad')
    mitftp.asignar_directorio()
    mitftp.escuchar_servidor()
    print('todo correcto')