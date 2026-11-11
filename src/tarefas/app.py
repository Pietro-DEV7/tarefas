
from flask import Flask, redirect, render_template, request, url_for

from tarefas.models.database import init_db
from tarefas.models.tarefa import Tarefa

app = Flask(__name__)

with app.app_context():
    init_db()


@app.route('/test')
def test():
    return 'Servidor online!'


@app.route('/apagar/<int:id_tarefa>', methods=['POST'])
def apagar(id_tarefa):

    Tarefa.apagarTarefa(id_tarefa)

    return redirect(url_for('home'))


@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        titulo_form = request.form['tituloTarefa']
        data_conclusao_form = request.form['dataConclusao']

        data_corrigida = data_conclusao_form if data_conclusao_form != '' else None

        # Instanciamos uma nova tarefa com os dados recebidos do form
        tarefa = Tarefa(titulo=titulo_form, data_conclusao=data_corrigida)

        # Salvamos a tarefa no banco
        tarefa.salvarTarefa()

        return redirect(url_for('home'))

    tarefas = Tarefa.listarTarefas()

    return render_template(
        'base.html',
        titulo_da_pagina='Minha lista de tarefas',
        tarefas_da_pagina=tarefas
    )

@app.route('/delete/<int:id>')
def apagar_id_especificado(id):
    pass

if __name__ == '__main__':
    app.run()
