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