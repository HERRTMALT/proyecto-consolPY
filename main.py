import mysql.connector as db, pandas as pd

config_database = {
    'database' : None,
    'user' : None,
    'password' : None,
    'port' : None,
    'host' : None
}

print('''
-------------------------------------------------------------------
 ██████╗  ██████╗ ███╗   ██╗███████╗ ██████╗ ██╗  ██████╗██╗   ██╗
 ██╔═══╝ ██╔═══██╗████╗  ██║██╔════╝██╔═══██╗██║  ██╔══██╗██╗ ██╔╝
 ██║     ██║   ██║██╔██╗ ██║███████╗██║   ██║██║  ██████╔╝╚████╔╝
 ██║     ██║   ██║██║╚██╗██║╚════██║██║   ██║██║  ██╔═══╝ ╔██╔╝
 ╚██████╗╚██████╔╝██║ ╚████║███████║╚██████╔╝████╗██║    ╔██║
  ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═══╝╚═╝    ╚══╝
-------------------------------------------------------------------
 inserte los datos que se le pidan para iniciar la conexion de la base de datos.''') # presentacion del proyecto

ejecucion=input('- ejcutar da database: ENTER.\n- salir del programa: 0\n\nEjecucion: ').strip() # ejecucion del programa

def pedir_datos():
    try:
        database=input('-------------------------------\nnombre de la database a conectar.\n- Database: ').lower().strip()
        while database == '':
            print('-!-- el nombre de la database no puede estar vacio.\n')
            database=input('nombre de la database a conectar.\n- Database: ').lower().strip()
        user=input('usuario administradosr de la database.\n- Usuario: ').lower().strip()
        password=input('contraseña de la dtabase. (si no tiene solo precione -ENTER-).\n- Contraseña: ').lower().strip()
        port=input('introdusca el puerto en el que esta hosteada la database.\n- puerto: ').strip()
        host=input('introdusca el hostname de origen de la database.\n- hostname: ').lower().strip() # inputs de conexion a la database

        config_database['database'] = database
        config_database['user'] = user or 'root'
        config_database['password'] = password or ''
        config_database['port'] = port or '3306'
        config_database['host'] = host or 'localhost'
    except Exception as e:print(f'\n----------------------------\nError: {e}.\n----------------------------\n')

while ejecucion != '0':
    try:
        pedir_datos()
        conexion = db.connect(
            database = config_database['database'],
            user = config_database['user'],
            password = config_database['password'],
            port = config_database['port'],
            host = config_database['host']
            ) # conexion a la database
        if conexion.is_connected():print(f'se conecto la base de datos"{config_database['database']}"') # confirmacion de conexion a la database
        else:print('no se conecto')

        cursor = conexion.cursor()

        table = input('----------------------------\ningrese nombre de tabla a mostrar.\n- Tabla: ').strip()
        while table == '':
            print('----------------------------\nel nombre de la tabla no puede estar vacio.')
            table = input('----------------------------\ningrese nombre de tabla a mostrar.\n- Tabla: ').strip()

            def select_query():
                cursor.execute(f'SELECT * FROM {table}')
                rows = cursor.fetchall()
                columns = [column[0] for column in cursor.description]
                files = pd.DataFrame(rows,columns=columns)
                print(files)
            def insert_query():
                try:
                    columns = input('----------------------------\ningrese los nombres de las columnas a insertar separados por comas.\n- Columnas: ').strip()
                    values = input('----------------------------\ningrese los valores a insertar separados por comas.\n- Valores: ').strip()
                    cursor.execute(f'INSERT INTO {table} ({columns}) VALUES ({values})')
                    conexion.commit()
                    print(f'\n----------------------------\nSe insertaron los datos en la tabla "{table}".\n----------------------------\n')

                except Exception as error:print(f'\n----------------------------\nError: {error}.\n----------------------------\n')

        select_query()

        operacion = input('\n----------------------------\n- añadir nuevos productos a la tabla: N\n- borrar productos de la tabla: B\n- Modificar datos de los productos: M\n- cerrar conexion de la database: ENTER.\n- Cerrar programa: 0\n\nEjecucion: ').lower().strip()

        if operacion == 'n':
            insert_query()
    except Exception as error:print(f'\n----------------------------\nError: {error}.\n----------------------------\n')

    ejecucion=input('\n\n- ejcutar da database: ENTER.\n- salir del programa: 0\n\nEjecucion: ').strip()