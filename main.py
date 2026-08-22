import mysql.connector as db, pandas as pd;
print('\n\n-------------------------------\nCONSOLPY PROYECT\n-------------------------------\n\n\n')

print('inserte los datos que se le pidan para iniciar lla coneccion de la base de datos')
database=input('nombre de la database a conectar.\n- Database: ').lower()
user=input('usuario administradosr de la database.\n- Usuario: ').lower()
password=input('contraseña de la dtabase. (si no tiene solo precione -ENTER-).\n- Contraseña: ').lower()
port=input('introdusca el puerto en el que esta hosteada la database.\n- puerto: ')
host=input('introdusca el hostname de origen de la database.\n- hostname: ')

config_database = {
    'port' : port,
    'host' : host,
    'user' : user,
    'database' : database,
    'password' : password
}
try:
    conexion = db.connect(config_database)
    if conexion.is_connected():print('se conecto la base de datos')
    else:print('no se conecto')
except:print('hubo algun error. mas que seguro un valor de conexion de la database invalido.')