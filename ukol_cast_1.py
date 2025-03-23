import math


class Locality:
    def __init__(self, name: str, locality_coefficient: int):
        self.name = name
        self.locality_coefficient = locality_coefficient

class Property:
    def __init__(self, locality: Locality):
        self.locality = locality

class Estate(Property):
    def __init__(self, locality: Locality, estate_type: str, area: int):
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

        tax = self.area * coefficients.get(self.estate_type) * self.locality.locality_coefficient
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

# Vyzkoušej svůj program pomocí následujících nemovitostí:
neratovice = Locality("Neratovice", 2)
praha = Locality("Praha", 3)
manetin = Locality("Manětín", 0.8)
brno = Locality ("Brno", 3)

estate_1 = Estate(neratovice, "forrest", 500)
estate_2 = Estate(manetin,"land", 900)

residence_1 = Residence(praha, 60, False)
residence_2 = Residence(praha, 60, True)
residence_3 = Residence(manetin, 120, False)
residence_4 = Residence(brno, 90, True)

print(f"Daň z daného pozemku je {estate_1.calculate_tax()} Kč.")
print(f"Daň z daného pozemku je {residence_1.calculate_tax()} Kč.")
print(f"Daň z daného pozemku je {residence_2.calculate_tax()} Kč.")
print(f"Daň z daného pozemku je {estate_2.calculate_tax()} Kč.")
print(f"Daň z daného pozemku je {residence_3.calculate_tax()} Kč.")
print(f"Daň z daného pozemku je {residence_4.calculate_tax()} Kč.")