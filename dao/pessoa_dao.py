import sqlite3
from dao import connection_factory


class Pessoa_Dao():

    def __init__(self,pessoa):
        self.pessoa = pessoa
        self.dao = connection_factory.Conexao()

    def salvar(self):

        try:
            sql = "INSERT INTO pessoa(nome,cpf,usuario,senha) " \
                "VALUES('"+self.pessoa.nome+"','"+self.pessoa.cpf+"','"+self.pessoa.usuario+"','"+self.pessoa.senha+"')"

            self.dao.inicia_conexao()
            self.dao.cursor.execute(sql)
            self.dao.con.commit()
            self.dao.con.close()

            print('usuario cadastrado com sucesso')
            return
        except Exception:
            print('Não foi possível cadastrar')
            return




