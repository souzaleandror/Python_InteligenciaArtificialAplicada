#18/01/2026

Curso de
Python: Inteligência Artificial Aplicada

https://cursos.alura.com.br/course/python-ia-aplicada

Faça esse curso de IA para Dados e:
Explore a sintaxe básica do Python e a manipulação de variáveis, strings e estruturas condicionais.
Aplique loops e funções para estruturar lógicas e resolver desafios.
Utilize o Google Colab para praticar e validar os conceitos apresentados.
Manipule listas e dicionários para criar estruturas de dados eficientes.
Integre APIs de inteligência artificial e desenvolva chatbots interativos.
Analise grandes conjuntos de dados utilizando bibliotecas como Pandas e NumPy.
Aulas
Python e operações básicas  Ver primeiro vídeo
0 / 13
89min
Manipulação de strings
0 / 14
107min
Entrada e conversão de dados
0 / 10
95min
Leitura e escrita
0 / 10
58min
Conhecendo a Pandas
0 / 11
53min
Desafio Final
0 / 15
132min


@01-Python e operações básicas 

@@01
Apresentação

Olá! Meu nome é Fabrício Carraro, sou Program Manager na Alura, apresentador do podcast IA Sob Controle, e autor do livro "Inteligência Artificial e Chat GPT", publicado pela Casa do Código. Serei o instrutor deste curso de Python básico, abordando Python desde o início, com um foco também em inteligência artificial.

Audiodescrição: Fabrício é um homem de pele parda, com cabelos pretos curtos e sem barba. Ele veste uma camiseta azul marinho com a inscrição "Alura".
Introduzindo a linguagem de programação Python
Olá! Neste curso, nós vamos aprender toda a base da linguagem de programação Python. Começaremos entendendo o que é uma linguagem de programação e abordaremos conceitos básicos, como exibir informações na tela e manipular variáveis para armazenar dados.

Explorando conceitos fundamentais e inteligência artificial
Exploraremos elementos fundamentais, como estruturas condicionais e de repetição, além de conexões com Inteligências Artificiais (IAs), incluindo a IA do Gemini, do Google, e o GPT-OSS20B, um modelo aberto da OpenAI que qualquer pessoa pode usar, baixar ou acessar na nuvem. Utilizaremos o Grok para isso.

Aprendendo sobre funções, listas e dicionários
Também aprenderemos sobre funções, listas e dicionários em Python, oferecendo uma visão abrangente desde os conceitos básicos até o início do nível intermediário. No final do curso, desenvolveremos vários projetos, incluindo a execução de um modelo de linguagem, um LLM, como o Gema 3 do Google, localmente em seu laptop, sem a necessidade de conexão com servidores privados do Google ou da OpenAI.

Trabalhando com LLMs e engenharia de prompt
Trabalharemos tanto localmente, de forma visual e acessível, quanto utilizando o código necessário para isso, seja no Google Colab ou em uma IDE, para realizar essa programação e conexão com os LLMs. Abordaremos também a engenharia de prompt.

Concluindo com expectativas e motivação
Esperamos que você aproveite bastante este curso, que é extenso e denso, mas que proporcionará um aprendizado significativo. Boa sorte!

@@02
Começando com Python: Introdução e Configuração do Google Colab

Vamos começar. Talvez estejamos preocupados com algum receio, mas fiquemos tranquilos, pois vamos juntos nessa aventura. Primeiramente, o que é Python? Trata-se de uma linguagem de programação amplamente utilizada no mercado há alguns anos. Criada em 1991, ela foi se expandindo cada vez mais pela comunidade. As pessoas começaram a perceber que é mais fácil programar em Python do que em outras linguagens, pois a sintaxe e a forma de dar comandos ao computador são mais simples. Python se aproxima mais da língua inglesa, já que geralmente programamos com palavras e comandos em inglês. Quanto mais próximos esses comandos estiverem da nossa linguagem falada, mais fácil será compreendê-los, pelo menos inicialmente.

Escrevemos os comandos, o Python os interpreta e transmite ao computador, que executa o que pedimos por meio desses comandos. Para programar em Python, precisamos de um editor de texto, que pode ser o bloco de notas do computador, mas também existem várias IDEs (Ambientes de Desenvolvimento Integrado). Esses programas específicos são preparados para código, oferecendo dicas sobre onde erramos e autocompletando comandos que já entenderam que vamos utilizar, pois possuem conhecimento sobre a linguagem. Quando a inteligência artificial está envolvida, ela compreende o código inteiro e pode autocompletar para nós. Embora nem sempre esteja correto, muitas vezes estará.

Escolhendo o ambiente de desenvolvimento
Geralmente, o desenvolvimento de programas é realizado em ambientes específicos, como o Visual Studio Code (também conhecido como VS Code), JetBrains, Cursor, entre outros. No entanto, para este curso, utilizaremos uma ferramenta gratuita do Google, o Google Colab. A escolha pelo Google Colab se deve ao fato de não ser necessário instalar nada no computador, permitindo que o curso seja realizado inteiramente a partir do navegador. Estamos utilizando o navegador Chrome, mas é possível usar qualquer outro.

Para começar, devemos digitar "Google Colab" no navegador e clicar no link correspondente. Ao acessar a tela inicial, caso já tenhamos outros projetos, eles serão exibidos. Se houver algum erro, podemos atualizar a página para corrigir. O Google Colab utiliza notebooks, que são locais onde programamos, semelhantes a arquivos. Também é possível criar um novo notebook diretamente com colab.new, mas ambos os métodos são válidos. Vamos clicar em "novo notebook" para abrir um novo projeto no Google Colab.

Conectando ao Google Colab
Na tela do Colab, há várias informações. Podemos aumentar o zoom para facilitar a leitura. Antes de tudo, é importante clicar no botão "conectar", localizado no canto superior direito da tela. Ao fazer isso, estamos nos conectando aos servidores do Google, pois não utilizamos o computador local. Mesmo que o computador não seja muito potente, é possível realizar projetos interessantes diretamente do navegador, seja ele o Google Chrome, Mozilla, Microsoft Edge, Safari, ou qualquer outro, pois estamos utilizando os recursos dos servidores do Google.

Com essa introdução ao Colab, que será o ambiente de trabalho, no próximo vídeo, começaremos a programar em Python.

@@03
Explorando Células, a Função `print` e Tipos de Dados

Agora que já criamos nosso notebook no Google Colab, podemos observar que provavelmente haverá um sinal de marcação verde, indicando que a conexão com os servidores do Google foi bem-sucedida. Com isso, podemos começar a programar.

Antes de iniciarmos, é importante destacar que no Colab, cada bloco é chamado de célula. Essas células podem ser de código ou de texto. Ao passar o mouse sobre o meio ou a parte inferior de uma célula, é possível adicionar um novo bloco de código ou texto. Vamos adicionar um bloco de texto, onde podemos digitar livremente, como se fosse um texto comum. Por exemplo, podemos começar a aula de Python. Este texto não tem relação com o código; serve apenas para organização, permitindo fechar e abrir conforme necessário. Podemos, por exemplo, nomear como aula 1, aula 2, aula 3, etc.

Explorando blocos de código e introduzindo a função print
Além disso, existe o bloco de código, semelhante ao que já estava presente ao abrirmos o notebook. Ele sugere que comecemos a programar ou geremos código com a IA. A inteligência artificial já faz parte de nossas vidas, e no futuro, muitas tarefas poderão ser realizadas com ela. Durante o curso, utilizaremos a IA para diversas atividades, como fazer perguntas. Deixamos o Google Gemini aberto para eventuais dúvidas, mas, por enquanto, faremos tudo manualmente.

Com essas informações, vamos iniciar a programação. Será mais simples do que talvez imaginemos. A primeira tarefa em Python será inserir um valor e solicitar que ele seja exibido.

Executando código e entendendo a função print
Para começar, vamos inserir o número 5 em uma célula de código e executá-la:

5
COPIAR CÓDIGO
Ao clicar no botão de reproduzir, que é um botão de play, podemos clicar com o mouse ou usar o atalho "Ctrl+Enter" para rodar essa célula. Ele mostrou o número 5, ou seja, passamos o valor 5 e ele entendeu. No entanto, isso não funciona para todos os tipos de dados. Quando queremos mostrar algo para a pessoa que está vendo nossa programação, a função que usamos na maioria das vezes é a print, que significa imprimir em inglês, no sentido de mostrar algo na tela.

Utilizando a função print para exibir texto
Vamos introduzir a função print:

print
COPIAR CÓDIGO
Sempre que temos uma função, precisamos abrir e fechar parênteses, e dentro do print, colocamos o que queremos mostrar. Vamos usar a função print para exibir o número 5:

print(5)
COPIAR CÓDIGO
Se clicarmos, ele faz a mesma coisa que antes, mostrando o mesmo resultado. Vamos adicionar mais um bloco de código, mais uma célula, e agora queremos mostrar frases e palavras.

Corrigindo erros de sintaxe ao imprimir texto
Vamos usar o print com a frase mais clássica quando começamos a aprender programação: "Hello World" em inglês, que em português é "Olá Mundo". Vamos escrever "Olá Mundo". Notamos um sublinhado amarelo estranho, mas vamos rodar para ver o que acontece. Encontramos nosso primeiro erro: um syntax error (erro de sintaxe). A sintaxe está inválida, ou seja, a forma como escrevemos não está correta. Isso ocorre porque, para números, não há problema, mas para texto, ele pode interpretar como um comando ou uma frase simples.

Para diferenciar comandos ou variáveis de texto simples, colocamos aspas em volta do texto. Podem ser aspas duplas ou simples. Vamos dar os dois exemplos. Primeiro, com aspas duplas:

print("Olá mundo")
COPIAR CÓDIGO
Agora, sem erro, ele imprimiu corretamente. Podemos copiar e trocar por aspas simples, e ele também imprimirá corretamente:

print('Olá mundo')
COPIAR CÓDIGO
Combinando strings e inteiros no print
Quando falamos de texto, chamamos de string. Podemos adicionar um bloco de texto, não de código, e explicar que textos ou palavras são chamados de string em programação.

Podemos combinar essas coisas dentro do print. Vamos dar um print novamente, abrir e fechar parênteses, e colocar "Olá Mundo". Queremos juntar um número, por exemplo, mais 5. Será que funciona?

print("Olá mundo" + 5)
COPIAR CÓDIGO
Não conseguimos. Ele tentou, mas só podemos concatenar strings (texto simples), não int (inteiros). O que é um int? É um número inteiro, como 1, 2, 3, 4, 5, 10, 20, sem frações.

Corrigindo a concatenação de strings e inteiros
Se quisermos que o número 5 seja um caractere, podemos colocá-lo entre aspas. Agora ele imprime "Olá Mundo 5" junto, porque não colocamos espaço. Vamos corrigir isso:

print("Olá mundo " + "5")
COPIAR CÓDIGO
Agora ele imprimirá "Olá Mundo 5" corretamente. Parabéns, conhecemos um pouco sobre strings, como usar o print, o que é um int em Python e como juntar essas coisas no print. Continuaremos na próxima aula.

@@04
Variáveis, Operações Matemáticas e Concatenação de Strings

Agora que já sabemos imprimir informações na tela para o usuário, vamos continuar explorando o Python. Por exemplo, mencionamos que o texto é "Olá Mundo" e o número é 5. No entanto, não conseguimos realizar operações com esses valores, pois tivemos que escrever manualmente esse número e essa palavra. Quando imprimimos o número 5 sozinho, como um número e não como uma string (texto), não conseguimos fazer mais nada com ele além disso.

Para começar, podemos imprimir uma combinação de texto e número como uma string. Veja o exemplo abaixo:

print("Olá mundo " + "5")
Se quisermos, por exemplo, somar esse número, como 5 mais 2, podemos adicionar um novo bloco de código e realizar a operação 5 + 2. Vamos ver o resultado:

5 + 2
O resultado é 7. O Python entende o que queremos fazer. Será que isso funciona dentro do comando print também? Vamos copiar a operação 5 + 2 e colocá-la dentro do print.

print(5 + 2)
Funcionou, e o resultado correto, que é 7, foi exibido.

Introduzindo o conceito de variáveis
Agora, imagine que temos uma situação em que queremos somar um ano à idade de uma pessoa, ou adicionar 5 anos, dependendo do caso. No entanto, não gostamos desse exemplo, então vamos mudar para outro. Vamos considerar uma situação em que precisamos guardar um valor para usar mais tarde, como o preço de um ingresso ou o valor de uma cesta de compras. Não queremos ter que escrever manualmente cada vez que precisarmos desse valor.

Para isso, utilizamos variáveis, que são basicamente "caixinhas" onde podemos armazenar um valor. Não importa o tipo de valor: pode ser um número inteiro, um número decimal, um texto, etc. Vamos supor que estamos no supermercado e queremos comprar um produto. Podemos chamar esse produto de produto1, por exemplo.

Se quisermos atribuir um valor a uma variável, é bastante simples. Basta usar o sinal de igual e definir o preço, por exemplo, de um produto. Suponhamos que um macarrão custe 5 reais. O produto1 terá esse valor de 5.

produto1 = 5
Ao executar o bloco de código, pode parecer que nada aconteceu. Anteriormente, quando digitávamos o número 5, ele era exibido abaixo. Ao usar um comando de impressão de texto ou número, ele também era exibido. Neste caso, nada foi mostrado porque o valor foi armazenado na memória para uso posterior. Se abrirmos um novo bloco de código e digitarmos produto1, ao executá-lo, ele retornará o valor 5.

produto1
Isso ocorre porque o valor está armazenado na variável produto1, que representa o macarrão que estamos comprando. Podemos também usar o comando print(produto1), que resultará no mesmo valor.

print(produto1)
Trabalhando com múltiplas variáveis e operações
No entanto, não compramos apenas macarrão no supermercado; adquirimos outros itens. Por exemplo, o produto2 pode ser um celular, que custa 2 mil reais.

produto2 = 2000
Ao executar o código, o valor de 2 mil é armazenado na variável. A variável é chamada assim porque pode ser alterada. Se usarmos print(produto2), ele retornará 2 mil, que é o valor armazenado na memória.

print(produto2)
Agora, podemos realizar operações com essas variáveis. Temos o produto1, que custa 5 reais, e o produto2, que custa 2 mil reais. Suponhamos que haja um produto3, que custa 1 real, como um chiclete.

produto3 = 1
Se quisermos somar os três produtos, podemos fazer isso dentro de um comando print, usando o sinal de mais. A soma de produto1, produto2 e produto3 resultará em 2.006 reais.

print(produto1 + produto2 + produto3)
Ao executar o código, ele confirmará esse valor. Esses valores são números inteiros armazenados nas variáveis produto1, produto2 e produto3. Podemos realizar operações com essas variáveis, assim como fizemos com números. O mesmo se aplica a textos. Por exemplo, podemos definir nome_do_produto1 como "macarrão", nome_do_produto2 como "celular" e nome_do_produto3 como "bala". Esses textos devem ser escritos entre aspas, duplas ou simples.

nome_do_produto1 = "Macarrão"
nome_do_produto2 = "Celular"
nome_do_produto3 = "Bala"
Podemos exibir esses nomes na tela. Se quisermos que os nomes apareçam separados por espaços, podemos adicionar espaços entre as variáveis. Uma opção é incluir o espaço dentro das aspas, mas uma abordagem melhor é adicionar um espaço em branco entre as variáveis ao exibi-las.

print(nome_do_produto1 + " " + nome_do_produto2 + " " + nome_do_produto3)
Isso garantirá que os nomes sejam exibidos de forma clara e separada. Na próxima aula, continuaremos a explorar variáveis e outras operações que podemos realizar com elas.

@@06
Nomeclatura e Tipos de Dados em Python: `int`, `float`, `str` e `bool`

Ao finalizarmos o tema de variáveis, é importante observar que todas as variáveis criadas foram nomeadas de forma descritiva, utilizando uma única palavra ou palavras unidas por um underscore (sublinhado). Nunca utilizamos espaços entre as palavras. Isso ocorre porque, ao criar variáveis em uma linguagem de programação como Python, devemos seguir algumas regras. Uma delas é que não podemos usar espaços nos nomes das variáveis. Por exemplo, se tentarmos criar uma variável chamada total por pessoa e atribuir a ela o valor de total dividido por amigos, ocorrerá um erro de sintaxe.

# Tentativa de criar uma variável com espaço no nome
total por pessoa = total / amigos
COPIAR CÓDIGO
Outra regra é que não podemos iniciar o nome de uma variável com um número. Se tentarmos criar uma variável chamada 10pessoas, o Python não entenderá, pois o número no início pode confundir o interpretador, que não saberá se é uma variável ou um comando.

# Tentativa de criar uma variável começando com um número
10pessoas = total / amigos
COPIAR CÓDIGO
Evitando nomes de comandos como variáveis
Além disso, não devemos usar nomes de comandos como nomes de variáveis. Por exemplo, chamar uma variável de print pode causar confusão, pois o Python pode interpretar que estamos tentando usar o comando print em vez de uma variável. Isso pode levar a erros no código, como aconteceu quando o Python interpretou print como um valor em vez de um comando, obrigando-nos a reiniciar o ambiente de execução.

# Tentativa de usar um nome de comando como variável
print = total / amigos
COPIAR CÓDIGO
Para reiniciar o ambiente no Google Colab, podemos ir em "ambiente de execução" e clicar em "reiniciar sessão". Isso reiniciará o ambiente, permitindo que o código seja executado novamente desde o início. Também podemos optar por "reiniciar sessão e executar tudo", o que reiniciará e executará todas as células de código na ordem.

Utilizando convenções de nomenclatura em Python
Ao nomear variáveis em Python, o padrão é usar underscores para separar palavras. Embora outras linguagens possam preferir outras convenções, como usar letras maiúsculas no início de cada palavra, a comunidade Python adotou o uso de underscores como padrão. Usar convenções de outras linguagens em Python pode parecer estranho, como um sotaque diferente. Portanto, é recomendável seguir o padrão da linguagem Python para facilitar a leitura e manutenção do código.

Entre as palavras no nome da variável, por exemplo, outra questão que queremos abordar sobre variáveis são os tipos. Podemos analisar os tipos das variáveis, que, como mencionado, incluem o tipo de número inteiro, número decimal, e string. Existe um comando, um método, uma função que podemos usar para saber qual é o tipo de uma variável específica. Podemos utilizar o comando type em inglês, que funciona de maneira semelhante ao print, onde abrimos e fechamos parênteses e colocamos uma variável dentro.

# Uso do comando type para verificar o tipo de uma variável
type()
COPIAR CÓDIGO
Verificando tipos de variáveis
Por exemplo, a variável aluguel, que tem o valor de mil reais, ao verificarmos o tipo com type(aluguel), deveria retornar um número inteiro. Ao executar, vemos que o resultado é int, que é a abreviação de inteiro, equivalente a um número inteiro.

# Verificando o tipo da variável aluguel
type(aluguel)
COPIAR CÓDIGO
Vamos agora verificar o total_por_pessoa, que não é um número inteiro, mas sim um número decimal. Ao executar type(total_por_pessoa), o resultado será float, que é uma palavra em inglês para flutuante. Em programação, números decimais são chamados de ponto flutuante, e a abreviação para isso é float. Assim, int representa números inteiros e float representa números decimais ou de ponto flutuante.

# Verificando o tipo da variável total_por_pessoa
type(total_por_pessoa)
COPIAR CÓDIGO
Explorando tipos de dados em Python
Lembrando de outras variáveis que utilizamos anteriormente, como o nome_do_produto_1, que era "macarrão", é importante lembrar que texto em linguagem de programação é chamado de string. Ao substituir pelo nome_do_produto_1 e verificar o tipo, obtemos str, que significa string.

# Verificando o tipo da variável nome_do_produto_1
type(nome_do_produto1)
COPIAR CÓDIGO
Para finalizar, queremos mostrar outro tipo que também existe, que é o tipo binário, muito utilizado para representar verdadeiro ou falso, 1 ou 0. Por exemplo, se uma pessoa tem carteira de motorista, podemos dizer que Pedro tem carteira de motorista, então True, que significa verdadeiro em inglês. Já Mário, que não tem carteira de motorista, recebe False, que significa falso.

# Definindo variáveis booleanas
pedro_tem_carteira_de_motorista = True
mario_tem_carteira_de_motorista = False
COPIAR CÓDIGO
Identificando variáveis booleanas
Ao verificar o tipo dessas variáveis, não encontramos um tipo True ou False como número ou string, pois não estão entre aspas. Eles são um tipo especial chamado bool, abreviação de booleano, que representa verdadeiro ou falso, sim ou não, 1 ou 0. No caso de Pedro, type(True) retorna bool, indicando que ele tem carteira de motorista. Para Mário, type(False) também retorna bool, indicando que ele não tem.

# Verificando o tipo das variáveis booleanas
type(pedro_tem_carteira_de_motorista)
type(mario_tem_carteira_de_motorista)
COPIAR CÓDIGO
Agora que já exploramos mais sobre variáveis, na próxima aula, vamos entrar nos métodos e nas operações que podemos realizar com textos e strings.

@@07
Manipulando Strings em Python: Métodos `lower`, `upper`, `strip` e `replace`

Agora vamos explorar as strings (cadeias de caracteres) em Python. O próprio Python já possui diversos métodos nativos que nos permitem manipular strings sem a necessidade de criar algo do zero. Podemos, por exemplo, converter todo o texto para letras minúsculas ou maiúsculas, substituir partes do texto, entre outras funcionalidades.

Para começar, vamos definir um texto de exemplo: "Fabrício Carraro da Alura". Este texto está sem padrão e com formatação estranha. Vamos adicionar alguns espaços extras no início, no meio e no final para torná-lo ainda mais desorganizado. Nosso objetivo será transformar esse texto inicial em um texto final, onde tudo estará em maiúsculas e sem os espaços extras.

Definindo e imprimindo o texto inicial
Vamos criar uma variável chamada texto e atribuir a ela o nosso texto inicial, incluindo os espaços adicionais. Lembrando que strings em Python são delimitadas por aspas simples ou duplas. Vamos imprimir o texto para visualizar como ele está no momento.

texto = " Fabricio CARRaro da alura "
print(texto)
COPIAR CÓDIGO
O primeiro passo será transformar todo o texto em letras minúsculas. Para isso, utilizamos o método lower. Em Python, aplicamos um método a uma variável utilizando a sintaxe variável.método(). Assim, para converter nosso texto para minúsculas, usamos texto.lower(). Podemos imprimir o resultado para verificar a mudança. Note que os espaços extras ainda estão presentes.

print(texto.lower())
COPIAR CÓDIGO
Convertendo texto para maiúsculas e removendo espaços
Em seguida, vamos converter todo o texto para letras maiúsculas utilizando o método upper, que é o oposto de lower. Aplicamos texto.upper() e imprimimos o resultado. Agora, o texto está em letras maiúsculas, mas ainda com os espaços indesejados.

print(texto.upper())
COPIAR CÓDIGO
Para remover os espaços extras, utilizamos o método strip. Este método elimina os espaços no início e no final da string, mas mantém os espaços entre as palavras. Aplicamos texto.strip() e imprimimos o resultado para verificar a remoção dos espaços.

print(texto.strip())
COPIAR CÓDIGO
Substituindo partes do texto e discutindo persistência de alterações
Por fim, vamos aprender a substituir partes do texto utilizando o método replace. Este método é um pouco diferente dos anteriores, pois requer argumentos. Precisamos especificar o que queremos substituir e pelo quê. Por exemplo, texto.replace("Carraro", "Silva") substituiria "Carraro" por "Silva" no texto.

Esses são alguns dos métodos básicos para manipulação de strings em Python. Com eles, podemos realizar diversas operações de formatação e substituição de texto de maneira eficiente.

Na string que estávamos antes do ponto, o método replace vai pegar o elemento que queremos substituir e também o elemento pelo qual queremos substituí-lo. No nosso caso, queremos substituir todos os lugares onde houver dois espaços por apenas um espaço. No replace, abrimos aspas, lembrando que mesmo o espaço deve estar entre aspas. Havíamos feito isso para adicionar espaços entre as palavras "macarrão", "celular" e "bala". Agora, vamos substituir dois espaços por um espaço apenas. Vamos imprimir isso e observar o resultado.

print(texto.replace("  ", " "))
COPIAR CÓDIGO
Ele retornou o texto sem estar todo em maiúsculo ou minúsculo, e com espaços antes e depois, mas não mais entre "carário" e "dá". Percebemos que, ao aplicar um método em uma variável, como a variável texto, o valor original não é alterado. Se imprimirmos a variável texto, ela estará como inicialmente. Isso ocorre porque não substituímos o valor. Para que a substituição ocorra, devemos realizar as operações e salvar o resultado em outra variável, como texto_novo, ou sobrescrever o valor da própria variável texto, como fizemos com a variável aluguel.

Aplicando múltiplos métodos e salvando alterações
No caso do aluguel, subtraímos 100 e sobrescrevemos o resultado na variável aluguel, substituindo o valor anterior. Os métodos não alteram o valor original da variável texto. Vamos agora tentar fazer tudo isso junto. Primeiro, podemos remover os espaços no início e no final com strip. Depois, podemos aplicar os outros métodos desejados, como deixar tudo em maiúsculo e substituir dois espaços por um. Podemos fazer isso passo a passo ou tudo de uma vez.

Sem alterar a variável texto, podemos simplesmente imprimir o resultado. Primeiro, aplicamos o strip para remover os espaços no início e no final da string. Depois, aplicamos o upper para deixar tudo em maiúsculo, e, por fim, o replace para substituir dois espaços por um. Ao imprimir, obtemos o resultado desejado: tudo em maiúsculo, sem espaços no meio, no início ou no final. No entanto, a variável texto permanece inalterada.

print(texto.strip().upper().replace("  ", " "))
COPIAR CÓDIGO
Em alguns casos, isso é desejável, mas em outros, queremos que a variável inicial seja alterada. Para isso, atribuímos o resultado das operações à variável texto e, em seguida, imprimimos. O processo começa do lado direito do sinal de igual: aplicamos o strip, depois o upper, e, por fim, o replace. Após realizar todas essas operações, o resultado é armazenado na variável texto, substituindo o valor anterior.

texto = texto.strip().upper().replace("  ", " ")
print(texto)
COPIAR CÓDIGO
Por fim, imprimimos o novo texto, que é "FABRICIO CARRARO DA ALURA". Podemos imprimir no mesmo bloco ou separadamente. Agora que fizemos essa substituição e salvamento, estamos prontos para, no próximo vídeo, aprender a pedir dados ao usuário, coletá-los e tratá-los internamente. Até mais!

@@08
Recebendo Dados do Usuário com `input` e Formatando Textos com fStrings

Agora que já vimos como usar métodos com strings, vamos aprender a receber dados, solicitando-os a uma pessoa usuária. Isso será muito importante quando formos trabalhar com modelos de linguagem, como LLMs (Large Language Models). Para isso, vamos criar mais uma célula de código.

Podemos criar um novo operador, um novo método. Como já percebemos, os métodos geralmente têm parênteses, como o print, e este não será diferente. É um método que espera uma entrada da pessoa usuária. Em inglês, o nome dele é uma forma de se referir a entrada de dados: input.

input()
COPIAR CÓDIGO
Ele terá parênteses, e dentro deles podemos não colocar nada, mas é recomendado inserir um texto, por exemplo, a informação que desejamos que a pessoa usuária forneça.

input("")
COPIAR CÓDIGO
Solicitando e armazenando dados do usuário
Vamos supor que queremos o nome da pessoa usuária. Podemos inserir um texto, lembrando que textos, ou strings, são sempre entre aspas: "Digite o seu nome:". Podemos adicionar um espaço para melhorar a formatação.

input("Digite o seu nome: ")
COPIAR CÓDIGO
Quando executamos essa célula, o texto que digitamos aparece como um pedido de entrada para a pessoa usuária, com um espaço para inserir algo, neste caso, um nome. Vou escrever "Fabrício". Diferente de outros casos, em que ao clicar no botão de executar a operação é realizada imediatamente, aqui o código fica aguardando até que algo seja digitado. Após digitar "Fabrício" e pressionar "Enter", o nome é exibido.

No entanto, o problema é que não armazenamos esse nome em nenhum lugar. Se quisermos saber qual era o nome da pessoa usuária, não temos onde procurar. Para resolver isso, vamos fazer o que temos feito até agora: realizar uma operação do lado direito do sinal de igual e armazenar o resultado em uma variável. Vamos chamar essa variável de nome.

nome = input("Digite o seu nome: ")
COPIAR CÓDIGO
Vamos executar novamente, escrever "Fabrício", e se quisermos, por exemplo, imprimir a variável nome, ela conterá "Fabrício".

print(nome)
COPIAR CÓDIGO
Solicitando múltiplos dados e verificando tipos
Agora, vamos fazer algo diferente. Em vez de apenas solicitar o nome, vamos perguntar também a idade da pessoa usuária: "Digite a sua idade:". Vamos supor que a idade seja 18 anos.

idade = input("Digite a sua idade: ")
COPIAR CÓDIGO
Vamos imprimir a idade, que será 18.

print(idade)
COPIAR CÓDIGO
No entanto, há um detalhe importante. Lembramos que aprendemos a verificar os tipos das variáveis: inteiro (int), números de ponto flutuante (float), texto (str), e booleano (bool), que representa verdadeiro ou falso. Vamos verificar o tipo das variáveis nome e idade usando a função type.

type(nome)
type(idade)
COPIAR CÓDIGO
Ao executar, veremos que nome é do tipo string, o que está correto. No entanto, idade também é uma string, apesar de termos inserido um número. Isso ocorre porque o input assume que tudo é texto. Em alguns casos, isso não será adequado, como no caso da idade. Se quisermos converter para um tipo específico, como um número inteiro, podemos usar o nome do tipo, neste caso, int, como se fosse um método ou função. Abrimos e fechamos parênteses, e ele fará a conversão.

int(idade)
COPIAR CÓDIGO
Vamos pegar a variável idade e aplicar a conversão para inteiro. Isso transformará a string em um tipo inteiro. O resultado será armazenado novamente na variável idade, sobrescrevendo o valor anterior.

idade = int(idade)
COPIAR CÓDIGO
Ao executar, veremos que o tipo da variável idade não é mais string, mas sim inteiro. Essa conversão pode ser muito útil, dependendo de como manipulamos essas variáveis.

type(idade)
COPIAR CÓDIGO
Concatenando strings e variáveis
Agora, já temos praticamente todas as ferramentas que precisamos para escrever um texto completo, misturando strings (cadeias de caracteres) e variáveis. Vamos tentar fazer isso normalmente. Vamos fazer um print: "A pessoa se chama..." e aqui, onde está o nome? Guardamos na variável nome. E tem... idade, que está na variável idade. Anos de idade. Vamos dar um print.

print("A pessoa se chama nome e tem idade anos de idade.")
COPIAR CÓDIGO
Opa! Deu tudo errado. Lembrando que, para coisas de texto, precisamos de parênteses. E, para textos, precisamos de aspas para englobá-los. Vamos rodar isso aqui: "A pessoa se chama nome e tem idade anos de idade." Faz sentido, não é? Porque o que fizemos aqui foi não colocar a variável nome, mas sim a palavra "nome", pois está dentro das mesmas aspas.

Para fazermos isso de forma correta, há dois jeitos. Ambos são usados, mas o segundo é o mais correto. Vamos ensinar os dois. O primeiro é mais fácil, que é exatamente o que fizemos anteriormente: separar variáveis e usar o sinal de mais. O texto, no caso, era apenas o espaço em branco. Lá embaixo será texto real. Vamos lá. O texto é: "A pessoa se chama", espaço, e então podemos usar o sinal de mais. Colocamos a variável nome, que lá em cima era a variável nome. Mais texto: "tem", opa, idade, variável idade. Separamos aqui, fechamos o texto, colocamos o sinal de mais para juntar tudo. Variável idade, soma de novo, separando. E aqui, o último texto: "tem tantos anos de idade."

print("A pessoa se chama " + nome + " e tem " + idade + " anos de idade")
COPIAR CÓDIGO
Houve um erro aqui, pois não podemos concatenar, ou juntar tudo, quando isso for int (inteiro). Como podemos ver, há uma complexidade aqui. O erro foi: "Can only concatenate string, not int." Então, ele consegue apenas concatenar strings (textos), como o nome, por exemplo. Ele não consegue concatenar números inteiros ou números de ponto flutuante, como int ou float. E a idade, nós a convertemos aqui. Poderíamos apenas convertê-la de volta para uma string dentro deste print. Da mesma forma que fizemos a conversão para int com o método int, dentro dos parênteses, a variável que queremos converter. Aqui, usamos o método str, que é o string. E dentro dele, a variável idade, que queremos colocar temporariamente como string. Não estamos salvando, então é temporariamente como string.

print("A pessoa se chama " + nome + " e tem " + str(idade) + " anos de idade.")
COPIAR CÓDIGO
"A pessoa se chama Fabrício e tem 18 anos de idade." Vou colocar um ponto final aqui. Beleza, funcionou.

Utilizando fStrings para formatação
Mas, como vimos, não é o jeito mais simples de fazer isso. Inicialmente, pode parecer mais simples, mas quando começamos a ver a mistura de texto, string, com número, pode ficar mais complicado. Então, o outro jeito, que é o mais utilizado em Python, é o chamado fString. Você concatena, ou junta as duas coisas, colocando a letra f na frente. Vamos voltar ao jeito que estávamos originalmente. Pegamos isso daqui e tiramos esses sinais de mais, deixando tudo como estava, do jeito que deu errado. "A pessoa se chama nome e tem idade anos de idade." Vamos imprimir de novo: "A pessoa se chama nome e tem idade anos de idade."

Para juntar frases, palavras e variáveis em Python, usamos o fString. Colocamos, literalmente, a letra f antes da nossa string, antes das aspas do conteúdo. O que for texto, permanece assim, e o que for variável, colocamos entre chaves. Abrimos e fechamos chaves. Então, nome é a variável, e idade é a variável. Assim, "A pessoa se chama nome", mas indicamos para o Python que estamos tratando da variável nome, não da palavra "nome". Colocamos as chaves, e o mesmo para idade.

print(f"A pessoa se chama {nome} e tem {idade} anos de idade.")
COPIAR CÓDIGO
Vamos rodar isso aqui: "A pessoa se chama Fabrício e tem 18 anos de idade." E aqui, nem precisamos converter de volta para str, para string. Se verificarmos o tipo de idade, o type de idade, ele ainda está como int, pois não gravamos na variável idade. Mas, quando usamos o fString, ele já faz isso tudo automaticamente, sem precisar se preocupar com isso.

type(idade)
COPIAR CÓDIGO
Por isso, recomendamos que usem o fString ao concatenar texto e variável. É muito fácil: basta colocar um f no começo e inserir tudo que quiser no meio, colocando as variáveis entre chaves. Com isso, concluímos essa parte de manipulação de dados e operações com dados, ficando mais preparados para o próximo passo, que é lidar com IA. Vamos lá!

@@09
Condicionais

Continuando a evolução com Python, vamos aprender sobre estruturas condicionais. Estruturas condicionais são fundamentais, pois permitem que o programa tome decisões baseadas em condições específicas. Por exemplo, se uma determinada condição for atendida, o programa executará uma ação; caso contrário, executará outra.

Vamos começar pedindo ao usuário que digite seu nome e idade. Para isso, utilizamos o método input para capturar o nome do usuário:

nome = input("Digite o seu nome: ")
COPIAR CÓDIGO
Solicitando e convertendo a idade do usuário
Em seguida, solicitamos a idade do usuário. É importante lembrar que, ao utilizar o método input, o dado recebido é armazenado como uma string. No entanto, para comparar a idade, precisamos que ela seja um número inteiro. Podemos converter a string para um inteiro usando o método int. Assim, ao solicitar a idade, já a converteremos diretamente para um número inteiro:

idade = int(input("Digite a sua idade: "))
COPIAR CÓDIGO
O processo funciona da seguinte forma: primeiro, o método input solicita ao usuário que digite sua idade. Em seguida, o valor digitado é convertido para um número inteiro e armazenado na variável idade.

Implementando a condição de entrada na festa
Agora, vamos implementar a condição. Se a pessoa tiver mais de 18 anos, poderá entrar na festa; caso contrário, não poderá. Utilizaremos a palavra-chave if para isso. Se a variável idade for maior que 18, executaremos um bloco de código. A indentação é importante aqui, pois indica que o código faz parte do bloco if. Podemos usar o botão "Tab" ou espaços para indentar o código.

if idade > 18:
    print(f"{nome} pode entrar na festa porque ele é maior de idade.")
COPIAR CÓDIGO
Dentro do bloco if, utilizamos o print com f-string para misturar texto com variáveis. Por exemplo, se a pessoa for maior de idade, exibiremos uma mensagem informando que ela pode entrar na festa.

Utilizando a estrutura else para condições não atendidas
Se a pessoa não for maior de idade, utilizaremos a palavra-chave else para definir o que acontecerá. O else é o oposto do if e será executado se a condição do if não for atendida. Dentro do bloco else, exibiremos uma mensagem informando que a pessoa não pode entrar na festa.

else:
    print(f"{nome} NÃO pode entrar na festa porque ele é menor de idade.")
    print(f"Ele tem {idade} anos de idade.")
COPIAR CÓDIGO
Vamos testar o código. Se a idade for 19, a mensagem indicará que a pessoa pode entrar na festa. Se a idade for 17, a mensagem indicará que a pessoa não pode entrar. No entanto, há um detalhe importante: se a idade for exatamente 18, o programa ainda considera a pessoa como menor de idade. Isso ocorre porque a comparação foi feita apenas para valores maiores que 18. Para corrigir isso, devemos alterar a condição para verificar se a idade é maior ou igual a 18, utilizando o operador >=.

Corrigindo a condição de idade para inclusão de 18 anos
if idade >= 18:
    print(f"{nome} pode entrar na festa porque ele é maior de idade.")
    print(f"Ele tem {idade} anos de idade.")
else:
    print(f"{nome} NÃO pode entrar na festa porque ele é menor de idade.")
    print(f"Ele tem {idade} anos de idade.")
COPIAR CÓDIGO
Quando executamos o código, percebemos que Fabrício pode entrar na festa porque ele é maior de idade. Inicialmente, o código considerava apenas se a idade era maior, mas 18 não é maior que 18, é igual. Por isso, ele não entrava. Agora, comparamos corretamente as idades.

Calculando médias escolares com estruturas condicionais
Se tivermos várias condições intermediárias, podemos lidar com isso também. Vamos usar outro exemplo: calcular as médias escolares para determinar se alguém será reprovado, precisará de recuperação ou será aprovado diretamente. Em uma escola rigorosa, temos três casos: média acima de 7 para aprovação direta, média entre 5 e 7 para recuperação, e abaixo de 5 para reprovação. Podemos implementar isso com blocos de IF e ELSE, mas também há outra maneira que vamos explorar.

Vamos adaptar o exemplo da idade para calcular a média. Digite a média das provas, que geralmente é um número decimal, pois é uma divisão. Vamos salvar esse valor na variável média:

media = float(input("Digite a sua média: "))
COPIAR CÓDIGO
Implementando condições para aprovação, recuperação e reprovação
Dentro do bloco de código, usaremos as regras mencionadas. Se a média for maior ou igual a 7.0, imprimimos "aprovado". Para o caso intermediário, entre 5 e 7, usamos elif, que é uma combinação de else e if. Se a média for maior ou igual a 5.0, imprimimos "recuperação". Caso contrário, imprimimos "reprovado".

if media >= 7.0:
    print("Aprovado!")
elif media >= 5.0:
    print("Recuperação")
else:
    print("Reprovado!")
COPIAR CÓDIGO
Vamos testar: se a média for 4.3, o resultado é "reprovado". Se for 8.9, o resultado é "aprovado". Para uma média de 5.7, o resultado é "recuperação". Tudo está funcionando corretamente.

Invertendo a lógica das condições
Agora, vamos inverter a lógica. Se a média for menor que 5, imprimimos "reprovado". Para elif, se a média for maior que 5, imprimimos "recuperação". Caso contrário, imprimimos "aprovado".

if media < 5.0:
    print("Reprovado!")
elif media >= 5.0:
    print("Recuperação")
else:
    print("Aprovado!")
COPIAR CÓDIGO
Testando novamente: com média 4.3, o resultado é "reprovado". Com 8.9, o resultado deveria ser "aprovado", mas foi "recuperação" porque não consideramos o caso de ser maior que 7.

Corrigindo a lógica com o operador AND
Para corrigir, usamos o operador AND para combinar condições. Se a média for maior ou igual a 5 e menor que 7, imprimimos "recuperação". Caso contrário, imprimimos "aprovado".

if media < 5.0:
    print("Reprovado!")
elif media >= 5.0 and media < 7.0:
    print("Recuperação")
else:
    print("Aprovado!")
COPIAR CÓDIGO
Testando novamente: com média 4.3, o resultado é "reprovado". Com 8.9, o resultado é "aprovado". Com 5.7, o resultado é "recuperação".

Concluindo o aprendizado sobre estruturas condicionais
Agora, compreendemos as estruturas condicionais IF, ELSE e ELIF. Estamos prontos para, na próxima aula, realizar nossa primeira chamada de Inteligência Artificial. Até mais.

@@10
Gerenciamento de custos em entregas

A Hermex Log, uma empresa de logística especializada em serviços de entrega, está buscando otimizar seus custos operacionais. Recentemente, a empresa decidiu alugar um novo depósito para armazenar pacotes antes da distribuição. O aluguel mensal do depósito é de R$ 5.000. Além disso, a empresa gasta R$ 2.000 mensais em combustível e R$ 1.500 em manutenção de veículos. A equipe de finanças deseja calcular o custo total mensal e, em seguida, dividir esse custo entre as 10 rotas de entrega que a empresa opera, para entender o custo médio por rota.
Como a equipe de finanças pode calcular o custo total mensal e o custo por rota usando conceitos de variáveis e operações matemáticas?

A equipe de finanças pode criar variáveis para armazenar cada um dos custos: aluguel = 5000, combustivel = 2000, manutencao = 1500. Em seguida, pode calcular o custo total mensal somando essas variáveis: custo_total = aluguel + combustivel + manutencao, resultando em R$ 8.500. Para calcular o custo por rota, a equipe pode dividir o custo total pelo número de rotas: custo_por_rota = custo_total / 10, resultando em R$ 850 por rota.
 
Correta, pois essa abordagem utiliza variáveis para armazenar os custos individuais e operações matemáticas básicas para calcular o custo total e o custo médio por rota, refletindo uma aplicação precisa dos conceitos discutidos.
Alternativa incorreta
A equipe de finanças deve somar o custo de combustível e manutenção, subtrair o aluguel, e dividir o resultado por 5 para encontrar o custo por rota, o que poderia ser uma tentativa de redistribuir os custos de forma alternativa, mas não se alinha com a metodologia correta.
 
Incorreta, pois subtrair o aluguel e dividir por 5 não representa corretamente o cálculo do custo total mensal ou o custo por rota, resultando em valores que não refletem os custos reais da operação, apesar de ser uma abordagem alternativa.
Alternativa incorreta
A equipe de finanças pode calcular o custo total mensal multiplicando o aluguel por 2, somando o resultado ao dobro do custo de combustível e ao triplo do custo de manutenção, e depois dividir o total por 10 para encontrar o custo por rota, considerando que essa abordagem poderia ser uma tentativa de ajustar os custos para diferentes cenários operacionais.
 
Alternativa incorreta
A equipe de finanças pode criar uma variável única para o custo total, custo_total = 5000 + 2000 + 1500, e depois multiplicar por 10 para encontrar o custo por rota, talvez considerando um cenário de expansão das rotas, mas isso não se aplica ao cálculo atual.

@@11
Para saber mais: a importância da indentação em python

O que é indentação?
Em Python, a indentação vai além de uma simples questão estética. Ela é parte integrante da sintaxe da linguagem e define blocos de código que estão logicamente associados. Isso significa que a forma como o código é alinhado à direita (ou seja, com espaços ou tabulações) determina quais instruções pertencem a cada estrutura de controle, como as condições (if, elif, else) e os loops.

Como a indentação organiza o fluxo de execução
A indentação em Python substitui o uso de chaves ou palavras-chave específicas para delimitar blocos. Por exemplo, em estruturas condicionais, tudo o que estiver indentado após o comando if é considerado parte daquele bloco. Se a indentação for removida ou estiver incorreta, o interpretador Python não conseguirá identificar os limites dos blocos, resultando em erros ou comportamentos imprevistos.

Veja o exemplo abaixo:

idade = 20

if idade >= 18:
    print("Pode entrar na festa")
    print("Bem-vindx!")
else:
    print("Acesso negado")
COPIAR CÓDIGO
Nesse código, as duas linhas indentadas após o if fazem parte da condição quando a idade é maior ou igual a 18. Já a linha após o else é executada quando a condição não é atendida. Essa organização facilita a leitura e a manutenção do código, tornando evidente a hierarquia e o fluxo de execução.

Benefícios e desafios
Entre os principais benefícios da indentação, podemos citar:

Clareza Visual: Um código bem indentado permite que qualquer pessoa, independentemente do nível de experiência, compreenda rapidamente a estrutura e a lógica implementada.
Redução de Erros: Ao impor regras estritas de formatação, Python incentiva a escrita de código organizado, o que diminui a probabilidade de erros lógicos decorrentes de blocos de código mal definidos.
Consistência: Quando adotam-se padrões de indentação (como 4 espaços por nível), a equipe de desenvolvimento garante que todos os trechos de código tenham um padrão unificado, facilitando revisões e colaborações.
No entanto, a indentação também pode apresentar desafios, especialmente para pessoas que estão migrando de linguagens que não dependem desse recurso para a definição de blocos (como C ou Java, que utilizam chaves). O principal desafio é manter a consistência e a atenção aos detalhes, pois misturar espaços e tabulações ou alterar o nível de indentação pode causar erros difíceis de detectar.

Em resumo, a indentação é um conceito fundamental no desenvolvimento em Python. Ela não só estrutura o código, mas também reflete o cuidado e a clareza na abordagem da solução. Dominar essa prática desde o início contribui para a criação de programas mais robustos e de fácil manutenção.

@@12
Faça como eu fiz: iniciando em Python

Nesta aula, exploramos a criação e execução de códigos em Python utilizando o Google Colab, além de manipulação de strings, variáveis, operações aritméticas e estruturas condicionais.
Agora é a sua chance de revisar e exercitar os conteúdos vistos nesta aula, se ainda não colocou em prática. Para isso:

Acesse o Google Colab e crie um novo notebook.
Conecte o notebook aos servidores do Google.
Insira células de código e de texto para organizar seu projeto.
Utilize o comando print para exibir números e textos.
Diferencie números e strings aplicando aspas em textos.
Concatene strings e converta tipos quando necessário.
Crie variáveis para armazenar valores e texto.
Realize operações de soma, subtração, multiplicação e divisão.
Utilize variáveis para calcular totais e dividir custos.
Guarde resultados de operações em novas variáveis.
Aplique métodos lower, upper, strip e replace em textos.
Atualize strings e sobrescreva variáveis conforme o resultado.
Capture dados do usuário usando input com mensagens.
Converta entradas para tipos adequados, como int, quando preciso.
Utilize f-string para concatenar variáveis e textos facilmente.
Implemente estruturas condicionais (if, elif, else) para verificações.
Mantenha a identação correta em blocos condicionais.
Ajuste condições para validar idades e definir fluxos (aprovado, recuperação, reprovado).
Para obter instruções detalhadas, verifique as transcrições da aula.

@@13
O que aprendemos?

Nesta aula, aprendemos:
Introdução ao Python como linguagem com sintaxe simples e acessível.
Uso do Google Colab para programação online sem necessidade de instalação local.
Identificação e manipulação de células de código e texto no Google Colab.
Conceito de variáveis e operações aritméticas básicas em Python.
Regras de nomenclatura de variáveis e uso do tipo de dados booleano.
Aplicação de métodos de manipulação de strings em Python.
Uso da função input() e conversão de tipos para interação com o usuário.
Estruturas condicionais com if, else, elif e operadores lógicos.

#19/01/2026

@02-Manipulação de strings

@@01
Projeto da aula anterior

Caso queira revisar o código até aqui ou começar a partir desse ponto, disponibilizamos os códigos realizados na aula anterior, para visualizar clique neste link.

https://colab.research.google.com/drive/1WETmeYAowvalnz1go_KIzTYeBjfdWWEG#scrollTo=GdljWTDDLKzF

@@02
Aprenda a conectar a IA do Google com Python no Colab

Agora é o momento de rodarmos nossa primeira Inteligência Artificial (IA) utilizando uma conexão com a API diretamente do Google Colab, onde estamos programando. Vamos escrever um texto sobre como rodar a IA no Google Colab.

Por exemplo, ao inserir um código, notamos que o uso do símbolo de jogo da velha (#) no início indica um título de nível 1 (H1). Isso permite ajustar o tamanho do texto, entre outras funcionalidades do Colab que não são tão relevantes no momento. O importante é que vamos nos conectar com o Gemini, a IA do Google, que será utilizada neste exemplo. Poderíamos usar qualquer outra IA, mas o Gemini é mais conveniente, pois o Google Colab é um ambiente do Google, facilitando o processo.

Obtendo a chave de API no Google AI Studio
Antes de rodarmos o Gemini, precisamos de uma chave de API (API Key). A chave de API pode ser comparada a um usuário e senha modernos, sendo um código alfanumérico extenso, semelhante a uma senha de Wi-Fi complexa. Com essa chave, o Google identificará que estamos acessando a API do Gemini.

Para obter a chave de API, devemos acessar o Google AI Studio. No Google, pesquisamos por Google AI Studio e clicamos no link correspondente. Ao abrir a página, no topo, há um botão destacado chamado "Get API Key". Ao clicar nele, seremos direcionados para outra página onde podemos criar uma nova chave de API, localizada no canto superior direito.

Criando e gerenciando a chave de API
Ao clicar na opção, podem ocorrer algumas situações. Se nunca tivermos criado uma chave de API com o Google, será necessário aceitar a conexão com nossa conta do Google, como a conta do Gmail, por exemplo, e permitir essa conexão. Caso já tenhamos gerado anteriormente, chegaremos à situação em que precisamos escolher um projeto. Pode ser qualquer projeto do Google Cloud. Se apenas quisermos conectar com algo, podemos escolher um projeto aleatório e clicar em criar uma chave de API. Independentemente do modo como fizermos isso, a chave será gerada, e podemos copiá-la. A única recomendação é usar as chaves de API com segurança, não compartilhando nem incorporando em códigos que o público possa ver. Isso é essencial, pois a chave funciona como um usuário e senha, devendo ser guardada em locais seguros.

Armazenando a chave de API no Google Colab
Vamos copiar o valor da chave e voltar ao nosso Colab. Para não inserirmos diretamente no código, temos no Colab um recurso semelhante a um cofre, onde podemos guardar nossas senhas e fazer a conexão de maneira mais segura. No menu esquerdo, clicamos na opção "Secrets". Se não houver nenhum, aparecerá vazio. Podemos adicionar uma nova chave clicando no botão "Adicionar novo Secret". No lado esquerdo, colocamos o nome da chave, como Gemini_API_Key, e no lado direito, colamos o valor da chave de API que copiamos. Após isso, podemos ativar a chave.

Importando e configurando a chave de API
O Colab oferece uma dica de como importar essa chave. Precisamos importar do ambiente com:

from google.colab import userdata
COPIAR CÓDIGO
Dentro de userdata.get, copiamos o nome da variável, no nosso caso, GEMINI_API_KEY_2. Ao rodar, ele exibirá que conseguiu pegar o valor da chave de API. No entanto, para se conectar, precisamos definir essa variável como uma variável de ambiente no Google Colab. Para isso, importamos o módulo os e utilizamos os.environ para definir a variável de ambiente GOOGLE_API_KEY com o valor da chave de API.

import os
from google.colab import userdata

os.environ['GOOGLE_API_KEY'] = userdata.get('GEMINI_API_KEY_2')
COPIAR CÓDIGO
A variável dentro do cofre pode ter qualquer nome, mas a variável de ambiente precisa ter o nome exato GOOGLE_API_KEY, pois é uma exigência do sistema do Google. Estamos usando importações do sistema para conectar essa variável de ambiente ao valor guardado no cofre, garantindo segurança. Poderíamos inserir o valor diretamente, mas isso não seria seguro. Portanto, ensinamos o método correto desde o início.

Conectando e interagindo com a IA do Google
No Colab, como é uma ferramenta do Google, não precisamos instalar nada para conectar com o Gemini, a IA do Google. Podemos importar diretamente Gen AI, que é uma abreviação de Generative AI (Inteligência Artificial Generativa). O Google Gen AI SDK oferece módulos prontos para facilitar a interação com o Gemini. Criamos um cliente com Gen AI.client() para se conectar aos servidores do Google.

from google import genai

client = genai.Client()
COPIAR CÓDIGO
Para ter nossa primeira interação com a IA, utilizamos client.models.generate_content(), que requer dois argumentos: o modelo do Google a ser usado e o conteúdo da pergunta. Existem várias opções de modelos, como Gemini-2.5-Flash e Gemini-2.5-Pro. Escolhemos Gemini-2.5-Flash por ser rápido e ter menos limites, ideal para testes. Passamos o modelo e a pergunta, como "O que é inteligência artificial?".

resposta = client.models.generate_content(model="gemini-2.5-flash", contents="O que é a Inteligência Artificial?")
COPIAR CÓDIGO
Exibindo a resposta da IA
Ao rodar, a resposta é gerada, mas inicialmente aparece de forma complexa. Para facilitar a leitura, salvamos a resposta em uma variável chamada resposta e imprimimos apenas o texto com resposta.text.

print(resposta.text)
COPIAR CÓDIGO
Assim, obtemos uma resposta clara sobre inteligência artificial.

Se estivermos acompanhando, já fizemos nossa primeira conexão com a API do Gemini, recebendo uma resposta da IA do Google. Agora, somos pessoas desenvolvedoras capazes de se comunicar com modelos de IA. Nos próximos vídeos, continuaremos explorando mais sobre Python, IA e dados. Até mais.

@@03
Conceito de loops

Agora que já vimos como se conectar e obter uma resposta a partir de uma IA usando a API e a chave da API, vamos explorar um conceito muito importante em Python e em todas as linguagens de programação: os loops, ou estruturas de repetição. Esses conceitos também são conhecidos como laços e têm diversos nomes, mas representam a mesma ideia.

Para começar, vamos introduzir o conceito de estruturas de repetição, também conhecidas como loops ou laços:

# Estruturas de Repetição, Loops, Laços
COPIAR CÓDIGO
Explicando o uso de loops para repetição de ações
Existem dois tipos principais de loops. Vamos começar com um deles, que é utilizado quando queremos repetir a mesma ação várias vezes. Por exemplo, se quisermos imprimir um asterisco na tela dez vezes, poderíamos simplesmente usar o comando print seguido do texto, repetindo-o dez vezes. Isso funcionaria bem para dez asteriscos, mas se quisermos imprimir 500 asteriscos, contar até 500 manualmente não seria uma boa ideia. Existem maneiras mais eficientes de fazer isso.

Para ilustrar, podemos usar o comando print para imprimir uma linha de asteriscos:

print("**********")
COPIAR CÓDIGO
Demonstrando o uso do loop while
Um dos métodos, que pode ser usado para essa e muitas outras situações, é o loop while. A palavra while em inglês significa "enquanto". Assim como no if, onde passamos uma condição, no while também passamos uma condição. No caso do if, se a condição for verdadeira, o bloco de código é executado. No while, enquanto a condição for verdadeira, o loop continua executando, repetindo o bloco de código até que uma condição de parada seja atingida. Geralmente, essa condição de parada é definida dentro do próprio loop while.

Vamos demonstrar na prática como isso funciona. Antes de usar o while, definimos que queremos imprimir 500 asteriscos. Para isso, vamos definir uma variável inicial, por exemplo, n, que receberá o valor 1:

n = 1
COPIAR CÓDIGO
Implementando a lógica de incremento no loop
Com essa variável definida, podemos começar a usar o while. Enquanto o valor da variável n for menor ou igual a 500, o loop continuará executando. A estrutura do while é semelhante à do if, com uma condição seguida de dois pontos:

while n <= 500:
COPIAR CÓDIGO
O que queremos fazer dentro do loop é imprimir o asterisco, ou seja, a string "*":

print("*")
COPIAR CÓDIGO
O texto "asterisco" está entre aspas, mas precisamos colocar um ponto de parada, pois o valor de n está igual a 1. Quando ele muda para 2, 3, 4, não está mudando. Vamos ver algumas vezes como fazer essa mudança. Por exemplo, pegamos um texto, aplicamos algumas alterações e depois salvamos o resultado na própria variável texto, alterando-a ao remover o que havia antes e colocando o novo valor no lugar.

O que faremos aqui é alterar o valor de n para que ele continue crescendo, evitando que fique em 1 infinitamente. Caso contrário, ele diminuirá sem parar, o que pode travar o computador. Isso é conhecido como loop infinito em programação. Vamos imprimir apenas um item, um asterisco. O próximo passo é incrementar n em 1:

n = n + 1
COPIAR CÓDIGO
Testando e ajustando o loop para evitar problemas
Podemos verificar se isso funciona. Ao rodar o código, ele executa várias ações. Um problema é que, quando fazemos um print seguido de outro, ele pula para a linha de baixo, não imprimindo tudo na mesma linha. No entanto, isso já serve para mostrar que o código está funcionando. Vamos mudar o valor de 500 para 10, para que fique mais visível:

n = 1

while n <= 10:
  print("*")
  n = n + 1
COPIAR CÓDIGO
Analisando o funcionamento do loop while
Vamos analisar passo a passo: n começa com o valor de 1. Ele faz a primeira comparação no if: 1 é menor ou igual a 10, o que é verdadeiro. Entramos no loop while. Imprimimos um asterisco e, em seguida, incrementamos n em 1, resultando em 2. Após essa operação, gravamos o resultado na variável n. Agora, n é igual a 2, e o loop recomeça.

Agora, 2 é menor ou igual a 10, o que é verdadeiro. Imprimimos novamente, e 2 mais 1 resulta em 3. Salvamos 3 e voltamos ao início do while. 3 é menor ou igual a 10, o que é verdadeiro, e assim por diante, até que n se torne 11. Quando 11 é comparado, 11 é menor ou igual a 10 é falso, e o loop para. Essa é a ideia por trás do laço while, uma estrutura de repetição que usaremos bastante nas últimas aulas. Essa é também outra estrutura que veremos em breve.

@@04
Entendendo a interação dinâmica com chatbots e o histórico de mensagens

Continuando, vamos revisar o que vimos na última aula. Importamos todos os elementos necessários, incluindo o sistema operacional, e salvamos a chave de API do Gemini, obtida no Google AI Studio, em nosso Secrets. Com essa chave, conseguimos definir a variável de ambiente os.environ.

Para isso, utilizamos o seguinte código:

import os
from google.colab import import userdata
os.environ['GOOGLE_API_KEY'] = userdata.get('GEMINI_API_KEY_2')
COPIAR CÓDIGO
Estabelecendo conexão com o SDK do Google
Em seguida, estabelecemos a conexão com o SDK do Google para lidar com IA generativa. Importamos o GeneAI do Google, criamos um cliente e, através do método modules.generateContent, conectamos ao modelo Gemini, especificamente o 2.5 Flash.

from google import import genai

client = genai.Client()
COPIAR CÓDIGO
Enviamos a pergunta "O que é inteligência artificial?" e exibimos a resposta, que é o texto retornado pelo modelo.

resposta = client.models.generate_content(model="gemini-2.5-flash", contents="o que é a Inteligência Artificial?")
print(resposta.text)
COPIAR CÓDIGO
Explorando interações dinâmicas com chatbots
Agora, vamos realizar algo semelhante, mas com um foco diferente. No exemplo anterior, enviamos uma pergunta e recebemos uma única resposta. Agora, exploraremos interações mais dinâmicas, semelhantes aos chatbots atuais, como Gemini, ChatGPT, Llama, Cloud, Maritaca e IA. Esses chatbots mantêm o contexto das perguntas anteriores, funcionando como um chatbot com histórico e memória. Isso também pode ser feito facilmente usando os módulos prontos do Google.

Utilizamos o cliente e chamamos o objeto Models, usando o método GenerateContent para gerar um conteúdo pontual. Agora, faremos algo um pouco diferente, mas ainda semelhante. Vamos abrir uma nova célula de código, usar o Client e, ao invés de escolher Models, selecionaremos Chats. Em seguida, usaremos a opção Create para criar um chatbot. Como é um método, colocamos os parênteses.

client.chats.create()
COPIAR CÓDIGO
Criando e interagindo com o chatbot
Dentro dos parênteses, faremos algo parecido com o que fizemos anteriormente. Passaremos o modelo que queremos usar e o conteúdo, ou seja, o prompt ou pergunta para a IA. No caso do chat, passaremos apenas o modelo, e o restante será definido dentro do chat. Vamos armazenar isso em uma variável, que pode ser chamada de chat ou chatbot.

chat = client.chats.create(model="gemini-2.5-flash")
COPIAR CÓDIGO
Após rodar essa célula, usaremos essa variável na próxima etapa. Chamaremos a variável criada, que utilizará a propriedade do objeto chats e o método create, para criar uma interação de chatbot com o Gemini, usando o modelo 2.5 Flash. Ao clicar no ponto, veremos algumas opções, como Get history, para obter um histórico, embora não tenhamos um histórico no momento.

A que vamos usar é a que faz mais sentido aqui, que é o método sendMessage, em inglês, enviar uma mensagem. Como é um método, nós abrimos e fechamos parênteses, e dentro desse sendMessage, podemos enviar, por exemplo, uma pergunta.

resposta = chat.send_message("o que é a Inteligência Artificial?")
print(resposta.text)
COPIAR CÓDIGO
Enviando perguntas e recebendo respostas
Podemos mandar exatamente a mesma pergunta: "O que é a inteligência artificial?" e obter uma resposta, do mesmo jeito que fizemos anteriormente. No entanto, antes era para uma questão mais pontual, uma pergunta e uma resposta, sem salvar histórico. Aqui, é um chat de fato, então temos a pergunta que fizemos, a resposta do modelo de IA, a próxima pergunta, e assim por diante.

Podemos clicar para rodar, e ele está fazendo novamente a conexão com os modelos Gemini, lá no Google. Em breve, ele responderá e salvará a resposta, armazenando-a na variável resposta. Podemos imprimir a resposta da mesma forma que fizemos antes, com print(resposta.text). Se quisermos mudar, podemos usar uma variável diferente, como resposta2, para não perder a resposta anterior, pois ao usar a mesma variável, ela é sobrescrita, apagando o que havia antes e colocando o novo conteúdo.

Vamos rodar o código, e ele está praticamente igual, mas com diferenças. A IA funciona de maneira simplificada, e a resposta pode variar, pois é uma IA generativa. Cada vez, ela responderá de uma maneira um pouco diferente. Vamos fazer mais uma pergunta para a Gemini, copiar e já colocar o print junto, na mesma célula, para exibir diretamente a resposta. Estamos usando a mesma variável, que será sobrescrita, apagando o conteúdo anterior e fornecendo uma nova resposta.

resposta = chat.send_message("Quando foi lançado o ChatGPT?")
print(resposta.text)
COPIAR CÓDIGO
Explorando o histórico de interações
Podemos fazer outra pergunta, por exemplo: "Quando foi lançado o ChatGPT?" Ao rodar, obtemos que o ChatGPT foi lançado publicamente pela OpenAI em 30 de novembro de 2022. Essas informações são passadas sem problemas.

Gostaríamos de mostrar algo mais. Vamos criar mais uma célula de código. Até agora, estávamos usando chat.sendMessage para enviar uma mensagem ao modelo Gemini e obter uma resposta, da mesma forma que fizemos antes. Podemos usar a variável chat, que criamos anteriormente com client.chats.create, para criar um chat e interações. Ao usar o ponto, vemos que há outras opções, não apenas o sendMessage, mas também o getHistory.

Vamos rodar o método chat.getHistory. Ele possui um histórico das mensagens enviadas durante este chat.

chat.get_history()
COPIAR CÓDIGO
A primeira entrada, userContent, é o conteúdo que veio do usuário, com o texto "O que é a inteligência artificial?" e o papel (role) de quem fez a pergunta, que foi o usuário. A resposta, text, é a primeira resposta que tivemos. Mais abaixo, temos o roleModel, indicando que a resposta foi dada pelo modelo, não pelo usuário. A pergunta "Quando foi lançado o ChatGPT?" também tem o role de usuário, e a resposta correspondente está registrada.

Ou seja, ele guarda esse histórico dentro do chat, permitindo ver todas as interações. Isso pode ser muito útil. No próximo vídeo, vamos integrar essas funcionalidades para criar um chatbot que permita interações, usando operadores e laços de repetição que vimos na última aula. Até mais.

@@05
Como criar um chatbot com Python e a IA Gemini

Vamos alterar o nome do arquivo de Untitled 31 para algo mais significativo, como "Python e Inteligência Artificial". O objetivo agora é criar um chatbot que permita ao usuário fazer perguntas, conectando-se a uma IA, neste caso, o Gemini, para oferecer respostas.

Primeiramente, precisamos capturar a pergunta do usuário, ou seja, o prompt. Já fizemos algo semelhante anteriormente, utilizando o método input, como em "Digite a sua média" ou "Digite o seu nome". Vamos aplicar o mesmo conceito para capturar o prompt do usuário. Podemos nomear a variável como prompt, que receberá a entrada do usuário com a mensagem "Digite a sua pergunta".

prompt = input("Digite a sua pergunta: ")
COPIAR CÓDIGO
Capturando e imprimindo a pergunta do usuário
Ao executar, o sistema solicitará que o usuário digite a pergunta, mas, inicialmente, apenas armazenará o texto na variável prompt. Podemos verificar isso imprimindo a variável, que mostrará exatamente o que foi digitado.

print(prompt)
COPIAR CÓDIGO
No entanto, nosso objetivo é utilizar laços de repetição, como o while, para continuar o processo enquanto uma condição for verdadeira. Podemos definir um texto que encerre a interação, como a palavra "fim". Assim, enquanto o usuário não digitar "fim", o sistema continuará capturando e respondendo novas perguntas.

Implementando o laço de repetição
Vamos implementar o laço while para que, enquanto o conteúdo da variável prompt for diferente de "fim", o sistema continue a operar. Utilizamos o operador "!=" para indicar diferença.

while prompt != "fim":
COPIAR CÓDIGO
A primeira ação dentro do laço será buscar a resposta no Gemini para o prompt recebido. Podemos reutilizar o método chat.sendMessage, mas, desta vez, a mensagem enviada será o prompt digitado pelo usuário. O resultado, ou seja, a resposta da IA Gemini, será armazenado na variável resposta.

resposta = chat.send_message(prompt)
COPIAR CÓDIGO
Exibindo a resposta e ajustando o loop
Próximo passo, vamos exibir na tela, fazer um print, dessa resposta, o texto dela resposta.text.

print(resposta.text)
COPIAR CÓDIGO
Tudo certo, isso já começa a funcionar. Podemos rodar, digitar a pergunta: "O que é IA? Responda sucintamente." Ele fará a chamada para o Gemini, o que pode demorar alguns segundos. Após responder, imprime na tela, mas ainda está rodando e imprimindo. Por que continua e não para? Lembramos que, na aula sobre o loop while, ele ficará rodando infinitamente enquanto a condição não for satisfeita. No nosso caso, estamos apenas pegando o prompt, o input do usuário, que inicialmente foi "O que é IA? Responda sucintamente." Esse é o valor da variável prompt. O que ele está fazendo? Ele entra, busca a resposta, imprime, termina e volta para o começo do loop while. Qual é o valor de prompt? Ele não mudou, pois não perguntamos novamente ao usuário. Continua sendo "O que é IA? Responda sucintamente." Ele não é igual à palavra "fim", então continua sendo diferente de "fim". Isso responde à pergunta: o conteúdo dessa variável prompt é diferente de "fim"? Sim, verdadeiro. Então, continua entrando, e por isso ele entrou várias vezes, dando quatro respostas na sequência, pois o prompt ainda não tinha mudado. Esse é um grande cuidado que devemos ter com loops como o while, pois precisamos definir um ponto de término. Caso contrário, ele entrará em um loop infinito e não sairá, podendo até bloquear a conta, por exemplo. Devemos ter muito cuidado com isso.

Atualizando o prompt dentro do loop
Então, o que precisamos aqui? Depois de buscar a resposta no Gemini e imprimir essa resposta, precisamos fazer uma nova pergunta ao usuário, alterando o valor da variável prompt. Como fazemos isso? Exatamente do mesmo jeito que fizemos antes, podemos copiar e colar dentro do loop while.

prompt = input("Digite a sua pergunta: ")
while prompt != "fim":
  resposta = chat.send_message(prompt)
  print(resposta.text)
  prompt = input("Digite a sua pergunta: ")
COPIAR CÓDIGO
Lembrando que o while está na linha principal, mais à esquerda, e todos os outros itens estão dentro do while, com a identação mais para dentro. Isso significa que estão acontecendo dentro do while. Tudo que estiver mais à direita e logo abaixo dele será executado um após o outro, e depois voltará para ele. Isso é muito importante sobre identação.

Testando o chatbot e finalizando o loop
Agora que está tudo pronto, vamos rodar novamente? Clicamos aqui, "O que é IA? Responda sucintamente." Vou copiar essa resposta, dar um "Enter". A resposta dessa pergunta: "IA é inteligência artificial." Ele respondeu e fez uma nova pergunta. O bloco continua rodando, mas finalmente fez uma nova pergunta, que antes não tinha feito, pois continuava com o mesmo prompt. Agora, vamos alterar o valor dessa variável prompt, dando uma nova pergunta, por exemplo: "Quando foi lançado o ChatGPT?" Dou um "Enter", e ele responde: "O ChatGPT foi lançado em 30 de novembro de 2022." Ele continua fazendo essas perguntas infinitamente, passando dentro desse loop while, até atingir a condição de parada que definimos como escrever a palavra "fim", tudo em minúsculo. Se escrevermos "fim", o processo termina. Aqui, parou de rodar o círculo da célula, e simplesmente imprimiu "fim" e tudo mais, não foi impresso novamente.

Melhorando a apresentação das respostas
Conseguimos fazer um chat que pega as perguntas do usuário e gera as respostas, chegando a um ponto de parada que definimos com a palavra "fim". Algo que podemos fazer para deixar mais bonito é usar um recurso que funciona em Python e na maioria das linguagens: dentro de um print, podemos colocar uma string com uma barra invertida e a letra "N". Quando fazemos isso, ele quebra a linha, pulando para a linha de baixo, facilitando a leitura. Assim, a pergunta e a resposta ficam diretas.

print("\n")
COPIAR CÓDIGO
Se estiverem se perguntando sobre os asteriscos que aparecem, isso é uma linguagem de exibição de texto chamada Markdown. Quando colocamos dois asteriscos antes e depois, o texto fica em negrito. O texto gerado pelo Gemini já vem estilizado, com negrito, itálico e outros. Podemos configurar o prompt para não fazer isso, mas, por padrão, ele vem assim. Não se assustem, é por isso que há tantos asteriscos. Na próxima aula, continuaremos nossas aventuras com loops e IA.

@@06
Explorando estruturas de dados em Python

Continuando nossa exploração em Python, Inteligência Artificial e dados, vamos aprofundar nosso conhecimento na linguagem Python, focando em aspectos importantes para o uso diário na programação. Vamos discutir algumas estruturas de dados essenciais, embora não todas, pois existem várias.

Imagine uma sala de aula com cinco alunos, como em um curso de inglês. Se quisermos listar os nomes desses alunos, da forma que conhecemos até agora, precisaríamos criar variáveis como nome1, nome2, e assim por diante, atribuindo a cada uma delas uma string correspondente, como "Bruna" ou "João". Esse método não é prático, especialmente com listas grandes, como uma sala com 40 alunos ou uma lista de funcionários de uma empresa com 100 mil funcionários, ou ainda produtos de uma empresa que vende um milhão de itens. Não é ideal lidar com dados dessa forma.

Introduzindo listas em Python
Para resolver isso, existem estruturas de dados em todas as linguagens de programação. Em Python, vamos aprender algumas das mais importantes, começando pelas listas. Para definir uma lista em Python, é muito simples: basta criar uma variável, como lista_de_nomes, e atribuir a ela uma lista entre colchetes ([]).

Em Python, não precisamos declarar o tipo da variável antecipadamente. Podemos simplesmente dar um nome à variável e atribuir um valor a ela. Se for um texto, colocamos entre aspas; se for um número inteiro, colocamos diretamente; se for um número decimal, também colocamos diretamente; e se for uma lista, usamos colchetes para indicar.

Criando e acessando listas
Para exemplificar, vamos pedir ajuda à inteligência artificial para gerar uma lista de cinco nomes brasileiros. Podemos solicitar uma lista em Python com cinco nomes, incluindo nome e sobrenome. A inteligência artificial nos fornecerá rapidamente essa lista, que estará entre colchetes e com os nomes separados por vírgulas. Embora a lista possa ser apresentada com um nome por linha para facilitar a leitura, neste primeiro momento, vamos mantê-los na mesma linha para simplificar o aprendizado.

Temos aqui cinco nomes: o primeiro é Maria Silva, o segundo é João Santos, o terceiro é Ana Oliveira, o quarto é Pedro Costa e o quinto é Juliana Pereira. Vamos ver como isso é feito em Python:

lista_de_nomes = ["Maria Silva", "João Santos", "Ana Oliveira", "Pedro Costa", "Juliana Pereira"]
COPIAR CÓDIGO
Já rodamos o código e isso está na memória dentro da variável lista_de_nomes. Se quisermos acessar alguns desses nomes, por exemplo, o nome da segunda pessoa na lista, podemos usar colchetes. Vamos pegar a variável lista_de_nomes e acessar o terceiro elemento, que é Ana Oliveira. Para isso, colocamos entre colchetes o número 3 e podemos imprimir o resultado.

print(lista_de_nomes[3])
COPIAR CÓDIGO
Compreendendo a indexação em Python
No entanto, ao imprimir o elemento número 3, o resultado foi Pedro Costa, que é o quarto elemento. Isso ocorre porque, em linguagens de programação como Python, a contagem começa no número 0. Assim, Maria é o elemento 0, João é o elemento 1, Ana é o elemento 2, Pedro é o elemento 3 e Juliana é o elemento 4. Portanto, quando pedimos para imprimir o elemento número 3, ele imprimiu Pedro Costa, que está na posição 3.

Agora, queremos calcular as médias desses alunos para saber se passaram de ano. Criamos uma lista chamada lista_de_medias, onde Maria tem média 8.9, João 7.5, Ana 4.2, Pedro 1.4 e Juliana 9.5. Para acessar a média de Pedro Costa, usamos a variável lista_de_medias e o índice 3, que corresponde à posição de Pedro na lista. Ao imprimir, vemos que a média de Pedro é 1.4.

lista_de_medias = [8.9, 7.5, 4.2, 1.4, 9.5]
print(lista_de_medias[3])
COPIAR CÓDIGO
Propondo um desafio de manipulação de listas
Queremos agora fazer um trabalho especial que adicionará um ponto à média de cada aluno. Para Pedro Costa, que tem 1.4, isso não fará muita diferença, pois ele chegaria a 2.4. Já Ana Oliveira, com 4.2, poderia passar para 5.2 e ser aprovada, considerando que a média para aprovação é 5. No entanto, para Juliana Pereira, que tem 9.5, somar 1 resultaria em 10.5, o que não é possível, pois a nota máxima é 10.

Deixamos isso como um desafio: percorrer a lista usando um loop while e adicionar 1 a cada valor, exceto quando a soma ultrapassar 10, caso em que o valor máximo deve ser 10. A resposta para esse desafio será dada no próximo vídeo.

@@07
Resolvendo desafios de programação com o loop while

Você conseguiu realizar o desafio? Vamos relembrar: o objetivo é criar um código que percorra uma lista de médias e some um a cada valor, exceto quando o valor ultrapassar 10, momento em que deve parar em 10. Esse era o desafio proposto. Se ainda não tentou, pause o vídeo e tente desenvolver o código. Se já tentou, vamos verificar se o raciocínio foi correto.

Existem várias maneiras de resolver esse problema, mas vamos optar por uma abordagem mais simples, utilizando o loop while, que já conhecemos. Quando o desafio foi proposto, mencionamos que seria necessário usar o while.

Definindo a lista de médias e explicando o uso do loop while
Para começar, vamos definir a lista de médias que iremos manipular:

lista_de_medias = [8.9, 7.5, 4.2, 1.4, 9.5]
COPIAR CÓDIGO
Temos uma lista de médias com cinco elementos, numerados de 0 a 4. Lembram-se de como fizemos anteriormente com os asteriscos? Quando aprendemos sobre o while, definimos o valor de N como um número aleatório, começando em 1 e indo até 10, enquanto fosse menor ou igual a 10. Isso foi mais para ensinar o uso do while.

No dia a dia, seguimos o padrão das linguagens de programação, que é começar a contagem pelo 0, e não pelo 1. A única alteração necessária é usar a condição de menor, em vez de menor ou igual. Assim, ao chegar em 10, a comparação será "10 é menor que 10?", o que não é verdade, e o loop não será executado novamente. Antes, a condição era "10 é menor ou igual a 10?", o que era verdadeiro, permitindo mais uma execução do loop.

Iniciando o loop while e somando valores
Podemos seguir o mesmo padrão, iniciando N em 0, já que queremos praticar a iteração a partir do elemento número 0. Enquanto N for menor que o número de elementos na lista de médias, que são 5, o loop deve continuar. Isso significa que N deve ser menor que 5, pois a lista vai de 0 a 4. Assim, N menor que 5 é o padrão, facilitando o entendimento.

Vamos iniciar o loop while:

n = 0
while n < 5:
COPIAR CÓDIGO
Vamos percorrer a lista de médias, somando 1 a cada valor. Já vimos como acessar cada valor usando colchetes para indicar a posição do elemento: posição 0, 1, 2, 3 ou 4. Queremos acessar o valor na posição N da lista de médias e somar 1 a ele. Pode ser 1.0, pois estamos lidando com float, mas usar 1 não causará problemas. O importante é somar 1.

    lista_de_medias[n] = lista_de_medias[n] + 1.0
COPIAR CÓDIGO
Implementando a condição de parada e ajustando valores
No entanto, se apenas somarmos, essa informação será perdida na memória. Precisamos realizar a soma, obter o resultado e armazená-lo na variável correspondente à posição N da lista de médias.

Vamos pensar: N começa em 0. Ele entra no loop e verifica se 0 é menor que 5, o que é verdadeiro.

A posição 0 é a da Maria Silva, que está com 8.9. Vamos entrar aqui e pegar a lista de médias na posição 0. Inicialmente, definimos N como 0, então a lista de médias na posição 0 será a da Maria Silva, que é 8.9. Vamos somar 1, resultando em 9.9, e salvar o resultado na mesma variável, sobrescrevendo o valor anterior de 8.9.

Funciona, mas há um problema. Precisamos de uma condição de parada para o loop while, caso contrário, ele continuará indefinidamente. A condição de parada que utilizamos é somar mais um ao valor de N. Quando o usuário insere um texto diferente da palavra "fim", o loop para. Aqui, faremos o mesmo, usando o valor de N para percorrer a lista de valores, incrementando N no final.

    n = n + 1
COPIAR CÓDIGO
Ajustando valores que ultrapassam 10 e finalizando o código
Vamos imprimir a lista de médias. Os valores foram atualizados: 8.9 foi para 9.9, 7.5 para 8.5, 4.2 para 5.2, 1.4 para 2.4, e 9.5 para 10.5. Quando o valor ultrapassa 10, ele deve ser ajustado para 10. Para resolver isso, podemos adicionar uma condição if dentro do while.

    if lista_de_medias[n] > 10.0:
        lista_de_medias[n] = 10.0
COPIAR CÓDIGO
Se a lista de médias na posição atual for maior que 10, definimos o valor como 10.0. Vamos analisar: na posição 4, N igual a 4, que é o da Juliana, a lista de médias na posição 4 é 9.5. Somamos 1, resultando em 10.5. Se o valor for maior que 10, substituímos por 10. Continuamos somando mais um a N. Quando N for 5, o loop para, e a lista de médias é impressa.

A indentação é importante. Tudo dentro do while está um pouco mais à direita. O if também tem sua própria indentação. Se colocarmos a operação de incremento dentro do if, ela só ocorrerá quando a nota for maior que 10, o que não é o desejado. Portanto, mantemos a lógica do incremento fora do if.

Ao rodar o código, ele funciona corretamente: 9.9, 8.5, 5.2, 2.4 e 10. Vamos continuar explorando a lógica do Python.

print(lista_de_medias)
COPIAR CÓDIGO
Apresentando o código completo
Aqui está o código completo:

lista_de_medias = [8.9, 7.5, 4.2, 1.4, 9.5]

n = 0
while n < 5:
    lista_de_medias[n] = lista_de_medias[n] + 1.0
    if lista_de_medias[n] > 10.0:
        lista_de_medias[n] = 10.0
    n = n + 1

print(lista_de_medias)
COPIAR CÓDIGO
Esse código percorre a lista de médias, soma 1 a cada valor e ajusta qualquer valor que ultrapasse 10 para exatamente 10.

@@08
Explorando o uso da função len

Agora que já começamos a explorar mais as estruturas de dados, como as listas, vamos aprofundar nosso conhecimento sobre elas. Há muito a aprender sobre listas, e uma das coisas importantes é que, por exemplo, na lista de médias que vimos, já sabíamos de antemão quantos elementos havia nela. São cinco elementos no total, do elemento zero até o elemento quatro. No entanto, se fosse uma lista muito grande e não soubéssemos seu tamanho, isso poderia ser um problema. Não é o caso aqui, pois colocamos o número 5 porque sabíamos exatamente quantos elementos havia. Se não soubéssemos, ainda assim não seria um problema, pois existe uma função em Python, não específica para listas, que nos dá essa informação automaticamente. Essa função é o len, que vem da palavra inglesa length (comprimento), mas aqui é abreviada para len, facilitando o uso.

Vamos supor que não soubéssemos quantos elementos há na lista. Poderíamos simplesmente chamar a função len e, como não é um método, passar a variável lista_de_medias dentro dos parênteses. Sabemos que ela é uma lista, e ao rodar o código, ele nos daria o resultado 5. Podemos fazer isso dentro de um print, que mostrará o resultado. Assim, o jeito mais seguro de fazer o mesmo código que fizemos anteriormente, quando não sabemos o tamanho da lista que estamos analisando, seria substituir o valor 5, que está "hard coded" (codificado de forma fixa), pelo resultado do len dessa lista. Ao rodar o código, ele funcionaria da mesma maneira, pois o resultado do len também é 5. Essa é uma maneira mais elegante de fazer isso.

len(lista_de_medias)
COPIAR CÓDIGO
Acessando elementos de listas
Outras coisas que podemos ver sobre listas incluem a possibilidade de percorrê-las ao contrário. Podemos, por exemplo, pegar o último elemento da lista. Se o primeiro elemento é o elemento zero, o último elemento pode ser acessado de duas maneiras. Uma delas é pegar o len da lista e subtrair um. Vamos imprimir a lista_de_medias, pegar o elemento na posição zero, que sabemos ser o primeiro, e o elemento na última posição. Se soubermos que a lista tem cinco elementos, do zero ao quatro, poderíamos simplesmente usar o valor 4. Se não soubéssemos o tamanho da lista, poderíamos usar o len menos um. Isso funcionaria sem problemas, pois len é 5, menos um é igual a quatro, que é o elemento na posição número quatro.

lista_de_medias = [8.9, 7.5, 4.2, 1.4, 9.5]
print(lista_de_medias)
lista_de_medias[0]
lista_de_medias[4]
lista_de_medias[len(lista_de_medias) - 1]
COPIAR CÓDIGO
Há um jeito ainda melhor de pegar o último elemento da lista: usar índices negativos. Se o zero é o primeiro elemento, o último elemento é o menos um. Assim, ao buscar o elemento menos um, ele retornará o último elemento da lista. Para pegar o penúltimo elemento, usamos menos dois, e assim por diante. Essa é uma maneira interessante de lidar com as posições dos elementos dentro de uma lista.

lista_de_medias[-1]
lista_de_medias[-2]
COPIAR CÓDIGO
Particionando listas
Outra coisa que podemos fazer é particionar a lista, pegando partes dela. Para isso, usamos os dois pontos. Vamos pegar a lista de nomes agora. Já exploramos bastante a lista de médias, então vamos voltar à lista de nomes. Podemos imprimir ou simplesmente rodar o código para mostrar os elementos: Maria, João, Ana, Pedro e Juliana. Se quisermos pegar apenas do elemento 1, que é João, até o elemento 3, que é Pedro, fazemos isso usando colchetes. Começamos no elemento 1, colocamos dois pontos e indicamos até onde queremos ir. Se fizermos de 1 até 3, ele retornará João e Ana, mas não incluirá Pedro. Isso ocorre porque o último valor é excludente. Para incluir Pedro, precisamos ir até 4.

lista_de_nomes = ["Maria Silva", "João Santos", "Ana Oliveira", "Pedro Costa", "Juliana Pereira"]
lista_de_nomes[1:3]
lista_de_nomes[1:4]
COPIAR CÓDIGO
Podemos também pegar do elemento 1 até o final da lista sem precisar saber o tamanho dela. Basta usar dois pontos após o índice inicial. Isso fará com que ele comece na posição 1 e vá até o final da lista. Da mesma forma, podemos pegar do início da lista até uma posição específica, como antes da posição 3. Para isso, usamos dois pontos seguidos do índice final. Podemos omitir o zero, pois ele é assumido automaticamente.

lista_de_nomes[1:]
lista_de_nomes[:4]
COPIAR CÓDIGO
Adicionando elementos a listas
Agora que sabemos manipular e percorrer listas, podemos também adicionar ou remover elementos. Se quisermos adicionar um novo valor à lista, podemos usar o método append, que adiciona um elemento ao final da lista. Por exemplo, se um novo aluno entrar na sala, podemos usar lista_de_nomes.append("Novo Aluno") para adicioná-lo à lista.

lista_de_nomes.append("Fábio Carraro")
print(lista_de_nomes)
len(lista_de_nomes)
COPIAR CÓDIGO
Podemos realizar diversas operações com listas, pois sabemos que a variável lista_de_nomes contém uma lista. Podemos usar o método append() para adicionar um novo nome, como "Fábio Carrara". Ao rodar a célula e imprimir novamente a lista, veremos que o append adicionou mais uma pessoa ao final da lista. Se utilizarmos a função len() nessa nova lista, veremos que agora há seis pessoas.

Usando append e extend para adicionar múltiplos elementos
Podemos também adicionar mais de uma pessoa. Vamos tentar com o append. Se já temos seis pessoas na lista, vamos adicionar "Joana da Silva" e "Paulo Silveira", nosso fundador. Ao tentar adicionar essas duas pessoas, ocorre um erro, pois o método append recebe exatamente um argumento, e dois foram dados. O append serve para incluir uma pessoa de cada vez. Para incluir duas ou mais pessoas, temos algumas opções. Uma delas é usar um while, adicionando com vários append para cada nome, percorrendo a lista enquanto não terminar. No entanto, há uma maneira mais fácil: o método extend.

# Isso causará um erro
# lista_de_nomes.append("Joana da Silva", "Paulo Silveira")
COPIAR CÓDIGO
O extend permite adicionar uma lista a outra lista. Em vez de append, usamos extend e passamos os nomes "Joana da Silva" e "Paulo Silveira". Ao rodar, ocorre um erro, pois o extend também recebe apenas um argumento. Isso acontece porque o que passamos não é uma lista, mas dois elementos separados. Para transformar em lista, colocamos colchetes antes de "Joana" e depois de "Paulo Silveira". Ao rodar novamente e exibir a lista de nomes, vemos que "Joana da Silva" e "Paulo Silveira" foram adicionados corretamente ao final da lista.

lista_de_nomes.extend(["Joana da Silva", "Paulo Silveira"])
print(lista_de_nomes)
COPIAR CÓDIGO
O extend é semelhante ao append, mas quando temos duas listas diferentes, ele adiciona todos os elementos da nova lista ao final da lista original. Podemos nos perguntar se não conseguiríamos fazer o mesmo com append, transformando em lista. Vamos tentar: copiamos o código, transformamos em lista, e trocamos os nomes para "Márcio Costa" e "Natália Pedreira". Ao rodar, vemos que o append adicionou uma lista de nomes como um único elemento, enquanto o extend adiciona cada nome individualmente.

lista_de_nomes.append(["Márcio Costa", "Natália Pedreira"])
print(lista_de_nomes)
COPIAR CÓDIGO
Removendo elementos de listas
Se quisermos acessar elementos específicos, podemos usar colchetes. Por exemplo, se o elemento na posição 8 é uma lista, podemos acessar o primeiro nome com lista[8][0], que retornará "Márcio Costa". No entanto, no nosso caso, o mais correto seria usar extend para adicionar "Joana" e "Paulo Silveira" ao final da lista, sem criar uma lista dentro de outra.

lista_de_nomes[8]
lista_de_nomes[8][0]
COPIAR CÓDIGO
Além de adicionar, podemos remover elementos de uma lista. Se "Paulo Silveira" quiser sair, usamos o método remove(), que remove a primeira ocorrência do valor especificado. Se quisermos remover um elemento pela posição, usamos o método pop(). Por padrão, pop() remove o último elemento, mas podemos especificar uma posição, como lista.pop(2), para remover o elemento na posição 2.

lista_de_nomes.remove("Paulo Silveira")
print(lista_de_nomes)
lista_de_nomes.pop()
print(lista_de_nomes)
lista_de_nomes.pop(2)
print(lista_de_nomes)
COPIAR CÓDIGO
Concluindo a exploração de listas
Agora sabemos como adicionar, contar, remover e percorrer partes de uma lista. Nas próximas aulas, continuaremos explorando as estruturas do Python.

@@09
Explorando a necessidade de uma nova estrutura de dados

Continuando, mencionamos que iríamos explorar outra estrutura de dados amplamente utilizada. Primeiramente, vamos discutir por que precisamos de outra estrutura. Será que a lista não seria suficiente para todas as situações? Observamos que tínhamos listas de nomes e também listas de médias. No nosso caso, precisávamos identificar, por exemplo, que a nota da Maria, que está na posição 0, corresponde à nota na posição 0 da lista de médias.

Na posição 1, o nome "João", que está na posição 1 da lista de nomes, também estará na posição 1 da lista de médias. Precisamos ter duas listas separadas e algo que as conecte. Por exemplo, ao manipularmos as listas, adicionamos nomes com append, extend e outras operações. Precisamos lembrar que, ao usar append ou extend na lista de nomes, devemos fazer o mesmo na lista de médias. Caso contrário, uma pessoa pode ficar sem nota, o que gera complicações.

Introduzindo a estrutura de dados dicionário
Existe uma estrutura de dados que facilita esse processo: o dicionário. Um dicionário é uma estrutura que, assim como um dicionário de palavras, possui uma chave (a palavra que buscamos) e um valor (o significado). Nos dicionários, a chave é sempre um valor textual, uma string, enquanto o valor pode ser qualquer coisa, como um número, texto ou lista. A chave é o que buscamos, e o valor é o significado ou número associado a ela, como a média.

Para converter as listas de nomes e médias em um dicionário, podemos criar um dict de nomes e médias. Vamos começar definindo nossas listas:

lista_de_nomes = ["Maria Silva", "João Santos", "Ana Oliveira", "Pedro Costa", "Juliana Pereira"]
lista_de_medias = [8.9, 7.5, 4.2, 1.4, 9.5]
Criando e manipulando dicionários em Python
Agora, vamos criar o dicionário que associa cada nome à sua respectiva média. Inicialmente, podemos começar com um dicionário vazio e depois preenchê-lo:

dict_de_nomes_e_media = {}
Em seguida, podemos preencher o dicionário com os pares de chave e valor:

dict_de_nomes_e_media = {
    "Maria Silva": 8.9,
    "João Santos": 7.5,
    "Ana Oliveira": 4.2,
    "Pedro Costa": 1.4,
    "Juliana Pereira": 9.5
}
Nos dicionários, usamos chaves ao invés de colchetes, que são usados em listas. Assim, o Python identifica que se trata de um dicionário. No nosso caso, a chave será "Maria Silva" e o valor da média dela será 8.9. O segundo elemento será "João Santos", com a média de 7.5. Podemos usar a função de autocompletar para facilitar a criação do dicionário.

Acessando e manipulando dados em dicionários
Para acessar os valores no dicionário, usamos colchetes. Por exemplo, para acessar a média de "Maria Silva", usamos:

dict_de_nomes_e_media["Maria Silva"]
Isso retornará 8.9. Diferente das listas, onde usamos posições, nos dicionários usamos a chave, que é sempre uma string.

Além disso, podemos usar métodos como get, que retorna o valor de uma chave se ela estiver no dicionário. Podemos buscar o valor correspondente a uma chave usando colchetes ou o método get:

dict_de_nomes_e_media.get("Maria Silva")
Outro método é o pop, que remove um elemento do dicionário. Diferente das listas, onde pop remove o último elemento, nos dicionários precisamos especificar a chave a ser removida:

dict_de_nomes_e_media.pop("Juliana Pereira")
Explorando métodos úteis de dicionários
Outros métodos úteis são items, que retorna todos os elementos do dicionário, keys, que retorna todas as chaves, e values, que retorna todos os valores:

dict_de_nomes_e_media.items()
dict_de_nomes_e_media.keys()
dict_de_nomes_e_media.values()
Os dicionários são amplamente usados em Python e podemos combiná-los com listas. Por exemplo, podemos ter uma chave "nome" com o valor "Maria Silva" e uma chave "média" com o valor 8.9. Isso fica como desafio para resolvermos na próxima aula.

@@10
Propondo o desafio de unir dicionários

Conseguimos resolver o desafio de como unir os dicionários, fazendo com que o nome seja a chave e o valor dessa chave seja, por exemplo, "Maria Silva", seguido pela média e demais informações para todos os alunos?

O desafio proposto é utilizar dicionários de forma que as chaves sejam "nome" e "nota" (ou "média", no nosso caso), e os valores sejam os nomes e médias dos alunos. Como faríamos isso?

Iniciando a resolução do desafio
Se não tentamos no último vídeo, vamos pausar agora e tentar novamente. Vamos começar a resolver isso agora.

Já vimos que não faz muito sentido tentar acessar um valor específico de forma direta, como ocorreu anteriormente quando tentamos usar o índice zero de Maria Silva para pegar a primeira posição. Vamos criar um dicionário chamado dict_desafio. Como é um dicionário, teremos chaves, mas se fizermos isso de forma direta, não funcionaria, pois já mostramos que não funciona. A chave é algo que será buscado. Para resolver esse desafio, precisamos unir duas estruturas de dados que aprendemos até agora: listas e chaves.

Criando a estrutura de dados
Primeiro, vamos iniciar nosso dicionário vazio:

dict_desafio = {}
COPIAR CÓDIGO
Agora, vamos criar uma lista que englobará os nomes e médias dos alunos. Dentro dessa lista, o primeiro elemento será um dicionário com a primeira chave sendo nome e o valor "Maria Silva". O outro elemento desse dicionário será média, com o valor 8.9. Esse é o primeiro elemento da nossa lista, que não é uma string, número ou float, mas sim um dicionário. Podemos manipular essas estruturas como se fossem peças de lego. Agora temos uma lista de dicionários.

dict_desafio = [
    {"nome": "Maria Silva", "média": 8.9}
]
COPIAR CÓDIGO
Adicionando mais elementos à lista
Para o segundo elemento, devemos separar com uma vírgula e começar o segundo elemento. Podemos usar a sugestão da inteligência artificial, que já entendeu o que queremos fazer. Agora temos o melhor dos dois mundos: uma lista de dicionários, onde a chave é nome e o valor é "Maria Silva", e a chave é média e o valor é 8.9.

dict_desafio = [
    {"nome": "Maria Silva", "média": 8.9},
    {"nome": "João Santos", "média": 7.5},
    {"nome": "Ana Oliveira", "média": 4.2},
    {"nome": "Pedro Costa", "média": 1.4}
]
COPIAR CÓDIGO
Acessando elementos da lista de dicionários
Vamos executar esse código para gravar na memória. Quando quisermos acessar o primeiro elemento dessa lista, como é uma lista, podemos usar índices numéricos. O elemento 0, que é o primeiro elemento, retornará um dicionário com chave nome e valor "Maria Silva", e chave média e valor 8.9.

dict_desafio[0]
COPIAR CÓDIGO
Se quisermos pegar apenas a média dessa pessoa, podemos continuar encadeando buscas. Como é um dicionário, só conseguimos buscar por chaves, não por valores. Queremos a chave chamada média. Então, na lista de dicionários, pegamos o primeiro elemento, que é um dicionário, e retornamos o valor correspondente à chave média, que é 8.9.

dict_desafio[0]["média"]
COPIAR CÓDIGO
Concluindo o desafio e sugestões de estudo
Podemos fazer isso de maneira separada para ficar mais claro o passo a passo. O índice 0 retorna o primeiro elemento, e 0 entre colchetes seguido de média entre colchetes retorna o valor correspondente à chave média desse dicionário. Lembrando que dicionários podem ter quantos pares chave-valor quisermos. Neste caso, as chaves são nome e média, e os valores são o nome e a média da pessoa correspondente. Conseguimos criar uma lista de dicionários, o que torna tudo mais organizado, fácil de ler, acessar e integrar no código.

Se você conseguiu resolver o desafio, parabéns! Se não conseguiu, recomendo revisar o conteúdo. Caso tenha dúvidas, use a inteligência artificial para ajudar a entender melhor. Por exemplo, copie e cole o dicionário no Gemini, ChatGPT ou Maritaca AI e peça uma explicação como se tivesse 5 anos de idade. Isso pode ajudar a entender de forma mais simples. A IA pode explicar usando analogias, como uma lista de brinquedos onde cada brinquedo é uma caixinha com um adesivo com o nome de uma pessoa e um papelzinho com a média da nota dela.

Essa interação com inteligências artificiais pode ajudar a esclarecer dúvidas durante este e outros cursos da Alura. Até mais e até a próxima aula.

@@11
Ajustando preços de produtos na TRATOTECH

A TRATOTECH, uma plataforma de classificados focada em produtos tecnológicos, está implementando um sistema para ajustar automaticamente os preços dos produtos listados. A ideia é que, ao final de cada mês, todos os preços dos produtos sejam aumentados em 5%, exceto aqueles que já atingiram ou ultrapassaram o valor de R$ 10.000,00, que devem ser mantidos nesse valor máximo. A equipe de desenvolvimento que você faz parte precisa garantir que o sistema funcione corretamente, ajustando os preços conforme a regra estabelecida.
Qual abordagem garantiria que os preços sejam ajustados corretamente?

Selecione uma alternativa

Criar uma função que aplique um aumento de 5% a todos os produtos, independentemente do preço atual, e depois verificar se algum produto ultrapassou R$ 10.000,00, ajustando-os para esse valor. Além disso, implementar um sistema de logs para registrar cada ajuste feito, permitindo auditoria e controle sobre as alterações de preços realizadas.
 
Alternativa incorreta
Utilizar uma estrutura condicional que apenas aumente os preços dos produtos que já estão acima de R$ 10.000,00 em 5%, mantendo os demais inalterados. Adicionalmente, incluir um relatório mensal que liste todos os produtos que tiveram seus preços ajustados, destacando aqueles que permaneceram inalterados devido ao limite de preço.
 
Alternativa incorreta
Implementar um loop que percorra a lista de produtos e, para cada produto, verificar o preço atual. Se já for maior ou igual a R$ 10.000,00, mantê-lo nesse valor. Caso contrário, aumentar o preço em 5% e, se após o reajuste ultrapassar R$ 10.000,00, ajustá-lo para exatamente R$ 10.000,00. A condição de parada do loop será quando todos os produtos tiverem seus preços ajustados.
 
Correta, pois essa abordagem garante que cada produto seja avaliado individualmente e ajustado conforme a regra, sem ultrapassar o valor máximo estipulado.
Alternativa incorreta
Aplicar um aumento de 5% a todos os produtos e, em seguida, aplicar um desconto de 5% aos produtos que ultrapassaram R$ 10.000,00 para ajustá-los ao valor correto. Além disso, desenvolver um mecanismo de notificação que informe os vendedores sobre as alterações de preços, garantindo transparência no processo de ajuste.

@@12
Para saber mais: índices negativos em listas

Conceito de Índice Negativo
Em Python, os índices negativos são uma funcionalidade que permite acessar elementos a partir do final de uma lista. Em vez de calcular manualmente a posição usando o comprimento da lista (por exemplo, len(lista) - 1 para o último elemento), você pode simplesmente usar -1. Essa abordagem torna o código mais legível e reduz a chance de erros de cálculo.

Funcionamento da Indexação Negativa
Quando você usa um índice negativo, Python começa a contar a partir do final. Assim, o índice -1 corresponde ao último elemento, -2 ao penúltimo, e assim por diante. Essa contagem inversa é útil para acessar elementos sem precisar saber o tamanho exato da lista. Por exemplo:

nomes = ['Maria', 'João', 'Ana', 'Pedro', 'Juliana']

print(nomes[-1])  # Exibe 'Juliana'
print(nomes[-2])  # Exibe 'Pedro'
COPIAR CÓDIGO
Nesse exemplo, o uso de índices negativos simplifica a obtenção dos elementos finais da lista sem precisar usar a função len().

Vantagens e Cuidados
Utilizar índices negativos melhora a clareza do código, especialmente quando o foco está em acessar elementos do fim da lista. Essa abordagem evita o 'hardcoding' de valores numéricos que dependem do tamanho da lista.

Por outro lado, é importante ter atenção para não ultrapassar a contagem da lista. Por exemplo, em uma lista de 5 elementos, tentar acessar o índice -6 resultará em um IndexError. Além disso, o uso excessivo de índices negativos pode, em alguns casos, dificultar a leitura se não for utilizado de forma consistente com o restante do código.

Aplicações Práticas
Os índices negativos são especialmente úteis em situações onde a lista pode ter um tamanho variável ou quando se deseja trabalhar com os últimos elementos de coleções de dados. Em operações de slicing, a combinação de índices positivos e negativos permite selecionar sublistas de maneira dinâmica, tornando o código mais flexível e robusto.

# Exemplo de slicing com índice negativo
ultimos_tres = nomes[-3:]
print(ultimos_tres)  # Exibe ['Ana', 'Pedro', 'Juliana']
COPIAR CÓDIGO
Essa funcionalidade mostra como a indexação negativa é poderosa para manipulações de dados em Python, proporcionando simplicidade sem abrir mão do controle dos elementos em uma lista.

@@13
Faça como eu fiz: API e Dados em Python

Nesta aula, aprendemos a conectar uma IA no Google Colab, configurar a API Key do Gemini, realizar requisições e manipular dados utilizando estruturas de repetição, listas e dicionários em Python.
Agora é a sua chance de revisar e aplicar os conteúdos desta aula. Para isso:

Abra um notebook no Google Colab e insira um título em Markdown
Insira comentários para organizar o código
Configure a conexão com a API do Gemini
Obtenha a API Key por meio do Google AI Studio
Copie a API Key e adicione-a ao cofre de Secrets do Colab
Configure a variável de ambiente usando o módulo os
Importe o SDK do Google Gen AI para facilitar a conexão
Crie uma instância do cliente utilizando Gen AI client
Utilize o método generateContent com o modelo "Gemini-2.5-Flash"
Envie uma requisição com um prompt de exemplo, como "o que é a inteligência artificial?"
Armazene e exiba a resposta obtida da API
Implemente um loop while para demonstrar a repetição de ações (ex.: imprimir asteriscos)
Utilize a variável de controle e incremente-a para evitar loops infinitos
Receba entrada do usuário por meio da função input
Crie um chat interativo usando client.chats.create e sendMessage
Armazene e exiba o histórico das interações com chat.getHistory
Crie listas para armazenar nomes e médias de alunos
Acesse, modifique e percorra elementos das listas utilizando índices e slices
Aplique uma operação de incremento nas notas e limite o valor máximo a 10
Construa dicionários unindo chaves e valores para representar nome e média dos alunos
Para acessar o guia detalhado, consulte as transcrições da aula.

@@14
O que aprendemos?

Nesta aula, aprendemos:
Compreendemos o uso e autenticação de APIs de IA no Google Colab.
Exploramos loops while e sua aplicação para evitar loops infinitos.
Implementamos um chatbot interativo utilizando o modelo Gemini.
Manipulamos listas, aprendendo a acessar, modificar e adicionar elementos.
Utilizamos dicionários para armazenar e acessar pares de chave-valor.
Estudamos métodos para manipulação de listas e dicionários, como append(), pop(), .items() e .get().
Criamos estruturas de dados complexas com listas de dicionários.
Compreendemos o acesso e manipulação de dados em estruturas aninhadas.

#21/01/2026

@03-Entrada e conversão de dados

@@01
Projeto da aula anterior

Caso queira revisar o código até aqui ou começar a partir desse ponto, disponibilizamos os códigos realizados na aula anterior, para visualizar clique neste link.

https://colab.research.google.com/drive/177ODspQ7QNJjHsRkhaqTyL8g2_sUNSba#scrollTo=J4awocILwTwU

@@02
Explorando o loop `for` em Python

Agora que já vimos algumas das estruturas, como listas e dicionários, e também como utilizar o loop while, vamos explorar outra estrutura de repetição, que é o loop for. Este é um dos mais utilizados na linguagem Python e em outras linguagens de programação. O for funciona de maneira um pouco diferente do while. No while, definimos um ponto inicial, por exemplo, começando com n = 0, e continuamos enquanto uma condição for verdadeira. No caso, enquanto o número dentro da variável n for menor do que o tamanho da lista de médias. Enquanto essa condição for verdadeira, o loop continua.

Para ilustrar, vamos criar uma lista de dicionários chamada dict_desafio que contém nomes e médias:

dict_desafio = [
    {"nome": "Maria Silva", "média": 8.9},
    {"nome": "João Santos", "média": 7.5},
    {"nome": "Ana Oliveira", "média": 4.2},
    {"nome": "Pedro Costa", "média": 1.4}
]
COPIAR CÓDIGO
Comparando while e for para percorrer listas
O for é diferente porque especificamos quantas vezes ele vai repetir ou iterar sobre uma lista. Ele é amplamente utilizado com as estruturas de dados que acabamos de discutir. Vamos tentar imprimir todos os itens de um dicionário de desafio na tela, um por um, usando print. Lembrando que criamos a variável dict_desafio, que é uma lista de dicionários. Podemos percorrê-la um por um. Já sabemos como fazer isso com o while. Vamos relembrar?

Podemos definir uma variável n = 0. Enquanto o valor de n for menor do que, por exemplo, o len da lista, podemos usar diretamente o número 4, mas é mais elegante usar len porque ele pode variar. Enquanto n for menor do que o tamanho de dict_desafio, imprimimos o valor de dict_desafio na posição n. Quando n for igual a 0, ele verifica se 0 é menor do que 4, e imprime o valor na posição 0. Para evitar um loop infinito, incrementamos n em 1. Assim, n passa de 0 para 1, depois 2, 3, e finalmente 4, quando a condição se torna falsa e o loop para.

n = 0
while n < len(dict_desafio):
    print(dict_desafio[n])
    n += 1
COPIAR CÓDIGO
Além disso, ao adicionar um valor a ele mesmo, podemos usar a notação n += 1 em vez de n = n + 1. Isso funciona da mesma maneira, somando 1 a n e atribuindo o resultado de volta a n. Essa notação é comum na programação e pode ser usada para outras operações, como subtração ou multiplicação.

Simplificando com o loop for
Para fazer a mesma interação com o for, é ainda mais simples. Não precisamos definir n = 0 ou usar len. Basta declarar uma variável temporária, que será usada dentro do for. Podemos chamá-la de elemento. Para cada elemento dentro de dict_desafio, imprimimos um por um os elementos.

for elemento in dict_desafio:
    print(elemento)
COPIAR CÓDIGO
Utilizando o for e o range no Python
Vamos começar discutindo como podemos simplificar o código utilizando o for. Ao invés de escrever quatro linhas, conseguimos fazer o mesmo em apenas duas. A única diferença é a variável elemento, que é criada no momento da execução, apenas para ser utilizada dentro do loop. Poderíamos nomeá-la de qualquer forma. Para cada n dentro de dict_desafio, imprimimos o valor desse elemento n. Isso é uma variável temporária que existe apenas durante o processamento do loop for.

No nosso exemplo, temos uma lista de quatro dicionários com nomes e médias. O loop imprime cada um deles sequencialmente. Se quisermos apenas listar números de 0 a 5, com o while, faríamos algo como declarar n = 0 e, enquanto n for menor que 5, executaríamos uma ação. Com o for, podemos gerar uma sequência de números de forma mais fácil. Utilizamos for n in range, especificando quantos números queremos. A função range cria uma faixa de elementos, similar às partições de listas que vimos anteriormente.

for n in range(5):
    print(n)
COPIAR CÓDIGO
Se não especificarmos um valor inicial, o range começa do 0 até o número especificado, não incluindo o último número. Por exemplo, range(5) gera os números de 0 a 4. Podemos também especificar um valor inicial diferente de 0, como range(2, 7), que gera os números de 2 a 6. Além disso, podemos definir um passo, como range(2, 7, 2), que gera os números 2, 4 e 6, pulando de 2 em 2.

for n in range(2, 7, 2):
    print(n)
COPIAR CÓDIGO
Trabalhando com dicionários
Vamos criar um dicionário chamado pessoa, que contém dados de uma pessoa. Um dicionário é composto por pares de chave e valor, onde o valor pode ser de qualquer tipo, como um número inteiro, decimal, texto ou lista. No nosso exemplo, pessoa terá um nome, idade e altura. Podemos imprimir esses dados facilmente.

pessoa = {
    "nome": "Fabricio",
    "idade": 19,
    "altura": 1.87
}
COPIAR CÓDIGO
Para percorrer o dicionário e retornar seus dados, podemos usar o for. Podemos iterar sobre as chaves ou sobre os pares de chave e valor. Usando for chave, valor in pessoa.items(), conseguimos acessar tanto as chaves quanto os valores. Utilizando f-strings, podemos formatar a saída de forma clara, imprimindo a chave e o valor correspondente.

for chave, valor in pessoa.items():
    print(f"A chave é {chave} e o valor é {valor}.")
COPIAR CÓDIGO
Explorando a operação de resto
Por fim, vamos explorar a operação de resto, que é bastante utilizada em programação. Para cada número n em range(0, 11), queremos imprimir apenas os números pares. Um número é par se o resto da divisão por 2 é zero. Utilizamos o operador % para obter o resto da divisão. Se n % 2 == 0, imprimimos n.

for n in range(11):
    if n % 2 == 0:
        print(n)
COPIAR CÓDIGO
Podemos também modificar o divisor para obter diferentes padrões. Por exemplo, n % 3 == 0 imprime os múltiplos de 3. Essa operação é comum em programação e será útil em diversas situações.

Essa foi a aula sobre o uso do for e loops no Python. Continuaremos avançando em direção ao nosso objetivo e desafio nas próximas aulas. Até mais!

@@03
Conceito de funções em Python

Vamos continuar explorando a linguagem Python. Hoje teremos uma das aulas mais importantes deste curso, pois aprenderemos sobre funções. Este é um conceito que qualquer pessoa desenvolvedora, cientista de dados ou engenheira de IA utilizará diariamente em suas atividades de programação.

Uma função é, basicamente, uma forma de encapsular um algoritmo ou um procedimento específico dentro de um bloco de código. Posteriormente, podemos passar novos dados para esse bloco, e ele executará a mesma operação de forma consistente.

Revisando operações com strings
Vamos retomar o exemplo inicial que demos com as strings. Utilizamos um nome fictício e aplicamos várias operações, como os métodos lower para deixar tudo em minúsculo, upper para deixar tudo em maiúsculo, strip para remover os espaços do começo e do final, e replace para substituir algo, como dois espaços por um espaço apenas. Conectamos tudo, começando com strip, depois upper, seguido de replace, e no final conseguimos imprimir o nome da maneira desejada no desafio.

Agora, vamos criar cinco variáveis (texto_2, texto_3, etc.), onde cada uma é uma string com um nome completo de uma pessoa, mas escrito de forma desordenada, misturando maiúsculas e minúsculas, com espaços a mais no começo, no final e no meio. Isso é comum em tabelas de Excel, onde os nomes podem estar em diferentes formatos. Já aprendemos a padronizar isso usando métodos como upper e strip. No entanto, fazer isso manualmente para cada texto não é prático. É para isso que existem as funções, que englobam uma ação ou algoritmo que queremos aplicar a vários elementos.

Criando a função escreve_texto_corretamente
Para criar uma função em Python, começamos com def, seguido do nome da função, que deve ser em minúsculas e, se necessário, separado por underline. Vamos chamar a função de escreve_texto_corretamente. Dentro dos parênteses, definimos o que a função vai receber. Por exemplo, o método range recebe um número como parâmetro. Da mesma forma, nossa função receberá um texto.

Vamos começar definindo a função:

def escreve_texto_corretamente(texto):
COPIAR CÓDIGO
Após definir a função, aplicamos os métodos strip, upper e replace ao texto. Para alterar o valor original da variável, atribuímos o resultado a ela ou imprimimos diretamente. Podemos também criar uma nova variável, como texto_novo, e imprimir o resultado.

    texto_novo = ' '.join(texto.strip().upper().split())
    print(texto_novo)
COPIAR CÓDIGO
Executando a função com exemplos práticos
Para rodar a função, usamos o nome definido com def, passando um argumento, como texto_1. A função busca na memória, aplica os métodos strip, upper e replace, e imprime o resultado.

texto1 = "  joÃO   sILVA de   Souza  "
escreve_texto_corretamente(texto1)
COPIAR CÓDIGO
Se quisermos que a função substitua qualquer número de espaços, podemos usar o método split, que separa uma string em uma lista de palavras, eliminando espaços extras. Para juntar as palavras novamente, usamos o método join, que requer um separador, como um espaço único.

Por exemplo, aplicamos split ao texto, que cria uma lista de palavras. Em seguida, usamos join para unir as palavras com um espaço entre elas, armazenando o resultado em uma variável como nome_final, e imprimimos o resultado.

Ao rodar a função, obtemos o texto formatado corretamente, sem espaços extras e com todas as letras em maiúsculo. Podemos aplicar o mesmo processo a outros textos, como texto_3, e obter resultados consistentes.

texto2 = "mArIA   aNA   sAntoS   pereIRA"
texto3 = "  PeDRO   alvaRes   cabrAl "
texto4 = "  anA   caroLINa   ferreirA"
texto5 = "rObertO   carlOS   OliVeIRa"

escreve_texto_corretamente(texto2)
escreve_texto_corretamente(texto3)
escreve_texto_corretamente(texto4)
escreve_texto_corretamente(texto5)
COPIAR CÓDIGO
Explorando possibilidades futuras com funções
Existem outros modos de trabalhar com funções, que podem ser mais úteis no dia a dia do que simplesmente imprimir o resultado. Exploraremos isso em breve.

@@04
Iniciando a simplificação da função

Iniciando esta aula, lembramos que comentamos anteriormente sobre a possibilidade de escrever uma função de maneira mais simples e curta, sem utilizar tantas variáveis. Vamos tentar fazer isso juntos agora no início, para simplificar. Vamos manter a função como está, mas copiar uma nova versão dela abaixo.

O nome final era o resultado do join, utilizando o espaço da nossa lista de palavras. A lista de palavras era obtida através de um texto_novo.split(). O texto_novo era um texto.upper(). Se juntarmos tudo isso em uma única operação, podemos fazer um texto.upper().split() e aplicar diretamente, eliminando a linha intermediária. Podemos colocar tudo isso como argumento do join. Podemos deixar o resultado em uma variável nome_final e retornar essa variável, ou podemos inserir tudo diretamente no print.

Apresentando a versão original e simplificada da função
Para ilustrar, vamos começar com a versão original da função:

def escreve_texto_corretamente(texto):
    texto_novo = texto.upper()
    lista_de_palavras = texto_novo.split()
    nome_final = " ".join(lista_de_palavras)
    print(nome_final)
COPIAR CÓDIGO
Agora, vamos simplificar essa função, eliminando as variáveis intermediárias:

def escreve_texto_corretamente(texto):
    nome_final = " ".join(texto.upper().split())
    print(nome_final)
COPIAR CÓDIGO
Se fizermos isso, descrevemos o nome corretamente. A alternativa é substituir o nome da função, e ela funcionará exatamente da mesma forma, mas com uma linha em vez de quatro. Com o tempo e experiência, aprendemos a fazer isso de maneira mais simples, sem precisar de tantas variáveis para alocar na memória, como texto_novo, lista_palavras e assim por diante.

Discutindo a importância do retorno em funções
O que queremos mostrar neste vídeo é que a primeira função que fizemos é mais simples, pois não retorna nada; ela apenas manipula o texto e imprime no final. No entanto, a maioria das funções que utilizamos no dia a dia precisa retornar algo. Enviamos algo para a função, e ela nos devolve uma resposta.

Vamos pensar na ideia que estávamos desenvolvendo sobre salas de aula e estudantes. Imaginemos que temos uma lista de nomes de alunos escrita incorretamente. Esta é a lista real, e não queremos apenas corrigir o nome do aluno. Nossa escola possui três salas de aula. Podemos definir uma variável para as salas de aula ou classes, como sala 1, sala 2 e sala 3, e temos uma lista com três elementos.

salas_de_aula = ["Sala 1", "Sala 2", "Sala 3"]
COPIAR CÓDIGO
Criando a função para alocar alunos em salas
O que queremos é que, sempre que recebermos um nome de aluno, que pode estar escrito de qualquer forma, padronizemos esse nome. Após isso, através da função que já temos, queremos atribuir aleatoriamente uma dessas salas aos alunos: sala 1, sala 2 ou sala 3. Não queremos seguir uma ordem fixa, mas sim de forma aleatória.

Para isso, podemos criar uma função. Lembrando como definimos uma função, utilizamos a palavra-chave def. A função pode ser chamada de aloca_alunos_em_salas. Ela receberá como parâmetros o nome do aluno e as salas disponíveis, que podem variar. Podemos definir isso posteriormente, mas, no exemplo, estamos utilizando sempre as mesmas salas.

def aloca_alunos_em_salas(nome_do_aluno, lista_de_salas):
COPIAR CÓDIGO
Podemos definir a lista de salas para não confundir, utilizando nomes diferentes. Esses nomes, como nome_do_aluno e lista_de_salas, são válidos apenas dentro da função def, não se aplicando ao restante do código.

Utilizando o módulo random para alocação aleatória
Continuando, o que precisamos fazer primeiro? Vamos supor que já tenhamos corrigido o texto com a função escreve_texto_corretamente, seja a alternativa ou a original, e agora queremos apenas passar o nome do aluno e alocá-lo de forma aleatória em uma das salas: sala 1, sala 2 ou sala 3. Como faríamos isso?

Já existe um módulo, uma biblioteca pronta que trata de assuntos aleatórios. Precisamos importar essa biblioteca com import random, da mesma forma que fizemos anteriormente ao lidar com as IAs, quando importamos o genAI e o userData. Esse módulo já está instalado nos computadores do Google Colab, então não precisamos instalá-lo do zero, basta fazer o import random, que já vem direto do Python.

import random
COPIAR CÓDIGO
Criando um dicionário para organizar dados do aluno
O que faremos é pegar o nome do aluno e escolher aleatoriamente uma das salas para ele. O ideal é que retornemos algo mais estruturado. Uma das estruturas de dados mais organizadas que vimos até agora são os dicionários. Podemos criar um dicionário específico que contenha o nome e a sala do aluno, facilitando nossa organização.

Primeiramente, vamos escolher aleatoriamente a sala do aluno. Criamos uma variável sala_do_aluno, que receberá o resultado do método choice do módulo random. Esse método fará uma escolha entre as salas de aula. Utilizaremos a variável lista_de_salas, que a função recebe, para garantir que estamos pegando a lista correta.

sala_do_aluno = random.choice(lista_de_salas)
COPIAR CÓDIGO
Se imprimirmos sala_do_aluno, veremos que ele escolhe aleatoriamente entre sala 1, sala 2 e sala 3. No entanto, não queremos apenas imprimir essa informação; queremos criar um dicionário com o nome corrigido do aluno e a sala para a qual ele foi alocado.

Corrigindo o nome do aluno e retornando o dicionário
Vamos criar esse dicionário, que podemos chamar de dict_aluno. Um dicionário é sempre representado por chaves e valores. Teremos a chave nome, que receberá o valor nome_do_aluno, e a chave sala, que receberá a sala escolhida aleatoriamente. Podemos imprimir dict_aluno para verificar se está tudo correto.

dict_aluno = {
    "nome": nome_do_aluno,
    "sala": sala_do_aluno
}
print(dict_aluno)
COPIAR CÓDIGO
Ao rodar o código, ele imprime o nome do aluno e a sala correta. No entanto, o nome ainda está incorreto. Queremos corrigir isso utilizando a função escreve_texto_corretamente. Essa função, ao invés de apenas imprimir o nome, deve retornar o nome corrigido para que possamos usá-lo posteriormente. Para isso, utilizamos a palavra-chave return.

def escreve_texto_corretamente(texto):
    nome_final = " ".join(texto.upper().split())
    return nome_final
COPIAR CÓDIGO
Integrando funções para alocação e correção de nomes
Vamos rodar a função escreve_texto_corretamente e armazenar o resultado em uma variável, como nome_final. Assim, podemos passar o nome corrigido para a função aloca_alunos_em_salas, garantindo que o nome esteja correto.

nome_processado = escreve_texto_corretamente(texto1)
aloca_alunos_em_salas(nome_processado, salas_de_aula)
COPIAR CÓDIGO
Podemos passar diferentes listas de salas para a função, como "classe 1", "classe 2" e "classe 3", e ela funcionará corretamente, pois a função foi definida para receber dois argumentos. Assim, conseguimos alocar alunos de forma aleatória e retornar o nome corrigido.

Desafio para prática e aplicação de conceitos
Agora, sabemos como fazer escolhas aleatórias com random.choice e como retornar valores de uma função. Podemos retornar qualquer tipo de dado, como uma String, um número ou uma lista, para utilizá-lo posteriormente.

Deixarei um desafio para vocês. A primeira parte faremos juntos. Vamos criar um bloco de texto com o título "Desafio". O primeiro passo é pedir para uma IA gerar, em Python, uma lista de 20 e-mails. A IA deve gerar uma lista de 20 strings, ou seja, 20 e-mails.

O segundo passo, sem usar inteligência artificial, é criar uma função que receba essa lista de 20 e-mails como argumento. A função deve percorrer a lista e, para cada e-mail, chamar a IA do Gemini via API para resumir o conteúdo do e-mail em uma linha, definindo o que a pessoa queria no e-mail.

Vamos pedir para a IA gerar uma lista de 20 corpos de e-mails de temas variados em Python. Podemos usar o Gemini, o ChatGPT, o Cloud, ou qualquer outra ferramenta. Ao pedir para a IA, devemos ser claros em nossos pedidos, utilizando a engenharia de prompt para garantir que a IA entenda corretamente.

Após gerar a lista, podemos copiá-la e salvá-la em uma variável email_bodies. Na próxima aula, resolveremos esse desafio juntos, mas encorajo vocês a tentarem resolvê-lo por conta própria, pois é o desafio mais interessante até agora do curso. Até mais!

@@05
Desafio de resumir e-mails

Continuando nossa jornada, nesta aula vamos aprender a rodar LLMs (Modelos de Linguagem de Grande Escala) que são open source (código aberto). Até agora, utilizamos o modelo Gemini 2.5 Flash, do Google, que é um modelo privado. Não conseguimos saber o que há dentro desse modelo, nem baixá-lo para rodar localmente ou em um cluster de computadores. Precisamos aceitar o que o Google nos fornece. No entanto, existem vários modelos de IA chamados open source ou open weights (pesos abertos), que podemos baixar e rodar localmente, seja em nossa máquina ou em um servidor na nuvem. Esses modelos oferecem mais liberdade, especialmente se atingirmos o limite do Gemini ou se quisermos mais privacidade, evitando enviar dados para servidores do Google, OpenAI, Anthropic ou XAI.

Para rodar esses modelos, existem várias formas. Uma delas é utilizando o serviço de uma empresa chamada Grok. Atenção: não é o Grok com K, que é um modelo de IA da XAI, empresa de Elon Musk. Estamos falando do Grok com Q, que oferece "Fast Inference for AI Builders" (Inferência Rápida para Construtores de IA). Inferência é o processo de gerar uma resposta a partir de um modelo de IA. Podemos utilizar o Grok com Q, e ao acessar a página, podemos clicar na opção "Start Building" (Começar a Criar). Caso não tenhamos uma conta, precisamos criar uma, podendo até conectar com uma conta do Google.

Configurando o ambiente para uso do Grok
Ao entrar, veremos uma tela onde podemos criar uma chave da API. Se já tivermos criado anteriormente, veremos o uso atual e créditos grátis para testar. Descendo a página, visualizamos alguns modelos open source disponíveis, como o GPT OSS de 20 bilhões de parâmetros, o DeepSeek R1, e outros. Esses modelos são indicados para diferentes finalidades, como Reasoning (raciocínio), uso de ferramentas, transcrição de fala para texto, entre outros.

Para este exemplo, utilizaremos o GPT OSS de 20 bilhões de parâmetros. Primeiro, clicamos em "Manage API Key" para criar uma chave da API. Damos um nome, como "aulas Python", e geramos a chave. É importante não compartilhar essa chave com ninguém. No Colab, criamos um novo bloco de código, mas não colamos a chave diretamente no código para evitar problemas de segurança. Em vez disso, adicionamos um novo Secret no Colab, chamando-o de "Grok API Key", e colamos a chave lá.

Instalando e utilizando a biblioteca Grok no Colab
Dentro do Grok, temos várias opções, como acessar o Playground para testar os modelos. Podemos escolher o modelo desejado, como o GPT OSS de 20 bilhões, e testar com perguntas, observando a rapidez das respostas. O modelo de Reasoning é rápido, processando 1103 tokens por segundo.

Para usar o Grok no Colab, precisamos instalar a biblioteca. Como o Colab é uma ferramenta do Google, já possui bibliotecas do Google instaladas, mas para bibliotecas externas, precisamos instalá-las manualmente. Utilizamos o comando !pip install -q groq para instalar o Grok. O -q é opcional e serve para suprimir mensagens detalhadas durante a instalação.

!pip install -q groq
COPIAR CÓDIGO
Depois, conectamos a chave da API da mesma forma que fizemos com a do Gemini. No ambiente do Colab, definimos a variável Grok API Key com o valor do Secret que criamos. Assim, podemos utilizar o Grok de forma segura e eficiente em nossos projetos.

os.environ["GROQ_API_KEY"] = userdata.get('GROQ_API_KEY')
COPIAR CÓDIGO
Executando consultas com o modelo GPT-OSS
Ao salvar o que estávamos fazendo, pegamos aquele número alfanumérico gigantesco, que estava escondido, mas conseguimos ver. Esse método coloca o alfanumérico dentro do nosso ambiente, em uma variável chamada Grok API Key. Com isso, estamos prontos para rodar o que quisermos. O código que copiamos está importando o Grok com from groq import Groq. Em seguida, fazemos client.chat.completions.create. Não é necessário decorar isso, pois é um padrão desse modelo e de vários outros, como os da OpenAI. Podemos copiar isso sempre que precisarmos.

from groq import Groq

client = Groq()

completion = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "user",
            "content": "O que é IA?"
        }
    ],
    temperature=1,
    max_completion_tokens=8192,
    top_p=1,
    reasoning_effort="medium",
    stream=True,
    stop=None,
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
COPIAR CÓDIGO
O model que vamos usar é o OpenAI do chat GPT, gpt-oss-20b, que possui 20 bilhões de parâmetros. Dentro dele, temos uma lista de mensagens, indicada pelos colchetes, chamada messages. A primeira mensagem passa o role, o papel do usuário, que pergunta "O que é IA?". O assistente responde que "IA é um ramo da ciência". Podemos limpar a conversa clicando em "clear", e veremos que há apenas um item dentro de messages. Temos a nossa pergunta, a resposta do gpt-oss-20b através do Grok, e uma possível nova pergunta que podemos fazer dentro dessa janela de chat.

Ajustando parâmetros do modelo para diferentes resultados
Podemos deixar apenas uma mensagem, com o role como user, e a pergunta pode ser qualquer outra, como "De que é feito o sol?". Passamos vários parâmetros para o modelo, um deles é a temperatura. Esse conceito define o quão criativo o modelo será, variando geralmente de 0 a 2, dependendo do modelo. No Gemini, varia de 0 a 1, enquanto no OpenAI, no chat GPT, varia de 0 a 2. O valor 0 significa o menos criativo possível, e o valor 2, o mais criativo.

Para explicar, podemos abrir uma janela do chat GPT e fazer algumas perguntas. Por exemplo, podemos jogar um jogo onde damos uma frase incompleta e pedimos as cinco principais possibilidades de palavras para continuar a frase, com a porcentagem de probabilidade. Ao enviar "Eu gosto de comer", ele pode responder com "pizza 28%", "chocolate 22%", "carne 15%", "frutas 12%" e "bolo 9%". Modelos de linguagem, como o Gemini e o chat GPT, funcionam tentando prever o próximo token, que é uma subpalavra. Por exemplo, a palavra "infeliz" pode ser dividida em dois tokens: "in" e "feliz". O token "in" pode ser usado em outras palavras, como "indivisível" e "incompreensível".

Quando treinamos esses modelos, é mais fácil passar as palavras de forma separada, pois os computadores não entendem palavras, apenas números. Suponhamos que o token "in" corresponda ao número 5 e "feliz" ao número 5734. O mesmo token "in" pode ser reutilizado em outras palavras. Isso é o que o modelo está prevendo: o próximo token.

Explorando a temperatura e outros parâmetros
Voltando à temperatura, quando colocamos um valor próximo de zero, o modelo será menos criativo e escolherá quase sempre as primeiras opções. Com uma temperatura mais alta, próxima de 1,5, ele variará mais, escolhendo diferentes opções. Isso é útil para escrever textos, onde podemos querer mais variação. Para casos que exigem precisão, como escrever código, usamos temperaturas mais baixas, próximas de zero.

O Max Completion Tokens define o número máximo de tokens. O TopP não é necessário. O Reasoning Effort define o esforço de raciocínio do modelo, podendo ser baixo, médio ou alto. Podemos deixar no médio ou apagar. O Stream faz o processamento em tempo real. Para cada pedaço na variável Completion, que recebemos do Grok, ele imprime a resposta.

Ao rodar o código, vemos que ele é extremamente rápido. Ele se comunica com os servidores do Grok, onde o modelo GPT-OSS de 20B está hospedado, processa a pergunta e retorna a resposta rapidamente. O Grok permite que usemos créditos para experimentar, mas eventualmente será necessário inserir um cartão de crédito para cobranças.

Podemos usar um modelo open source como o Gemini ou o Grok, mudando apenas algumas configurações. Na próxima aula, continuaremos explorando a linguagem Python.

@@06
LLMs open source

Continuando nossa jornada, nesta aula vamos aprender a rodar LLMs (Modelos de Linguagem de Grande Escala) que são open source (código aberto). Até agora, utilizamos o modelo Gemini 2.5 Flash, do Google, que é um modelo privado. Não conseguimos saber o que há dentro desse modelo, nem baixá-lo para rodar localmente ou em um cluster de computadores. Precisamos aceitar o que o Google nos fornece. No entanto, existem vários modelos de IA chamados open source ou open weights (pesos abertos), que podemos baixar e rodar localmente, seja em nossa máquina ou em um servidor na nuvem. Esses modelos oferecem mais liberdade, especialmente se atingirmos o limite do Gemini ou se quisermos mais privacidade, evitando enviar dados para servidores do Google, OpenAI, Anthropic ou XAI.

Para rodar esses modelos, existem várias formas. Uma delas é utilizando o serviço de uma empresa chamada Grok. Atenção: não é o Grok com K, que é um modelo de IA da XAI, empresa de Elon Musk. Estamos falando do Grok com Q, que oferece "Fast Inference for AI Builders" (Inferência Rápida para Construtores de IA). Inferência é o processo de gerar uma resposta a partir de um modelo de IA. Podemos utilizar o Grok com Q, e ao acessar a página, podemos clicar na opção "Start Building" (Começar a Criar). Caso não tenhamos uma conta, precisamos criar uma, podendo até conectar com uma conta do Google.

Configurando o ambiente para uso do Grok
Ao entrar, veremos uma tela onde podemos criar uma chave da API. Se já tivermos criado anteriormente, veremos o uso atual e créditos grátis para testar. Descendo a página, visualizamos alguns modelos open source disponíveis, como o GPT OSS de 20 bilhões de parâmetros, o DeepSeek R1, e outros. Esses modelos são indicados para diferentes finalidades, como Reasoning (raciocínio), uso de ferramentas, transcrição de fala para texto, entre outros.

Para este exemplo, utilizaremos o GPT OSS de 20 bilhões de parâmetros. Primeiro, clicamos em "Manage API Key" para criar uma chave da API. Damos um nome, como "aulas Python", e geramos a chave. É importante não compartilhar essa chave com ninguém. No Colab, criamos um novo bloco de código, mas não colamos a chave diretamente no código para evitar problemas de segurança. Em vez disso, adicionamos um novo Secret no Colab, chamando-o de "Grok API Key", e colamos a chave lá.

Instalando e utilizando a biblioteca Grok no Colab
Dentro do Grok, temos várias opções, como acessar o Playground para testar os modelos. Podemos escolher o modelo desejado, como o GPT OSS de 20 bilhões, e testar com perguntas, observando a rapidez das respostas. O modelo de Reasoning é rápido, processando 1103 tokens por segundo.

Para usar o Grok no Colab, precisamos instalar a biblioteca. Como o Colab é uma ferramenta do Google, já possui bibliotecas do Google instaladas, mas para bibliotecas externas, precisamos instalá-las manualmente. Utilizamos o comando !pip install -q groq para instalar o Grok. O -q é opcional e serve para suprimir mensagens detalhadas durante a instalação.

!pip install -q groq
COPIAR CÓDIGO
Depois, conectamos a chave da API da mesma forma que fizemos com a do Gemini. No ambiente do Colab, definimos a variável Grok API Key com o valor do Secret que criamos. Assim, podemos utilizar o Grok de forma segura e eficiente em nossos projetos.

os.environ["GROQ_API_KEY"] = userdata.get('GROQ_API_KEY')
COPIAR CÓDIGO
Executando consultas com o modelo GPT-OSS
Ao salvar o que estávamos fazendo, pegamos aquele número alfanumérico gigantesco, que estava escondido, mas conseguimos ver. Esse método coloca o alfanumérico dentro do nosso ambiente, em uma variável chamada Grok API Key. Com isso, estamos prontos para rodar o que quisermos. O código que copiamos está importando o Grok com from groq import Groq. Em seguida, fazemos client.chat.completions.create. Não é necessário decorar isso, pois é um padrão desse modelo e de vários outros, como os da OpenAI. Podemos copiar isso sempre que precisarmos.

from groq import Groq

client = Groq()

completion = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "user",
            "content": "O que é IA?"
        }
    ],
    temperature=1,
    max_completion_tokens=8192,
    top_p=1,
    reasoning_effort="medium",
    stream=True,
    stop=None,
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
COPIAR CÓDIGO
O model que vamos usar é o OpenAI do chat GPT, gpt-oss-20b, que possui 20 bilhões de parâmetros. Dentro dele, temos uma lista de mensagens, indicada pelos colchetes, chamada messages. A primeira mensagem passa o role, o papel do usuário, que pergunta "O que é IA?". O assistente responde que "IA é um ramo da ciência". Podemos limpar a conversa clicando em "clear", e veremos que há apenas um item dentro de messages. Temos a nossa pergunta, a resposta do gpt-oss-20b através do Grok, e uma possível nova pergunta que podemos fazer dentro dessa janela de chat.

Ajustando parâmetros do modelo para diferentes resultados
Podemos deixar apenas uma mensagem, com o role como user, e a pergunta pode ser qualquer outra, como "De que é feito o sol?". Passamos vários parâmetros para o modelo, um deles é a temperatura. Esse conceito define o quão criativo o modelo será, variando geralmente de 0 a 2, dependendo do modelo. No Gemini, varia de 0 a 1, enquanto no OpenAI, no chat GPT, varia de 0 a 2. O valor 0 significa o menos criativo possível, e o valor 2, o mais criativo.

Para explicar, podemos abrir uma janela do chat GPT e fazer algumas perguntas. Por exemplo, podemos jogar um jogo onde damos uma frase incompleta e pedimos as cinco principais possibilidades de palavras para continuar a frase, com a porcentagem de probabilidade. Ao enviar "Eu gosto de comer", ele pode responder com "pizza 28%", "chocolate 22%", "carne 15%", "frutas 12%" e "bolo 9%". Modelos de linguagem, como o Gemini e o chat GPT, funcionam tentando prever o próximo token, que é uma subpalavra. Por exemplo, a palavra "infeliz" pode ser dividida em dois tokens: "in" e "feliz". O token "in" pode ser usado em outras palavras, como "indivisível" e "incompreensível".

Quando treinamos esses modelos, é mais fácil passar as palavras de forma separada, pois os computadores não entendem palavras, apenas números. Suponhamos que o token "in" corresponda ao número 5 e "feliz" ao número 5734. O mesmo token "in" pode ser reutilizado em outras palavras. Isso é o que o modelo está prevendo: o próximo token.

Explorando a temperatura e outros parâmetros
Voltando à temperatura, quando colocamos um valor próximo de zero, o modelo será menos criativo e escolherá quase sempre as primeiras opções. Com uma temperatura mais alta, próxima de 1,5, ele variará mais, escolhendo diferentes opções. Isso é útil para escrever textos, onde podemos querer mais variação. Para casos que exigem precisão, como escrever código, usamos temperaturas mais baixas, próximas de zero.

O Max Completion Tokens define o número máximo de tokens. O TopP não é necessário. O Reasoning Effort define o esforço de raciocínio do modelo, podendo ser baixo, médio ou alto. Podemos deixar no médio ou apagar. O Stream faz o processamento em tempo real. Para cada pedaço na variável Completion, que recebemos do Grok, ele imprime a resposta.

Ao rodar o código, vemos que ele é extremamente rápido. Ele se comunica com os servidores do Grok, onde o modelo GPT-OSS de 20B está hospedado, processa a pergunta e retorna a resposta rapidamente. O Grok permite que usemos créditos para experimentar, mas eventualmente será necessário inserir um cartão de crédito para cobranças.

Podemos usar um modelo open source como o Gemini ou o Grok, mudando apenas algumas configurações. Na próxima aula, continuaremos explorando a linguagem Python.

@@07
Para saber mais: operador de resto em python

Como Funciona o Operador de Resto
O operador de resto, representado pelo símbolo %, é usado para obter o valor que sobra após a divisão inteira de dois números. Em Python, quando dividimos um número a por outro b, o resultado da operação a % b é o resto dessa divisão. Essa funcionalidade é fundamental para determinar, por exemplo, se um número é par ou ímpar ou para restringir valores dentro de um intervalo específico.

Quando um número é divisível exatamente por outro, o resto será zero. Caso contrário, o resultado será um número menor que o divisor. Essa simples verificação pode ser usada em estruturas condicionais para aplicar comportamentos diferentes dependendo do valor do resto.

Exemplos e Aplicações Práticas
Considere o seguinte exemplo, onde decidimos imprimir apenas os números pares de uma sequência:

for n in range(11):
    if n % 2 == 0:
        print(n)  # Imprime números pares: 0, 2, 4, 6, 8, 10
COPIAR CÓDIGO
Nesse caso, para cada valor de n, o operador % calcula o resto da divisão de n por 2. Se o resultado for zero, sabemos que n é par e procedemos com a impressão. Esse padrão de uso pode ser adaptado para outros tipos de verificação, como para identificar múltiplos de um determinado número ou realizar operações cíclicas em algoritmos.

Variações e Cenários de Uso
O operador de resto possui algumas particularidades que o tornam versátil:

Verificação de Condições: Além de identificar números pares, pode ser usado para detectar condições específicas. Por exemplo, n % 3 == 0 verifica se n é múltiplo de 3. Essa característica é útil em contagens recorrentes ou para modular comportamentos em laços de repetição.
Cálculos Cíclicos: Em algoritmos que necessitam de ciclos, como rotação de elementos em uma lista ou acesso circular a índices, o operador de resto garante que os valores se mantenham dentro de um certo intervalo. Por exemplo:
lista = ['a', 'b', 'c', 'd']
for i in range(10):
    print(lista[i % len(lista)])  # Acessa sempre um índice válido na lista
COPIAR CÓDIGO
Manipulação de Sequências: Em alguns casos, é possível implementar funções que dependem da periodicidade dos números, permitindo comportamentos que se repetem de forma regular a cada iteração.
Considerações Importantes
Embora o operador de resto seja simples, é crucial entender seu comportamento com números negativos. Em Python, a operação % garante que o sinal do divisor seja respeitado e que o resultado tenha o mesmo sinal do divisor, o que pode divergir de outras linguagens. Essa particularidade deve ser levada em conta ao desenvolver algoritmos que precisam de consistência em diferentes plataformas ou ambientes.

O entendimento do operador % é essencial para aprimorar o controle de fluxo e a lógica dos seus programas, seja para filtragens, cálculos cíclicos ou outras técnicas que exigem manipulação precisa dos números. Ao dominar esse operador, você amplia o leque de soluções criativas e eficientes na programação.

@@08
Padronizando descrições de produtos

A TRATOTECH, uma plataforma de classificados focada em produtos tecnológicos, conecta compradores e vendedores de eletrônicos. A equipe de desenvolvimento que você faz parte está enfrentando um problema com a padronização das descrições dos produtos. As descrições são enviadas pelos vendedores em formatos variados, com uso inconsistente de maiúsculas e minúsculas, além de espaços desnecessários. Para melhorar a experiência do usuário e a busca por produtos, a equipe decidiu criar uma função que padronize essas descrições, removendo espaços extras e uniformizando o uso de minúsculas.
Qual das alternativas abaixo descreve a melhor abordagem para implementar essa função de padronização?

Desenvolver uma função que apenas aplique o método upper() para converter toda a descrição em maiúsculas, sem remover espaços extras, e que também ignore a necessidade de ajustar a formatação dos espaços internos, mantendo o texto como está.
 
Incorreta, pois embora uniformize o uso de maiúsculas, não resolve o problema dos espaços desnecessários, o que pode prejudicar a legibilidade e a busca por produtos, além de não atender ao objetivo de padronização completa.
Alternativa incorreta
Criar uma função em Python que receba a descrição do produto, utilize strip() para remover espaços no início e no final, lower() para uniformizar o uso de minúsculas, e replace() para substituir múltiplos espaços por um único espaço.
 
Correta, pois essa abordagem utiliza métodos adequados para remover espaços desnecessários e uniformizar o uso de maiúsculas e minúsculas, garantindo que todas as descrições sigam um padrão consistente.
Alternativa incorreta
Implementar uma função que use strip() para remover espaços no início e no final, mas mantenha o uso original de maiúsculas e minúsculas, sem alterações, e que também não se preocupe em ajustar os espaços internos, deixando-os como foram inseridos originalmente.
 
Alternativa incorreta
Criar uma função que substitua todos os espaços por hífens e converta a descrição para minúsculas usando lower(), além de ignorar a necessidade de manter a legibilidade original das descrições, alterando completamente o formato do texto.
 
Incorreta, pois substituir espaços por hífens altera o formato original das descrições, o que pode confundir as pessoas usuárias e não atende ao objetivo de padronização desejado, além de comprometer a clareza e a busca por produtos.

@@09
Faça como eu fiz: textos, loops e APIs

Nesta aula, aprendemos a manipular listas, dicionários, laços de repetição e funções para corrigir textos e integrar chamadas de API. Agora é a sua chance de revisar e exercitar os conteúdos vistos nesta aula, se ainda não colocou em prática. Para isso:
Configure a estrutura de repetição for para iterar sobre listas e dicionários;
Imprima cada item de uma lista individualmente;
Utilize o operador += para atualizar índices em loops;
Percorra dicionários exibindo chaves e pares chave-valor;
Gere sequências numéricas com a função range;
Valide números pares usando a operação de resto (%);
Crie funções para processar strings com strip, upper e replace;
Aplique o método split para eliminar espaços extras;
Reúna as palavras com o método join para formatar textos;
Implemente funções que retornem valores processados;
Integre a correção de nomes com funções personalizadas;
Padronize diferentes textos usando a função criada;
Utilize random.choice para alocar elementos de forma aleatória;
Monte dicionários contendo nomes corrigidos e dados associados;
Crie uma função que percorra uma lista de e-mails com for;
Faça chamadas de API para resumir o conteúdo de e-mails;
Empregue f-strings para formatar os resumos dinamicamente;
Utilize enumerate para numerar os e-mails na iteração;
Teste a função e verifique a saída dos resumos com separadores.
Para acessar o guia detalhado, consulte as transcrições da aula.

@@10
O que aprendemos?

Nesta aula, aprendemos:
A utilizar o loop for e a função range() em Python para iterar sobre elementos de estruturas de dados.
A criar funções em Python com parâmetros e a importância de encapsular algoritmos para a reutilização.
A manipular strings utilizando os métodos split(), join(), e upper() para formatação e limpeza de texto.
A simplificar a definição de funções, retornando valores com return e utilizando o módulo random para operações aleatórias.
A usar a função enumerate() em loops for para obter índices e elementos de listas.
A explorar o uso de modelos de linguagem de código aberto e a implementação de Groq no Google Colab.
A realizar inferências em modelos de linguagem configurando parâmetros como temperature e max_completion_tokens.
A gerenciar a segurança em chamadas de API usando variáveis de ambiente no Google Colab.

#24/01/2026

@04-Leitura e escrita

@@01
Projeto da aula anterior

Caso queira revisar o código até aqui ou começar a partir desse ponto, disponibilizamos os códigos realizados na aula anterior, para visualizar clique neste link.

https://colab.research.google.com/drive/1jcP3Q4OVr-ZCfpXhnuwNrK1PVV_xxN4k#scrollTo=Xa1xNOntzmpb

@@02
Explorando a leitura e escrita de arquivos

Continuando nosso estudo de Python, hoje vamos explorar uma nova habilidade: ler e escrever em arquivos usando Python. Podemos trabalhar com arquivos de texto, como .txt, ou arquivos de tabelas, como .csv.

Vamos criar um novo bloco de código. No contexto do nosso desafio anterior, o resumidor de e-mails, já desenvolvemos a função e a executamos até o final, mas não salvamos os dados em nenhum lugar, o que resultou na perda dessas informações. Suponhamos que desejamos salvar esses dados em uma variável, como uma lista, e posteriormente em um arquivo .txt. Vamos abordar isso passo a passo.

Salvando resumos de e-mails em uma lista
Atualmente, nossa função apenas exibe na tela o número do e-mail e a resposta do resumo. Vamos começar com a exibição do resumo do e-mail:

print(f"Resumo do e-mail {numero + 1}: {resposta.text}")
COPIAR CÓDIGO
Além de exibir, agora ela também irá salvar essas informações em uma lista que criaremos. Vamos chamá-la de lista_de_resumos e iniciá-la como uma lista vazia, representada por colchetes [].

lista_de_resumos = []
COPIAR CÓDIGO
Podemos utilizar métodos que aprendemos para manipular listas. Em vez de apenas imprimir o e-mail e a resposta, vamos adicionar essas informações à lista_de_resumos usando o método append.

lista_de_resumos.append(f"E-mail {numero + 1}: {resposta.text}")
COPIAR CÓDIGO
Retornando a lista de resumos
Não precisamos imprimir o separador, pois ele era apenas para visualização. Cada linha da lista representará um e-mail.

Após salvar as informações na lista, precisamos retornar essa lista ao final da função. Assim, ao sair do laço for, utilizaremos return para retornar a variável lista_de_resumos já populada com todos os e-mails.

return lista_de_resumos
COPIAR CÓDIGO
Ao executar o código, podemos encontrar um erro: "models has no attribute, generate content". Isso ocorre porque, em uma aula anterior, chamamos o grok de client, que era o mesmo nome do client do GMI que estávamos usando. Agora, o sistema está confundindo os dois. Precisamos rodar novamente a célula inicial para definir corretamente o client como GMI.client.

Corrigindo o nome do cliente para evitar confusões
Podemos alterar o nome para client_groq em todos os lugares necessários para evitar confusões.

client_groq = Groq()
COPIAR CÓDIGO
Após salvar as alterações, o código rodará rapidamente como antes.

Ao final da execução, verificamos que não salvamos o retorno da função em lugar algum. Precisamos criar uma nova variável, lista_resumos, para armazenar o retorno da função.

lista_resumos = resumidor_de_emails(email_bodies)
COPIAR CÓDIGO
Armazenando e imprimindo resumos de e-mails
Agora, ao executar novamente, a variável lista_resumos conterá os 20 e-mails resumidos.

Com a execução concluída, podemos imprimir o conteúdo de lista_resumos, que conterá uma lista com os e-mails resumidos, do e-mail 1 ao e-mail 20.

Agora, vamos escrever cada um desses itens em um arquivo .txt, que pode ser enviado ou lido posteriormente. Para salvar arquivos em Python, utilizamos a palavra-chave dupla with open(). Essa função recebe alguns parâmetros e argumentos que configuraremos a seguir.

Escrevendo resumos em um arquivo .txt
with open("lista-de-resumos.txt", "w", encoding="utf-8") as arquivo:
COPIAR CÓDIGO
Aqui, o primeiro elemento será o nome do nosso arquivo, especificamente um arquivo .txt. Podemos chamá-lo, por exemplo, de lista-resumos.txt. O segundo elemento será o modo como queremos que ele escreva nesse arquivo .txt. Existem duas opções: o modo w e o modo a. O modo w é uma abreviação de write (escrever). Ao utilizar with open, ele tentará abrir o arquivo lista-resumos.txt. Se o arquivo não existir, ele será criado automaticamente e começará a escrever os dados nele. No entanto, se o arquivo já existir, há uma diferença. No modo w, ele apagará todo o conteúdo existente e começará do zero. Por exemplo, se tivermos um arquivo chamado lista-resumos.txt com 25 resumos e o abrirmos novamente usando o modo w, todo o conteúdo será apagado e sobrescrito.

Se utilizarmos o modo a, que é uma abreviação de append (acrescentar), ele continuará a partir da última linha escrita. A escolha entre os modos depende do caso de uso: se desejamos apagar e reescrever ou continuar escrevendo no final. No nosso caso, tanto faz, mas podemos usar o modo w por enquanto.

Configurando a codificação e escrevendo no arquivo
O terceiro elemento é o encoding, que já está definido como utf-8. Vamos mantê-lo assim. O utf-8 é um modo de codificação de texto na internet que lida bem com caracteres acentuados, como acento agudo, til, cedilha e circunflexo. Existem outras codificações que não lidam bem com esses caracteres, resultando em símbolos estranhos quando a codificação não está correta.

Agora, vamos dar um apelido ao nosso arquivo. Para isso, usamos a palavra-chave as, que significa "como" em inglês. Podemos chamá-lo de arquivo. Esse nome é uma variável temporária que existirá apenas durante a execução. Dentro desse contexto, decidiremos o que fazer. No nosso caso, queremos escrever no arquivo. Ao digitar um ponto, várias opções são sugeridas. Temos duas opções principais: write, que escreve uma linha de cada vez, ou writelines, que recebe uma lista e escreve tudo de uma vez. Se quisermos ter mais controle, podemos usar write, mas precisaremos de um for.

for resumo in lista_resumos:
    arquivo.write(resumo + "\n")
COPIAR CÓDIGO
O \n é um caractere de quebra de linha, muito usado em programação. Ele permite escrever um resumo, pular uma linha, e assim por diante. Vamos executar novamente. Agora, a lista de resumos está linha a linha, mas há um elemento extra, que não era necessário. Isso é apenas um detalhe do ordenamento interno, não relacionado aos nossos e-mails. No próximo vídeo, veremos como ler os arquivos. Primeiro, escrevemos; depois, aprenderemos a lê-los. Até breve.

@@03
Leitura de arquivos

Agora que já escrevemos um arquivo, vamos aprender a ler um arquivo. Pode ser até mesmo este exato arquivo, o lista-de-resumos.txt. Vamos criar mais um bloco de código para fazer a leitura. O processo é muito parecido, praticamente a mesma coisa. Por isso, vamos copiar o código do bloco anterior. A principal diferença é que, em vez de utilizarmos o w para escrever ou o a para adicionar ao final, vamos usar a letra r, que é de reads (ler, em inglês). O restante é idêntico.

Para começar, vamos abrir o arquivo lista-de-resumos.txt com os parâmetros r e encoding='utf-8'. Veja como fazemos isso:

with open("lista-de-resumos.txt", "r", encoding="utf-8") as arquivo:
COPIAR CÓDIGO
Percorrendo linhas do arquivo
Na linha with open, vamos abrir o arquivo lista-de-resumos.txt, que já existe no local, com os parâmetros r e encoding='utf-8'. Aqui, faremos um for, mas será um for diferente. Não será for resumo in lista_de_resumos, mas sim algo mais claro: para cada linha nesse arquivo. Antes, estávamos percorrendo os resumos da lista de resumos; agora, vamos percorrer as linhas do arquivo que abrimos.

    for linha in arquivo:
COPIAR CÓDIGO
O que faremos em vez de arquivo.write para escrever? Não precisamos, pois já temos um arquivo aberto. Vamos querer fazer algo com essa linha. Podemos, por exemplo, salvá-la em uma variável. Então, criaremos uma nova_lista_de_leitura, que será uma lista (abre e fecha colchetes). Para cada linha que lermos nesse arquivo, vamos adicionar (append) essa linha à nova_lista_de_leitura, tornando-a um novo elemento dessa variável.

nova_lista_de_leitura = []
with open("lista-de-resumos.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        nova_lista_de_leitura.append(linha)
COPIAR CÓDIGO
Explorando métodos de leitura
Vamos rodar o código para ver o que acontece. Rodamos e tudo certo. Conseguimos ler o arquivo linha por linha. Este é o primeiro modo de fazer essa leitura. É um dos modos. Lemos até o índice 20, pois o 21 era apenas um índice interno vazio, sem conteúdo. Conseguimos ler linha por linha o que havia no arquivo, que está separado por vírgulas. Está tudo certo. Esta é uma forma de fazer isso, apenas percorrendo o arquivo que acabamos de abrir.

Existem mais duas formas. Uma delas é usar o método read. Vamos pegar apenas a primeira linha, não as outras. Vamos abrir o arquivo e usar arquivo.read. Esta é uma das opções que temos. Se observarmos, temos a opção readline, read e readlines.

conteudo = ""
with open("lista-de-resumos.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
COPIAR CÓDIGO
Manipulando o conteúdo lido
Vamos pegar o ponto read e salvar em algum lugar. O conteúdo será armazenado em uma variável que inicialmente recebe um espaço em branco. Em seguida, salvamos tudo em conteúdo. Ao rodar o código e imprimir conteúdo, ele salva tudo de uma vez, incluindo os espaços e quebras de linha (\n). No exemplo anterior, também salvamos as quebras de linha. Se quisermos removê-las, podemos usar o método strip nas linhas. Os métodos que vimos nas aulas passadas sobre manipulação de strings e texto podem ser aplicados aqui. O método strip remove espaços e quebras de linha, e ao rodar o código, não há mais as quebras de linha, ficando apenas o elemento sem espaçamento. O arquivo é lido e populado dessa forma.

nova_lista_de_leitura = []
with open("lista-de-resumos.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        nova_lista_de_leitura.append(linha.strip())
COPIAR CÓDIGO
Comparando métodos de leitura
Neste caso, ele salva tudo de uma vez usando o ponto read. Vamos copiar essa linha e criar uma nova lista, por exemplo, nova_lista_de_leitura_2, que será uma lista. Ela receberá o conteúdo do arquivo usando readlines, que lê as linhas no plural. Ao rodar o código, o que temos dentro de nova_lista_de_leitura_2 é basicamente o mesmo que em nova_lista_de_leitura, com a diferença na escrita. Conseguimos separar em posições, como zero, um, dois, sem problema, mas ainda com todas as quebras de linha (\n). Não conseguimos controlar isso muito bem porque está lendo tudo de uma vez, ou seja, o arquivo inteiro lista_de_resumos.txt, e cada linha se torna uma posição na lista em Python. Não temos tanto controle, mas é possível usar. No entanto, ele vem com todas as quebras de linha e espaços adicionais.

nova_lista_de_leitura_2 = []
with open("lista-de-resumos.txt", "r", encoding="utf-8") as arquivo:
    nova_lista_de_leitura_2 = arquivo.readlines()
COPIAR CÓDIGO
Concluindo a leitura de arquivos
Utilizando o primeiro modo, com um for indo linha a linha, conseguimos usar o método strip para remover elementos indesejados. Isso é a leitura e escrita de arquivos em Python. Na próxima aula, começaremos a explorar uma área relacionada à ciência de dados, o famoso data science. Vamos conhecer o framework mais famoso quando falamos sobre lidar com dados e inteligência artificial. Ele é amplamente utilizado e vocês vão adorar conhecê-lo, pois é muito interessante. Nos vemos em breve!

@@04
Preparando o ambiente

Na próxima aula, faremos um teste com um arquivo CSV. Você pode criar o seu próprio ou, se preferir, usar o modelo que disponibilizaremos como exemplo abaixo:
Arquivo .csv
Bons estudos!

https://cdn3.gnarususercontent.com.br/4790-python/meu_csv.csv

@@05
Pandas e sua importância

Nesta aula, vamos explorar um dos frameworks fundamentais para a ciência de dados moderna: o pandas. Este framework é frequentemente associado a um animal fofo devido ao seu nome. Talvez já tenhamos ouvido falar dele, mas, independentemente disso, é uma ferramenta muito interessante para manipular dados.

Como estamos utilizando o Google Colab, não precisamos instalar o pandas, pois ele já vem pré-instalado. A única ação necessária é importá-lo. Assim como fizemos anteriormente com outros pacotes, como os e GNI, vamos importar o pandas.

Importando e configurando o pandas
Primeiro, vamos adicionar um texto: "Manipulando dados com pandas". Em seguida, faremos a importação. É um processo simples: basta usar import pandas. No entanto, é comum na comunidade dar um apelido ao pandas. Assim como demos apelidos a outros elementos, usamos a palavra-chave as para isso. O padrão é chamá-lo de pd, então a importação fica:

import pandas as pd
COPIAR CÓDIGO
Isso será muito útil para lidar com dados em tabelas, como as do Excel, Google Sheets ou arquivos CSV, que são amplamente utilizados no mundo dos dados e da tecnologia.

Explorando o formato CSV
Se não estivermos familiarizados com o formato CSV, vamos explorá-lo agora. Vamos abrir o Gemini e solicitar a geração de uma tabela em formato CSV, contendo nomes de 10 pessoas na primeira coluna e suas médias de 0 a 10 na segunda coluna. O CSV, que significa comma separated values (valores separados por vírgula), é um formato de arquivo onde os valores são separados por vírgulas. Por exemplo, temos o título "nome, média", onde "nome" é a primeira coluna e "média" é a segunda. Os dados seguem o mesmo padrão: "Ana, 7.5", "Carlos, 8.2", e assim por diante.

Este formato de arquivo pode ser separado por outros caracteres, como ponto e vírgula, dependendo da escolha do separador. Vamos salvar este arquivo no computador, seja no Windows ou Mac, utilizando um editor de texto. Ao salvar, devemos escolher "Salvar como" e nomear o arquivo como meu_arquivo.csv. É importante selecionar "todos os arquivos" ao invés de "documento de texto" para garantir que o arquivo seja salvo com a extensão .csv e não .txt.

Fazendo upload e lendo arquivos CSV no Colab
Para ler arquivos CSV, primeiro precisamos fazer o upload do arquivo no Colab. Abrimos a pasta na lateral, clicamos em "fazer upload" e selecionamos o arquivo meu.csv.csv. Após o upload, verificamos se o arquivo foi salvo corretamente. Podemos copiar o caminho do arquivo clicando nos três pontos ao lado do nome e selecionando "copiar caminho".

Criamos um novo bloco de código e utilizamos o caminho copiado, que será algo como:

"/content/meu_csv.csv"
COPIAR CÓDIGO
Se o arquivo tiver outro nome, o caminho refletirá isso. Para ler o arquivo, utilizamos a biblioteca pandas, referenciada como pd. Usamos o método pd.read_csv() para ler o arquivo CSV, passando o caminho completo como parâmetro:

df = pd.read_csv("/content/meu_csv.csv")
COPIAR CÓDIGO
Visualizando e manipulando dados com pandas
Salvamos o resultado em uma variável, geralmente chamada de df, que representa um DataFrame. Executamos a linha de código e, para visualizar o conteúdo do CSV, imprimimos o df:

df
COPIAR CÓDIGO
O pandas interpreta o CSV, separando-o por vírgulas e identificando as colunas, como nomes e médias. O pandas, especialmente o método read_csv, permite trabalhar com tabelas de forma semelhante ao Excel, mas usando Python, sendo muito útil na ciência de dados.

Além disso, podemos usar o método df.head() para visualizar os primeiros cinco elementos do DataFrame:

df.head()
COPIAR CÓDIGO
Se quisermos ver mais elementos, podemos passar um número como argumento, por exemplo, df.head(10) para ver os dez primeiros. O método df.tail() mostra os últimos cinco elementos, ou mais, se especificarmos um número. Isso nos dá uma ideia do conteúdo do arquivo CSV.

Desafio do curso: criando e manipulando arquivos
Agora, estamos prontos para um desafio do curso. O desafio consiste em cinco etapas. A primeira etapa é criar um arquivo TXT a partir de uma lista de perguntas em Python. Vamos criar uma lista de perguntas, por exemplo, sobre astronomia, com cinco perguntas. A lista pode ser personalizada com perguntas de qualquer tema de interesse:

lista_de_perguntas = [
    "De que é feito o Sol?",
    "De que é feito o planeta Saturno?",
    "Qual é a galáxia mais antiga já encontrada?",
    "Qual é a maior estrela já encontrada?",
    "Qual é a estrela mais próxima do Sol?"
]
COPIAR CÓDIGO
Após definir a lista, criamos um arquivo TXT com essas perguntas. Em seguida, lemos o arquivo TXT e salvamos as perguntas em uma lista Python, revertendo o processo inicial. Na terceira etapa, obtemos respostas de um LLM para cada pergunta, sugerindo respostas sucintas. Salvamos as perguntas e respostas em um arquivo CSV, separado por vírgulas.

Para criar o CSV, podemos usar o método with open ou outras abordagens, como manipulação de strings. Após salvar o CSV, lemos o arquivo usando a biblioteca pandas e o método read_csv, exibindo o conteúdo em formato de tabela, com colunas de perguntas e respostas.

Este desafio não é extremamente complexo, mas envolve vários passos. Esperamos que consigam resolvê-lo com o conhecimento adquirido até agora. Retornaremos em breve com a solução.

@@06
Desafio e a etapa 1

Conseguimos resolver o desafio proposto? Imagino que tenhamos precisado realizar algumas pesquisas online, especialmente na parte de criação de um arquivo CSV, que corresponde ao ponto 4, nossa etapa número 4. Vamos agora seguir o passo a passo juntos.

Na primeira parte da etapa 1, precisávamos gerar uma lista de 10 perguntas sobre um tema de nosso interesse. Ainda na etapa 1, deveríamos criar um arquivo txt a partir dessa lista de perguntas. Isso é algo simples, pois acabamos de aprender a lidar com esses arquivos. Recapitulando, utilizaremos o with open para abrir o arquivo. Passamos três parâmetros para o with open: o nome do arquivo txt que vamos salvar, como perguntas.txt, o modo de salvamento do arquivo, que será "w", e a codificação, que é UTF-8. Podemos dar um nome ao arquivo, como as arquivo, por exemplo.

with open("perguntas.txt", "w", encoding="utf-8") as arquivo:
COPIAR CÓDIGO
Em seguida, salvamos os itens da lista, escrevendo-os um a um. Para cada pergunta na lista de perguntas, utilizamos o método write para escrever a pergunta no arquivo, adicionando uma quebra de linha após cada uma.

for pergunta in lista_de_perguntas:
    arquivo.write(pergunta + "\n")
COPIAR CÓDIGO
Assim, conseguimos salvar nosso novo arquivo, concluindo a etapa 1. Podemos verificar nos arquivos à esquerda se o perguntas.txt está salvo corretamente.

Lendo perguntas e preparando respostas
Na etapa 2, precisamos ler as perguntas do arquivo txt e salvá-las em uma lista Python. Este é o processo inverso do que fizemos anteriormente. Utilizamos novamente o with open para abrir o arquivo perguntas.txt no modo de leitura "r", com a codificação UTF-8. Criamos uma lista vazia chamada lista_desafio.

lista_desafio = []
with open("perguntas.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        lista_desafio.append(linha.strip())
COPIAR CÓDIGO
Com isso, resolvemos a etapa 2, e podemos imprimir a lista_desafio para verificar seu conteúdo.

print(lista_desafio)
COPIAR CÓDIGO
Na etapa 3, obtemos as respostas de um LLM para cada pergunta. Queremos que a resposta obtida corresponda à pergunta na mesma posição. Podemos criar uma nova lista em Python para as respostas, garantindo que as posições correspondam entre as listas de perguntas e respostas. Outra opção é criar um dicionário, onde cada pergunta é uma chave e a resposta correspondente é o valor. Optamos por utilizar uma lista de dicionários em Python, pois já vimos essa abordagem anteriormente.

Criamos a lista_de_dicionarios_de_respostas, que começa vazia.

lista_de_dicionarios_de_respostas = []
COPIAR CÓDIGO
Percorremos as perguntas e chamamos o modelo Gemini para obter uma resposta, que será armazenada em um dicionário. Cada elemento da lista será um dicionário com a pergunta e a resposta. Para adicionar um item à lista, utilizamos append.

for pergunta in lista_desafio:
    resposta = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Gere uma resposta muito sucinta para a pergunta: {pergunta}"
    )
    lista_de_dicionarios_de_respostas.append({"pergunta": pergunta, "resposta": resposta.text})
COPIAR CÓDIGO
Com isso, concluímos as etapas do desafio.

Gerando e salvando respostas em CSV
Indo passo a passo novamente, utilizamos o for para iterar sobre nossa lista, que contém cinco elementos, ou dez, dependendo do caso. Pegamos o primeiro desses elementos, geramos a resposta e pedimos para o Gemini gerar uma resposta bastante sucinta para essa pergunta. Ele gera a resposta, que é salva na variável resposta. Em seguida, geramos um dicionário com a pergunta e a resposta, utilizando o texto da resposta em resposta.text. Adicionamos esse dicionário à nossa lista de dicionários de respostas. Quando executamos, não há exibição imediata, pois não incluímos um print. Se desejarmos visualizar, podemos adicionar um print ou simplesmente exibir o conteúdo da variável lista de dicionários de respostas.

Por exemplo, a pergunta zero, "De que é feito o Sol?", tem como resposta "Principalmente hidrogênio e hélio". A pergunta da posição 1, "De que é feito o planeta Saturno?", também tem como resposta "Hidrogênio e hélio". A pergunta da posição 2, "Qual a galáxia mais antiga já encontrada?", tem como resposta "HD1". A pergunta da posição 3, "Qual a maior estrela já encontrada?", tem como resposta "UY Scuti". E a última pergunta, da posição 4, "Qual é a estrela mais próxima do Sol?", tem como resposta "Próxima Centauri". Com isso, nossa etapa 3 está concluída com sucesso.

Na etapa 4, vamos salvar os resultados em um novo arquivo .csv. Existem alguns modos de fazer isso. Podemos fazer manualmente, utilizando o modo de escrita, lembrando que um arquivo .csv é uma lista separada por vírgulas. Por exemplo, um arquivo .csv pode ter um cabeçalho com os títulos dos campos e, em seguida, os dados separados por vírgulas. Podemos fazer isso manualmente, mas também podemos utilizar a biblioteca pandas, que possui um método específico para isso.

No primeiro modo, escrevemos um arquivo utilizando with open, chamando-o de respostas1.csv. No modo de escrita, completamos com o encoding como utf-8.

with open("respostas1.csv", "w", encoding="utf-8") as arquivo:
    arquivo.write("pergunta,resposta\n")
    for pergunta_dict in lista_de_dicionarios_de_respostas:
        arquivo.write(f"{pergunta_dict['pergunta']},{pergunta_dict['resposta']}\n")
COPIAR CÓDIGO
Se houver um erro com aspas duplas, podemos usar aspas simples para evitar problemas. Recapitulando, abrimos o arquivo no modo de escrita, escrevemos o cabeçalho manualmente e iteramos sobre a lista de dicionários, escrevendo cada linha no arquivo. Ao rodar, verificamos que o arquivo respostas1.csv está correto.

Utilizando pandas para manipulação de dados
Agora, vamos para o outro modo, utilizando pandas. Criamos um DataFrame chamado df_perguntas_e_respostas a partir da lista de dicionários de respostas. O pandas já sabe separar dicionários em DataFrames.

df_perguntas_e_respostas = pd.DataFrame(lista_de_dicionarios_de_respostas)
COPIAR CÓDIGO
Para salvar em um arquivo .csv, utilizamos o método to_csv, passando o nome do arquivo, se queremos incluir o índice (neste caso, False), e o encoding como utf-8.

df_perguntas_e_respostas.to_csv("resposta2.csv", index=False, encoding="utf-8")
COPIAR CÓDIGO
Ao rodar, o arquivo respostas2.csv é salvo corretamente.

Por fim, na etapa 5, vamos ler o arquivo .csv que criamos utilizando pandas. Criamos um novo DataFrame chamado novo_df utilizando pd.read_csv, passando o nome do arquivo.

novo_df = pd.read_csv("resposta2.csv")
COPIAR CÓDIGO
Podemos imprimir o novo_df inteiro ou apenas o head.

novo_df.head()
COPIAR CÓDIGO
Essas foram as cinco etapas do nosso desafio, utilizando tanto código Python manual quanto o framework de dados pandas. Espero que tenham gostado do desafio. Em breve, continuaremos explorando o mundo do Python.

@@07
Gerenciamento de arquivos de transações no Bytebank

O Bytebank, um banco digital que oferece serviços bancários online, está desenvolvendo um sistema para gerenciar transações financeiras de seus clientes. A equipe de desenvolvimento, da qual você faz parte, precisa garantir que todas as transações do dia sejam registradas em um arquivo de texto para auditoria e análise futura. No entanto, é crucial que, ao final de cada dia, o arquivo seja sobrescrito com as novas transações para evitar acúmulo de dados desnecessários.
Qual abordagem a equipe deve adotar para implementar um sistema que grava as transações diárias em um arquivo de texto, garantindo que o arquivo seja sobrescrito a cada dia?

Utilizar a função open em Python com o modo 'a' (append), que adiciona as novas transações ao final do arquivo existente, preservando o histórico de transações anteriores, e assim mantém um registro contínuo de todas as operações realizadas ao longo do tempo, o que pode ser útil para auditorias detalhadas.
 
Incorreta, pois o modo 'a' (append) adiciona dados ao final do arquivo sem apagar o conteúdo anterior, o que resultaria no acúmulo de dados, contrariando o requisito de sobrescrever o arquivo diariamente, embora possa ser vantajoso para manter um histórico completo.
Alternativa incorreta
Configurar o sistema para criar um novo arquivo a cada dia com um nome diferente, incluindo a data no nome do arquivo, para manter um registro separado de transações diárias, o que facilita a organização e a busca por transações específicas em datas distintas, além de permitir uma análise temporal detalhada.
 
Incorreta, pois essa abordagem cria novos arquivos diariamente em vez de sobrescrever o mesmo arquivo, o que não atende ao requisito de evitar o acúmulo de dados desnecessários em um único arquivo, embora ofereça uma maneira estruturada de arquivar dados.
Alternativa incorreta
Utilizar a função open em Python com o modo 'w' (write), que apaga o conteúdo anterior do arquivo e grava as novas transações do dia, garantindo que o arquivo seja atualizado diariamente sem acúmulo de dados antigos.
 
Correta, pois o modo 'w' na função open em Python abre o arquivo para escrita, apagando qualquer conteúdo existente e permitindo que as novas transações sejam registradas, atendendo ao requisito de sobrescrever o arquivo diariamente.
Alternativa incorreta
Utilizar a função open em Python com o modo 'r+' (read and write), que permite ler e escrever no arquivo sem apagar o conteúdo existente, mantendo um registro contínuo de todas as transações, o que pode ser vantajoso para revisões históricas e análises de longo prazo.

@@08
Para saber mais: salvar arquivos csv

Abordagem manual com open()
Na criação de um arquivo CSV utilizando apenas funções nativas do Python, como o open(), o processo é realizado linha a linha. Essa técnica consiste em escrever primeiramente o cabeçalho (com os nomes das colunas) e, em seguida, cada registro formatado com vírgulas para separar os campos. Essa abordagem funciona bem para arquivos simples, pois o CSV, em essência, é um arquivo de texto estruturado.

Uma vantagem desse método é a liberdade de definir exatamente como cada linha será formatada, o que pode ser útil em cenários onde se deseja um controle específico sobre a saída. Por outro lado, a responsabilidade pelo tratamento de casos especiais – como campos que contenham vírgulas, quebras de linha ou a necessidade de envolver valores entre aspas – recai inteiramente sobre o desenvolvedor, o que pode levar a erros inesperados ou complicações se o arquivo possuir dados mais complexos.

Utilizando o Pandas para gerar CSV
A biblioteca Pandas oferece uma abordagem mais prática e robusta para a exportação de data frames para o formato CSV. Ao converter uma lista de dicionários para um data frame, por exemplo, é possível utilizar o método to_csv(), que gerencia automaticamente as questões de formatação e escape de caracteres especiais.

Essa alternativa possui a vantagem de ser altamente confiável em projetos de ciência de dados, já que o Pandas cuida dos detalhes técnicos e permite, com poucos parâmetros, incluir ou excluir o índice, definir o encoding e outros ajustes. Dessa forma, o risco de inconsistências no arquivo gerado é bem menor. Por outro lado, esse método exige a dependência da biblioteca Pandas, o que pode aumentar o tamanho da aplicação ou limitar seu uso em ambientes onde a instalação de pacotes externos não é viável.

Considerações para a escolha de abordagem
A decisão entre utilizar o método manual ou recorrer ao Pandas depende do contexto do projeto:

Em situações em que o volume de dados é pequeno e os requisitos de formatação são simples, a abordagem manual pode ser suficiente e leve.
Para projetos que envolvem manipulação consistente de dados complexos e integração com análises posteriores, utilizar o Pandas se torna uma opção mais segura, legível e escalável.
Por fim, compreender os pontos fortes e limitações de cada estratégia permite que a escolha seja feita de forma adequada ao objetivo final, garantindo tanto a eficiência quanto a manutenibilidade do código.

@@09
Faça como eu fiz: arquivos e pandas

Nesta aula, foram abordados conceitos de leitura e escrita de arquivos em Python e a manipulação de dados com o Pandas.
Agora é a sua chance de praticar os conteúdos vistos. Para isso:

Crie uma lista vazia para armazenar os resumos dos e-mails.
Utilize a função append para inserir cada resumo formatado via fString na lista.
Configure a função para retornar a lista populada após um loop de iterações.
Implemente o with open com modo 'W' para criar e sobrescrever um arquivo .txt com os resumos.
Use write ou write lines com '\n' para separar cada entrada no arquivo.
Abra o arquivo em modo 'R' e leia suas linhas, salvando em uma nova lista com strip para remover quebras de linha.
Explore os métodos read, readline e readlines para diferentes formas de leitura em Python.
Importe o Pandas utilizando o alias pd para manipulação de dados.
Construa um arquivo .csv manualmente, escrevendo o cabeçalho e as linhas com as chaves de cada dicionário.
Crie um DataFrame com a lista de dicionários e utilize o método to_csv para salvar o CSV com encoding UTF-8.
Desenvolva um desafio para gerar um arquivo .txt a partir de uma lista de perguntas e depois lê-lo para criar uma lista.
Integre uma chamada ao LLM para obter respostas sucintas, associando cada pergunta com sua resposta e salvando o resultado final em um novo arquivo .csv.
Para acessar o guia detalhado, consulte as transcrições da aula.

@@10
O que aprendemos?

Nesta aula, aprendemos:
A manipular arquivos em Python usando with open() para gerenciar contexto automaticamente.
A diferença entre os modos w (write) e a (append) para escrita de arquivos.
A utilizar encoding=utf-8 para garantir compatibilidade com caracteres especiais.
A ler arquivos em modo r e manipular conteúdo com read(), readline(), e readlines().
A introduzir o Pandas para manipulação de dados tabulares e a importância do DataFrame.
A ler arquivos CSV com Pandas usando read_csv e visualizar dados com .head() e .tail().
A criar e manipular arquivos TXT e CSV a partir de listas e dicionários em Python.
A exportar DataFrames para arquivos CSV com Pandas usando to_csv.

#25/01/2026

@04-Conhecendo a Pandas

@@01
Projeto da aula anterior

Caso queira revisar o código até aqui ou começar a partir desse ponto, disponibilizamos os códigos realizados na aula anterior, para visualizar clique neste link.

https://colab.research.google.com/drive/1vO1OK8_lwc0FAN75KAR0PGCY6Ra-ozBj#scrollTo=NgsQVAG3NHtg

@@02
Manipulação de dados com Pandas

Agora que já compreendemos a base do que é um DataFrame no Pandas e as primeiras operações que podemos realizar, como criar um DataFrame com pd.DataFrame ou ler um arquivo CSV com pd.read_csv, podemos avançar para aprender mais sobre como manipular os dados contidos nesses DataFrames que criamos.

Talvez você tenha notado algo diferente nas perguntas e respostas. Isso ocorre porque, quando a conexão com o Google é encerrada, perdemos as informações anteriores. Ao executar novamente, as respostas podem mudar um pouco, mas o essencial permanece o mesmo, então não se preocupe com isso. Vamos continuar explorando o mundo da manipulação de dados com o Pandas.

Solicitando ajuda de IA para criar um DataFrame
O que faremos agora é solicitar a ajuda de uma IA para gerar alguns exemplos de tabelas. Vamos criar um DataFrame básico. Podemos utilizar o GRCódigo, o Gemini, o ChatGPT, o Cloud, ou qualquer outra ferramenta de sua preferência. Vamos passar um prompt para que a IA nos auxilie.

Solicitaremos a criação de um DataFrame no Pandas com cinco colunas: a primeira coluna será o tipo de produto, ou simplesmente "produto"; a segunda coluna será a categoria do produto; a terceira será o preço do produto; a quarta será a nota ou avaliação do produto; e a quinta coluna será a quantidade de itens vendidos. Vamos gerar 50 linhas para cada uma dessas colunas.

Definindo dados e criando o DataFrame
Para começar, precisamos importar as bibliotecas necessárias, que são o Pandas e o NumPy. Vamos definir os dados para as colunas do nosso DataFrame:

import pandas as pd
import numpy as np

# Definindo os dados para as colunas
nomes_produtos = [f"Produto {i+1}" for i in range(50)]
categorias_produtos = np.random.choice(["Eletrônicos", "Livros", "Roupas", "Alimentos", "Brinquedos"], 50)
precos_produtos = np.random.uniform(10.0, 500.0, 50).round(2)
itens_vendidos = np.random.randint(1, 1000, 50)
avaliacoes_produtos = np.random.uniform(1.0, 5.0, 50).round(1)
COPIAR CÓDIGO
Ao pressionar "Enter", o sistema começará a processar e gerar os dados. Ele utilizará o Gemini, mas, como mencionado, você pode usar qualquer ferramenta de sua escolha. Após a execução, podemos aceitar os dados gerados, que são aleatórios e utilizam a biblioteca NumPy. Assim como o Pandas, o NumPy é amplamente utilizado para manipulação de dados, especialmente para operações numéricas e geração de números aleatórios.

Criando e exibindo o DataFrame
Agora, vamos criar o DataFrame utilizando pd.DataFrame, onde adicionamos cada uma das listas que definimos:

# Criando o DataFrame
df_produtos = pd.DataFrame({
    "Nome do produto": nomes_produtos,
    "Categoria do produto": categorias_produtos,
    "Preço do produto": precos_produtos,
    "Itens vendidos": itens_vendidos,
    "Avaliação do produto": avaliacoes_produtos
})
COPIAR CÓDIGO
Podemos exibir o DataFrame utilizando o método head para ver as primeiras linhas:

# Exibindo as primeiras linhas do DataFrame
display(df_produtos.head())
COPIAR CÓDIGO
Assim, criamos um novo DataFrame armazenado na variável df_produtos. Ele contém produtos como eletrônicos, brinquedos e alimentos, com preços variados, quantidades vendidas e avaliações dos produtos. Esses detalhes não são a parte mais importante; o foco está no que faremos com esses dados.

Explorando e filtrando dados no DataFrame
Aprendemos a exibir o DataFrame inteiro, com todos os produtos. Embora estejamos utilizando o método head, poderíamos exibir o DataFrame completo, que contém 50 itens, permitindo visualizar do índice 0 ao 50. Já discutimos anteriormente como utilizar head e tail para ver o início e o final do DataFrame, mas nosso objetivo agora é diferente. Suponhamos que queremos visualizar apenas a coluna de categorias dos produtos. Como faríamos isso? O DataFrame funciona de maneira semelhante a um dicionário, permitindo nomear a coluna desejada entre colchetes. Assim, ao especificar a coluna "categoria do produto", obtemos os dados ordenados na mesma sequência do DataFrame, como eletrônicos, brinquedos e alimentos, mas apenas dessa coluna específica. Essa é uma primeira filtragem que podemos realizar.

df_produtos["Categoria do produto"]
COPIAR CÓDIGO
Agora, imaginemos que queremos identificar os tipos de categorias únicas. Quando analisamos uma base de dados da empresa ou da internet, não sabemos necessariamente quais categorias estão presentes. Podemos querer identificar todos os valores únicos de uma categoria específica. Para isso, podemos criar um novo bloco de código. Existem algumas maneiras de fazer isso. Uma delas é utilizar o método unique(), que retorna um array com os elementos únicos da coluna.

df_produtos["Categoria do produto"].unique()
COPIAR CÓDIGO
Outra opção é usar o método set(), que retorna um dicionário, identificado pelas chaves. Ambos os métodos permitem trabalhar com os valores únicos da coluna.

set(df_produtos["Categoria do produto"])
COPIAR CÓDIGO
No próximo vídeo, aprenderemos como filtrar esses elementos. Até breve.

@@03
Filtragem de elementos

Continuando de onde nós paramos nesta aula, vamos aprender como filtrar os elementos.

Podemos colocar um texto com duas hashtags para filtrar elementos de um DataFrame do pandas. Para entendermos o que é exatamente uma filtragem, imagine que estamos visualizando o nome do produto, a categoria e outras informações. A filtragem consiste em selecionar apenas os produtos eletrônicos, ou os produtos que custam mais de 400 reais, ou aqueles com avaliação menor que duas estrelas ou maior ou igual a quatro estrelas. São várias possibilidades de filtragem que podemos aplicar em um DataFrame ou em qualquer outro DataFrame.

Aplicando filtros em colunas específicas
Para realizar essa filtragem, é bastante simples. Primeiramente, precisamos pensar em qual coluna específica aplicar o filtro. Já aprendemos a separar uma coluna, que é o df_produtos, e entre colchetes colocamos a categoria do produto. Suponhamos que queremos todos os produtos da categoria eletrônicos, por exemplo. No Python, podemos usar os sinais de maior, maior ou igual, menor, menor ou igual, ou quando for exatamente igual, utilizamos o igual duplo (==). Para diferente, usamos a exclamação igual (!=). Esses são os modos de comparação no Python.

Para começar, vamos acessar a coluna "Categoria do produto" do nosso DataFrame:

df_produtos["Categoria do produto"]
COPIAR CÓDIGO
Para fazer a comparação, utilizamos o igual duplo (==). É importante lembrar que o igual simples (=) é usado para atribuição, ou seja, para substituir o que estava em uma variável ou coluna por outra coisa. Já o igual duplo (==) faz uma comparação entre os itens. Queremos comparar o DataFrame, df_produtos, na coluna categoria, onde essa categoria deve ser igual a "eletrônicos".

df_produtos["Categoria do produto"] == "Eletrônicos"
COPIAR CÓDIGO
Exibindo resultados filtrados
Ao executar isso, ele retornará um valor booleano, verdadeiro ou falso (true ou false em inglês). Por exemplo, o item no índice zero pode retornar verdadeiro, indicando que é um eletrônico.

No entanto, não queremos apenas ver os valores booleanos; queremos exibir o DataFrame inteiro contendo apenas os produtos eletrônicos. Para isso, combinamos as duas operações: pegamos o nome do DataFrame, df_produtos, e aplicamos o filtro. Assim, obtemos o DataFrame completo apenas com os itens que são eletrônicos.

df_produtos[df_produtos["Categoria do produto"] == "Eletrônicos"]
COPIAR CÓDIGO
Ao executar, teremos o retorno esperado: oito produtos eletrônicos de um total de cinquenta, com diferentes avaliações e preços.

Realizando filtragem por avaliação
Podemos também realizar outra filtragem. Por exemplo, em vez de analisar a categoria do produto, podemos filtrar por avaliação, buscando produtos com avaliação menor que 2.0.

df_produtos[df_produtos["Avaliação do produto"] < 2.0]
COPIAR CÓDIGO
Ao executar, veremos produtos com avaliações de 1.8, 1.5, 1.3, todas menores que 2. Isso pode ser útil para analisar por que certos produtos estão com desempenho ruim.

Para saber quantos itens existem, podemos usar o método shape, que nos dá o formato do DataFrame. O df_produtos inteiro tem 50 linhas e 5 colunas.

df_produtos.shape
COPIAR CÓDIGO
Armazenando e combinando filtros
Podemos criar uma nova variável para armazenar os valores filtrados, como df_produtos_filtro_avaliacao_menor_que_2, e exibi-la.

df_produtos_filtro_avaliacao_menor_que_2 = df_produtos[df_produtos["Avaliação do produto"] < 2.0]
df_produtos_filtro_avaliacao_menor_que_2
COPIAR CÓDIGO
Ao aplicar o shape nesse novo DataFrame, veremos que ele contém 10 itens e 5 colunas.

df_produtos_filtro_avaliacao_menor_que_2.shape
COPIAR CÓDIGO
Também podemos combinar mais de um filtro. Por exemplo, podemos querer todos os produtos da categoria eletrônicos que custem mais de 350 reais. Para isso, usamos o símbolo de e comercial (&) para combinar os filtros. O primeiro filtro verifica se a categoria é eletrônicos, e o segundo verifica se o preço é maior ou igual a 350.0. É importante agrupar os filtros entre parênteses para evitar erros.

df_produtos[(df_produtos["Categoria do produto"] == "Eletrônicos") & (df_produtos["Preço do produto"] >= 350.0)]
COPIAR CÓDIGO
Ao executar, teremos três itens que são eletrônicos e custam mais de 350 reais.

Na próxima aula, continuaremos explorando mais dados com o pandas.

@@04
Métodos LOC e ILOC

Neste vídeo, vamos explorar dois métodos essenciais para seleção e filtragem de dados em Python com Pandas: os métodos LOC e ILOC. Eles são utilizados quando queremos selecionar, por exemplo, dados de um índice específico até outro, ou de um nome até outro, considerando que o índice seja numérico ou algo similar.

Começaremos com o ILOC. Suponhamos que queremos acessar o produto 34, que está no índice 33. Estamos utilizando índices que foram gerados automaticamente quando criamos nosso DataFrame com a ajuda de uma inteligência artificial. Esses índices são numéricos e representam a localização de cada item. Para encontrar um item específico, como o que está na posição 15, utilizamos o nome do DataFrame seguido de .ILOC e o número do índice entre colchetes.

df_produtos.iloc[15]
COPIAR CÓDIGO
Demonstrando o uso do método ILOC
Ao executar, obtemos todas as informações do produto no índice 15, como nome, categoria, preço, itens vendidos e avaliação.

Podemos também selecionar um intervalo de linhas, como da primeira linha até a linha 16, o que retornará do índice 0 até 15.

df_produtos.iloc[0:16]
COPIAR CÓDIGO
Ou ainda, selecionar de uma linha intermediária, como da linha 34 até 42.

df_produtos.iloc[34:42]
COPIAR CÓDIGO
Podemos passar esses intervalos de números ou, se preferirmos, indicar apenas o início ou o fim, como da linha 43 até o final.

df_produtos.iloc[43:]
COPIAR CÓDIGO
Isso é similar ao que vimos em Python ao trabalhar com listas.

Explicando o método LOC
O método LOC funciona de maneira semelhante, mas é utilizado quando o índice não é numérico, mas sim um nome ou texto. Para isso, precisamos converter nosso DataFrame para que o índice seja, por exemplo, o nome do produto. Podemos usar a inteligência artificial do Gemini para criar um novo DataFrame baseado no DFProducts, onde o índice será a coluna de nome do produto.

df_produtos_com_indice = df_produtos.set_index("Nome do produto")
display(df_produtos_com_indice)
COPIAR CÓDIGO
Com o novo DataFrame, onde o nome do produto é o índice, podemos usar o LOC. Em vez de procurar por dfprodutos.iloc[15], procuramos por dfprodutos_com_índice.LOC['produto 15'].

df_produtos_com_indice.loc["Produto 15"]
COPIAR CÓDIGO
Selecionando intervalos e colunas específicas
Isso nos permite acessar dados específicos do produto 15, como categoria, preço, itens vendidos e avaliação. Podemos também selecionar intervalos, como do produto 15 até o produto 35.

df_produtos_com_indice.loc["Produto 15":"Produto 35"]
COPIAR CÓDIGO
Ou do produto 45 até o final da lista.

df_produtos_com_indice.loc["Produto 45":]
COPIAR CÓDIGO
Esses métodos são extremamente úteis para manipulação de dados em DataFrames, permitindo acesso preciso e eficiente a informações específicas.

Para isso servem o LOC e o ILOC. Com eles, conseguimos realizar filtragens interessantes, como selecionar apenas o produto 45 e obter apenas o preço dele.

df_produtos_com_indice.loc["Produto 45", "Preço do produto"]
COPIAR CÓDIGO
Realizando filtragens avançadas
Podemos passar a coluna "preço do produto", que é o indicador da linha. Aqui, temos o índice, que é um indicador textual, e a coluna desejada. Estamos fazendo uma correspondência literal: produto 45 na coluna "preço do produto" deve retornar apenas esse valor, como se fosse uma célula de uma tabela do Excel, como B1, B2, D5, etc. Quando executamos isso, ele retorna o valor 236.39, mostrando que é do tipo float64, um tipo de ponto flutuante. Se fosse um inteiro, como "itens vendidos", ele retornaria int64, indicando o número 42 como um inteiro. Isso faz parte dos tipos do NumPy, uma biblioteca de matemática.

Podemos especificar mais coisas. Por exemplo, podemos passar uma lista de produtos, como 45, 47 e 16, e selecionar as colunas "preço do produto" e "itens vendidos".

df_produtos_com_indice.loc[["Produto 45", "Produto 47", "Produto 16"], ["Preço do produto", "Itens vendidos"]]
COPIAR CÓDIGO
Filtrando por categoria de produto
Ao executar, ele retorna exatamente isso. Podemos passar uma lista de produtos no primeiro argumento e uma lista de colunas, tanto para o LOC quanto para o ILOC. Aqui, usamos o LOC com índices de texto, mas poderíamos usar o ILOC com índices numéricos, seguindo a mesma ideia.

Vamos pegar o nosso DataFrame com índice textual e selecionar todos os itens da categoria "produto", como fizemos antes. Queremos onde a categoria seja "eletrônicos", mas não queremos apenas o valor booleano. Chamamos o método para retornar todo o DataFrame.

eletronicos = df_produtos_com_indice[df_produtos_com_indice["Categoria do produto"] == "Eletrônicos"]
COPIAR CÓDIGO
Nem sempre queremos tudo; às vezes, queremos apenas algumas colunas específicas. Podemos fazer isso com o LOC ou ILOC. Podemos salvar o resultado em uma variável chamada eletrônicos e usar o LOC para ver apenas algumas colunas dos produtos eletrônicos.

df_produtos_com_indice.loc[eletronicos.index, ["Preço do produto", "Itens vendidos"]]
COPIAR CÓDIGO
Alterando valores no DataFrame
Usamos dfprodutos com índice .loc para pegar todos os eletrônicos, indicando que é o índice, pois o LOC lê índices numéricos. Queremos, por exemplo, o "preço do produto" e o "número de itens vendidos". Lembrando que deve ser uma lista, ele aceita uma coluna sozinha ou uma lista de colunas, e um índice sozinho ou uma lista de índices, sempre com colchetes. Ao executar, ele retorna apenas os produtos eletrônicos e as colunas específicas desejadas. É uma filtragem combinada e avançada, útil em muitos casos.

Por fim, vamos ver como alterar valores. Imagine que precisamos alterar todos os itens de uma categoria, como mudar "brinquedos" para "produtos infantis". Não é prático alterar manualmente cada um. Podemos fazer isso com código, alterando todos de uma vez. Primeiro, fazemos um filtro no DataFrame na coluna "categoria do produto", onde seja igual a "brinquedos".

brinquedos = df_produtos_com_indice[df_produtos_com_indice["Categoria do produto"] == "Brinquedos"]
COPIAR CÓDIGO
Queremos o DataFrame inteiro para esses itens. Temos todos os itens da categoria "brinquedos". Podemos colocá-los em uma nova variável chamada brinquedos e usar produtos com índice .loc para passar os índices textuais dos brinquedos e selecionar apenas a coluna "categoria do produto".

df_produtos_com_indice.loc[brinquedos.index, "Categoria do produto"] = "Infanto-juvenil"
COPIAR CÓDIGO
Concluindo a manipulação de dados
Alteramos para "infantis" ou "infanto juvenil". Ao executar, quando exibimos os itens da categoria "brinquedos", eles aparecem como "infanto juvenil". Quando usamos .unique para ver os itens únicos da coluna "categoria do produto", ele mostra "eletrônicos", "infanto juvenil", "alimentos", "livros" e "roupas".

df_produtos_com_indice['Categoria do produto'].unique()
COPIAR CÓDIGO
Não existem mais "brinquedos". A variável salva mantém o estado anterior, mas o DataFrame foi alterado para "infanto juvenil".

Essas são algumas das funcionalidades do LOC e ILOC. Na próxima aula, explicaremos o próximo desafio do curso. Até mais!

@@05
Desafio com Python e Pandas

Estão preparados para o próximo desafio que vamos realizar com Python e Pandas? Vamos apresentar o desafio no texto, e este será relativamente tranquilo, considerando tudo o que já sabemos. No entanto, haverá um aspecto que talvez não saibamos fazer, e será necessário pesquisar para realizá-lo.

O primeiro passo do desafio será carregar um arquivo CSV específico que contém feedbacks de clientes. O arquivo se chama Reviews.csv. Devemos carregá-lo usando o Pandas. Ele estará disponível ao lado, em algum lugar, e já deve ter sido baixado no item anterior, antes deste vídeo. Podemos mostrar o arquivo, que é um dataset (conjunto de dados) público, ou pelo menos uma parte dele. Ele contém 41 linhas, sendo que a primeira é o cabeçalho, totalizando 40 itens. O arquivo possui reviews (avaliações) de usuários aleatórios sobre produtos que compraram.

Focando na coluna relevante para o desafio
O arquivo contém diversas informações, como Reviewer ID e Reviewer Name, que podem não ser relevantes para nós no momento. Em um cenário real, ao lidar com dados em uma empresa, podemos nos deparar com situações semelhantes. No entanto, o que realmente precisamos aqui é apenas a coluna Review Text, que contém o texto das avaliações ou resenhas sobre os produtos.

O primeiro passo será carregar e ler esse arquivo utilizando o Pandas. Em seguida, usaremos um LLM para classificar o sentimento de cada feedback como positivo, negativo ou neutro. Vamos padronizar a formatação, deixando a primeira letra maiúscula, para manter a consistência visual.

Adicionando uma nova coluna ao DataFrame
O terceiro e último passo será adicionar uma nova coluna ao nosso DataFrame, contendo essa classificação de sentimento (positivo, negativo ou neutro) que obtivemos a partir do arquivo CSV. Este é um desafio simples, considerando o que já aprendemos, mas a adição de uma nova coluna pode ser algo que ainda não sabemos fazer. Por isso, como parte do desafio, devemos pesquisar na documentação do Pandas ou utilizar Inteligência Artificial para descobrir como adicionar uma nova coluna a um DataFrame existente.

Essa será a tarefa proposta, e no próximo vídeo, retornaremos com a solução do desafio. Até mais.

@@06
Preparando o ambiente: reviews.csv

Tudo pronto para começar o desafio? O material principal que você precisará está no arquivo reviews.csv.
Faça o download, explore os dados e coloque seus conhecimentos em prática. Bom trabalho!

@@07
Análise de sentimento de reviews com o Gemini

A primeira etapa da nossa resolução do desafio, como sempre fazemos, é carregar o arquivo csv, que vocês devem ter baixado.

Vamos carregar o arquivo reviews.csv como um dataframe utilizando o pandas, que apelidamos de pd. Para isso, utilizamos a função pd.read_csv() para ler o arquivo CSV. Para obter o caminho completo do arquivo, copiamos o caminho da pasta e colamos entre aspas, pois é um texto. O caminho será //content//reviews.csv. Armazenamos isso em uma variável que podemos chamar de df_reviews, df_resenhas, ou df_avaliacoes, conforme preferirmos.

df_reviews = pd.read_csv("/content/reviews.csv")
Verificando o conteúdo do dataframe
Vamos verificar o conteúdo do dataframe, que deve ser o mesmo da planilha ao lado. Para não exibir tudo na tela, faremos uma leitura apenas dos cinco primeiros registros para analisar o que precisamos classificar como positivo, negativo ou neutro. O campo a ser analisado é review-text.

df_reviews.head()
Podemos ler cada texto, mesmo que não falemos inglês, pois a IA entende o idioma e retornará uma classificação como positivo, negativo ou neutro. O próximo passo é passar cada texto da coluna review-text para um laço for, que percorrerá essa coluna. Existem várias maneiras de fazer isso. Podemos isolar a coluna review-text em uma variável chamada coluna_reviews e, em seguida, utilizar um laço for para enviar cada texto ao Gemini para análise.

coluna_de_reviews = df_reviews["reviewText"]
Analisando sentimentos com o Gemini
Para chamar o Gemini, utilizamos o client.models.generateContent, passando dois parâmetros: o modelo, que será Gemini-2.5-flash, e o conteúdo, que é o nosso prompt. Vamos criar um prompt que instrui o Gemini a analisar a resenha e retornar uma análise de sentimento, respondendo apenas com "positivo", "negativo" ou "neutro". Podemos utilizar a técnica de Few Shot Prompting, fornecendo exemplos como "Eu adorei esse produto" (positivo), "Gostei, mas não é nada especial" (neutro), e "Odiei esse produto" (negativo).

for review_numero, resenha in enumerate(coluna_de_reviews):
    resposta = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""Você irá analisar a resenha que eu te mandarei abaixo, e retorna com uma análise de sentimento.
        Você deve responder APENAS com uma das seguintes palavras: 'Positiva', 'Negativa' ou 'Neutra',
        indicando o sentimento relativo aquela resenha específica.
        Exemplos:
        "Eu adorei esse produto" -> Positiva
        "Gostei, mas não é nada de especial" -> Neutra
        "Odiei esse produto" -> Negativa

        Segue a resenha a ser analisada: {resenha}
        """
    )
Armazenando e exibindo resultados
Armazenamos a resposta em uma variável e precisamos salvá-la em uma lista, pois o laço for irá sobrescrever a variável a cada iteração. Criamos uma lista chamada lista_analises_sentimentos, inicialmente vazia. Após obter a resposta, extraímos o texto com resposta.text e adicionamos à lista usando append.

lista_de_analises_de_sentimentos = []
lista_de_analises_de_sentimentos.append(resposta.text)
Podemos exibir o progresso durante o laço com um print, mostrando o número da resenha, o texto em inglês e a análise de sentimento.

print(f"Resenha {review_numero}: '{resenha}' -> Sentimento: {resposta.text}")
Atualizando o dataframe com análises de sentimento
Ao final do laço for, teremos uma lista completa com as análises de sentimento para cada uma das 40 resenhas. Após o término do processo, verificamos a lista lista_analises_de_sentimentos para garantir que contém apenas as palavras desejadas: "negativa", "positiva" ou "neutra". Em seguida, adicionamos uma nova coluna ao dataframe com essa classificação. Para isso, criamos uma coluna chamada "análises de sentimentos" e atribuímos a lista a ela. É importante garantir que o tamanho da lista corresponda ao número de linhas do dataframe.

df_reviews["Análises de Sentimentos"] = lista_de_analises_de_sentimentos
Ao exibir o dataframe atualizado, veremos a nova coluna "análises de sentimentos" com as classificações correspondentes a cada texto.

df_reviews
Considerações finais e próximos passos
Podemos expandir essa análise, por exemplo, criando uma coluna adicional com as resenhas traduzidas para o português usando o Gemini. Esse foi o nosso desafio, e na próxima aula continuaremos explorando Python, Pandas, dados e inteligência artificial.

@@08
Filtrando recompensas personalizadas na Clickbonus

A Clickbonus, uma plataforma digital que oferece um clube de vantagens e recompensas personalizadas por meio de parcerias com diversas empresas, está buscando melhorar a experiência de seus usuários. A equipe de desenvolvimento que você faz parte foi encarregada de analisar o banco de dados de recompensas para identificar quais recompensas são mais populares entre os usuários que gastaram mais de R$ 500,00 em compras no último mês. Para isso, é necessário filtrar as recompensas que pertencem à categoria "eletrônicos" e que foram resgatadas por esses usuários.
Qual abordagem de filtragem de dados você utilizaria para resolver essa situação?

Selecionar todas as recompensas da categoria "eletrônicos" e, em seguida, aplicar um filtro para usuários que gastaram qualquer valor no último mês, além de realizar uma segmentação demográfica para entender melhor o perfil dos usuários.
 
Alternativa incorreta
Aplicar um filtro no DataFrame para selecionar recompensas da categoria "eletrônicos" e, em seguida, filtrar usuários que gastaram mais de R$ 500,00 no último mês, utilizando o operador lógico "E" para combinar os critérios.
 
Correta, pois essa abordagem garante que apenas as recompensas que atendem a ambos os critérios sejam exibidas, permitindo identificar as recompensas eletrônicas mais populares entre os usuários que gastaram acima do valor estipulado.
Alternativa incorreta
Filtrar o DataFrame para selecionar recompensas resgatadas por usuários que gastaram mais de R$ 500,00 no último mês, sem considerar a categoria das recompensas, mas incluindo uma análise temporal para verificar a frequência de resgates ao longo do mês.
 
Incorreta, pois essa abordagem não considera a categoria "eletrônicos", o que é essencial para identificar as recompensas específicas que a equipe deseja analisar, mesmo que a análise temporal possa oferecer insights adicionais.
Alternativa incorreta
Utilizar um filtro para recompensas resgatadas no último mês, sem especificar a categoria ou o valor gasto pelos usuários, mas incluindo uma análise de tendências para prever futuras preferências de recompensas.

@@09
Para saber mais: set_index em pandas

Como o set_index transforma um DataFrame
O método set_index do pandas é uma ferramenta poderosa para tornar uma coluna específica do DataFrame os rótulos das linhas, substituindo os índices numéricos padrão. Ao utilizar esse recurso, você pode tornar os dados mais intuitivos, principalmente quando os elementos dessa coluna possuem significado único, como nomes, datas ou códigos. Essa transformação melhora a legibilidade da estrutura dos dados e pode facilitar filtragens e consultas subsequentes.

Por exemplo, ao converter a coluna que contém os nomes dos produtos em índices, você passa a acessar os dados como se estivesse consultando um dicionário. Assim, ao pedir os dados de um produto específico, em vez de usar um índice numérico, você pode utilizar diretamente a chave textual associada ao produto.

# Exemplo simples: convertendo uma coluna para índice
import pandas as pd

dados = {'Produto': ['Produto A', 'Produto B', 'Produto C'],
         'Preço': [100, 150, 200],
         'Estoque': [30, 20, 50]}
df = pd.DataFrame(dados)

# Transformando a coluna 'Produto' em índice
df_indexado = df.set_index('Produto')
print(df_indexado)
COPIAR CÓDIGO
Abordagens alternativas e considerações
Embora o set_index seja muito útil, é interessante conhecer as variações dessa abordagem para que você possa escolher a melhor para o seu fluxo de trabalho. Algumas considerações:

Quando utilizar índices textuais, a consulta de dados pode se assemelhar à consulta em dicionários, mas deve-se estar atento ao fato de que operações envolvendo ordenação podem ter um comportamento diferente dos índices numéricos.
Caso seja necessário manter o índice original, é comum realizar o reset_index posteriormente, utilizando o método reset_index, que reverte a operação e recria um índice numérico padrão.
Em cenários com grandes volumes de dados, índices textuais podem influenciar a performance de determinadas operações, então é importante avaliar se a legibilidade e a semântica dos dados compensam essa escolha.
Ao considerar essas alternativas, é possível equilibrar a clareza na representação dos dados com a eficiência das operações. Dessa forma, o uso do set_index pode ser adaptado para atender necessidades específicas, tornando as análises mais intuitivas e alinhadas ao contexto dos seus dados.

Explore essas variações e experimente diferentes abordagens para encontrar a melhor estratégia para o seu projeto.

@@10
Faça como eu fiz: DataFrames e Filtros

Nesta aula, exploramos a criação, manipulação e filtragem de dados com o Pandas, além de integrar análises de sentimentos via LLM. Agora é a sua chance de revisar e exercitar os conteúdos vistos, colocando a mão na massa. Para isso:
Crie um DataFrame com 5 colunas: nome do produto, categoria, preço, avaliação e itens vendidos;
Utilize pd.read_csv para importar dados de um arquivo CSV;
Exiba o DataFrame completo e com .head para visualizar os registros iniciais;
Selecione uma coluna específica utilizando a notação de colchetes;
Extraia valores únicos de uma coluna com os métodos unique ou set;
Realize um filtro simples para selecionar registros com categoria igual a 'eletrônicos';
Aplique um filtro condicional para obter produtos com avaliação menor que 2.0;
Combine filtros usando o operador & para condições simultâneas, como categoria e preço;
Utilize o método iloc para selecionar linhas por índices numéricos;
Acesse registros com índices textuais utilizando o método loc após definir um novo índice;
Implemente o desafio: carregue o CSV de reviews, utilize um LLM para classificar o sentimento de cada feedback e adicione essa classificação como nova coluna no DataFrame.
Para acessar o guia detalhado, consulte as transcrições da aula.

@@11
O que aprendemos?

Nesta aula, aprendemos:
Como criar e manipular DataFrames do Pandas, utilizando colunas e dados específicos.
Como usar o NumPy para gerar números aleatórios e popular DataFrames.
Métodos para acessar e filtrar dados em DataFrames, usando colchetes e condições.
Técnicas de filtragem utilizando operadores de comparação e lógicos no Pandas.
Uso dos métodos loc e iloc para seleção de dados.
A carregar e processar arquivos CSV com o Pandas.
Análise de sentimentos com integração de modelos de linguagem e manipulação de resultados.
A adicionar novas colunas a DataFrames para incorporar resultados de análises.

#26/01/2026

@06-Desafio Final

@@01
Código completo da aula anterior

Caso queira revisar o código até aqui ou começar a partir desse ponto, disponibilizamos os códigos realizados na aula anterior, para visualizar clique neste link.

https://colab.research.google.com/drive/1BuF1wYXLM8zWusEDhH8EN81vOFHmWQbn#scrollTo=5i0bhuooMVla

@@02
Preparando o ambiente

Nas próximas aulas utilizaremos o arquivo abaixo:
Módulo 6.
Bons estudos!

https://cdn3.gnarususercontent.com.br/4790-python/modulo-6.zip

@@03
Tratamento de erros com Try, Except e Finally

Nesta aula, continuaremos nosso mergulho em Python, pandas e inteligência artificial. O tema abordado será mais relacionado à programação em Python, sem ligação direta com pandas, dados ou inteligência artificial. No entanto, é uma base importante para o desenvolvimento de sistemas que envolvam inteligência artificial e pandas.

Vamos explorar um conceito da programação em si, que é imaginar situações em que algo pode dar errado, como algumas experiências que já tivemos durante nosso aprendizado.

Discutindo conversões e erros comuns
Imaginemos que vamos tentar realizar conversões, como fizemos anteriormente no curso. Por exemplo, ao pegarmos tipos de dados e tentarmos converter uma idade de 18 anos para um valor inteiro, podemos fazer isso utilizando a função int().

int()
COPIAR CÓDIGO
No entanto, se tentarmos converter uma string como "abc" para um inteiro, ocorrerá um erro.

int("abc")
COPIAR CÓDIGO
Um exemplo prático seria um input onde solicitamos que a pessoa usuária digite sua idade. Normalmente, isso funciona, mas se a pessoa digitar letras em vez de números, ocorrerá um erro de valor, pois tentamos converter algo não numérico para um valor inteiro. Vamos começar capturando a entrada do usuário.

pegando_algo = input("Digite a sua idade:")
COPIAR CÓDIGO
Agora, tentamos converter essa entrada para um inteiro.

pegando_algo = int(input("Digite a sua idade:"))
COPIAR CÓDIGO
Explorando tipos de erros e suas soluções
Existem diversos tipos de erros, como quando tentamos somar uma variável que contém um número com outra que contém um nome, resultando em um erro de tipo. Por exemplo:

pessoas = 6
pessoas_2 = "Mário, João, Silvia, Maria"
pessoas + pessoas_2
COPIAR CÓDIGO
Para lidar com esses casos, a linguagem Python, assim como a maioria das linguagens de programação, oferece comandos para tentar executar algo e capturar erros, permitindo que o programa continue. Em vez de exibir um erro para a pessoa usuária, podemos mostrar uma mensagem como "Você digitou um valor inválido, por favor, insira um valor numérico" ou continuar o programa com um valor padrão.

Utilizando blocos try e except
Esses são os chamados blocos de tentativa e exceção, conhecidos como exceptions. O bloco geralmente envolve os comandos try, except e, opcionalmente, finally. Vamos demonstrar como alterar um código para evitar erros e exibir mensagens adequadas para a pessoa usuária.

Primeiro, utilizamos o try para tentar executar um bloco de código. Se ocorrer um erro, o except captura o tipo específico de erro. Vamos ver um exemplo de como capturar um ValueError.

try:
    pegando_algo = int(input("Digite a sua idade:"))
except ValueError:
    print("Você não digitou um número inteiro válido")
COPIAR CÓDIGO
Existem muitos tipos de erros pré-definidos no Python, como TypeError, ValueError, KeyError, entre outros. Podemos consultar a documentação do Python para ver a lista completa de exceções.

Criando exceções personalizadas e múltiplos excepts
É recomendável criar exceções personalizadas para casos específicos. Ao capturar um erro, podemos exibir uma mensagem para a pessoa usuária e outra para a equipe de desenvolvimento, detalhando o erro. Por exemplo, ao capturar um ValueError, podemos exibir "Você não digitou um número inteiro válido" para a pessoa usuária e "Detalhes do erro: valor literal inválido para conversão" para a equipe de desenvolvimento.

except ValueError as ve:
    print("Você não digitou um número inteiro válido")
    print("Detalhes do erro:", ve)
COPIAR CÓDIGO
Além disso, podemos combinar vários blocos except para capturar diferentes tipos de erros. Por exemplo, podemos ter um except ValueError e outro except TypeError.

try:
    pessoas = 6
    pessoas_2 = "Mário, João, Silvia, Maria"
    pessoas + pessoas_2
except ValueError:
    print("Você não digitou um número inteiro válido")
except TypeError:
    print("Você não pode somar um número inteiro com uma string")
COPIAR CÓDIGO
Utilizando except Exception e finally
Se ocorrer um erro que não foi capturado por nenhum dos except específicos, podemos usar um except Exception para capturar qualquer erro restante.

except Exception as e:
    print("Detalhes do erro:", e)
COPIAR CÓDIGO
O comando finally é utilizado para executar um bloco de código independentemente de ter ocorrido um erro ou não. Isso é útil, por exemplo, ao trabalhar com arquivos, garantindo que eles sejam fechados corretamente, mesmo que ocorra um erro durante a execução do código.

finally:
    print("Finalizei o processo")
COPIAR CÓDIGO
Concluindo o uso de blocos try, except e finally
Em resumo, o uso de blocos try, except e finally nos permite tratar erros de forma eficaz, garantindo que o programa continue funcionando e fornecendo mensagens claras para a pessoa usuária e a equipe de desenvolvimento. Na próxima aula, continuaremos explorando a linguagem Python e a inteligência artificial.

@@04
Selecionando análises negativas para categorização

Continuando, vamos imaginar que desejamos, naquela tabela que analisamos em aulas anteriores, selecionar apenas as análises negativas e passá-las para um modelo de linguagem. Queremos que a inteligência artificial identifique as categorias de reclamações presentes nessas análises negativas e as divida em cinco categorias gerais, por exemplo.

Se passássemos as análises uma por uma, o modelo poderia perder o contexto. Ao perguntar a categoria de uma análise, ele poderia dar uma resposta específica, e ao passar outra análise, poderia dar uma categoria diferente, mesmo que ambas pudessem ser englobadas na mesma categoria. Por exemplo, uma reclamação sobre atraso na entrega ou produto quebrado poderia ser categorizada de formas diferentes em chamadas separadas. Portanto, o ideal seria passar todas as análises juntas, ao mesmo tempo.

Preparando o DataFrame para filtragem
Para isso, precisamos ter o DataFrame DFReviews carregado com as análises de sentimento processadas. Caso a aula anterior tenha sido feita há algum tempo, pode ser necessário rodar novamente o upload do arquivo reviews.csv e fazer a leitura com o pandas. Assim, o modelo poderá classificar as análises como negativas, neutras ou positivas, criando o novo DataFrame DFReviews.

O primeiro passo é filtrar apenas as análises de sentimentos que tenham a categoria negativa. Aprendemos a fazer isso anteriormente, então vamos relembrar criando um bloco de código. No DFReviews, a coluna que precisamos filtrar é a de análise de sentimentos. Podemos usar o atalho ctrl + espaço para visualizar as opções disponíveis. O filtro será para análises iguais a "negativa". Lembrando que o operador de igualdade é usado para comparação, então precisamos usar == para isso.

Filtrando e visualizando análises negativas
Primeiro, vamos visualizar o DataFrame e a coluna de análises de sentimentos:

df_reviews
df_reviews["Análises de Sentimentos"]
COPIAR CÓDIGO
Agora, aplicamos o filtro para selecionar apenas as análises negativas:

df_reviews["Análises de Sentimentos"] == "Negativa"
COPIAR CÓDIGO
Queremos visualizar o DataFrame inteiro para as análises negativas, então colocamos tudo entre colchetes. Ao exibir, veremos apenas os itens com análise negativa. Podemos salvar esse resultado em um novo DataFrame, como dfReviewsNegativas, e exibi-lo se desejarmos:

df_reviews_negativas = df_reviews[df_reviews["Análises de Sentimentos"] == "Negativa"]
df_reviews_negativas
COPIAR CÓDIGO
Também podemos verificar o tamanho desse DataFrame usando .shape, que nos mostrará, por exemplo, 25 linhas e 10 colunas, dando uma noção maior do conjunto de dados:

df_reviews_negativas.shape
COPIAR CÓDIGO
Extraindo e unindo resenhas negativas
A próxima etapa é extrair apenas a coluna ReviewText. Não podemos criar uma lista diretamente a partir disso, pois se pegássemos apenas essa coluna, seria criada uma lista. Vamos tentar pegar uma lista do novo DataFrame, dfReviews_negativas, e extrair apenas a coluna ReviewText, onde estão as resenhas. Isso resultará em uma lista completa, que podemos chamar de lista de resenhas negativas. Podemos imprimir essa lista para mantê-la visível:

resenhas_negativas = df_reviews_negativas["reviewText"]
resenhas_negativas
COPIAR CÓDIGO
No entanto, não podemos processar uma por uma; precisamos passar todas juntas. Existem várias opções para isso. Poderíamos, por exemplo, criar um novo texto concatenando as resenhas nas posições 0, 5, 6, 8, etc., mas isso seria trabalhoso e sem sentido. Uma alternativa seria usar um for para percorrer a lista e adicionar cada item a um texto, começando com um texto vazio e adicionando um por um até completar. Isso funcionaria, mas há uma maneira mais eficiente: o método join.

Utilizando o método join para unir textos
O método join é usado para unir textos e é mais fácil do que usar um for, pois permite fazer tudo em uma única linha de código. Para usar o join, precisamos escolher um separador. Como é um texto, deve estar entre aspas. Podemos escolher, por exemplo, cinco hashtags como separador, pois é improvável que elas apareçam no texto.

Após escolher o separador, usamos o método join para unir a lista de resenhas negativas:

resenhas_negativas_unidas = "#####".join(resenhas_negativas)
COPIAR CÓDIGO
Quando executamos, ele une tudo, separando por cinco hashtags. O texto resultante mostra claramente onde cada resenha termina e a próxima começa.

Chamando a IA para categorização
Agora, vamos salvar esse texto unido em uma variável chamada resenhas_negativas_unidas. Com isso, podemos chamar a IA do Gemini. Vamos copiar o código para fazer essa chamada, ajustando a identação conforme necessário. No código, vamos pedir à IA para analisar as resenhas negativas e encontrar cinco categorias diferentes de reclamações. Passamos o texto unido como argumento:

resposta_de_categorias = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"Você é um analista de dados. Vou te passar muitas resenhas negativas de análises de um produto, separadas por '#####', e eu quero que você encontre 5 categorias diferentes para os tipos de reclamações. Quero que você me retorne as 5 categorias. Cada categoria deve ser definida por APENAS uma palavra. Não escreva nada mais além das 5 categorias. Quero que elas sejam retornadas separadas por vírgula e em letra minúscula, e sem acentos gráficos.

    Exemplo:
    'eletronicos, roupas, alimentos, viagens, brinquedos'

    Aqui estão as resenhas negativas: {resenhas_negativas_unidas}'''"
)
print(resposta_de_categorias.text)
COPIAR CÓDIGO
Se quisermos que a IA retorne apenas uma palavra para cada categoria, podemos ajustar o prompt para especificar isso. Podemos também pedir que as categorias sejam retornadas separadas por vírgulas e em letras minúsculas, sem acentos gráficos.

Finalizando com a criação de lista de categorias
Após rodar o código, a IA retorna as categorias desejadas. Se quisermos, podemos incrementar o prompt usando o conceito de few-shot, fornecendo exemplos de categorias. Isso pode resultar em respostas ligeiramente diferentes, mas ainda assim úteis.

Finalmente, podemos salvar as categorias em uma variável e usar o método split para criar uma lista em Python. O split divide a string em substrings usando um separador, que neste caso será uma vírgula seguida de um espaço. Após rodar o código, obtemos uma lista de categorias em Python:

categorias = resposta_de_categorias.text
lista_de_categorias = categorias.split(sep=", ")
COPIAR CÓDIGO
Na próxima aula, continuaremos explorando a integração do Python com a inteligência artificial. Até mais.

@@05
Revisando a categorização de resenhas

Voltando às nossas aulas de Python, na última aula, separamos e categorizamos as resenhas, criando uma taxonomia dessas categorias. Essa abordagem é interessante e muito útil. Retornamos apenas as categorias das resenhas negativas, mas poderíamos ter explorado mais a fundo.

Imaginemos que já tivéssemos as categorias definidas, como fizemos anteriormente, quando solicitamos à IA que dividisse em positivo, negativo e neutro, as três categorias que passamos naquele momento.

Classificando resenhas com inteligência artificial
Imaginemos que já temos cinco categorias e um texto extenso de resenhas negativas unidas. Poderíamos classificar uma por uma, como antes, utilizando um for para ir de um a um, mas agora temos uma string gigantesca que não está bem separada. Existe um separador, mas poderia não haver, ou poderia ser apenas uma quebra de linha, o que dificultaria encontrar esse separador. Queremos que a inteligência artificial analise essas resenhas, as separe, atribua uma categoria a cada uma e retorne em um formato específico, como um dicionário do Python, que é mais organizado.

No mercado, existe um formato de retorno de arquivos muito utilizado na internet, chamado JSON (JavaScript Object Notation). Ele é similar a um dicionário do Python, podendo ser também um array, vetor ou lista. É comum que, ao fazer uma chamada para um serviço online ou uma IA, recebamos um arquivo nesse formato JSON. Vamos ver um exemplo de como ele funciona. É parecido com um dicionário Python, começando com chaves. À esquerda, temos uma chave e, à direita, um valor. Por exemplo:

{
    "name": "Chris",
    "age": 23,
    "address": {
        "city": "New York",
        "country": "America"
    },
    "friends": [
        {
            "name": "Emily",
            "hobbies": [
                "biking",
                "music",
                "gaming"
            ]
        },
        {
            "name": "John",
            "hobbies": [
                "soccer",
                "gaming"
            ]
        }
    ]
}
COPIAR CÓDIGO
Gerando categorias com código Python
Queremos que nossa IA, ou Gemini, faça algo similar. Vamos copiar a maior parte do texto que temos, mas mudar algumas coisas. Em vez de respostas de categorias, queremos um dicionário de resenhas classificadas. O começo pode ser parecido: "Você é o analista de dados. Vou te passar muitas resenhas negativas de análise de um produto, separadas por cinco hashtags, e quero que encontre cinco categorias diferentes para os tipos de reclamações. Retorne as cinco categorias."

Para isso, podemos usar o seguinte código para gerar as categorias:

resposta_de_categorias = client.models.generate_content(
    model="gemini-1.5-flash",
    contents=f"""Você é um analista de dados. Vou te passar muitas resenhas negativas de
    análises de um produto, separadas por '#####'', e eu quero que você encontre 5 categorias diferentes
    para os tipos de reclamações. Quero que você me retorne as 5 categorias.
    Cada categoria deve ser definida por APENAS uma palavra.
    Não escreva nada mais além das 5 categorias. Quero que elas sejam retornadas
    separadas por vírgula e em letra minúscula, e sem acentos gráficos.
    
    Exemplo:
    'eletronicos, roupas, alimentos, viagens, brinquedos'
    
    Aqui estão as resenhas negativas: {resenhas_negativas_unidas}"""
)
categorias = resposta_de_categorias.text
print(categorias)
COPIAR CÓDIGO
Criando um arquivo JSON de resenhas classificadas
Agora, queremos que ele continue trabalhando. Cada categoria deve ser definida por uma palavra, e queremos que ele retorne um arquivo no formato JSON. Especificamos que a separação será por cinco categorias, em letra minúscula e sem acentos gráficos. Depois, queremos que retorne um texto no formato JSON contendo três chaves: resenha original, resenha em PT (português) e categoria. Podemos dar um exemplo de arquivo JSON, como:

{
    'resenha_original': 'I didn`t like the color of the product',
    'resenha_pt': 'Eu não gostei da cor do produto',
    'categoria': 'design'
}
COPIAR CÓDIGO
Vamos passar a lista de resenhas negativas unidas e, em vez de categorias, ele nos dará o dicionário de resenhas classificadas, que esperamos ser um arquivo JSON. Chamaremos de JSON de resenhas classificadas, que receberá o dicionário de resenhas classificadas. Vamos imprimir e rodar, torcendo para dar certo. Ele identificou cinco categorias: durabilidade, desempenho, compatibilidade, funcionalidade e propaganda. Abaixo, encontramos as resenhas formatadas em JSON.

Convertendo JSON para dicionário Python
Para garantir que o retorno seja apenas o texto JSON, podemos reforçar o prompt:

Retorne APENAS o texto JSON. Não escreva nada mais além do texto JSON.
COPIAR CÓDIGO
Podemos transformar isso em um dicionário do Python usando a biblioteca JSON, que já está embutida no Python e no Google Colab. Importamos a biblioteca com:

import json
COPIAR CÓDIGO
E então, carregamos o JSON para um dicionário Python:

dicionario_de_resenhas_negativas_classificadas = json.loads(json_de_resenhas_classificadas)
COPIAR CÓDIGO
Se ocorrer um erro devido aos indicadores de código JSON, podemos substituí-los por nada, apagando-os do texto:

json_de_resenhas_classificadas_limpo = json_de_resenhas_classificadas.replace("```json", "").replace("```", "")
COPIAR CÓDIGO
Passamos essa variável para o loads, que converterá para um dicionário do Python:

dicionario_de_resenhas_negativas_classificadas = json.loads(json_de_resenhas_classificadas_limpo)
COPIAR CÓDIGO
Verificando o resultado final
Vamos imprimir o dicionário final e verificar se funcionou. Agora temos uma lista de dicionários com resenha original, resenha em português e categoria. Podemos usar métodos de lista, como len, para verificar o tamanho da lista, que tem 25 elementos:

len(dicionario_de_resenhas_negativas_classificadas)
COPIAR CÓDIGO
Podemos continuar trabalhando com esse formato JSON, utilizando loads para converter para um dicionário Python.

Na próxima aula, vamos explorar mais a inteligência artificial de uma forma diferente.

@@06
Explorando a execução local de IAs

Nesta aula, vamos explorar uma abordagem diferente para lidar com Inteligências Artificiais (IAs) em Python, executando-as localmente. Pode-se questionar: por que fazer isso? Existem diversos motivos. Muitas vezes, lidamos com dados privados e sensíveis, e mesmo confiando em empresas que oferecem esses serviços, como Google, OpenAI e Anthropic, pode haver razões pessoais ou empresariais, ou até mesmo leis de proteção de dados, que nos levam a preferir rodar esses modelos localmente.

Outro motivo seria o desenvolvimento de um modelo próprio, do zero, ou a utilização de modelos disponíveis online, como o GPT OSS de 20 bilhões de parâmetros, que é um modelo de código aberto. Podemos realizar um fine tuning (ajuste fino) nesses modelos para especializá-los em áreas específicas, como jurídico, financeiro ou recursos humanos, por exemplo. Se o modelo for menor, podemos executá-lo localmente em nossa máquina ou em um cluster de GPUs.

Utilizando ferramentas para execução local
Existem várias maneiras de fazer isso, mas duas são bastante populares atualmente: o Ollama, que funciona por linha de comando, e o LM Studio, que possui uma interface mais visual e amigável. Para este exemplo, utilizaremos o LM Studio. Primeiramente, é necessário baixá-lo e instalá-lo em sua máquina, disponível para Windows, Linux e Mac. Após a instalação, ao abrir o LM Studio, podemos pular as perguntas iniciais e acessar uma interface semelhante a um chatbot, como o ChatGPT ou Gemini, mas sem nenhum modelo carregado inicialmente.

Para carregar um modelo, podemos acessar a aba "Discover" no lado esquerdo, onde é possível baixar modelos de IA disponíveis na comunidade, como no Hugging Face. Esses modelos são abertos e podem ser baixados e utilizados. É importante notar que o número ao lado do modelo, como 4B, indica a quantidade de parâmetros do modelo, representando as conexões da rede neural. Modelos maiores, como o GPT OSS de 20 bilhões de parâmetros, são mais complexos do que modelos menores, como os de 4 bilhões.

Escolhendo e configurando o modelo
Para este curso, sugerimos baixar o modelo Gemma 3 de 1 bilhão de parâmetros, que é um modelo aberto do Google, baseado no Gemini. Acreditamos que esse modelo pode ser executado na maioria das máquinas, até mesmo em celulares. Se possuir uma máquina com GPU melhor, pode-se optar por modelos maiores, como o Gemma 3 de 4 bilhões de parâmetros.

Após escolher o modelo, na aba de opções de download, podemos ver as opções de quantização, que influenciam no tamanho e na qualidade do modelo. A quantização reduz o tamanho do modelo, convertendo números decimais em inteiros, sem perder muita qualidade. Para o Gemma 3 de 1 bilhão, temos a opção Q4, que representa a quantização com quatro números inteiros.

Integrando o modelo com Python
Depois de baixar o modelo, ele pode ser carregado e utilizado localmente, permitindo interações como em um chatbot. Podemos fazer perguntas e obter respostas rapidamente, dependendo da capacidade da máquina.

Agora, vamos explorar como integrar isso com código. Para isso, precisamos do Python instalado em nossa máquina e de uma IDE (Ambiente de Desenvolvimento Integrado), como o VS Code, JetBrains ou Cursor. Vamos utilizar o Cursor para este exemplo. Após instalar o Python e a IDE, criamos uma nova pasta e um arquivo chamado chamada-llm.py para começar a codificar.

Configurando o ambiente virtual
Dentro do Cursor, abrimos o terminal e criamos um ambiente virtual com o comando:

python -m venv .venv
COPIAR CÓDIGO
Após a criação, ativamos o ambiente virtual, o que varia conforme o sistema operacional. No Windows, utilizamos o comando:

.venv\Scripts\Activate
COPIAR CÓDIGO
No MacOS ou Linux, o comando é:

source .venv/bin/activate
COPIAR CÓDIGO
Ambos ativam o ambiente virtual, mas é necessário usar o comando específico para cada sistema operacional. Para desativar, basta digitar:

deactivate
COPIAR CÓDIGO
Instalando e configurando a biblioteca OpenAI
O motivo de ativarmos o ambiente virtual é para instalar a biblioteca da OpenAI, que será necessária. Embora o modelo que utilizaremos, o Gemma, seja do Google, a OpenAI estabeleceu um padrão com seu SDK, que é amplamente aceito. Assim, podemos usar a biblioteca da OpenAI para trabalhar com modelos como o Gemma, DeepSeek, Maritaca AI, entre outros.

Para instalar a biblioteca da OpenAI, usamos o comando:

pip install -q openai
COPIAR CÓDIGO
O -q é para que a instalação não seja muito verbosa. Após a instalação, importamos a biblioteca com:

from openai import OpenAI
COPIAR CÓDIGO
Criando o cliente OpenAI e configurando o modelo
Em seguida, criamos um cliente para a OpenAI, semelhante ao que fizemos com o Grok. O cliente OpenAI será configurado para se conectar ao nosso servidor local de modelos de IA, que será configurado no LMStudio. No LMStudio, ativamos o modelo e ele estará disponível em um endereço local, geralmente na porta 1234. Copiamos esse endereço e configuramos a URL base no nosso código:

client_openai = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"
)
COPIAR CÓDIGO
Realizando interações com o modelo
No código, configuramos o cliente para realizar uma completion (completude) com o método client.OpenAI.chat.completions.create. Passamos o modelo que estamos rodando localmente e as mensagens que queremos enviar. As mensagens são configuradas em uma lista de dicionários, onde podemos definir o papel (role) e o conteúdo (content). O papel pode ser, por exemplo, de sistema ou usuário, e o conteúdo é a mensagem que queremos enviar.

Podemos ajustar a personalidade do modelo através do system prompt, definindo como ele deve responder. Além disso, configuramos parâmetros como temperatura e número máximo de tokens:

resposta_do_llm = client_openai.chat.completions.create(
    model="google/gemma-3-1b",
    messages=[
        {"role":"system", "content":"Você é um assistente de IA que sempre responde de forma muito sarcástica."},
        {"role":"user", "content":"O que é a IA Generativa?"}
    ],
    temperature=1.0,
)
COPIAR CÓDIGO
Executando o código e obtendo respostas
Após configurar tudo, rodamos o código localmente com:

python chamada-ao-llm.py
COPIAR CÓDIGO
O modelo responde de acordo com as configurações que fizemos, e podemos ver a resposta no terminal. A resposta é extraída do objeto retornado pelo modelo, acessando o conteúdo dentro de choices[0].message.content:

print(resposta_do_llm.choices[0].message.content)
COPIAR CÓDIGO
Com isso, conseguimos rodar modelos de IA localmente, sem depender de serviços externos, o que pode ser importante para muitos casos de uso. No próximo vídeo, teremos o enunciado do nosso último desafio e, em seguida, a resolução.

@@07
Introduzindo o desafio final

Está preparado para o desafio final deste curso de Python? Ele pode parecer, a princípio, um pouco complexo, mas com tudo que aprendemos nos vídeos anteriores, temos certeza de que, com isso e mais uma iniciativa de nossa parte para buscar informações que talvez não saibamos, conseguiremos resolvê-lo. Vamos entender exatamente o que faremos neste desafio.

Este é o desafio final. A primeira coisa é que precisaremos realizá-lo usando uma IDE, ou seja, um desses ambientes de programação. Podemos utilizar o Cursor, como mencionado anteriormente, o VS Code, o JetBrains, ou qualquer outro com o qual nos sintamos mais confortáveis.

Descrevendo as etapas do desafio
O desafio final terá quatro etapas. A primeira etapa será carregar um arquivo .txt, um arquivo de texto básico, onde cada linha representará um elemento em uma lista do Python. Precisaremos carregar o arquivo e armazenar cada linha em uma lista. Assim, o elemento na posição zero da lista será o primeiro elemento da primeira linha do arquivo .txt, e a posição um da lista do Python será a segunda linha desse arquivo.

O arquivo em questão está relacionado ao tema de inteligência artificial e contém resenhas do aplicativo JetGPT na Play Store do Android ou na Apple Store dos iPhones. Cada resenha possui um ID de usuário, um identificador padrão, o nome do usuário que deixou a resenha, a reclamação ou o elogio, e a resenha em si, que estará em vários idiomas diferentes. Podemos observar que a primeira resenha está em francês, a segunda, terceira e quarta estão em inglês, há uma em espanhol, outra em turco, mais uma em francês, uma em polonês, outra em romeno, italiano, sueco, ou seja, este dataset está bem variado.

Carregando e processando o arquivo
O arquivo possui aproximadamente 25 entradas no formato .txt. Vamos carregá-lo e popular uma lista em Python. Esse é o primeiro passo.

O segundo passo consiste em enviar os itens dessa lista para o modelo que estamos executando localmente no laptop. Isso foi abordado na última aula, quando rodamos localmente com o LM Studio. Caso tenha pesquisado mais e esteja utilizando o Ollama, qualquer um dos dois é válido. O objetivo é enviar essa lista para o modelo e tentar extrair, em um formato JSON, um dicionário ou uma lista de dicionários. Nessa estrutura, teremos os itens: o usuário, que será o nome do usuário presente no arquivo; a resenha original; a tradução dessa resenha para o português; e uma avaliação da resenha, categorizada como positiva, negativa ou neutra. Existem várias maneiras de realizar essa tarefa, e deixaremos a escolha do método para você. Posteriormente, apresentaremos nossa solução no próximo vídeo.

Transformando e analisando os dados
O terceiro passo é transformar as respostas do modelo em uma lista de dicionários em Python. Por último, criaremos uma função que receberá essa lista de dicionários, como se fosse um arquivo JSON. A função percorrerá a lista e realizará duas ações: contará a quantidade de avaliações positivas, negativas e neutras presentes no arquivo .txt original, agora transformado em uma lista de dicionários; e unirá cada item dessa lista em uma variável do tipo string, utilizando um separador à sua escolha. Ao final, a função retornará tanto a quantidade de avaliações positivas, negativas e neutras quanto uma única variável do tipo string, contendo todos os itens separados pelo separador escolhido.

Concluindo o desafio
Esse é o desafio. O arquivo estará disponível para download, permitindo que você trabalhe com ele. Desejamos boa sorte, e a resolução será apresentada no próximo vídeo. Até já!

@@08
Preparando o ambiente: resenhas-app-gpt.txt

Tudo pronto para começar o desafio? O material principal que você precisará está no arquivo Resenhas_App_ChatGPT.txt.
Faça o download e coloque seus conhecimentos em prática. Bons estudos!

https://cdn3.gnarususercontent.com.br/4790-python/Resenhas_App_ChatGPT.txt

@@09
Resolução do desafio

Vamos resolver o desafio juntos, passo a passo, utilizando snippets de código para complementar as explicações.

Primeiro, vamos criar um novo arquivo chamado desafio-final.py dentro da mesma pasta onde estamos trabalhando. Este arquivo será em Python e será utilizado para resolver o desafio.

Lendo o arquivo de resenhas
Etapa 1: Ler o arquivo de resenhas
A primeira tarefa é carregar um arquivo .txt, onde cada linha será um elemento de uma lista em Python. Para isso, utilizaremos o comando with open, seguido do nome do arquivo. Vamos começar declarando uma lista chamada lista_de_resenhas, que inicialmente estará vazia.

# Etapa 1: Ler o arquivo de resenhas
lista_de_resenhas = []
with open("resenhas-app-gpt.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        lista_de_resenhas.append(linha.strip())

print(lista_de_resenhas)
Neste trecho de código, abrimos o arquivo resenhas-app-gpt.txt no modo de leitura ("r") e com codificação utf-8. Utilizamos um loop for para percorrer cada linha do arquivo, removendo espaços em branco com strip() e adicionando cada linha à lista lista_de_resenhas. Por fim, imprimimos a lista para verificar se a etapa foi concluída corretamente.

Processando as resenhas com o modelo LLM
Etapa 2: Processar as resenhas com o modelo LLM
Agora, passamos para a etapa 2 do desafio: enviar as resenhas para o modelo que estamos rodando localmente, para extrair informações em formato JSON. Para isso, vamos modularizar a função que interage com o LLM em outro arquivo, contato_com_LLM.py.

No arquivo contato_com_LLM.py, criaremos uma função que recebe uma linha e retorna um JSON. A função abrirá um cliente OpenAI, se necessário, e fará a chamada ao LLM.

# contato_com_llm.py
from openai import OpenAI

client_openai = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"
)

def recebe_linha_e_retorna_json(linha):
    resposta_do_llm = client_openai.chat.completions.create(
        model="google/gemma-3-1b",
        messages=[
            {"role": "system", "content": """
            Você é um especialista em análise de dados e conversão de dados para JSON.
            Você receberá uma linha de texto que é uma resenha de um aplicativo em um marketplace online.
            Eu quero que você analise essa resenha, e me retorne um JSON com as seguintes chaves:
            - 'usuario': o nome do usuário que fez a resenha
            - 'resenha_original': a resenha no idioma original que você recebeu
            - 'resenha_pt': a resenha traduzida para o português
            - 'avaliacao': uma avaliação se essa resenha foi 'Positiva', 'Negativa' ou 'Neutra' (apenas uma dessas opções)
            """},
            {"role": "user", "content": f"Resenha: {linha}"}
        ],
        temperature=0.0
    )
    return resposta_do_llm.choices[0].message.content
Neste código, configuramos o modelo com temperatura zero para obter resultados específicos. No messages, definimos o system e o user, passando a linha de resenha. O system é configurado para que o modelo saiba que é um especialista em análise de dados e conversão para JSON.

Voltamos ao arquivo principal e chamamos a função para cada resenha, convertendo a resposta em um dicionário Python com json.loads.

from contato_com_llm import recebe_linha_e_retorna_json
import json

lista_de_resenhas_json = []

for resenha in lista_de_resenhas:
    resenha_json = recebe_linha_e_retorna_json(resenha)
    resenha_dict = json.loads(resenha_json)
    lista_de_resenhas_json.append(resenha_dict)

print(lista_de_resenhas_json)
Aqui, percorremos a lista_de_resenhas, chamamos a função recebe_linha_e_retorna_json para cada resenha, e armazenamos o resultado em lista_de_resenhas_json.

Contando e unindo as avaliações
Etapa Final: Contar e unir as avaliações
Na etapa final, criamos uma função para contar as avaliações positivas, negativas e neutras, e unir todas as resenhas em uma única string com um separador.

def contador_e_juntador(lista_de_dicionarios):
    contador_positivas = 0
    contador_negativas = 0
    contador_neutras = 0

    for dicionario in lista_de_dicionarios:
        if dicionario['avaliacao'] == 'Positiva':
            contador_positivas += 1
        elif dicionario['avaliacao'] == 'Negativa':
            contador_negativas += 1
        else:
            contador_neutras += 1

    lista_de_dicionarios_str = [str(dicionario) for dicionario in lista_de_dicionarios]
    textos_unidos = "#####".join(lista_de_dicionarios_str)

    return contador_positivas, contador_negativas, contador_neutras, textos_unidos

pos, neg, neut, textos = contador_e_juntador(lista_de_resenhas_json)

print(f"Positivas: {pos}")
print(f"Negativas: {neg}")
print(f"Neutras: {neut}")
print(textos)
Executamos o código novamente, corrigindo eventuais erros, como a necessidade de converter dicionários para strings antes de usar join. Após ajustes, o código roda com sucesso, processando todas as resenhas e exibindo as contagens e o texto unido.

@@10
Tratamento de exceções em buscas de livros

A Buscante, um buscador e e-commerce de livros variados, está aprimorando seu sistema de busca para oferecer uma experiência mais fluida às pessoas usuárias. Durante o desenvolvimento, a equipe identificou que, ao buscar por títulos de livros, algumas pessoas usuárias digitam caracteres especiais ou números em vez de letras, resultando em erros que interrompem a busca. A equipe de desenvolvimento que você faz parte precisa implementar um sistema que trate esses erros de forma a não interromper a experiência da pessoa usuária, mas sim fornecer uma mensagem amigável ou uma sugestão de correção.
Como você aplicaria o conceito de tratamento de exceções para resolver esse problema e melhorar a experiência da pessoa usuária?

Criar um sistema de validação prévia que rejeita qualquer entrada que não seja composta exclusivamente por letras, sem fornecer feedback adicional à pessoa usuária, e sem considerar a possibilidade de erros de digitação comuns que poderiam ser corrigidos automaticamente. Essa abordagem ignora a importância de uma comunicação clara e eficaz com a pessoa usuária, que poderia ser orientada sobre como ajustar sua busca para obter melhores resultados.
 
Incorreta, pois rejeitar a entrada sem feedback não melhora a experiência da pessoa usuária e não utiliza o tratamento de exceções para lidar com o problema, além de não oferecer qualquer orientação sobre como corrigir a entrada.
Alternativa incorreta
Implementar blocos de try e except no código de busca, onde o sistema tenta processar a entrada dentro de um bloco try e captura erros como ValueError em um bloco except, retornando uma mensagem amigável ou sugestão de correção.
 
Correta, pois essa abordagem permite capturar erros específicos causados por entradas inválidas e fornecer feedback útil à pessoa usuária, sem interromper a busca.
Alternativa incorreta
Utilizar apenas um bloco try para processar a entrada e, em caso de erro, deixar que o sistema retorne uma mensagem de erro padrão do servidor, sem qualquer personalização ou tentativa de correção. Além disso, não se preocupa em identificar o tipo de erro ocorrido, o que pode levar a uma experiência menos satisfatória para a pessoa usuária, que não recebe orientações claras sobre como corrigir a entrada.
 
Incorreta, pois essa abordagem não fornece uma mensagem amigável ou sugestão de correção, o que pode resultar em uma experiência negativa para a pessoa usuária, já que a falta de personalização na mensagem de erro não ajuda a resolver o problema.
Alternativa incorreta
Implementar um sistema que substitui automaticamente caracteres especiais por letras aleatórias antes de processar a busca, sem considerar o contexto ou a intenção original da pessoa usuária. Essa abordagem pode levar a resultados de busca que não correspondem ao que a pessoa usuária estava realmente procurando, além de não fornecer qualquer tipo de feedback ou sugestão de correção que poderia melhorar a experiência de busca.

@@11
Para saber mais: modularização de funções em python

A importância de dividir o código em módulos
Ao desenvolver projetos mais complexos em Python, separar funcionalidades em arquivos diferentes é essencial para manter a clareza e facilitar a manutenção. Essa abordagem, chamada de modularização, permite que cada parte do programa tenha uma responsabilidade bem definida, o que torna o código mais organizado e reutilizável. Ademais, trabalhar com módulos favorece o trabalho em equipe, pois diferentes integrantes podem desenvolver e testar partes distintas do projeto independentemente.

Estrutura e benefícios da modularização
Ao modularizar o código, você isola funções e classes que realizam tarefas específicas em arquivos separados. Essa separação traz diversas vantagens:

Legibilidade: O código fica mais limpo, facilitando a compreensão do fluxo e da lógica implementada.
Manutenção: Atualizações ou correções podem ser feitas em um módulo específico sem afetar outras partes do sistema.
Reutilização: Funções que cumprem tarefas comuns podem ser importadas e utilizadas em diferentes projetos, evitando a duplicação de código.
Veja o exemplo prático a seguir que demonstra como dividir uma funcionalidade em um arquivo e importá-la em outro:

# No arquivo utilidades.py

def saudar(nome):
    return f"Olá, {nome}! Seja bem-vindx."

# No arquivo principal.py

from utilidades import saudar

nome_usuario = "Alex"
print(saudar(nome_usuario))
COPIAR CÓDIGO
Nesse exemplo, a função de saudação foi isolada em um módulo separado, o que torna a utilização da função por outros arquivos um processo simples e intuitivo.

Considerações sobre vantagens e desafios
Embora a modularização traga muitos benefícios, é importante estar atento a alguns pontos:

Planejamento: Decidir como dividir o projeto em módulos requer uma análise cuidadosa da arquitetura da aplicação. Módulos mal organizados podem criar dependências circulares indesejadas.
Overhead de importação: Em projetos muito grandes, o gerenciamento de importações pode se tornar complexo, demandando o uso de pacotes e subpacotes para manter a hierarquia organizada.
No geral, investir tempo na estruturação modular do código é uma prática que melhora a escalabilidade e a qualidade do software, permitindo que o programador se concentre em resolver problemas de forma mais eficaz.

Aprofundar-se nesses conceitos e aplicar boas práticas de organização pode ser um grande diferencial na hora de trabalhar em projetos colaborativos e de larga escala.

@@12
Faça como eu fiz: lidar com exceções e IA

Nesta aula, aprendemos a tratar exceções usando blocos try/except/finally, filtrar dados com pandas, manipular strings com join e integrar chamadas de LLM para análise e classificação. Agora é a sua chance de colocar em prática os conteúdos explorados. Para isso:
Identifique diferentes erros: value, type e divisão por zero;
Crie um bloco try para isolar operações arriscadas;
Configure except para capturar value error e alertar o usuário;
Configure except para capturar type error com mensagem de apoio;
Utilize except geral para erros não previstos;
Aplique finally para executar ações de finalização (ex.: fechar arquivos);
Replique exemplos de tratamento de exceções conforme demonstrado;
Filtre DataFrame por análises negativas usando pandas;
Extraia a coluna de resenhas negativas do DataFrame;
Una as resenhas com o método join e delimitador definido;
Armazene o texto unificado em variável para processamento;
Prepare um prompt para enviar as resenhas ao LLM;
Configure o cliente de LLM com parâmetros específicos;
Realize chamadas à IA e capture as respostas;
Extraia categorias das respostas conforme solicitado;
Refine o prompt para limitar a resposta a uma palavra por categoria;
Converta a resposta em lista utilizando o método split;
Implemente exemplo de extração de JSON para cada resenha;
Converta textos JSON para dicionários Python;
Utilize try/except ao conectar com serviços de LLM;
Demonstre execução de modelos de IA localmente (LM Studio/Ollama);
Selecione e baixe um modelo adequado (ex.: Gema 3 1B);
Configure ambiente virtual Python e IDE de desenvolvimento;
Crie script integrando chamadas LLM com código Python;
Desenvolva função para processar em lote resenhas e contagem de avaliações;
Implemente função que una os resultados num único texto.
Para mais conteúdos, consulte as transcrições da aula.

@@13
Arquivos do curso

Aqui você pode baixar o zip da aula 06:
chamada-ao-llm.py;
contato_com_llm.py;
desafio_final.py.
E o download completo.

https://cdn3.gnarususercontent.com.br/4790-python/chamada-ao-llm.py

https://cdn3.gnarususercontent.com.br/4790-python/contato_com_llm.py

https://cdn3.gnarususercontent.com.br/4790-python/desafio_final.py

http://cdn3.gnarususercontent.com.br/4790-python/modulo-6_final.zip

@@14
O que aprendemos?

Nesta aula, aprendemos:
A tratar erros e exceções em Python com blocos try, except, e finally.
A filtrar um DataFrame Pandas e manipular strings com métodos como join() e split().
As vantagens de rodar modelos de IA localmente e usar o LM Studio.
A importância de ambientes de programação e o uso de IDEs como VSCode.
A integrar modelos de linguagem locais para processar dados e converter resenhas em JSON.
A manipular arquivos .txt em Python para processar dados textuais.
O uso do formato JSON e a transformação em dicionários Python com a biblioteca json.
A aplicar prompts em IA para produzir JSONs bem formatados.

@@15
Conclusão

Agora que concluímos este curso e realizamos os desafios, esperamos que todos tenham aproveitado ao máximo o conhecimento adquirido. Desde o início, aprendemos a criar variáveis em Python, imprimir valores, criar variáveis que armazenam valores numéricos e textos em string, e realizar operações matemáticas.

Para começar, vamos ver como imprimir valores em Python. Podemos usar a função print() para exibir números e textos. Veja alguns exemplos básicos:

print(5)
print("Olá mundo")
print("Olá mundo" + "5")
print(5 + 2)
COPIAR CÓDIGO
Armazenando e manipulando variáveis
Além disso, exploramos como armazenar valores em variáveis e manipulá-los. Por exemplo, podemos criar variáveis para armazenar números e depois usá-las em operações:

produto1 = 5
print(produto1)

produto2 = 2000
print(produto2)

produto3 = 1
print(produto1 + produto2 + produto3)
COPIAR CÓDIGO
Também trabalhamos com variáveis de texto, ou strings, e vimos como concatená-las:

nome_do_produto1 = "Macarrão"
nome_do_produto2 = "Celular"
nome_do_produto3 = "Bala"

print(nome_do_produto1 + " " + nome_do_produto2 + " " + nome_do_produto3)
COPIAR CÓDIGO
Explorando estruturas condicionais e de repetição
Além disso, exploramos operações com texto, recebemos valores do usuário por meio de prompts e lidamos com eles. Estudamos valores condicionais e estruturas condicionais, como if, else e elif. Por exemplo, podemos pedir ao usuário para digitar seu nome e idade, e então usar uma estrutura condicional para verificar se ele pode entrar em uma festa:

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

if idade >= 18:
  print(f"{nome} pode entrar na festa porque ele é maior de idade.")
  print(f"Ele tem {idade} anos de idade.")
else:
  print(f"{nome} NÃO pode entrar na festa porque ele é menor de idade.")
  print(f"Ele tem {idade} anos de idade.")
COPIAR CÓDIGO
As estruturas de repetição, como while e for, foram amplamente utilizadas durante o curso para criar chats e respostas. Exploramos estruturas de dados, como listas, e manipulamos dicionários. Criamos funções próprias para realizar ações específicas.

Por exemplo, podemos usar um loop while para imprimir um padrão de asteriscos:

n = 1
while n <= 10:
  print("*")
  n = n + 1
COPIAR CÓDIGO
Enfrentando desafios e aplicando conhecimentos
Enfrentamos diversos desafios, utilizando IAs privadas e conectando com a API do Gemini e a IA do Grok, que é uma IA de pesos abertos, mas ainda na nuvem do Grok. Aprendemos também os fundamentos da ciência de dados, utilizando o framework Pandas para ler e escrever arquivos CSV e de texto.

Todo esse aprendizado culminou no desafio final, que é uma oportunidade de aplicar todas as habilidades adquiridas durante o curso no VS Code.

Incentivando o aprendizado contínuo
Sempre enfatizamos que este é apenas o primeiro passo. O aprendizado de uma linguagem de programação, inteligência artificial ou qualquer outra área requer evolução contínua, com novos projetos e aprendizados diários. Muitas coisas que não tivemos tempo de ensinar neste curso podem ser exploradas no Tech Guide, um guia gratuito promovido pela Alura.

Na carreira de Python, por exemplo, é importante aprender lógica de programação, algo que já abordamos. Testes são fundamentais para o mercado, mas não foram cobertos neste curso inicial. Já vimos os fundamentos e utilizamos orientação a objetos sem nos aprofundarmos no conceito. Na Alura, há cursos específicos sobre Python, incluindo orientação a objetos, essencial para qualquer pessoa que deseja se tornar programadora Python.

Explorando tópicos avançados e próximos passos
Também abordamos superficialmente a comunicação com APIs, conectando-nos com a API do Gemini e do Grok. No entanto, há mais a aprender sobre comunicação com APIs sem usar uma SDK própria, como as do Google, Gemini, OpenAI e Grok. Já vimos várias estruturas de dados e coleções, mas não abordamos Flask e Django, que são interessantes. Além disso, há orientação a objetos avançada, Lambdas e muito mais no universo do Python, sem mencionar o mundo da inteligência artificial, que também requer estudo contínuo.

Esperamos que agora tenhamos uma base sólida em Python para continuar aprendendo e adquirindo novas habilidades e conhecimentos ao longo do tempo. Desejamos boa sorte em seu percurso e incentivamos a continuar na Alura, onde estamos sempre disponíveis para ajudar. Até mais!