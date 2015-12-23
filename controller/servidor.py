from http.server import HTTPServer, BaseHTTPRequestHandler
from model import pessoa
from model import login


class RoutesAndRequestHandler(BaseHTTPRequestHandler):
    root_dir = '/home/welker/Documentos/projetos/python/htdocs/'
    destine = ''

    def do_GET(self):

        try:
            if self.path.endswith('.html'):
                # trata a rota solicitada e direciona para a página
                #if self.path == '/home.html':
                 #   self.destine = self.path
                    #abre o arquivo solicitado (concatena o endereço rais com o nome do arquivo solicitado)
                    f = open(self.root_dir + self.path)

                    # Envia Status OK
                    self.send_response(200)
                    self.send_header('Content-type', 'text-html')
                    self.end_headers()
                    #lê o arquivo encontrado e imprime o conteúdo no browser
                    self.wfile.write(f.read().encode('utf-8'))

                    f.close()
                    return
            if self.path.endswith('.css'):
                print('Entrou')
                f = open(self.root_dir + 'css/' + self.path)
                self.send_response(200)
                self.send_header('Content-type', 'text/css')
                self.end_headers()
                self.wfile.write(f.read().encode('utf-8'))
                f.close()

                return
        except IOError:
            self.send_error(404,"Arquivo não encontrado")
            return

    def do_POST(self):

        # recebe uma lista de parâmetros referente aos campos do formulário
        varLen = int(self.headers['Content-Length'])
        postVars = self.rfile.read(varLen)
        # decodifica a lista de parâmetros transformando em string
        string = postVars.decode('utf-8')

        if self.path == '/cadastrar':
            # estancia o objeto pessoa
            usuario = pessoa.Pessoa(string)
            self.destine = usuario.execute()

            try:
                f = open(self.root_dir + self.destine)

                # Envia Status OK
                self.send_response(200)
                self.send_header('Content-type', 'text-html')
                self.end_headers()
                self.wfile.write(f.read().encode('utf-8'))
                self.destine = None
                return
            except IOError:
                self.send_error(404,"Arquivo não encontrado")
                return

        if self.path == '/logar':
            logar = login.Login(string)
            self.destine = logar.execute()

            try:
                f = open(self.root_dir + self.destine)

                # Envia Status OK
                self.send_response(200)

                self.send_header('Content-type', 'text-html')
                self.end_headers()
                self.wfile.write(f.read().encode('utf-8'))
                self.destine = None
                return
            except IOError:
                self.send_error(404,"Arquivo não encontrado")
                return


# método que inicia o servidor
def run():

     httpd = None
     try:
       server_address = ('127.0.0.1',8000)
       httpd = HTTPServer(server_address, RoutesAndRequestHandler)
       print("Server active on IP = 127.0.0.1 and Port = 8000")
       httpd.serve_forever()

     except KeyboardInterrupt:
        httpd.socket.close()


if __name__ == '__main__':
   run()