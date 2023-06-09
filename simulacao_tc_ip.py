# Classe para representar um pacote de dados
class Pacote:

    def __init__(self, origem, destino, dados):
        self.origem = origem
        self.destino = destino
        self.dados = dados

    def __str__(self):
        return f"Origem: {self.origem}\nDestino: {self.destino}\nDados: {self.dados}\n"

# Classe para representar a camada de aplicação

class CamadaDeAplicacao: #Dados da aplicação que estão sendo transmitidos, como uma mensagem de texto, arquivo de áudio ou vídeo, e-mail, etc. O cabeçalho pode incluir informações como a porta de origem e destino, protocolo de aplicação, tamanho dos dados, etc. Definição para ilustar melhor.

    def __init__(self):
        self.camada_de_transporte = camada_de_transporte

    def enviar(self, dados, destino):
        # Empacotando os dados na camada de aplicação
        pacote = Pacote("Máquina 1", destino, dados)
        print(
            f"Enviado da Camada de Aplicação:")
        print(pacote)
        # Enviando o pacote para a camada de transporte
        self.camada_de_transporte().enviar(pacote)

    def receber(self, pacote):
        # Desempacotando os dados na camada de aplicação
        print(
            f"Recebido na Camada de Aplicação:")
        print(pacote)


# Classe para representar a camada de transporte

class CamadaDeTransporte: #Segmentos ou datagramas que contêm informações sobre o controle de fluxo, confirmação de recebimento, multiplexação e demultiplexação de conexões. O cabeçalho pode incluir informações como número de sequência, número de confirmação, tamanho da janela, tipo de protocolo de transporte, etc. Definição para ilustar melhor.
    def __init__(self):
        self.camada_de_aplicacao = camada_de_aplicacao
        self.camada_de_rede = camada_de_rede

    def receber(self, pacote):
        # Desempacotando os dados na camada de transporte
        print(f"Recebido na Camada de Transporte:")
        print(pacote)

        # Chamando a função anterior
        self.camada_de_aplicacao().receber(pacote)

    def enviar(self, pacote):
        # Empacotando os dados na camada de transporte
        pacote_transportado = Pacote(
            pacote.origem, pacote.destino, f"[{pacote.dados}]")
        print(f"Enviado da Camada de Transporte:")
        print(pacote_transportado)

        # Enviando o pacote para a camada de rede
        self.camada_de_rede().enviar(pacote_transportado)


# Classe para representar a camada de Rede

class CamadaDeRede: # Pacotes IP que são usados para encaminhar os dados através da rede. O cabeçalho pode incluir informações como endereço IP de origem e destino, identificação de pacote, tempo de vida (TTL), tipo de protocolo de rede, etc. Definição para ilustar melhor.
    def __init__(self):
        self.camada_de_transporte = camada_de_transporte
        self.camada_fisica = camada_fisica

    def receber(self, pacote):
        # Desempacotando os dados na camada de rede
        print(f"Recebido na Camada de Rede:")
        print(pacote)
        # Chamando a função anterior
        self.camada_de_transporte().receber(pacote)

    def enviar(self, pacote):
        # Empacotando os dados na camada de rede
        pacote_rede = Pacote(pacote.origem, pacote.destino,
                             pacote.dados.encode())
        print(f"Enviado da Camada de Rede:")
        print(pacote_rede)
        # Enviando o pacote para a camada física
        self.camada_fisica().enviar(pacote_rede)


class CamadaFisica: #Bits que são transmitidos fisicamente na rede. O cabeçalho pode incluir informações como o endereço MAC de origem e destino, tipo de quadro, tamanho do quadro, sequência de bits de verificação de erros, etc. Definição para ilustar melhor.

    def __init__(self):
        self.camada_de_rede = camada_de_rede
        # Inicialização da camada física

    def receber(self, pacote):
        # Decodificando os dados na camada física
        print("Recebido na Camada Física:")
        print(pacote)
        self.camada_de_rede().receber(pacote)

    def enviar(self, pacote):
        # Codificando os dados na camada física
        pacote_fisico = Pacote(pacote.origem, pacote.destino, pacote.dados)
        print("Enviado da Camada Física:")
        print(pacote_fisico)
        destino = pacote_fisico.destino
        self.receber(Pacote(pacote_fisico.origem,
                     destino, pacote_fisico.dados))


# Criando as camadas
camada_fisica = CamadaFisica
camada_de_rede = CamadaDeRede
camada_de_transporte = CamadaDeTransporte
camada_de_aplicacao = CamadaDeAplicacao

# Enviando os dados
camada_de_aplicacao().enviar("Hello World", "Máquina 2")
