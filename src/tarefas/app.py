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
        tarefas_da_pagina=tarefas,
        tarefa_em_edicao=None
    )


"""criar rota de editar tarefa."""

"""<int:id_tarefa>: recebe um número inteiro pela URL."""
"""methods: determina quais métodos HTTP serão aceitos. Usei GET e POST, como sugerido."""
@app.route('/editar/<int:id_tarefa>', methods=['GET', 'POST'])
def editar(id_tarefa):


    """definição de uma variavel que busca tarefa."""
    tarefa = Tarefa.carregarTarefa(id_tarefa)

    if tarefa is None:
        return redirect(url_for('home'))

    """Se o ID não existir, o usuário volta para a página inicial."""

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
    pass


if __name__ == '__main__':
    app.run()