from dao import connection_factory


class Login_Dao():

    def __init__(self,login):
        self.login = login
        self.dao = connection_factory.Conexao()
        self.permitido = bool(0)

    def autenticar(self):

        try:
            sql = 'SELECT * FROM pessoa'

            self.dao.inicia_conexao()
            self.dao.cursor.execute(sql)

            for registro in self.dao.cursor.fetchall():
                if registro[3] == self.login.usuario and registro[4] == self.login.senha:
                    print('Usuario permitido')
                    self.permitido = bool(1)
                    continue

            self.dao.con.close()
            return self.permitido
        except IOError:
            print('Erro ao retornar dados')
            return self.permitido