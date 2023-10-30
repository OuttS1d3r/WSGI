import mysql.connector
def BaseDeDatos():
    conexion1=mysql.connector.connect(
        host="localhost",
        user="br1", 
        passwd="martingonzalez070204", 
        database="sra")
    return conexion1

def get_all_empleados():

    conexion = BaseDeDatos()
    cursor = conexion.cursor(named_tuple=True)
    cursor.execute("SELECT Nombre, Dni, Telefono FROM Empleado")
    result_query = cursor.fetchall()
    cursor.close()
    conexion.close()
    return result_query

def get_emp_name():
    conexion = BaseDeDatos()
    cursor = conexion.cursor(named_tuple=True)
    cursor.execute("SELECT idEmpleado,Nombre FROM Empleado")
    names_emps = cursor.fetchall()
    cursor.close()
    conexion.close()
    return names_emps

def get_turnos_AL():
    conexion = BaseDeDatos()
    cursor = conexion.cursor(named_tuple=True)
    cursor.execute("SELECT * FROM turno")
    turno = cursor.fetchall()
    cursor.execute("SELECT * FROM arealaboral")
    al = cursor.fetchall()
    conjunto=turno,al
    cursor.close()
    conexion.close()
    return conjunto

def RegistrarAsis(empleado, turno, area):
    conexion = BaseDeDatos()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO ut (Empleado, AreaLaboral, Turno) VALUES (%s, %s, %s)", (empleado, area, turno))
    conexion.commit()
    cursor.close()
    conexion.close()

def DevolverUTS(nombreEMP):
    conexion = BaseDeDatos()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM UT WHERE Empleado = %s", (nombreEMP,))
    UTS = cursor.fetchall()
    conexion.commit()
    cursor.close()
    conexion.close()
    return UTS

def MostrarUTS():
    conexion = BaseDeDatos()
    cursor = conexion.cursor(named_tuple=True)
    cursor.execute(
    "SELECT " 
    "empleado.Nombre AS NombreEmpleado, "
    "turno.Nombre AS NombreTurno, "
    "turno.Horario AS HorarioTurno"
    "arealaboral.Nombre AS NombreArea "
    "FROM UT "
    "JOIN empleado ON UT.empleado = empleado.idEmpleado " 
    "JOIN turno ON UT.turno = turno.idTurno "
    "JOIN arealaboral ON UT.arealaboral = arealaboral.idAL;"
)
    VistaUT = cursor.fetchall()
    conexion.commit()
    cursor.close()
    conexion.close()
    return VistaUT

def RegistrarRDA():
    conexion = BaseDeDatos()
    cursor = conexion.cursor()

    cursor.execute('INSERT INTO rda (Fecha,Horario,idDispositivo,idUT) VALUES (%s,%s,%s,%s,%s)')

    conexion.commit()
    cursor.close()
    conexion.close()
    pass


if __name__ == "__main__":
    result = get_all_empleados(BaseDeDatos())
    result2 = get_emp_name(BaseDeDatos())
    result3 = get_turnos_AL(BaseDeDatos())
    result4= MostrarUTS(BaseDeDatos())
    print("...")
    print("...")