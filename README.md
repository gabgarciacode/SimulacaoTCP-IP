# SimulacaoTCP-IP (Visão Geral)

O código apresenta uma implementação de um simulador da pilha TCP/IP, que é um conjunto de protocolos de comunicação de dados amplamente utilizado na internet e em redes de computadores. A pilha TCP/IP é composta por várias camadas, cada uma com suas responsabilidades específicas no processo de comunicação. Nesse código, são representadas as camadas de aplicação, transporte, rede e física, e são utilizadas classes em Python para implementar cada uma dessas camadas. Através da interação entre essas camadas, é possível enviar e receber pacotes de dados entre diferentes máquinas em uma rede.

O código é dividido em cinco classes que representam cada uma das camadas: CamadaFisica, CamadaDeRede, CamadaDeTransporte, CamadaDeAplicacao e Pacote. Cada classe tem suas funções específicas e trabalha em conjunto com as demais camadas.

`Pacote:`
A classe Pacote é responsável por representar uma unidade básica de dados que será transmitida entre as diferentes camadas de rede no modelo OSI. Ela é composta por três atributos: origem, destino e dados.

O atributo origem armazena a origem do pacote, ou seja, o endereço IP da máquina que está enviando o pacote. Já o atributo destino representa o destino do pacote, ou seja, o endereço IP da máquina que deve receber o pacote. Por fim, o atributo dados contém os dados que serão transmitidos entre as máquinas.

A classe Pacote é utilizada pelas outras classes do código para encapsular os dados que serão transmitidos, facilitando o processo de envio e recebimento dos dados entre as diferentes camadas de rede.

Linguagem utilizada: `Python`

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






