
def auto():
    auto_neve:str=str(input("Kérem, adja meg az autó nevét!"))
    gyartasi_datum:int=int(input("Kérem, adja meg a gyártási dátumot!"))
    print("")
    print(f"\t Autó neve:{auto_neve}")
    print(f"\t Gyártási dátum:{gyartasi_datum}")

    if gyartasi_datum == 2024:
        print(f"\t Ez a(z){auto_neve} friss gyártás")
    elif gyartasi_datum < 2000:
        print(f"\t Ez a(z){auto_neve} öreg autó")
    elif 2000 <= gyartasi_datum <= 2024:
        print(f"\t Ez a(z){auto_neve} átlagos korú")

    


