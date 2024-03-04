import pandas as pd

print('Bem vindo ao Prototipo!')

#Escolha o diretorio em que deseja
data = pd.read_excel('main/data/alunos.xlsx')

print('1. Quais são os 10 alunos com melhor desempenho.')
print('2. Quais são os alunos com desempenho mais baixo.')
print('3. Os 10 melhores alunos por disciplina.')
print('4. Os 10 piores alunos por disciplina.')
print('5. Dados do aluno.')


dadoselecionado = input('Escolha a opção desejada: ')

if dadoselecionado == '1': 
    print('Alunos com desempenho mais alto:')
    #Escolhe a coluna de interesse
    X = data[['nome','idade','genero','media']]
    #Ordena os dados da maior para menor
    X_media = X.sort_values(by='media', ascending=False)
    #Filtra somente 10 pessoas
    dado_aluno =  X_media.head(10)
    print(dado_aluno)
    #Cria um arquivo xlsx com esses dados
    dado_aluno.to_excel('main/resultado.xlsx', index=False)
    
elif dadoselecionado == '2':
    print('Alunos com desempenho mais baixo:')
    X = data[['nome','idade','genero','media']]
    #Ordena os dados da menor para maior
    X_media = X.sort_values(by='media', ascending=True)
    dado_aluno =  X_media.head(10)
    print(dado_aluno)
    dado_aluno.to_excel('main/resultado.xlsx', index=False)
elif dadoselecionado == '3':
    print('Os 10 melhores alunos por disciplina')
    materia = input('Escolha a matéria desejada (com letras minúsculas): ')
    if materia in ['lingua portuguesa', 'matematica', 'ciencias', 'historia', 'geografia', 'educacao fisica', 'artes', 'ingles']:
        X = data[[ 'nome', 'idade', 'genero', materia]]
        X_media = X.sort_values(by=materia, ascending=False)
        dado_aluno = X_media.head(10)
        print(dado_aluno)
        dado_aluno.to_excel('main/resultado.xlsx', index=False)
elif dadoselecionado == '4':
    print('Os 10 piores alunos por disciplina')
    materia = input('Escolha a matéria desejada: ')
    #Obtem as informações referentes às matérias escolhidas
    if materia in ['lingua portuguesa', 'matemática', 'ciencias', 'historia', 'geografia', 'educacao fisica', 'artes', 'ingles']:
        X = data[[ 'nome', 'idade', 'genero', materia]]
        X_media = X.sort_values(by=materia, ascending=True)
        dado_aluno = X_media.head(10)
        print(dado_aluno)
        dado_aluno.to_excel('main/resultado.xlsx', index=False)
elif dadoselecionado == '5':
    print('Dados do aluno.')
    aluno = input('Insira o nome do Aluno: ')
    #Verifica se o aluno existe na base de dados
    dado_aluno = data.query('nome == @aluno')
    print(dado_aluno)
    dado_aluno.to_excel('main/resultado.xlsx', index=False)
else:
    print("Opção inválida")