import datetime

# Function which gives date and time for entering of log
def getdate():
    return str(datetime.datetime.now())


print("\nWELCOME TO THIS HEALTH MANAGEMENT SYSTEM\n")

try:
    print("Press 0 to log data or press 1 to retrieve data")
    log_ret = int(input())

    print("Press 1 for Sancho\nPress 2 for Rashy\nPress 3 for Bruno")
    person = int(input())
    

    # Log data
    if log_ret==0:
        # Now use txt file to log data 

        if(person==1):
            print("Welcome Sancho: Enter your diet for log:")
            san1 = input()

            with open (r'C:\APURV\4th Year\VISUAL STUDIO CODE\Health Management System\Sancho.txt', "a") as f1:
                f1.write("\n")
                f1.write(getdate())
                f1.write(":  ")
                f1.write(san1)
                f1.write("\n")

            # Again entering log till user type NO
            print("Type YES to continue and NO to exit")
            yes_no1 = input()
            yes_no1 = yes_no1.upper()
            while(yes_no1=="YES"):
                print("Welcome Sancho: Enter your diet for log:")
                san1 = input()

                with open (r'C:\APURV\4th Year\VISUAL STUDIO CODE\Health Management System\Sancho.txt', "a") as f1:
                    f1.write("\n")
                    f1.write(getdate())
                    f1.write(":  ")
                    f1.write(san1)
                    f1.write("\n")

                print("Type YES to continue and NO to exit")
                yes_no1 = input()
                yes_no1 = yes_no1.upper()

            # End of log for Sancho


        if(person==2):
            print("Welcome Rashy: Enter your diet for log:")
            san2 = input()

            with open (r'C:\APURV\4th Year\VISUAL STUDIO CODE\Health Management System\Rashy.txt', "a") as f2:
                f2.write("\n")
                f2.write(getdate())
                f2.write(":  ")
                f2.write(san2)
                f2.write("\n")

            # Again entering log till user type NO
            print("Type YES to continue and NO to exit")
            yes_no2 = input()
            yes_no2 = yes_no2.upper()
            while(yes_no2=="YES"):
                print("Welcome Rashy: Enter your diet for log:")
                san2 = input()

                with open (r'C:\APURV\4th Year\VISUAL STUDIO CODE\Health Management System\Rashy.txt', "a") as f2:
                    f2.write("\n")
                    f2.write(getdate())
                    f2.write(":  ")
                    f2.write(san2)
                    f2.write("\n")

                print("Type YES to continue and NO to exit")
                yes_no2 = input()
                yes_no2 = yes_no2.upper()

            # End of log for Rashy
            
        if(person==3):
            print("Welcome Bruno: Enter your diet for log:")
            san3 = input()

            with open (r'C:\APURV\4th Year\VISUAL STUDIO CODE\Health Management System\Bruno.txt', "a") as f3:
                f3.write("\n")
                f3.write(getdate())
                f3.write(":  ")
                f3.write(san3)
                f3.write("\n")

            # Again entering log till user type NO
            print("Type YES to continue and NO to exit")
            yes_no3 = input()
            yes_no3 = yes_no3.upper()
            while(yes_no3=="YES"):
                print("Welcome Bruno: Enter your diet for log:")
                san3 = input()

                with open (r'C:\APURV\4th Year\VISUAL STUDIO CODE\Health Management System\Bruno.txt', "a") as f3:
                    f3.write("\n")
                    f3.write(getdate())
                    f3.write(":  ")
                    f3.write(san3)
                    f3.write("\n")

                print("Type YES to continue and NO to exit")
                yes_no3 = input()
                yes_no3 = yes_no3.upper()

            # End of log for Bruno
            

    # Retrieve data
    elif log_ret==1:
        
        if(person==1):
            with open(r'C:\APURV\4th Year\VISUAL STUDIO CODE\Health Management System\Sancho.txt') as r1:
                print(r1.read())

        elif(person==2):
            with open(r'C:\APURV\4th Year\VISUAL STUDIO CODE\Health Management System\Rashy.txt') as r2:
                print(r2.read())
        
        elif(person==3):
            with open(r'C:\APURV\4th Year\VISUAL STUDIO CODE\Health Management System\Bruno.txt') as r3:
                print(r3.read())

        else:
            print("Enter 1,2 or 3 only")

    # If the user enter other than 0 or 1
    else:
        print("Enter the correct input")

except:
    print("Enter the correct input there is error")
