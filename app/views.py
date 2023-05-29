from app import app
from flask import render_template

from .models import *

@app.route('/')
def index():
    # Lógica para recuperar os usuários do banco de dados
    to_do = get_all_records()

    # Renderiza o template 'users.html' passando a lista de usuários
    return render_template('home.html', to_do=to_do)

@app.route('/add/<title>/<sub_title>/<text>')
def insert_to_do(title, sub_title, text):
    print(title, sub_title, text)
    insert_record(title, sub_title, text)
    return "Registro inserido com sucesso!"