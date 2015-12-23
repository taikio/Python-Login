import sqlite3


class Conexao():

    def __init__(self):
        self.con = ''
        self.cursor = ''

    def inicia_conexao(self):
        try:

            self.con = sqlite3.connect('users.db')
            self.cursor = self.con.cursor()

            tabela = 'CREATE TABLE IF NOT EXISTS pessoa'\
                     '(id integer primary key autoincrement,'\
                     'nome varchar(100),'\
                     'cpf varchar(50),'\
                     'usuario varchar(50),'\
                     'senha varchar(20))'
            self.cursor.execute(tabela)

            return
        except Exception:
            print('Não foi possível se conectar com o banco ')
            return