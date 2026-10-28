import mysql.connector as mc

class Database:
    def __init__():
        self.host = 'localhost'
        self.username = 'root'
        self.password = 'admin'
        self.database = 'tarefas'
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = return mc.connect(
                host= self.host,
                database= self.database,
                user= self.username,
                password= self.password
            )

            if self.connection.is_connected():
                self.cursor = self.connection.cursor(dictionary=True)
                print("Conexão com o banco de dados estabelecida com sucesso!")
        except Error as e:
            print(f"Erro de conexão: {e}")
            self.connection = None
            self.cursor = None

    def desconectar(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print("Conexão com o banco de dados encerrada.")

db = Database()
db.conectar()
db.desconectar()