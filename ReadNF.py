import os, sys
import random
dirpath = os.path.realpath(__file__)
dir_up = os.path.dirname(os.path.dirname(dirpath))
print(dir_up)
sys.path.append(dir_up)

def ReadNFFile():
    re_path = os.path.abspath(os.getcwd())
    re_path = str(re_path)
    arquivo = open('{}\\Notas.csv'.format(re_path),'r', encoding='utf-8')
    linhas = arquivo.readlines()

    notas = []
    cont = 0
    for i in linhas:
        if cont == 0:
            cont+=1
            continue
        nota = i.strip('\n').split(',')
        notas.append(nota)
        
        cont+=1
    return notas

def ReturnNfInformations():
    notas  = ReadNFFile()
    nfs_to_close = []
    for nota in notas:
        array_nota = nota[0].split(';')
        if array_nota[5] == 'ENTREGA REALIZADA':
            nfs_to_close.append(nota)
    nfs = {
        "nfs_to_close": nfs_to_close,
        'nfs' : notas,
        'total_nfs' : len(notas)
    }
    return nfs

ReturnNfInformations()