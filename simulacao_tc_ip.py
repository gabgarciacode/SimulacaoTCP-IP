# Classe para representar um pacote de dados
class Pacote:
    def __init__(self, origem, destino, dados):
        self.origem = origem
        self.destino = destino
        self.dados = dados

    def __str__(self):
        return f"Origem: {self.origem}\nDestino: {self.destino}\nDados: {self.dados}"

# Classe para representar a camada de aplicação
class CamadaDeAplicacao:
    def __init__(self, camada_de_transporte):
        self.camada_de_transporte = camada_de_transporte

    def enviar(self, dados, destino):
        # Empacotando os dados na camada de aplicação
        pacote = Pacote("Máquina 1", destino, dados)
        print("Enviado da Camada de Aplicação:")
        print(pacote)
        # Enviando o pacote para a camada de transporte
        self.camada_de_transporte.receber(pacote)

    def receber(self, pacote):
        # Desempacotando os dados na camada de aplicação
        print("Recebido na Camada de Aplicação:")
        print(pacote)


# Classe para representar a camada de transporte
class CamadaDeTransporte:
    def __init__(self, camada_de_rede):
        self.camada_de_rede = camada_de_rede

    def receber(self, pacote):
        # Desempacotando os dados na camada de transporte
        print("Recebido na Camada de Transporte:")
        print(pacote)
        # Chamando a função anterior
        self.camada_de_rede.receber(pacote)

    def enviar(self, pacote):
        # Empacotando os dados na camada de transporte
        pacote_transportado = Pacote(
            pacote.origem, pacote.destino, f"[{pacote.dados}]")
        print("Enviado da Camada de Transporte:")
        print(pacote_transportado)
        # Enviando o pacote para a camada de rede
        self.camada_de_rede.receber(pacote_transportado)


# Classe para representar a camada de Rede
class CamadaDeRede:
    def __init__(self, camada_fisica):
        self.camada_fisica = camada_fisica

    def receber(self, pacote):
        # Desempacotando os dados na camada de rede
        print("Recebido na Camada de Rede:")
        print(pacote)
        # Chamando a função anterior
        self.camada_fisica.receber(pacote)

    def enviar(self, pacote):
        # Empacotando os dados na camada de rede
        pacote_rede = Pacote(pacote.origem, pacote.destino,
                             pacote.dados.encode())
        print("Enviado da Camada de Rede:")
        print(pacote_rede)
        # Enviando o pacote para a camada física
        self.camada_fisica.receber(pacote_rede)


# Classe para representar a camada física
class CamadaFisica:
    def __init__(self):
        pass  # Inicialização da camada física

    def receber(self, pacote):
        # Decodificando os dados na camada física
        print("Recebido na Camada Física:")
        print(pacote)
        # Transmitindo o pacote pela rede física
        print("Transmitindo o Pacote pela Rede Física...")

    def enviar(self, pacote):
        # Codificando os dados na camada física
        pacote_fisico = Pacote(pacote.origem, pacote.destino, pacote.dados)
        print("Enviado da Camada Física:")
        print(pacote_fisico)
        # Transmitindo o pacote pela rede física
        print("Transmitindo o Pacote pela Rede Física...")
        # Simulando a recepção do pacote pela camada física de destino
        destino = pacote_fisico.destino
        self.receber(Pacote(pacote_fisico.origem,
                     destino, pacote_fisico.dados))


# Criando as instâncias das camadas
camada_fisica = CamadaFisica()
camada_de_rede = CamadaDeRede(camada_fisica)
camada_de_transporte = CamadaDeTransporte(camada_de_rede)
camada_de_aplicacao = CamadaDeAplicacao(camada_de_transporte)

# Enviando um pacote da camada de aplicação
camada_de_aplicacao.enviar("Olá, mundo!", "Máquina 2")
