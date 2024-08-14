import reports 

def main():
    while True:
        try:
            
            option = input(''' 
                                MAIN MENU
                
                'w' -     Start New Outcomes List
                'gr -     Generate Outcomes' Report
                'va'-     View Outcomes
                't' -     Open RTT status codes .pdf
                'q' -     Quit
                        
                Enter your option: ''').lower()
            
            if option == 'w':
                reports.create_outcomes()  
            elif option =='gr':
                reports.generate_reports() 
            elif option == 'va':
                reports.view_outcomes() 
            elif option =='t':
                reports.view_RTT()  # Call the function to open RTT status codes PDF

            elif option == 'q':
                print("\t\tGoodbuy!!!")  
                quit()  

        except ValueError:
            return  

if __name__ == "__main__":
    main()  
