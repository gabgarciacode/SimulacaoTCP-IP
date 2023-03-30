# SimulacaoTCP-IP

O código apresenta uma implementação de um simulador da pilha TCP/IP, que é um conjunto de protocolos de comunicação de dados amplamente utilizado na internet e em redes de computadores. A pilha TCP/IP é composta por várias camadas, cada uma com suas responsabilidades específicas no processo de comunicação. Nesse código, são representadas as camadas de aplicação, transporte, rede e física, e são utilizadas classes em Python para implementar cada uma dessas camadas. Através da interação entre essas camadas, é possível enviar e receber pacotes de dados entre diferentes máquinas em uma rede.

O código é dividido em cinco classes que representam cada uma das camadas: CamadaFisica, CamadaDeRede, CamadaDeTransporte, CamadaDeAplicacao e Pacote. Cada classe tem suas funções específicas e trabalha em conjunto com as demais camadas.

`Pacote`
Essa classe representa um pacote de dados que será transmitido na rede. Ela possui três atributos: origem, destino e dados. O atributo dados pode ser uma string ou qualquer outro tipo de dado que precise ser transmitido na rede.

`CamadaDeAplicacao`
CamadaDeAplicacao demonstra a camada de aplicação, sendo responsável por empacotar os dados em um objeto Pacote e enviar para a camada de transporte. A função enviar recebe os dados e o destino para criar um objeto Pacote e chamada a função receber da camada de transporte.

`CamadaDeTransporte`
A classe CamadaDeTransporte representa a camada de transporte, que é responsável por empacotar os dados em um novo objeto Pacote com a adição de informações de controle, como o número de sequência, checksum, entre outros. Esses dados são transmitidos para a camada de rede. A função enviar recebe um objeto Pacote, cria um novo objeto Pacote com as informações adicionais e chama a função receber da camada de rede.

`CamadaDeRede`
CamadaDeRede representa a camada de rede, que é responsável por enviar os pacotes através da rede física. Ela adiciona informações de endereçamento IP no pacote e transmite para a camada física. A função enviar recebe um objeto Pacote, cria um novo objeto Pacote com as informações de endereçamento IP e chama a função receber da camada física.

`CamadaFisica`
A classe CamadaFisica representa a camada física, sendo responsável por transmitir o pacote pela rede física. Ela recebe o objeto Pacote da camada de rede, codifica os dados e os transmite pela rede física. A função enviar recebe um objeto Pacote, codifica os dados, transmite pela rede física e chama a função receber da camada de destino.

`Exemplo de uso`
No final do código, há um exemplo de uso das classes, onde é criada uma instância de cada camada e é enviado um pacote da camada de aplicação para a máquina 2.

`Execução`
Para executar o código, basta copiar e colar no seu ambiente de desenvolvimento preferido, como o Visual Studio Code ou Jupyter Notebook, e executar.
