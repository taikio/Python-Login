from dao import pessoa_dao

class Pessoa():

    def __init__(self,params, param_list=list()):
        self.params = params
        self.param_list = param_list

        # quebra a lista de parâmetros deixando 'nome=valor'
        array = self.params.split('&')
        # index que indica quantas vezes o array será percorrido
        index = len(array)

        for i in range(index):
            # quebra a lista que até então é 'nome=valor'
            n = array[i].split('=')
            # atribui o valor (nome=valor) a lista de valores
            param_list.append(n[1])

        self.nome = param_list[0]
        self.cpf = param_list[1]
        self.usuario = param_list[2]
        self.senha = param_list[3]
        self.param_list.clear()

    def execute(self):
        print(self.nome+'\n')
        print(self.cpf+'\n')
        print(self.usuario+'\n')
        print(self.senha+'\n')
        dao = pessoa_dao.Pessoa_Dao(self)
        dao.salvar()
        return 'home.html'