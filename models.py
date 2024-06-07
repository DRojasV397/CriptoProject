from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
'''
generate_password_hash(password, method='pbkdf2', salt_length=8):
Esta función toma una contraseña como entrada y devuelve su hash seguro. 
Utiliza un algoritmo de derivación de clave basado en la contraseña (PBKDF2) 
con una función hash SHA256 por defecto. También se puede especificar la longitud 
de la sal (un valor aleatorio que se añade a la contraseña antes de hashearla) con 
el argumento salt_length.



check_password_hash(hash, password):
Esta función verifica si una contraseña proporcionada coincide con un hash almacenado. 
Toma el hash generado previamente y la contraseña sin hashear como entrada y devuelve 
True si la contraseña coincide con el hash, y False si no coincide.

'''


db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)
    return app
