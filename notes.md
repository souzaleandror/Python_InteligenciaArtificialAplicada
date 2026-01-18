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