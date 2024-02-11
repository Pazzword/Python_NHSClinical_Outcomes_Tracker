import os
import csv

class Appointment:
    def __init__(self, appointment_type, direct_access, review_type, outcome_code):
        self.appointment_type = appointment_type
        self.direct_access = direct_access
        self.review_type = review_type
        self.outcome_code = outcome_code

class AppointmentManager:
    def __init__(self, csv_filename):
        self.csv_filename = csv_filename
        self.create_csv_if_not_exists()

    def create_csv_if_not_exists(self):
        if not os.path.exists(self.csv_filename):
            with open(self.csv_filename, "w", newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(["APPOINTMENT TYPE", "DIRECT ACCESS/INVESTIGATION", "TYPE OF REVIEW", "OUTCOME CODE"])

    def write_to_csv(self, appointment):
    # Replace empty strings with "N/A"
        appointment_values = [appointment.appointment_type, appointment.direct_access, appointment.review_type, appointment.outcome_code]
        for i in range(len(appointment_values)):
            if not appointment_values[i]:
                appointment_values[i] = "N/A"
            
        with open(self.csv_filename, "a", newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(appointment_values)


def main():
    # Create an instance of AppointmentManager
    appointment_manager = AppointmentManager("appointments.csv")

    # Dictionary to map user input to full words
    input_mapping = {"R": "Review", "D": "Doctor", "P": "Procedure", "Y": "Yes", "N": "No", "DA": "Direct Access", "I": "Investigation", "F": "First Doctor's Appt", "FU": "Follow-up"}

    while True:
        # Type of outcome
        while True:
            outcome1 = input('''
            🟡 Is this appointment with the Doctor (D) or Procedure (P) appointment? ''').upper()

            # Check if the input is valid
            if outcome1 in ["D", "P"]:
                break  # Exit the loop if the input is valid
            else:
                print('''
            🟡 Invalid input. Please enter 'D' or 'P'.''')

        # Procedure appointments could be Direct Access and Investigation
        # Direct Access procedure:
        if outcome1 == "P":
            while True:
                Clinic_Review = input('''
            🔵🟡 Is it Direct Access (DA) or Investigation (I) appointment? ''').upper()

                # Check if the input is valid
                if Clinic_Review in ["DA", "I"]:
                    break  # Exit the loop if the input is valid
                else:
                    print('''
            ❌ Invalid input. Please enter 'DA' or 'I'.''')

            # Continue with the rest of your code based on valid inputs
            if Clinic_Review == "DA":
                code = "Code 92"
                print("\n✅ DIRECT ACCESS\n", "NEW PATIENT\n", "🔵 CODE: 92\n" "\nNOTE: THIS OUTCOME APPLIES TO ALL ECG FOR INTERPRETATION AND ALL ULTARASOUND APPOINTMENTS ")
            elif Clinic_Review == "I":
                print("\n✅ INVESTIGATION\n", "REVIEW PATIENT\n", "🟡 CODE: 20\n")
                code = "Code 20"
            
        elif outcome1 == "D":
            # Code for Clinic Review appointments:
            while True:
                Clinic_Review = input('''
            🟡 Is this the patient's first (F) doctor's appointment or Follow-up (FU)? ''').upper()

                # Check if the input is valid
                if Clinic_Review in ["F", "FU"]:
                    break  # Exit the loop if the input is valid
                else:
                    print("❌ Invalid input. Please enter 'F' or 'FU'.")

            if Clinic_Review == "F":
                print("\n✅ NEW PATIENT\n", "🟡 CODE: 20\n")
                code = "Code 20"
            elif Clinic_Review == "FU":
                print("\n✅ FOLLOW-UP\n", "REVIEW PATIENT\n", "🟡 CODE: 20\n")
                code = "Code 20"

        else:
            print("\n❌ Invalid input. Please enter 'D' or 'P'.")

        # Create an Appointment object
        appointment = Appointment(input_mapping.get(outcome1, ""), input_mapping.get(Clinic_Review, "") if outcome1 == "P" else "", input_mapping.get(Clinic_Review, "") if outcome1 == "D" else "", code if 'code' in locals() else "")

        # Write user inputs to CSV
        appointment_manager.write_to_csv(appointment)

        # Ask the user if they want to start over
        start_over = input('''
            ⬜️ Do you want to start over? Type 'Y' for Yes, 'N' for No: ''').upper()
        if start_over != 'Y':
            break  # Exit the loop if the user does not want to start over

if __name__ == "__main__":
    main()
