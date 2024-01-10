import bevezetes
import sorozat

print("1/A,B")
bevezetes.auto()

print("2/A,B,C")
lista=sorozat.lotto()
print(f"\t{lista}")

print("")
print("2/D,E")
kiiras=sorozat.egyjegyuek_szama(lista)
sorozat.konzol_kiir(kiiras)

sorozat.file_kiir(kiiras)



