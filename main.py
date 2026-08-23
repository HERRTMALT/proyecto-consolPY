import mysql.connector as db, pandas as pd
print('''  
██████╗  ██████╗ ███╗   ██╗███████╗ ██████╗ ██╗  ██████╗██╗   ██╗
██╔═══╝ ██╔═══██╗████╗  ██║██╔════╝██╔═══██╗██║  ██╔══██╗██╗ ██╔╝
██║     ██║   ██║██╔██╗ ██║███████╗██║   ██║██║  ██████╔╝╚████╔╝
██║     ██║   ██║██║╚██╗██║╚════██║██║   ██║██║  ██╔═══╝ ╔██╔╝
╚██████╗╚██████╔╝██║ ╚████║███████║╚██████╔╝████╗██║    ╔██║
 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═══╝╚═╝    ╚══╝''') # presentacion del proyecto
print('inserte los datos que se le pidan para iniciar la conexion de la base de datos.')
ejecucion=input('- ejcutar da database: ENTER.\n- salir del programa: 0\n\nEjecucion: ').strip()
while ejecucion != '0':
    database=input('-------------------------------\nnombre de la database a conectar.\n- Database: ').lower().strip()
    while database == '':
        print('-!-- el nombre de la database no puede estar vacio.\n')
        database=input('nombre de la database a conectar.\n- Database: ').lower().strip()
    user=input('usuario administradosr de la database.\n- Usuario: ').lower().strip()
    password=input('contraseña de la dtabase. (si no tiene solo precione -ENTER-).\n- Contraseña: ').lower().strip()
    port=input('introdusca el puerto en el que esta hosteada la database.\n- puerto: ').strip()
    host=input('introdusca el hostname de origen de la database.\n- hostname: ').lower().strip() # inputs de conexion a la database
    try:
        conexion = db.connect( database= database,user= user or 'root',password= password or '',port=port or '3306',host=host or 'localhost') # conexion a la database
        if conexion.is_connected():print(f'se conecto la base de datos"{database}"') # confirmacion de conexion a la database
        else:print('no se conecto')
        cursor = conexion.cursor()
        table = input('----------------------------\ningrese nombre de tabla a mostrar.\n- Tabla: ').strip()
        while table == '':
            print('----------------------------\nel nombre de la tabla no puede estar vacio.')
            table = input('----------------------------\ningrese nombre de tabla a mostrar.\n- Tabla: ').strip()
        cursor.execute(f'SELECT * FROM {table}')
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        files = pd.DataFrame(rows,columns=columns)
        print(files)
        operacion = input('\n----------------------------\n- añadir nuevos productos a la tabla: N\n- borrar productos de la tabla: B\n- Modificar datos de los productos: M\n- cerrar conexion de la database: ENTER.\n- Cerrar programa: 0\n\nEjecucion: ').strip()
    except Exception as error:print(f'\n----------------------------\nError: {error}.\n----------------------------\n')
    ejecucion=input('\n\n- ejcutar da database: ENTER.\n- salir del programa: 0\n\nEjecucion: ').strip()

