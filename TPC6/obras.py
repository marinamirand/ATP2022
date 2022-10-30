#Model:
# obras = [(nome, desc, anoCriacao, periodo, compositor, duracao, -id)]

import csv
import matplotlib.pyplot

def readDataset (fnome):
    f = open (fnome, encoding='utf-8')
    f.readline() #lê uma linha, se eu não fizer nada com ela, o programa descarta-a
    csv_reader =csv.reader (f, delimiter = ';')
    obras= []
    for row in csv_reader:
        obras.append(tuple(row))
    return obras

def pp(obras):
    print (f"{obras[0][:25]:25} | {obras[4][:30]:30} | {obras[3][:15]:15} | {obras[2][:6]:6}") #primeiro [:xx] quer dizer quando acaba de passar texto, o seguinte :xx quer dizer quantos espaços anda

def ordTit (t):
    return t[0]


def titAno (obras):
    res = []
    for nome, _, ano, *_ in obras: # _, quer dizer que não queremo a informação ma coluna a seguir ithink
        res.append((nome, ano))
        res.sort(key=ordTit)
    return res

def titPorAno (obras):
    res = {}
    for nome, _, ano, *_ in obras:
        if ano in res.keys():
            res [ano].append(nome)
        else:
            res [ano] = [nome]
    return res

def ordenaCompositores (obras):
    res = []
    for _, _, _, _, compositor, *_ in obras:
        if compositor in res:
            res.sort()
        else: 
            res.append (compositor)
    return res

def obrasPorPeriodo (obras):
    res = {}
    for _, _, _, periodo, *_ in obras:
        if periodo in res.keys():
            res [periodo]= res[periodo] + 1 
        else:
            res [periodo] = 1
    return (res)

def obrasPorAno (obras):
    res = {}
    for _, _, ano, *_ in obras:
        if ano in res.keys():
            res [ano]= res[ano] + 1 
        else:
            res [ano] = 1
    return (res)

def obrasPorCompositor (obras):
    res = {}
    for _, _, _, _, compositor, *_ in obras:
        if compositor in res.keys():
            res [compositor]= res[compositor] + 1 
        else:
            res [compositor] = 1
    return (res)  

def desenhargrafico (dicionario):
    x = []
    y = []
    for key in dicionario:
        x.append (key)
        y.append (dicionario[key])
    return matplotlib.pyplot.plot(x,y)

def titPorCompositor (obras):
    res = {}
    for nome, _, _, _, compositor, *_ in obras:
        if compositor in res.keys():
            res [compositor].append(nome)
        else:
            res [compositor] = [nome]
    return res



    

