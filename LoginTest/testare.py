from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from datetime import datetime

import csv
import os
import time


class TestingLexforce:
    def __init__(self, path: str, username: str, password: str):
        """Constructorul clasei de testare in care trebuie specificat adresa unde este webdriver-ul stocat,
        numele de utilizator si parola folosite pentru autentificarea pe site"""


        self.filename = "Test" + datetime.now().strftime("%d-%m-%Y-%H-%M-%S") +".txt"
        print(self.filename)

        #Completarea campurilor provenite de la utilizator si initializarea driver-urului

        self.path = path
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(self.path)
        self.driver.get('http://demo.lexforce.ro/lexforce_new/login.php')


        #Cautarea elementelor HTML pentru completarea campulurilor, si completarea lor propriu-zis

        utilizator = self.driver.find_element(By.ID,"username")
        parola = self.driver.find_element(By.ID,"password")
        autentificare = self.driver.find_element(By.ID,"bid-ok")
        utilizator.send_keys(username)
        parola.send_keys(password)
        autentificare.click()
        with open(self.filename, "w") as fileObject:
            fileObject.write("----------\n")
            fileObject.write("Test started with:\n")
            fileObject.write("Username: "+ self.username + "\n")
            fileObject.write("Password: "+ self.password+ "\n")
            fileObject.write("Path of driver: "+ self.path+ "\n")




    def switch_frame(self, frame_name):
        """Functie pentru a schimba frame-ul principal al paginii care este testata"""


        try:
            self.driver.switch_to.frame(f"{frame_name}")
        except:
            print("No frames were found")

    def calendar_menu(self):
        """Functie pentru accesarea meniului calendar"""

        try:
            self.driver.find_element(
                By.CSS_SELECTOR, 'a[href*="calendar"').click()
            print("Calendar menu accessed")
            time.sleep(2)
        except:
            print("Couldn't press calendar button")

    def clienti_menu(self):
        """Functie pentru accesarea meniului clienti"""

        try:
            self.driver.find_element(
                By.CSS_SELECTOR, 'a[href*="clients"').click()
            print("Clients menu accessed")
            time.sleep(2)
        except:
            print("Couldn't press clients button")

    def contracte_menu(self):
        """Functie pentru accesarea meniului contracte"""


        try:
            self.driver.find_element(
                By.CSS_SELECTOR, 'a[href*="contracts"').click()
            print("Contracts menu accessed")
            time.sleep(2)
        except:
            print("Couldn't press contracts button")

    def facturi_menu(self):
        """Functie pentru accesarea meniului facturi"""

        try:
            self.driver.find_element(
                By.CSS_SELECTOR, 'a[href*="invoices"').click()
            print("invoices menu accessed")
            time.sleep(2)
        except:
            print("Couldn't press invoices button")

    def dosare_menu(self):
        """Functie pentru accesarea meniului dosare"""
        try:
            self.driver.find_element(
                By.CSS_SELECTOR, 'a[href*="cases"').click()
            print("cases menu accessed")
            time.sleep(2)
        except:
            print("Couldn't press cases button")

    def termene_menu(self):
        """Functie pentru accesarea meniului termenului"""
        try:
            self.driver.find_element(
                By.CSS_SELECTOR, 'a[href*="cases/terms"').click()
            print("cases/terms menu accessed")
            time.sleep(2)
        except:
            print("Couldn't press cases/terms button")

    def operatii_menu(self):
        """Functie pentru accesarea meniului operatii"""
        try:
            self.driver.find_element(
                By.CSS_SELECTOR, 'a[href*="operations/operations"').click()
            print("operations/operations menu accessed")
            time.sleep(2)
        except:
            print("Couldn't press operations/operations button")

    def resurse_umane_menu(self):
        """Functie pentru accesarea meniului resurse umane"""
        try:
            self.driver.find_element(
                By.CSS_SELECTOR, 'a[href*="documents/leave"').click()
            print("documents/leave menu accessed")
            time.sleep(2)
        except:
            print("Couldn't press documents/leave button")

    def sesiuni_cronometrare(self):
        """Functie pentru accesarea meniului sesiuni cronometrare"""
        try:
            self.driver.find_element(
                By.CSS_SELECTOR, 'a[href*="timing_session"').click()
            print("timing_session menu accessed")
            time.sleep(2)
        except:
            print("Couldn't timing_session cases button")

    def adauga_contract(self):
        """Functie pentru accesarea functiei de adaugare contract"""
        try:
            self.driver.find_element(By.ID, "btn_add_contract").click()
            time.sleep(2)
        except:
            print("no btn was found")


    def adauga_persoana_juridica(self, nume_companie: str, data_nastere: str, oras_companie: str):
        """Functie pentru testarea functionarii corecte a functiei de adaugare persoana juridica."""

        try:
            self.switch_frame("menu_frame_id")
            self.clienti_menu()
            self.driver.switch_to.parent_frame()
            self.driver.switch_to.frame("a")
            self.driver.find_element(By.ID, "btn_add_client_pj").click()
            company_name = self.driver.find_element(By.ID, "company_name")
            company_name.send_keys(nume_companie)
            time.sleep(2)

            # TESTARE BUTON DE TIP CHECKBOX
            active = self.driver.find_element(By.ID, "active")
            active.click()
            time.sleep(2)
            # INCHEIEREA TESTARII BUTONULUI DE TIP CHECKBOX


            data = self.driver.find_element(By.ID, "rep_birth_date")
            data.send_keys(data_nastere)
            time.sleep(2)

            optiuni = self.driver.find_element(By.ID, "company_county")
            for option in optiuni.find_elements_by_tag_name('option'):
                if option.text == oras_companie:
                    option.click()
            time.sleep(2)

            with open(self.filename, "a") as fileObject:
                fileObject.write("\n")
                fileObject.write("Adauga persoana juridica cu parametrii "+
                                 nume_companie + " " +
                                 data_nastere + " " +
                                 oras_companie + " " +
                                 "testat cu succes.")
            self.driver.switch_to.parent_frame()
            self.switch_frame("menu_frame_id")
            self.calendar_menu()


        except:
            with open(self.filename, "a") as fileObject:
                fileObject.write("\n")
                fileObject.write("Adauga persoana juridica cu parametrii "+
                                 nume_companie + " " +
                                 data_nastere + " " +
                                 oras_companie + " " +
                                 "testat cu eroare.")
            print("Error at PERSOANA JURIDICA")

    def adauga_persoana_juridica_boilerplate(self, nume_companie: str, data_nastere: str, oras_companie: str):
        try:
            self.driver.find_element(By.ID, "btn_add_client_pj").click()
            company_name = self.driver.find_element(By.ID, "company_name")
            company_name.send_keys(nume_companie)
            time.sleep(2)

            active = self.driver.find_element(By.ID, "active")
            active.click()
            time.sleep(2)

            data = self.driver.find_element(By.ID, "rep_birth_date")
            data.send_keys(data_nastere)
            time.sleep(2)

            optiuni = self.driver.find_element(By.ID, "company_county")
            for option in optiuni.find_elements_by_tag_name('option'):
                if option.text == oras_companie:
                    option.click()
            time.sleep(2)
        except:
            print("error at PERSOANA JURIDICA BOILERPLATE")

    def adauga_persoana_fizica_boilerplate(self, nume_persoana: str, data_nastere: str, oras: str):
        try:
            self.driver.find_element(By.ID, "btn_add_client_pf").click()
            name = self.driver.find_element(By.ID, "name")
            name.send_keys(nume_persoana)
            time.sleep(2)

            #TESTARE BUTON DE TIP CHECKBOX
            active = self.driver.find_element(By.ID, "active")
            active.click()
            time.sleep(2)
            #INCHEIEREA TESTARII

            data = self.driver.find_element(By.ID, "birth_date")
            data.send_keys(data_nastere)
            time.sleep(2)

            optiuni = self.driver.find_element(By.ID, "county")
            for option in optiuni.find_elements_by_tag_name('option'):
                if option.text == oras:
                    option.click()
            time.sleep(3)
        except:
            print("error at PERSOANA FIZICA BOILERPLATE")

    def adauga_persoana_fizica(self, nume: str, data_nastere: str, oras):
        try:
            self.switch_frame("menu_frame_id")
            self.clienti_menu()
            self.driver.switch_to.parent_frame()
            self.driver.switch_to.frame("a")
            self.driver.find_element(By.ID, "btn_add_client_pf").click()
            name = self.driver.find_element(By.ID, "name")
            name.send_keys(nume)
            time.sleep(2)


            #TESTARE BUTON DE TIP CHECKBOX
            active = self.driver.find_element(By.ID, "active")
            active.click()
            time.sleep(2)
            #INCHEIERA TESTARII

            data = self.driver.find_element(By.ID, "birth_date")
            data.send_keys(data_nastere)
            time.sleep(2)

            optiuni = self.driver.find_element(By.ID, "county")
            for option in optiuni.find_elements_by_tag_name('option'):
                if option.text == oras:
                    option.click()
            time.sleep(3)

            with open(self.filename, "a") as fileObject:
                fileObject.write("\n")
                fileObject.write("Adauga persoana fizica cu parametrii "+
                                 nume + " " +
                                 data_nastere + " " +
                                 oras + " " +
                                 "testat cu succes.")


            self.driver.switch_to.parent_frame()
            self.switch_frame("menu_frame_id")
            self.calendar_menu()

        except:
            with open(self.filename, "a") as fileObject:
                fileObject.write("\n")
                fileObject.write("Adauga persoana fizica cu parametrii "+
                                 nume + " " +
                                 data_nastere + " " +
                                 oras + " " +
                                 "testat cu eroare.")
            print("error at PERSOANA FIZICA")

    def adauga_contract_pf(self, nume_persoana: str, data_nastere: str, oras: str):
        try:
            self.switch_frame("menu_frame_id")
            self.contracte_menu()
            self.driver.switch_to.parent_frame()
            self.driver.switch_to.frame("a")
            time.sleep(2)
            buton_contract = self.driver.find_element(By.ID, "btn_add_contract")
            buton_contract.click()
            time.sleep(2)
            self.adauga_persoana_fizica_boilerplate(nume_persoana, data_nastere, oras)
            self.driver.switch_to.parent_frame()
            with open(self.filename, "a") as fileObject:
                fileObject.write("\n")
                fileObject.write("Adauga contract persoana fizica cu parametrii "+
                                 nume_persoana + " " +
                                 data_nastere + " " +
                                 oras + " " +
                                 "testat cu succes.")
            self.switch_frame("menu_frame_id")
            self.calendar_menu()
        except:
            with open(self.filename, "a") as fileObject:
                fileObject.write("\n")
                fileObject.write("Adauga contract persoana fizica cu parametrii "+
                                 nume_persoana + " " +
                                 data_nastere + " " +
                                 oras + " " +
                                 "testat cu succes.")
            print("error at CONTRACT PERSOANA FIZICA")

    def adauga_contract_pj(self, nume_companie: str, data_nastere: str, oras_companie: str):
        try:
            self.switch_frame("menu_frame_id")
            self.contracte_menu()
            self.driver.switch_to.parent_frame()
            self.driver.switch_to.frame("a")
            buton_contract = self.driver.find_element(By.ID, "btn_add_contract")
            buton_contract.click()
            time.sleep(2)
            self.adauga_persoana_juridica_boilerplate(nume_companie, data_nastere, oras_companie)
            with open(self.filename, "a") as fileObject:
                fileObject.write("\n")
                fileObject.write("Adauga contract persoana juridica cu parametrii "+
                                 nume_companie + " " +
                                 data_nastere + " " +
                                 oras_companie + " " +
                                 "testat cu succes.")
            self.driver.switch_to.parent_frame()
            self.switch_frame("menu_frame_id")
            self.calendar_menu()
        except:
            with open(self.filename, "a") as fileObject:
                fileObject.write("\n")
                fileObject.write("Adauga contract persoana juridica cu parametrii "+
                                 nume_companie + " " +
                                 data_nastere + " " +
                                 oras_companie + " " +
                                 "testat cu eroare.")
            print("error at CONTRACT PERSOANA JURIDICA")

    def emitere_facturi_contract(self, valoare_param: str, denumire_produse: str):
        self.switch_frame("menu_frame_id")
        self.facturi_menu()
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame("a")
        buton_facturi = self.driver.find_element(By.CLASS_NAME, "largeActionBtn")
        buton_facturi.click()
        try:
            time.sleep(2)
            self.driver.find_element(By.CSS_SELECTOR, 'a[href*="id="').click()
            optiuni = self.driver.find_element(By.ID,"invoice_tva")
            for index, option in enumerate(optiuni.find_elements_by_tag_name('option')):
                if(index == 1):
                    option.click()
                    time.sleep(1)

            optiuni = self.driver.find_element(By.ID, "society_address")
            for index, option in enumerate(optiuni.find_elements_by_tag_name('option')):
                if (index == 1):
                    option.click()
                    time.sleep(1)

            optiuni = self.driver.find_element(By.ID, "client_delegate_select")
            for index, option in enumerate(optiuni.find_elements_by_tag_name('option')):
                if (index == 1):
                    option.click()
                    time.sleep(1)

            valoare = self.driver.find_element(By.ID, "invoice_entries_value_3")
            valoare.send_keys(valoare_param)
            time.sleep(2)
            denumirea_produselor = self.driver.find_element(By.ID, "invoice_entries_represent_3")
            denumirea_produselor.send_keys(denumire_produse)

            with open(self.filename, "a") as fileObject:
                fileObject.write("\n")
                fileObject.write("Emitere factura contract cu parametrii "+
                                 valoare_param + " " +
                                 denumire_produse + " " +
                                 "testat cu succes.")
            time.sleep(2)
        except:
            with open(self.filename, "a") as fileObject:
                fileObject.write("\n")
                fileObject.write("Emitere factura contract cu parametrii "+
                                 valoare_param + " " +
                                 denumire_produse + " " +
                                 "testat cu eroare.")
            print("error at EMITERE FACTURI CONTRACT")

        self.driver.switch_to.parent_frame()
        self.switch_frame("menu_frame_id")
        self.calendar_menu()

    def emitere_facturi_client(self, val: str, denumire_produse: str):
        self.switch_frame("menu_frame_id")
        self.facturi_menu()
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame("a")
        time.sleep(2)
        buton_facturi = self.driver.find_element(By.CLASS_NAME, "largeActionBtn")
        buton_facturi.click()
        time.sleep(2)
        buton_facturi_client = self.driver.find_element(By.CLASS_NAME, "largeActionBtn")
        buton_facturi_client.click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, 'a[href*="id="').click()
        try:
            optiuni = self.driver.find_element(By.ID,"invoice_tva")
            for index, option in enumerate(optiuni.find_elements_by_tag_name('option')):
                if(index == 1):
                    option.click()
                    time.sleep(1)

            optiuni = self.driver.find_element(By.ID, "society_address")
            for index, option in enumerate(optiuni.find_elements_by_tag_name('option')):
                if (index == 1):
                    option.click()
                    time.sleep(1)

            optiuni = self.driver.find_element(By.ID, "client_delegate_select")
            for index, option in enumerate(optiuni.find_elements_by_tag_name('option')):
                if (index == 1):
                    option.click()
                    time.sleep(1)

            valoare = self.driver.find_element(By.ID, "invoice_entries_value_3")
            valoare.send_keys(val)
            time.sleep(1)
            denumirea_produselor = self.driver.find_element(By.ID, "invoice_entries_represent_3")
            denumirea_produselor.send_keys(denumire_produse)
            time.sleep(1)

            with open(self.filename, "a") as fileObject:
                fileObject.write("\n")
                fileObject.write("Emitere factura client cu parametrii "+
                                 val + " " +
                                 denumire_produse + " " +
                                 "testat cu succes.")
        except:
            with open(self.filename, "a") as fileObject:
                fileObject.write("\n")
                fileObject.write("Emitere factura client cu parametrii "+
                                 val + " " +
                                 denumire_produse + " " +
                                 "testat cu eroare.")
            print("error at EMITERE FACTURI CLIENT")
        self.driver.switch_to.parent_frame()
        self.switch_frame("menu_frame_id")
        self.calendar_menu()

    def termene_noi(self, data_termen_param: str, ora_termen_param: str):
        try:
            self.switch_frame("menu_frame_id")
            self.dosare_menu()
            self.driver.switch_to.parent_frame()
            self.driver.switch_to.frame("a")
            time.sleep(2)
            self.driver.find_element(By.CSS_SELECTOR, 'a[href*="manage_term"').click()
            time.sleep(2)
            data_termen = self.driver.find_element(By.ID, "term_term")
            data_termen.send_keys(data_termen_param)
            time.sleep(1)
            ora_termen = self.driver.find_element(By.ID, "hour")
            ora_termen.send_keys(ora_termen_param)
            time.sleep(1)
            with open(self.filename, "a") as fileObject:
                fileObject.write("\n")
                fileObject.write("Emitere factura client cu parametrii "+
                                 data_termen_param + " " +
                                 ora_termen_param + " " +
                                 "testat cu succes.")
            self.driver.switch_to.parent_frame()
            self.switch_frame("menu_frame_id")
            self.calendar_menu()
        except:
            with open(self.filename, "a") as fileObject:
                fileObject.write("\n")
                fileObject.write("Adaugare termene noi cu parametrii "+
                                 data_termen_param + " " +
                                 ora_termen_param + " " +
                                 "testat cu eroare.")
            print("error at TERMENE NOI")

    def sarcina_noua(self, titlu_param:str, descriere_param: str):
        try:
            self.switch_frame("menu_frame_id")
            self.calendar_menu()
            self.driver.switch_to.parent_frame()
            self.driver.switch_to.frame("a")
            time.sleep(2)
            self.driver.find_element(By.CLASS_NAME, "tab_element_active").click()
            buton_sarcina = self.driver.find_element(By.CLASS_NAME, "largeBtnAreaTitle")
            buton_sarcina.click()
            time.sleep(1)
            titlu = self.driver.find_element(By.ID, "todo_title")
            titlu.send_keys(titlu_param)
            time.sleep(1)
            optiuni = self.driver.find_element(By.ID, "todo_status")
            for index, option in enumerate(optiuni.find_elements_by_tag_name('option')):
                if (index == 1):
                    option.click()
                    time.sleep(1)

            optiuni = self.driver.find_element(By.ID, "todo_priority")
            for index, option in enumerate(optiuni.find_elements_by_tag_name('option')):
                if (index == 1):
                    option.click()
                    time.sleep(1)

            descriere = self.driver.find_element(By.ID, "todo_description")
            descriere.send_keys(descriere_param)
            time.sleep(1)
            with open(self.filename, "a") as fileObject:
                fileObject.write("\n")
                fileObject.write("Adaugare sarcina noua cu parametrii "+
                                 titlu_param + " " +
                                 descriere_param + " " +
                                 "testat cu succes.")
        except:
            with open(self.filename, "a") as fileObject:
                fileObject.write("\n")
                fileObject.write("Adaugare sarcina noua cu parametrii "+
                                 titlu_param + " " +
                                 descriere_param + " " +
                                 "testat cu eroare.")
            print("error at SARCINA NOUA")
        self.driver.switch_to.parent_frame()
        self.switch_frame("menu_frame_id")
        self.calendar_menu()

    def adauga_operatie(self, nume_operatie: str, fee_param: str):
        try:
            self.switch_frame("menu_frame_id")
            self.operatii_menu()
            self.driver.switch_to.parent_frame()
            self.driver.switch_to.frame("a")
            time.sleep(2)
            self.driver.find_element(By.ID, "btn_add_operation").click()
            time.sleep(2)
            self.driver.find_element(By.CSS_SELECTOR, "a[href*='id=' ").click()
            time.sleep(2)

            operation_name = self.driver.find_element(By.ID, "operation_name")
            operation_name.send_keys(nume_operatie)
            time.sleep(2)

            fee = self.driver.find_element(By.ID, "fee")
            fee.clear()
            fee.send_keys(fee_param)
            time.sleep(2)

            with open(self.filename, "a") as fileObject:
                fileObject.write("\n")
                fileObject.write("Adaugare operatie cu parametrii "+
                                 nume_operatie + " " +
                                 fee_param + " " +
                                 "testat cu succes.")

            self.driver.switch_to.parent_frame()
            self.switch_frame("menu_frame_id")
            self.calendar_menu()

        except:
            with open(self.filename, "a") as fileObject:
                fileObject.write("\n")
                fileObject.write("Adaugare operatie cu parametrii "+
                                 nume_operatie + " " +
                                 fee_param + " " +
                                 "testat cu eroare.")
            print("error at ADAUGA OPERATIE")

