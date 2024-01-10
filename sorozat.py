import random

def lotto():
    lista=[]
    lista_szoveg=""


    for i in range(0,5,1):
        szam=random.randint(1,99)
        if i < 4:
            lista_szoveg+=str(szam) + ";"
        else:
            lista_szoveg+=str(szam)

    lista.append(lista_szoveg)
    return lista

def egyjegyuek_szama(lista):
    kiiras:str=""
    lista=lista[0].split(";")
    b=0
    for i in range(0, len(lista),1):
        if int(lista[i])>0 and int(lista[i])<10:
            b+=1
        i+=1
    kiiras=f"\tEgyjegyűek száma: {b}."
    return kiiras

def konzol_kiir(kiiras):
    print(kiiras)

def file_kiir(kiiras):
    fajl=open("szamok.txt","w",encoding="utf-8")
    fajl.write("2/F:\n")
    fajl.write(kiiras)
    fajl.close()





