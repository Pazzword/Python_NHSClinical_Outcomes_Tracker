import reports  # Importing the module containing functions for managing appointments and generating reports

def main():
    while True:
        try:
            # Prompt the user for their choice in the main menu
            option = input(''' 
                                MAIN MENU
                
                'w' -     Start New Outcomes List
                'gr -     Generate Outcomes' Report
                'va'-     View Outcomes
                't' -     Open RTT status codes .pdf
                'q' -     Quit
                        
                Enter your option: ''').lower()
            
            if option == 'w':
                reports.create_outcomes()  # Call the function to start creating a new outcomes list
            elif option =='gr':
                reports.generate_reports()  # Call the function to generate outcomes report
            elif option == 'va':
                reports.view_outcomes()  # Call the function to view outcomes
            elif option =='t':
                reports.view_RTT()  # Call the function to open RTT status codes PDF

            elif option == 'q':
                print("\t\tGoodbuy!!!")  # Print farewell message
                quit()  # Exit the program

        except ValueError:
            return  # Exit the program in case of ValueError

if __name__ == "__main__":
    main()  # Call the main function when the script is executed
