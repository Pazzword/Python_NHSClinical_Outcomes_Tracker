import os
import csv
import pdfplumber

# Importing custom module
import appointments

def create_outcomes():
    # Create an instance of AppointmentManager from the appointments module
    appointment_manager = appointments.AppointmentManager("appointments.csv")

    # Dictionary to map user input to full words
    input_mapping = {"R": "Review", "D": "Doctors'", "P": "Procedure", "Y": "Yes", "N": "No", "DA": "Direct Access", "I": "Investigation", "F": "First Appt", "FU": "Follow-up Appt"}

    while True:
        # Type of outcome
        while True:
            # Prompt the user for the type of appointment
            outcome1 = input('''
            🟡 Is this appointment with the Doctor (D) or Procedure (P) appointment? ''').upper()

            # Check if the input is valid
            if outcome1 in ["D", "P"]:
                break  # Exit the loop if the input is valid
            else:
                print('''
            ❌ Invalid input. Please enter 'D' or 'P'.''')

        # Procedure appointments could be Direct Access and Investigation
        # Direct Access procedure:
        if outcome1 == "P":
            while True:
                # Prompt the user for Direct Access or Investigation
                Clinic_Review = input('''
            🔵🟡 Is it Direct Access (DA) or Investigation (I) appointment? ''').upper()

                # Check if the input is valid
                if Clinic_Review in ["DA", "I"]:
                    break  # Exit the loop if the input is valid
                else:
                    print('''
            ❌ Invalid input. Please enter 'DA' or 'I'.''')

            # Continue with the rest of the code based on valid inputs
            if Clinic_Review == "DA":
                code = "Code 92"
                print("\n✅ DIRECT ACCESS\n", "NEW PATIENT\n", "🔵 CODE: 92\n" "\nNOTE: THIS OUTCOME APPLIES TO ALL ECG FOR INTERPRETATION AND ALL ULTARASOUND APPOINTMENTS ")
            elif Clinic_Review == "I":
                print("\n✅ INVESTIGATION\n", "REVIEW PATIENT\n", "🟡 CODE: 20\n")
                code = "Code 20"
            
        elif outcome1 == "D":
            # Code for Clinic Review appointments:
            while True:
                # Prompt the user for the type of doctor's appointment
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
        appointment = appointments.Appointment(input_mapping.get(outcome1, ""), input_mapping.get(Clinic_Review, "") if outcome1 == "P" else "", input_mapping.get(Clinic_Review, "") if outcome1 == "D" else "", code if 'code' in locals() else "")

        # Write user inputs to CSV
        appointment_manager.write_to_csv(appointment)

        # Ask the user if they want to start over
        start_over = input('''
            ⬜️ Do you want to go to the next outcome? Type 'Y' for Yes, 'N' for No: ''').upper()
        if start_over != 'Y':
            break

def generate_reports():
    # Read data from appointments.csv
    appointments_data = []
    with open("appointments.csv", newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            appointments_data.append(row)

    # Process data and generate the report
    report_lines = []
    report_lines.append("CLINIC OUTCOMES REPORT\n\n")
    report_lines.append("PATIENT NUM\tAPPOINTMENT\tTYPE\t\tOUTCOME CODE\n")
    
    patient_number = 1
    for appointment in appointments_data:
        appointment_with_patient = [f"Patient {patient_number}"] + appointment
        report_lines.append("\t".join(appointment_with_patient) + "\n")
        patient_number += 1

    # Save the report to clinic_outcomes.txt
    with open("clinic_outcomes.txt", "w") as report_file:
        report_file.writelines(report_lines)

    print("\t\t✅ Report generated and saved to 'clinic_outcomes.txt'.")

def view_outcomes():
    print("\n--- CLINIC OUTCOMES ---\n")
    try:
        with open("clinic_outcomes.txt", "r") as file:
            # Read the header
            header = next(file).strip().split("\t")

            # Print the header
            print("\t".join(header))

            # Print the outcomes
            for line in file:
                outcome = line.strip().split("\t")
                # Filter out "N/A" values
                filtered_outcome = [field for field in outcome if field != "N/A"]
                print("\t".join(filtered_outcome))
    except FileNotFoundError:
        print("No outcomes available. Please generate the report first.")

def view_RTT():
    try:
        os.system("open RTT_status_codes.pdf")
    except FileNotFoundError:
        print("PDF file not found.")
