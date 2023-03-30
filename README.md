# SimulacaoTCP-IP (Visão Geral)

O código apresenta uma implementação de um simulador da pilha TCP/IP, que é um conjunto de protocolos de comunicação de dados amplamente utilizado na internet e em redes de computadores. A pilha TCP/IP é composta por várias camadas, cada uma com suas responsabilidades específicas no processo de comunicação. Nesse código, são representadas as camadas de aplicação, transporte, rede e física, e são utilizadas classes em Python para implementar cada uma dessas camadas. Através da interação entre essas camadas, é possível enviar e receber pacotes de dados entre diferentes máquinas em uma rede.

O código é dividido em cinco classes que representam cada uma das camadas: CamadaFisica, CamadaDeRede, CamadaDeTransporte, CamadaDeAplicacao e Pacote. Cada classe tem suas funções específicas e trabalha em conjunto com as demais camadas.

`Pacote:`
A classe Pacote é responsável por representar uma unidade básica de dados que será transmitida entre as diferentes camadas de rede no modelo OSI. Ela é composta por três atributos: origem, destino e dados.

O atributo origem armazena a origem do pacote, ou seja, o endereço IP da máquina que está enviando o pacote. Já o atributo destino representa o destino do pacote, ou seja, o endereço IP da máquina que deve receber o pacote. Por fim, o atributo dados contém os dados que serão transmitidos entre as máquinas.

A classe Pacote é utilizada pelas outras classes do código para encapsular os dados que serão transmitidos, facilitando o processo de envio e recebimento dos dados entre as diferentes camadas de rede.

Linguagem utilizada: `Python`

Topologia utilizada: `Ponto a ponto`

`Exemplo de uso`
No final do código, há um exemplo de uso das classes, onde é criada uma instância de cada camada e é enviado um pacote da camada de aplicação para a máquina 2.

`Execução`
Para executar o código, basta copiar e colar no seu ambiente de desenvolvimento preferido, como o Visual Studio Code ou Jupyter Notebook, e executar.

# Funcionamento

O código fornece uma implementação simplificada de uma pilha de protocolos de rede com quatro camadas principais: camada de aplicação, camada de transporte, camada de rede e camada física.

`Camada de Aplicação:`
A camada de aplicação é responsável por empacotar e desempacotar os dados da aplicação. Quando a camada de aplicação envia um pacote, ela cria uma instância da classe Pacote e adiciona informações de origem, destino e dados. Em seguida, ela passa esse pacote para a camada de transporte enviar. Quando a camada de transporte recebe um pacote, ele chama a função receber da camada de aplicação para desempacotar os dados.

`Camada de Transporte:`
A camada de transporte é responsável por fornecer serviços de comunicação confiáveis. Quando a camada de transporte recebe um pacote da camada de aplicação, ele empacota novamente os dados na classe Pacote e adiciona informações de transporte. Ele então passa o pacote para a camada de rede enviar. Quando a camada de transporte recebe um pacote da camada de rede, ele chama a função receber da camada de aplicação para desempacotar os dados.

`Camada de Rede:`
A camada de rede é responsável por fornecer serviços de comunicação de rede. Quando a camada de rede recebe um pacote da camada de transporte, ele empacota novamente os dados na classe Pacote e adiciona informações de rede. Ele então passa o pacote para a camada física enviar. Quando a camada de rede recebe um pacote da camada física, ele chama a função receber da camada de transporte para desempacotar os dados.

`Camada Física:`
A camada física é responsável por enviar e receber dados físicos. Quando a camada física recebe um pacote, ele chama a função receber da camada de rede para desempacotar os dados. Quando a camada física envia um pacote, ele chama a função receber passando o mesmo pacote, simulando assim a recepção do pacote pelo destino.

A ordem de chamada das camadas é a seguinte: Camada de aplicação -> Camada de transporte -> Camada de rede -> Camada física. Cada camada chama a próxima camada na pilha para enviar ou receber os pacotes.

Ao final do código, é criada uma instância da classe CamadaDeAplicacao e invocado o método enviar, passando a mensagem "Hello World" e o destino "Máquina 2". Isso inicia todo o processo de envio e recebimento de pacotes pelas camadas da pilha de protocolos de rede.

`Tipos de dados encapsulados nas Camadas`

Geralmente, os seguintes tipos de dados são encapsulados nas camadas de rede:

Camada de aplicação: Dados da aplicação que estão sendo transmitidos, como uma mensagem de texto, arquivo de áudio ou vídeo, e-mail, etc. O cabeçalho pode incluir informações como a porta de origem e destino, protocolo de aplicação, tamanho dos dados, etc.

Camada de transporte: Segmentos ou datagramas que contêm informações sobre o controle de fluxo, confirmação de recebimento, multiplexação e demultiplexação de conexões. O cabeçalho pode incluir informações como número de sequência, número de confirmação, tamanho da janela, tipo de protocolo de transporte, etc.

Camada de rede: Pacotes IP que são usados para encaminhar os dados através da rede. O cabeçalho pode incluir informações como endereço IP de origem e destino, identificação de pacote, tempo de vida (TTL), tipo de protocolo de rede, etc.

Camada física: Bits que são transmitidos fisicamente na rede. O cabeçalho pode incluir informações como o endereço MAC de origem e destino, tipo de quadro, tamanho do quadro, sequência de bits de verificação de erros, etc.

Esses dados são encapsulados nos cabeçalhos das respectivas camadas do modelo OSI ou TCP/IP. Cada camada adiciona informações específicas ao cabeçalho, que são usadas para controlar e gerenciar a transmissão dos dados. O encapsulamento é o processo de adicionar informações de cabeçalho em torno dos dados em cada camada, e a remoção dessas informações de cabeçalho é conhecida como desencapsulamento.





