
from datetime import datetime

from tarefas.models.database import Database


class Tarefa:
    """Provê métodos para armazenar, recuperar e processar os dados das tarefas
    criadas a partir do formulário principal.
    """

    def __init__(self, titulo, id=None, data_conclusao=None):
        self.id = id
        self.titulo = titulo
        self.data_conclusao = data_conclusao

    def salvarTarefa(self):
        """Salva a tarefa no banco de dados."""

        sql = '''
            INSERT INTO tarefa
            (id_tarefa, titulo_tarefa, data_tarefa)
            VALUES (%s, %s, %s);
        '''

        params = (
            int(datetime.now().timestamp() * 1000),
            self.titulo,
            self.data_conclusao
        )

        with Database() as db:
            db.executar(sql, params)

    @staticmethod
    def listarTarefas() -> list:
        """Lista as tarefas cadastradas."""

        sql = '''
            SELECT
                id_tarefa,
                titulo_tarefa,
                data_tarefa AS data_conclusao
            FROM tarefa
            LIMIT 100;
        '''

        with Database() as db:
            tarefas_banco = db.executar(sql)

        return tarefas_banco if tarefas_banco else []

    @staticmethod
    def carregarTarefa(id_tarefa):
        """Carrega uma tarefa específica do banco de dados."""

        sql = '''
            SELECT
                id_tarefa,
                titulo_tarefa,
                data_tarefa AS data_conclusao
            FROM tarefa
            WHERE id_tarefa = %s;
        '''

        params = (id_tarefa,)

        with Database() as db:
            resultado = db.executar(sql, params)

        if resultado:
            dados = resultado[0]

            return Tarefa(
                id=dados['id_tarefa'],
                titulo=dados['titulo_tarefa'],
                data_conclusao=dados['data_conclusao']
            )

        return None

    def atualizarTarefa(self):
        """Atualiza uma tarefa no banco de dados."""

        sql = '''
            UPDATE tarefa
            SET
                titulo_tarefa = %s,
                data_tarefa = %s
            WHERE id_tarefa = %s;
        '''

        params = (
            self.titulo,
            self.data_conclusao,
            self.id
        )

        with Database() as db:
            db.executar(sql, params)

    @staticmethod
    def apagarTarefa(id_tarefa):
        """Apaga uma tarefa do banco de dados."""

        sql = 'DELETE FROM tarefa WHERE id_tarefa = %s;'

        params = (id_tarefa,)

        with Database() as db:
            db.executar(sql, params)
