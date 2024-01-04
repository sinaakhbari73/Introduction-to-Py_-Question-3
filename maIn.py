class Patient:
    def __init__(self, first_name, middle_name, last_name, address, city, state, zip_code, phone_number, emergency_contact_name, emergency_contact_phone):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.emergency_contact_name = emergency_contact_name
        self.emergency_contact_phone = emergency_contact_phone

    def get_first_name(self): # Accessor methods.
        return self.first_name

    def set_first_name(self, first_name): # Mutator methods.
        self.first_name = first_name


class Procedure:
    def __init__(self, name, date, practitioner, charge):
        self.name = name
        self.date = date
        self.practitioner = practitioner
        self.charge = charge

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


def main():
    # Create a Patient instance.
    patient = Patient("John", "A.", "Doe", "123 Main St", "Anytown", "Anystate", "12345", "123-456-7890", "Jane Doe", "987-654-3210")

    procedures = [     # Create Procedure instances.
        Procedure("Physical Exam", "Today's Date", "Dr. Irvine", 250.00),
        Procedure("X-ray", "Today's Date", "Dr. Jamison", 500.00),
        Procedure("Blood test", "Today's Date", "Dr. Smith", 200.00)
    ]

    # Display patient information.
    print(f"Patient Information:\nName: {patient.get_first_name()} {patient.middle_name} {patient.last_name}\nAddress: {patient.address}, {patient.city}, {patient.state}, {patient.zip_code}\nPhone: {patient.phone_number}\nEmergency Contact: {patient.emergency_contact_name}, {patient.emergency_contact_phone}")

    total_charge = 0 # Display procedures and calculate total charge.
    print("\nProcedures:")
    for procedure in procedures:
        print(f"{procedure.get_name()} performed on {procedure.date} by {procedure.practitioner} for ${procedure.charge}")
        total_charge += procedure.charge

    print(f"\nTotal Charges: ${total_charge}")     # Display total charges.


if __name__ == "__main__":
    main()
