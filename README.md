Análise de Dados de Alunos com Python e Pandas

Este repositório contém um script principal (main.py) que analisa dados de alunos usando a biblioteca Pandas. O script lê um arquivo Excel contendo informações sobre os alunos, realiza cálculos e gera insights sobre o desempenho de cada aluno em diferentes disciplinas.

Pré-requisitos:
Python 3.x
Bibliotecas: openpyxl e pandas

Para instalar as dependências, execute:
pip install openpyxl pandas

Dados de Entrada
O script espera que os dados de entrada estejam no formato de um arquivo Excel com as seguintes colunas:

id
nome
idade
genero
lingua portuguesa
matematica
ciencias
história
geografia
educacao física
artes
ingles
media

Um exemplo do arquivo Excel pode ser encontrado em:
alunos.xlsx

Como executar o script:
Salve o arquivo de dados de entrada no mesmo diretório doscript main.py.

Execute o script usando o comando a seguir:
python main.py

Como o script main.py funciona
Após ter satisfeito todos os pré-requisitos e garantido que o arquivo de dados de entrada esteja no formato correto e no mesmo diretório do script, basta executar o comando python main.py.

O script fará a leitura do arquivo Excel e realizará as análises dos dados usando a biblioteca Pandas. Serão calculados e apresentados insights sobre o desempenho de cada aluno em diferentes disciplinas.

Após a conclusão da análise, será gerado um arquivo no formato Excel chamado "resultado.xlsx" contendo as estatísticas e os insights obtidos a partir dos dados de entrada. O arquivo será salvo no mesmo diretório do script main.py. 
