class Patient:
    def __init__(self, name: str, bill_amount: float):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_bill_amount(self):
        return self.__bill_amount 

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount

    def calculate_bill(self):
        return self.__bill_amount

class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.8

class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85

regular_patient = Patient("Vince Collado", 15000.00)
senior_patient = SeniorPatient("Maria Santos", 15000.00)
philhealth_patient = PhilHealthPatient("Prince Ronulo", 15000.00)

patients = [regular_patient, senior_patient, philhealth_patient]

print("Hospital Billing System")
print("-----------------------")

for patient in patients:
    print("Patient Name:", patient.get_name())
    print("Original Bill: ₱", patient.get_bill_amount())
    print("Final Bill: ₱", patient.calculate_bill())
    print()