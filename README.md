  ![campus_marica](https://github.com/YagoTarsin/PetMatch/assets/125316134/3fc4ac24-6883-4096-a319-143fd04e76a2)
 

**Curso:** Engenharia de software	 

**Período:** 3º 

**Disciplina:** Estrutura de Dados 

**Professor:** [Márcio Alexandre Dias Garrido](https://github.com/marciogarridoLaCop) 

**Participantes:** _Angélica Gomes da Silva_ – 202211538  e _Yago Guimarães Tavares_ – 202211459 
##

**PROJETO: Sistema de Cadastro e Adoção de Animais** 

A Universidade de Vassouras do Campus 1 foi convidada pela prefeitura de Maricá para promover uma solução tecnológica em um dos problemas sociais da cidade, o abandono de animais. Mesmo considerado crime (O abandono de animais é crime, previsto na Lei de Crimes Ambientais - Lei Federal n° 9.605 de 1998), e notório que o índice de abandono vem crescendo a cada ano. 

Os alunos do curso de Engenharia de Software foram convocados para a reunião com a secretaria da cidade para entender a demanda solicitada e alguns pontos foram levantados. 

A prefeitura precisa de um sistema que possa cadastrar todos os animais por tipo (canino, felino, etc.) e para tanto, é uma premissa que seja possível inserir novos tipos dinamicamente. Precisa ainda, que sejam classificados por idade aproximada, cor, porte e se possui alguma particularidade. No mesmo sistema, deverá ter também um cadastro de pessoas interessadas na adoção, contendo os dados principais de contato e qual espécie teria o interesse de adotar. Ao escolher a espécie, deve também informar se possui alguma preferência do animal. Por fim, no final do mês a prefeitura emitirá um relatório de cruzamento de espécies disponíveis x possíveis candidatos, ou quando um candidato a adoção ligar, que o atendente possa pesquisar se há algum animal com as características informadas. 

Os alunos anotaram atentamente a todas as observações, criaram o fluxograma do estudo de caso, e posteriormente o primeiro protótipo em Python, ainda que em modo texto, e sem requisitos gráficos. A ideia foi apenas validar a proposta do programa junto ao solicitante. 

 

Um fluxograma foi criado para exemplificar a forma de funcionamento do sistema desde o cadastro até o seu momento final que se dá por meio da adoção. Veja abaixo: 


![Cadastro e adoção de animais](https://github.com/YagoTarsin/PetMatch/assets/125316134/0b6cc626-1825-46df-9bf3-539ff42729fe)

# Dependências:
 
- **python 3** (Modelo de linguagem) 
- **biblioteca PyQt5** (Interface gráfica) 
- **biblioteca csv** (Interações com arquivo .csv) 
- **biblioteca pandas** (Tratamento de dados) 
- **biblioteca webbrowser** (Abrir links web)

Use o seguinte comando para instalação: `pip install -r requirements.txt`

# Uso:

PetMatch é um sistema simples de cadastros de Pets para adoção/doação de animais.

## Interface Principal:

A interface principal é composta por 1 menu e 5 botões:

![image](https://github.com/YagoTarsin/PetMatch/assets/102929131/79b45342-97bc-43ad-b01e-3d6d4ee266ec)

## Cadastro de animais:

Quando clicado no botão "Cadastro de animais" abrirá uma tela de cadastro para todas as informações necessárias:

![image](https://github.com/YagoTarsin/PetMatch/assets/102929131/11a4c38a-2e59-42a3-8c51-3135ec5b5214)

## Caninos, Felinos e Outros:

Os 3 botões da direita são para mostrar as raças disponíveis de cada espécie, por exemplo quando escolho "Caninos" essa tela abrirá:

![image](https://github.com/YagoTarsin/PetMatch/assets/102929131/ae1c1dab-52a3-46c2-a992-2dc276fdfb5c)

![image](https://github.com/YagoTarsin/PetMatch/assets/102929131/4609fb37-090b-461b-be07-71293bacd3ea)


## Terminal de informações:

Quando escolhido algumas das opções demonstrado acima, uma tela de terminal mostrará todas as informações de contato da pessoa que deseja doar o pet da raça especifica:

![image](https://github.com/YagoTarsin/PetMatch/assets/102929131/b34362d3-06d7-4cc7-b764-98a55137d189)

## Site Univassouras:

Quando clicado na logo da Universidade de vassouras, será redirecionado para a pagina principal do site da Univassouras:

![image](https://github.com/YagoTarsin/PetMatch/assets/102929131/40549882-843f-4be7-bea5-d055cf853849)

## Arquivo (Remover Pet)

Quando clicado em (menu > arquivo > Remover Pet):

![image](https://github.com/YagoTarsin/PetMatch/assets/102929131/f6418332-38f7-46a4-94b1-aac05d6c2df8)

Uma tela irá se abrir para remover um pet por motivos de adoção, desistência ou felcimento:

![image](https://github.com/YagoTarsin/PetMatch/assets/102929131/f46c3e3e-c473-4a99-b320-af552d86e2a6)

## Arquivo (Novo interessado):

Quando clicado em (menu > arquivo > Novo Interessado):

![image](https://github.com/YagoTarsin/PetMatch/assets/102929131/f6418332-38f7-46a4-94b1-aac05d6c2df8)

Uma tela irá abrir para cadastrar os dados da pessoa interessada em um pet por espécie:

![image](https://github.com/YagoTarsin/PetMatch/assets/102929131/47d13e81-c390-499b-9ad9-f72e8ab55ad3)

## Arquivo (Interessados)

Quando clicado em (menu > arquivo > Interessados):

![image](https://github.com/YagoTarsin/PetMatch/assets/102929131/f6418332-38f7-46a4-94b1-aac05d6c2df8)

Uma tela de terminal irá abrir mostrando todas as pessoas interessadas em um pet com seus repectivos dados de contato e interesse:

![image](https://github.com/YagoTarsin/PetMatch/assets/102929131/a1b02088-a94f-49a7-9ae8-0de51bfae526)

## Pets

No menu Pets, temos 3 opções (Sobre Cães, Sobre Gatos, Sobre Animais). Quando clicado em um dessas opções você será redirecionado para sites interessantes que dão conhecimentos sobre os respectivos animais. A ideia é que os operadores do app saibam com o que estão lidando.

![image](https://github.com/YagoTarsin/PetMatch/assets/102929131/49bd787c-5b5a-4317-b340-e71fd2116dc6)

# Hierarquia de arquivos:

**1. Em seu diretório principal temos 2 arquivos e 1 pasta:**

- README.md (Arquivo README)
- requirements.txt (Arquivo para instalação das dependências)
- src (Pasta origem do app)

**2. Dentro do diretório "src" temos o diretório principal do app, composta por 5 arquivos e 3 diretórios**

- Principal.py (Arquivo python principal do app, onde rodamos o código inicialmente e nos mostra a interface principal)
- Cadastro.py (Arquivo python que abre a tela de cadastro de pets)
- RemoverPet.py (Arquivo python que abre a tela de remoção de pets)
- Terminal.py (Arquivo python que abre as telas de terminal para mostrar interessados e dados de doadores)
- Interessados.py (Arquivo python que abre a tela de cadastro de pessoas interessadas em adotar um pet)
- Imagens (Diretório onde ficam as imagens usadas no app)
- Banco (Diretório onde ficam os arquivos CSV)
- Scripts (Diretorio onde ficam arquivos .py paa scripts)

**3. Dentro da pasta "imagens" temos 7 arquivos PNG:**

- Cadastrar um novo pet.png (Imagem para botão de cadastro de pets)
- Gatos.png (Imagem para botão de felinos)
- caninos.png (imagem para botão de Caninos)
- Outros.png (Imagem para botão de Outros)
- univassouras.png (Imagem para botão do site de vassouras)
- fundo_cadastro (Imagem de fundo da tela de cadastro)
- icone.png (Icone do app)

**4. Dentro da pasta "Banco" temos 4 pastas:**

- Felinos (Onde são salvos os arquivos .csv de doadores de felinos)
- Caninos (Onde são salvos os arquivos .csv de doadores de caninos)
- Outros (Onde são salvos os arquivos .csv de doadores de outros tipos de animais)
- Interessados (Onde são salvos os arquivos .csv de pessoas interessadas)

**5. Dentro da pasta "Scripts" temos 1 arquivo:**

- FuncoesButtons.py (Arquivo python que executa funções necessária para tratamento de dados dentre outros)

# Código:

## Pilhas:

- Uso de pilhas para carregar combobox:

![image](https://github.com/YagoTarsin/PetMatch/assets/102929131/e11744d7-eb20-4aed-9206-2136d06765a6)

- Uso de pilhas para mostrar raças disponíveis:

![image](https://github.com/YagoTarsin/PetMatch/assets/102929131/88fff771-19f4-4a26-9a14-6491e9780cae)

- Uso de pilhas para remover pet

![image](https://github.com/YagoTarsin/PetMatch/assets/102929131/e3b3c1be-4201-4d92-a692-f5d3686ee6d8)

## Pesquisa binária:

- Pesquisa binária para pesquisar raça especifica de cada .csv

![image](https://github.com/YagoTarsin/PetMatch/assets/102929131/b671ab86-debd-4c39-979e-87895664bc1e)

- Pesquisa binária para pesquisar por raça e email:

![image](https://github.com/YagoTarsin/PetMatch/assets/102929131/4ef57e7b-9f30-4ea6-95d0-6be81ca27ad0)


