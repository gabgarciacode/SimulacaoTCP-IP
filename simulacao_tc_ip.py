# Classe para representar um pacote de dados
class Pacote:
    contador = 0

    def __init__(self, origem, destino, dados):
        self.origem = origem
        self.destino = destino
        self.dados = dados
        Pacote.contador += 1

    def __str__(self):
        return f"Origem: {self.origem}\nDestino: {self.destino}\nDados: {self.dados}\nQuantidade de pacotes criados: {Pacote.contador}"

# Classe para representar a camada de aplicação
class CamadaDeAplicacao:
    contador = 0

    def __init__(self, camada_de_transporte):
        self.camada_de_transporte = camada_de_transporte

    def enviar(self, dados, destino):
        # Empacotando os dados na camada de aplicação
        pacote = Pacote("Máquina 1", destino, dados)
        print(
            f"Enviado da Camada de Aplicação (Contador: {CamadaDeAplicacao.contador}):")
        print(pacote)
        # Enviando o pacote para a camada de transporte
        self.camada_de_transporte.enviar(pacote)
        CamadaDeAplicacao.contador += 1

    def receber(self, pacote):
        # Desempacotando os dados na camada de aplicação
        print(
            f"Recebido na Camada de Aplicação (Contador: {CamadaDeAplicacao.contador}):")
        print(pacote)
        CamadaDeAplicacao.contador += 1



# Classe para representar a camada de transporte
class CamadaDeTransporte:
    def __init__(self, camada_de_rede):
        self.camada_de_rede = camada_de_rede
        self.contador = 0

    def receber(self, pacote):
        # Desempacotando os dados na camada de transporte
        print(f"Recebido na Camada de Transporte (contador: {self.contador}):")
        print(pacote)
        # Incrementando o contador
        self.contador += 1
        # Chamando a função anterior
        self.camada_de_rede.receber(pacote)

    def enviar(self, pacote):
        # Empacotando os dados na camada de transporte
        pacote_transportado = Pacote(
            pacote.origem, pacote.destino, f"[{pacote.dados}]")
        print(f"Enviado da Camada de Transporte (contador: {self.contador}):")
        print(pacote_transportado)
        # Incrementando o contador
        self.contador += 1
        # Enviando o pacote para a camada de rede
        self.camada_de_rede.receber(pacote_transportado)


# Classe para representar a camada de Rede
class CamadaDeRede:
    def __init__(self, camada_fisica):
        self.camada_fisica = camada_fisica
        self.contador = 0

    def receber(self, pacote):
        # Desempacotando os dados na camada de rede
        print(f"Recebido na Camada de Rede ({self.contador}):")
        print(pacote)
        self.contador += 1
        # Chamando a função anterior
        self.camada_fisica.receber(pacote)

    def enviar(self, pacote):
        # Empacotando os dados na camada de rede
        pacote_rede = Pacote(pacote.origem, pacote.destino,
                             pacote.dados.encode())
        print(f"Enviado da Camada de Rede ({self.contador}):")
        print(pacote_rede)
        self.contador += 1
        # Enviando o pacote para a camada física
        self.camada_fisica.receber(pacote_rede)

        # Simulação da transmissão do pacote pela rede
        print("Transmitindo o Pacote pela Rede...")
        # Simulação da chegada do pacote na camada de rede do destino
        print("Pacote Recebido na Camada de Rede do Destino!")
        # Desempacotando os dados na camada de rede do destino
        pacote_destino = Pacote(
            pacote_rede.origem, pacote_rede.destino, pacote_rede.dados.decode())
        print(f"Pacote Desempacotado na Camada de Rede do Destino:")
        print(pacote_destino)
        # Enviando o pacote para a camada física do destino
        self.camada_fisica.enviar(pacote_destino)

# Classe para representar a camada física


class CamadaFisica:
    contador = 0  # Variável de classe para contar os pacotes

    def __init__(self):
        pass  # Inicialização da camada física

    def receber(self, pacote):
        # Decodificando os dados na camada física
        print("Recebido na Camada Física:")
        print(pacote)
        # Incrementando o contador de pacotes
        CamadaFisica.contador += 1
        print(f"Contador de Pacotes: {CamadaFisica.contador}")
        # Transmitindo o pacote pela rede física
        print("Transmitindo o Pacote pela Rede Física...")

    def enviar(self, pacote):
        # Codificando os dados na camada física
        pacote_fisico = Pacote(pacote.origem, pacote.destino, pacote.dados)
        print("Enviado da Camada Física:")
        print(pacote_fisico)
        # Incrementando o contador de pacotes
        CamadaFisica.contador += 1
        print(f"Contador de Pacotes: {CamadaFisica.contador}")
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
