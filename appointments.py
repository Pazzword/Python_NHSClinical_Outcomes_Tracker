import os
import csv

class Appointment:
    def __init__(self, appointment_type, direct_access, review_type, outcome_code):
        """
        Initialize an Appointment object with specified attributes.

        Args:
            appointment_type (str): The type of appointment.
            direct_access (str): The type of access for the appointment (Direct Access or Investigation).
            review_type (str): The type of review for the appointment.
            outcome_code (str): The outcome code associated with the appointment.
        """
        self.appointment_type = appointment_type
        self.direct_access = direct_access
        self.review_type = review_type
        self.outcome_code = outcome_code

class AppointmentManager:
    def __init__(self, csv_filename):
        """
        Initialize an AppointmentManager object.

        Args:
            csv_filename (str): The filename of the CSV file to manage appointments.
        """
        self.csv_filename = csv_filename
        self.create_csv_if_not_exists()

    def create_csv_if_not_exists(self):
        """
        Create a CSV file with headers if it does not exist.
        """
        if not os.path.exists(self.csv_filename):
            with open(self.csv_filename, "w", newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(["APPOINTMENT TYPE", "DIRECT ACCESS/INVESTIGATION", "TYPE OF REVIEW", "OUTCOME CODE"])

    def write_to_csv(self, appointment):
        """
        Write appointment data to the CSV file.

        Args:
            appointment (Appointment): The Appointment object to write to the CSV file.
        """
        # Replace empty strings with "N/A"
        appointment_values = [appointment.appointment_type, appointment.direct_access, appointment.review_type, appointment.outcome_code]
        for i in range(len(appointment_values)):
            if not appointment_values[i]:
                appointment_values[i] = "N/A"
            
        with open(self.csv_filename, "a", newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(appointment_values)
