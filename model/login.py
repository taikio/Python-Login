from dao import login_dao


class Login():

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
            self.param_list.append(n[1])

        self.usuario = self.param_list[0]
        self.senha = self.param_list[1]
        self.param_list.clear()

    def execute(self):
        user = login_dao.Login_Dao(self)

        if user.autenticar():
            print(self.usuario+'\n')
            print(self.senha+'\n')
            return 'painel.html'
        else:
            return 'erro.html'
