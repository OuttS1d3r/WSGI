from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from BDD import *
import calendar, datetime


app = Flask(__name__)


@app.route('/Inicio')
def inicio():
    todos_empleados = get_all_empleados()
    calendario = generar_calendario()
    return render_template('index.html', data=todos_empleados, calendario=calendario)

@app.route('/Perfil')
def Perfil():
    return render_template('Perfil.html')

@app.route('/Calendario')
def Calendario():
    calendario = generar_calendario()
    return render_template('Calendario.html', calendario=calendario) 

@app.route('/RegistrarUT', methods=['GET'])
def InicioSesion():
    nombres_emp = get_emp_name()
    grupo=get_turnos_AL()
    turnos=grupo[0]
    areas=grupo[1]
    UTS = MostrarUTS()
    return render_template('RUT.html',  nombres=nombres_emp, areas=areas, turnos=turnos, data=UTS )

@app.route('/RegistrarUT', methods=['POST', 'GET'])
def procesar():
    todos_empleados = get_all_empleados()
    if request.method == 'POST':
        empleado = int(request.form['EMPLEADO'])
        turno = int(request.form['TURNO'])
        area = int(request.form['AREA'])
        RegistrarAsis(empleado, turno, area)
    return render_template('index.html', data=todos_empleados)

@app.route('/RegistrarDispositivo', methods=['POST', 'GET'])
def RegisDispo():
    return render_template('RASISD.html')

@app.route('/RegistrarEmpleado', methods=['POST', 'GET'])
def RegisEmp():
    return render_template('REMP.html')

@app.route('/RegistrarAsistencia', methods=['POST', 'GET'])
def RegisAsis():
    nombres_emp = get_emp_name()
    if request.method == 'POST':
        empleado_id = int(request.form['EMPLEADO'])
        Unida = int(request.form['Unity'])
        DATE = request.form['fecha']
    else:
        empleado_id = None
    return render_template('RASIS.html', nombres=nombres_emp)

@app.route('/RegistrarAsistencia', methods=['POST', 'GET'])
def procesar_formulario():
    if request.method=='POST':
        Emp = int(request.form['EMPLEADO'])
    Result = DevolverUTS(Emp)
    nombres_emp = get_emp_name()
    return render_template('RASIS.html',dato=Result )

def generar_calendario():
    # Obtener la fecha actual
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    cal = cal = calendar.HTMLCalendar().formatmonth(year, month)
    return cal

if __name__=='__main__':
    app.run(debug=True, port=5000)