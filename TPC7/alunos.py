import csv
import matplotlib.pyplot

def readDataset (alunos):
    f = open (alunos, encoding='utf-8')
    f.readline() 
    csv_reader =csv.reader (f, delimiter = ',')
    alunos = []
    for row in csv_reader:
        alunos.append(tuple(row))
    return alunos

def aluPorCurso (alunos):
    res = {}
    for _, aluno, curso, *_ in alunos:
        if curso in res.keys():
            res [curso].append(aluno)
        else:
            res [curso] = [aluno]
    return res

def mediaporAluno (alunos):
    lista = []
    media = 0
    for id, aluno, curso, tpc1, tpc2, tpc3, tpc4 in alunos:
        media = (int(tpc1) + int (tpc2) + int (tpc3) + int (tpc4)) / 4
        tuplo = (id, aluno, curso, tpc1, tpc2, tpc3, tpc4, media)
        lista.append (tuplo)
    return lista

def alunoporEscalao (alunos):
    lista =[]
    for id, aluno, curso, tpc1, tpc2, tpc3,tpc4, media in alunos:
        escaloes = [(n, n + 4) for n in range (1, 20, 3)]
        for inf,sup in escaloes:
            if media >= inf and media <= sup:
                escalao = (inf,sup)
                tuplo = (id, aluno, curso, tpc1, tpc2, tpc3, tpc4, media, escalao)
                lista.append (tuplo)
    return lista
                
def desenhargrafico (alunos):
    res = {}
    for _,_,_,_,_,_,_,_, escaloes in alunos:
        if escaloes in res:
            res[escaloes]+=1
        else:
            res[escaloes]= 1
        y= res.values ()
        x= res.values ()
    matplotlib.pyplot.plot(x,y)
    matplotlib.pyplot.xlabel ("escalão")
    matplotlib.pyplot.ylabel ("numero de alunos")
    matplotlib.pyplot.show


def tabela (alunos):
    print ("Id.     :: Nome                 :: Curso                 :: Media")
    for id, aluno, curso, _, _, _, _, media in alunos:
        print (f"{id['id']:7} :: {aluno['nome']:20} :: {curso['curso']: 20} :: {media['media']:20}")
    

def menu (alunos):
    print (""" 
    1. Organizar alunos por curso
    2. Organizar media por alunos
    3. Organizar aluno por escalão
    4. Desenhar grafico aluno por curso
    5. Desenhar tabela""")
    b = int(input("Qual função deseja usar"))
    if b == 1:
        print (aluPorCurso) 
    elif b == 2:
        print (mediaporAluno)
    elif b == 3:
        print (alunoporEscalao)
    elif b == 4:
        print (desenhargrafico)
    elif b == 5:
        print (tabela)



