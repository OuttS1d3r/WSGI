# Imports
import wsgiref
from wsgiref.simple_server import make_server  
from jinja2 import Environment, FileSystemLoader
import mysql.connector
from wtforms import Form, StringField  
from BDD import *
import datetime, calendar

# Configuración
HOST = 'localhost'
PORT = 4000  
class Router:
    def __init__(self):
        self.routes = {}

    def route(self, path):
        def wrapper(handler):
            self.routes[path] = handler
            return handler
        return wrapper

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        handler = self.routes.get(path)
        if handler:
            return handler(environ, start_response)
        else:
            start_response('404 Not Found', [('Content-Type', 'text/plain')])
            return [b'Pagina no encontrada']
router = Router()

# Motor de plantillas
template_loader = FileSystemLoader(searchpath='./templates')
template_env = Environment(loader=template_loader)

# Formulario
class LoginForm(Form):
    username = StringField('Username') 

# Rutas
@router.route('/inicio')
def inicio(environ, start_response):
    
    data = get_all_empleados()
    calendario = generar_calendario()

    template = template_env.get_template('index.html')
    html = template.render(data=data, calendario=calendario)

    start_response('200 OK', [('Content-Type','text/html')])
    return [html.encode('utf-8')] 

def generar_calendario():
    # código para generar calendario
    now = datetime.datetime.now()
    year = now.year
    month = now.month

    return calendar.HTMLCalendar().formatmonth(year, month) 

# Asignar router a app  
app = router

# Crear servidor WSGI
httpd = make_server(HOST, PORT, app)
print(f"Servidor corriendo en http://{HOST}:{PORT}") 
httpd.serve_forever()