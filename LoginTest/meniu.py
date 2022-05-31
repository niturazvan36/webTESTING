from testare import TestingLexforce

class Interfata:
    def __init__(self):
        path = input("Introdu adresa catre webdriver-ul folosit: ")
        username = input("Introdu numele de utilizator: ")
        parola = input("Introdu parola: ")
        self.clasa_testare = TestingLexforce(path, username, parola)

    def interpretare_teste(self, lista: list):

        self.clasa_testare.switch_frame("menu_frame_id")
        for i in lista:
            if i == 1:
                self.clasa_testare.calendar_menu()
            elif i == 2:
                self.clasa_testare.clienti_menu()
            elif i == 3:
                self.clasa_testare.contracte_menu()
            elif i == 4:
                self.clasa_testare.facturi_menu()
            elif i == 5:
                self.clasa_testare.dosare_menu()
            elif i == 6:
                self.clasa_testare.termene_menu()
            elif i == 7:
                self.clasa_testare.operatii_menu()
            elif i == 8:
                self.clasa_testare.resurse_umane_menu()
            elif i == 9:
                self.clasa_testare.sesiuni_cronometrare()
    def meniu_navigare(self):
        ans = True
        lista_teste = []
        while ans:
            print("""
                1.Meniu calendar
                2.Meniu Clienti
                3.Meniu Contracte
                4.Meniu Facturi
                5.Meniu Dosare
                6.Meniu Termene
                7.Meniu Operatii
                8.Meniu Resurse Umane
                9.Meniu Sesiuni Cronometrare
                10.Ruleaza Testul.
                11.Inapoi.
                """)
            ans = input("Introdu o actiune specificand numarul ei: ")
            if ans == "1":
                lista_teste.append(1)
            elif ans == "2":
                lista_teste.append(2)
            elif ans == "3":
                lista_teste.append(3)
            elif ans == "4":
                lista_teste.append(4)
            elif ans == "5":
                lista_teste.append(5)
            elif ans == "6":
                lista_teste.append(6)
            elif ans == "7":
                lista_teste.append(7)
            elif ans == "8":
                lista_teste.append(8)
            elif ans == "9":
                lista_teste.append(9)
            elif ans == "10":
                self.interpretare_teste(lista_teste)
                lista_teste.clear()
            elif ans == "11":
                ans = None
            else:
                print("\n Alegere invalida.")


    def interpretare_teste_functii(self, lista):
        for element in lista:
            if int(element[0]) == 1:
                self.clasa_testare.adauga_persoana_fizica(element[1], element[2], element[3])
            elif int(element[0]) == 2:
                self.clasa_testare.adauga_persoana_juridica(element[1], element[2], element[3])
            elif int(element[0]) == 3:
                self.clasa_testare.adauga_contract_pf(element[1], element[2], element[3])
            elif int(element[0]) == 4:
                self.clasa_testare.adauga_contract_pj(element[1], element[2], element[3])
            elif int(element[0]) == 5:
                self.clasa_testare.emitere_facturi_contract(element[1], element[2])
            elif int(element[0]) == 6:
                self.clasa_testare.emitere_facturi_client(element[1], element[2])
            elif int(element[0]) == 7:
                self.clasa_testare.termene_noi(element[1], element[2])
            elif int(element[0]) == 8:
                self.clasa_testare.sarcina_noua(element[1], element[2])
            elif int(element[0]) == 9:
                self.clasa_testare.adauga_operatie(element[1], element[2])

    def meniu_functii(self):
        ans = True
        lista_teste = []
        while ans:
            print("""
                1.Adauga persoana fizica
                2.Adauga persoana juridica
                3.Adauga contract persoana fizica
                4.Adauga contract persoana juridica
                5.Adauga emitere facturi contract
                6.Adauga emitere facturi clienti
                7.Adauga termene noi
                8.Adauga sarcina noua
                9.Adauga operatie
                10.Ruleaza Testul.
                11.Preia testele din fisier
                12.Inapoi.
                """)
            ans = input("Introdu o actiune specificand numarul ei: ")
            if ans == "1":
                nume = input("Introdu numele: ")
                data = input("Introdu data nastere (ZZ/LL/AAAA): ")
                oras = input("Introdu oras companie: ")
                lista_teste.append((1,nume, data, oras))
            elif ans == "2":
                nume = input("Introdu numele companiei: ")
                data = input("Introdu data nastere (ZZ/LL/AAAA): ")
                oras = input("Introdu oras companie: ")
                lista_teste.append((2, nume, data, oras))
            elif ans == "3":
                nume = input("Introdu numele: ")
                data = input("Introdu data nastere (ZZ/LL/AAAA): ")
                oras = input("Introdu oras companie: ")
                lista_teste.append((3, nume, data, oras))
            elif ans == "4":
                nume = input("Introdu numele companiei: ")
                data = input("Introdu data nastere (ZZ/LL/AAAA): ")
                oras = input("Introdu oras companie: ")
                lista_teste.append((4, nume, data, oras))
            elif ans == "5":
                valoare  = input("Introdu o valoare (numar): ")
                den_prod = input("Introdu denumire produs: ")
                lista_teste.append((5, valoare, den_prod))
            elif ans == "6":
                valoare = input("Introdu o valoare (numar): ")
                den_prod = input("Introdu denumire produs: ")
                lista_teste.append((6, valoare, den_prod))
            elif ans == "7":
                data = input("Introdu data termen (ZZ/LL/AAAA): ")
                ora = input("Introdu ora termen (HH:MM): ")
                lista_teste.append((7, data, ora))
            elif ans == "8":
                titlu = input("Introdu titlu sarcina: ")
                descriere = input("Introdu descriere: ")
                lista_teste.append((8, titlu, descriere))
            elif ans == "9":
                nume = input("Introdu nume operatie: ")
                fee = input("Introdu valoare plata: ")
                lista_teste.append((9, nume, fee))
            elif ans == "10":
                self.interpretare_teste_functii(lista_teste)
                lista_teste.clear()
            elif ans == "11":
                self.filepath = input("Introdu adresa catre fisierul cu teste (adresa absoluta): ")
                with open(self.filepath, "r") as fileObject:
                    aux = fileObject.read().split("\n")
                    for i in aux:
                        aux_tuple = i.split(",")
                        lista_teste.append(tuple(aux_tuple))
                print(lista_teste)

            elif ans == "12":
                ans = None
            else:
                print("\n Alegere invalida.")


    def meniu_principal(self):
        ans = True
        while ans:
            print("""
            1.Testare Navigare meniu.
            2.Testare Functii Website.
            3.Iesire.
            """)
            ans = input("Alege o actiune:  ")

            if ans == "1":
                self.meniu_navigare()
            elif ans == "2":
                self.meniu_functii()
            elif ans == "3":
                print("\n La revedere.")
                ans = None
            else:
                print("\n Alegere Invalida")
