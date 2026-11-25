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

        tarefa = Tarefa(titulo=titulo_form, data_conclusao=data_corrigida)

        tarefa.salvarTarefa()

        return redirect(url_for('home'))

    tarefas = Tarefa.listarTarefas()

    return render_template(
        'base.html',
        titulo_da_pagina='Minha lista de tarefas',
        tarefas_da_pagina=tarefas,
        tarefa_em_edicao=None
    )


@app.route('/editar/<int:id_tarefa>', methods=['GET', 'POST'])
def editar(id_tarefa):
    tarefa = Tarefa.carregarTarefa(id_tarefa)

    if tarefa is None:
        return redirect(url_for('home'))

    if request.method == 'POST':
        titulo_form = request.form['tituloTarefa']
        data_conclusao_form = request.form['dataConclusao']

        data_corrigida = data_conclusao_form if data_conclusao_form != '' else None

        tarefa.titulo = titulo_form
        tarefa.data_conclusao = data_corrigida

        tarefa.atualizarTarefa()

        return redirect(url_for('home'))

    return render_template(
        'base.html',
        titulo_da_pagina='Editar tarefa',
        tarefas_da_pagina=Tarefa.listarTarefas(),
        tarefa_em_edicao=tarefa
    )


@app.route('/delete/<int:id>')
def apagar_id_especificado(id):
    Tarefa.apagarTarefa(id)

    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run()