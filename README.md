# National Referral Coding System for Clinic Appointments

## Overview
The National Referral Coding System is a Python-based application designed to facilitate the creation, saving, and tracking of clinic appointments. This system is particularly useful for medical facilities and clinics that need an efficient way to manage their appointments and generate invoices.

## Features
- Create New Appointments: Users can create appointments for doctors or procedures,    specifying details such as appointment type, review type, and outcome code.
- Appointment Differentiation: The system can differentiate between various types of appointments, including doctor's appointments, procedures, direct access, or investigations.
- Track Review Type: Users can track the type of review for each appointment, whether it's a new patient visit, follow-up, or review.
- Generate Outcome Codes: The system generates outcome codes for each appointment to aid in tracking and reporting.
- Automatic Saving: Appointment details are automatically saved to a CSV file named appointments.csv for easy retrieval and analysis.
- Data Consistency: The system ensures data consistency by replacing empty fields with "N/A" in the saved CSV file.

## Usage
1. Clone the repository to your local machine.
2. Run the `main.py` file to launch the application.
3. Follow the prompts to input appointment details such as appointment type, review type, and outcome code.
4. The application will save the appointment details to a CSV file named `appointments.csv`.

## Dependencies
- Python 3.x
- `csv` module (standard library)
- `os` module (standard library)

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments
- This project was inspired by the need for a simple yet effective system for managing clinic appointments and generating invoices.
- Special thanks to the developers of Python and the open-source community for their valuable contributions.
