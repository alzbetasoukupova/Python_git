# ZADANI

# Tvým úkolem je vytvořit program pro zjednodušený výpočet daně z nemovitostí. Aplikace bude postavená na principech OOP. Tato daň se vztahuje na pozemky, bytové a komerční prostory.
# Výše daně se odvíjí od několika faktorů, např. typu nemovitosti, velikosti, lokalitě, kde se nemovitost nachází atd.

# V rámci aplikace nejprve vytvoř třídu Locality, která označuje lokalitu, kde se nemovitost nachází.
# Třída bude mít atributy name (název katastru/obce) a locality_coefficient (tzv. místní koeficient, který se používá k výpočtu daně).

import math

class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name
        self.locality_coefficient = locality_coefficient

# Vytvoř třídu Property, která bude reprezentovat nějakou nemovitost. Třída bude mít atribut locality (lokalita, kde se pozemek nachází, bude to objekt třídy Locality).
class Property:
    def __init__(self, locality):
        self.locality = locality

# Dále vytvoř třídu Estate, která reprezentuje pozemek a je potomkem třídy Property.
# Třída bude mít atributy locality, estate_type (typ pozemku), area (plocha pozemku v metrech čtverečních). 
class Estate(Property):
    def __init__(self, locality, estate_type, area):
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area

#Dále přidej metodu calculate_tax(),která spočítá výši daně pro pozemek a vrátí hodnotu jak celé číslo (pro zaokrouhlení použij funkci ceil() z modulu math).
# Daň vypočítej pomocí vzorce: plocha pozemku * koeficient dle typu pozemku (atribut estate_type) * místní koeficient. U atributu estate_type následující hodnoty a koeficienty:

# - land (zemědělský pozemek) má koeficient 0.85.
# - building site (stavební pozemek) má koeficient 9.
# - forrest (les) má koeficient 0.35,
# - garden (zahrada) má koeficient 2.

    def calculate_tax(self):
        coefficients = {
            "land": 0.85,
            "building site": 9,
            "forrest": 0.35,
            "garden": 2
        }
        estate_coefficient = coefficients.get(self.estate_type)
        tax = self.area * estate_coefficient * self.locality.locality_coefficient
        return math.ceil(tax)
    
# Uvažujme tedy například lesní pozemek o ploše 500 metrů čtverečních v lokalitě s místním koeficientem 2. Potom je daň 500 * 0.35 * 2 = 350.   
Neratovice = Locality("Neratovice", 2)
estate1 = Estate(Neratovice, "forrest", 500)
print(f"Daň z daného pozemku je {estate1.calculate_tax()} Kč.")

# Vytvoř třídu Residence, která reprezentuje byt, dům či jinou stavbu a je potomkem třídy Property.
# Třída bude mít atributy locality, area (podlahová plocha bytu nebo domu) a commercial (pravdivostní hodnota, která určuje, zda se jedná o nemovitost používanou k podnikání).
class Residence(Property):
    def __init__(self, locality, area, commercial):
        super().__init__(locality)
        self.area = area
        self.commercial = commercial

# Dále přidej metodu calculate_tax(), která spočítá výši daně pro byt a vrátí hodnotu jako číslo.
# Daň vypočítej pomocí vzorce: podlahová plocha * koeficient lokality * 15. Pokud je hodnota parametru commercial True, tj. pokud jde o komerční nemovitost, vynásob celou daň číslem 2.
    def calculate_tax(self):
        tax = self.area *  self.locality.locality_coefficient * 15
        if self.commercial:
            tax = tax * 2
        return math.ceil(tax)
    
# Příklad výpočtu: Uvažujme tedy například byt (určený k bydlení) o ploše 60 metrů čtverečních v lokalitě s koeficientem 3. Potom je daň 60 * 3 * 15 = 2700.
Praha = Locality("Praha", 3)
residence1 = Residence(Praha, 60, False)
print(f"Daň z daného pozemku je {residence1.calculate_tax()} Kč.")

# Pokud by stejný byt byl používán k podnikání, daň by byla 60 * 3 * 15 * 2 = 5400.
residence2 = Residence(Praha, 60, True)
print(f"Daň z daného pozemku je {residence2.calculate_tax()} Kč.")

# Vyzkoušej svůj program pomocí následujících nemovitostí:

Manetin = Locality("Manětín", 0.8)
Brno = Locality ("Brno", 3)

# - Zemědělský pozemek o ploše 900 metrů čtverečních v lokalitě Manětín s koeficientem 0.8. Daň z této nemovitosti je 900 * 0.85 * 0.8 = 612.
estate2 = Estate(Manetin,"land", 900)
print(f"Daň z daného pozemku je {estate2.calculate_tax()} Kč.")
# - Dům s podlahovou plochou 120 metrů čtverečních v lokalitě Manětín s koeficientem 0.8. Daň z této nemovitosti je 120 * 0.8 * 15 = 1440.
residence3 = Residence(Manetin, 120, False)
print(f"Daň z daného pozemku je {residence3.calculate_tax()} Kč.")
# - Kancelář (tj. komerční nemovitost) s podlahovou plochou 90 metrů čtverečních v lokalitě Brno s koeficientem 3. Daň z této nemovitosti je 90 * 3 * 15 * 2 = 8100.
residence4 = Residence(Brno, 90, True)
print(f"Daň z daného pozemku je {residence4.calculate_tax()} Kč.")



# BONUSY

# Tyto bonusy jsou nepovinné a záleží čistě na tobě, zda se do nich pustíš. Jednotlivé části jsou nezávislé, můžeš si tedy vybrat libovolné odrážky a ty vyřešit.

# - Ke třídě Estate a Residence přidej výpisy informací do metody __str__(). Např.: Zemědělský pozemek, lokalita Manětín (koeficient 1), 900 metrů čtverečních, daň 765 Kč.

# - Uprav třídu Property na abstraktní třídu. Tato třída totiž nereprezentuje žádnou konkrétní nemovitost, nemovitost totiž musí být pozemek nebo stavba.
import math

class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name
        self.locality_coefficient = locality_coefficient

#uprava puvodniho kodu
from abc import ABC, abstractmethod
class Property(ABC):
    def __init__(self, locality):
        self.locality = locality
    @abstractmethod
    def calculate_tax(self):
        pass
#konec upravy
class Estate(Property):
    def __init__(self, locality, estate_type, area):
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area
    def calculate_tax(self):
        coefficients = {
            "land": 0.85,
            "building site": 9,
            "forrest": 0.35,
            "garden": 2
        }
        estate_coefficient = coefficients.get(self.estate_type)
        tax = self.area * estate_coefficient * self.locality.locality_coefficient
        return math.ceil(tax)
    
class Residence(Property):
    def __init__(self, locality, area, commercial):
        super().__init__(locality)
        self.area = area
        self.commercial = commercial
    def calculate_tax(self):
        tax = self.area *  self.locality.locality_coefficient * 15
        if self.commercial:
            tax = tax * 2
        return math.ceil(tax)

Manetin = Locality("Manětín", 0.8)
Brno = Locality ("Brno", 3)

estate2 = Estate(Manetin,"land", 900)
print(f"Daň z daného pozemku je {estate2.calculate_tax()} Kč.")

residence3 = Residence(Manetin, 120, False)
print(f"Daň z daného pozemku je {residence3.calculate_tax()} Kč.")

residence4 = Residence(Brno, 90, True)
print(f"Daň z daného pozemku je {residence4.calculate_tax()} Kč.")

# Přidej třídu TaxReport, která bude reprezentovat daňové přiznání.
# Třída bude mít atributy name (jméno osoby, která přiznání podává) a property_list, což je seznam nemovitostí, které jsou v přiznání uvedeny.
# Dále přidej metodu add_property(), která bude mít jako parametr objekt (nemovitost, která je součástí přiznání) a vloží ji do seznamu property_list.
# Dále přidej metodu calculate_tax(), která vypočte daň ze všech nemovitostí v seznamu property_list.

import math

class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name
        self.locality_coefficient = locality_coefficient

class Property:
    def __init__(self, locality):
        self.locality = locality

class Estate(Property):
    def __init__(self, locality, estate_type, area):
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area
    def calculate_tax(self):
        coefficients = {
            "land": 0.85,
            "building site": 9,
            "forrest": 0.35,
            "garden": 2
        }
        estate_coefficient = coefficients.get(self.estate_type)
        tax = self.area * estate_coefficient * self.locality.locality_coefficient
        return math.ceil(tax)
    
class Residence(Property):
    def __init__(self, locality, area, commercial):
        super().__init__(locality)
        self.area = area
        self.commercial = commercial
    def calculate_tax(self):
        tax = self.area *  self.locality.locality_coefficient * 15
        if self.commercial:
            tax = tax * 2
        return math.ceil(tax)
    
#uprava puvodniho kodu
class TaxReport:
    def __init__(self, name):
        self.name = name
        self.property_list = []

    def add_property(self, property):
        self.property_list.append(property)

    def calculate_tax(self):
        total_tax = 0
        for property in self.property_list:
            total_tax += property.calculate_tax()
        return total_tax
#konec upravy

Manetin = Locality("Manětín", 0.8)
Brno = Locality ("Brno", 3)

estate2 = Estate(Manetin,"land", 900)
print(f"Daň z daného pozemku je {estate2.calculate_tax()} Kč.")

residence3 = Residence(Manetin, 120, False)
print(f"Daň z daného pozemku je {residence3.calculate_tax()} Kč.")

residence4 = Residence(Brno, 90, True)
print(f"Daň z daného pozemku je {residence4.calculate_tax()} Kč.")

#novy vysledek pro danove priznani
tax_report = TaxReport("Jan Dvořák")
tax_report.add_property(residence3)

total_tax = tax_report.calculate_tax()
print(f"Celková daň pro {tax_report.name} je {total_tax} Kč.")

# - Podívej se na to, jak fungují tzv. enum třídy. Můžeš si přečíst například tento text.
# Zkus vytvořit třídu pro typy pozemků (zemědělský pozemek, stavební pozemek, les, zahrada) a použít ji ve třídě Estate.
# Použití této třídy zabrání, aby byl vytvořen pozemek s neexistujícím typem.

