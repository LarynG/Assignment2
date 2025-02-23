# Program Title: Hinterland Clinic Patient Console (PROG1700 Assignment 2)
#     Objective: "Receive input from user, process multiple ‘strings’ based on their values, perform appropriate calculations on numeric data, and output results."
#        Author: Laryn Groom (W0503136)
#          Date: 02-21-2025
#         Notes: Flowchart should be passed in on Brightspace AND the Git Repository. (Not included yet. Will remove this part of the note when available)

# Introduction Print Statement
print("Hinterland Clinic - Patient Servicing Console")

# Hard-Coded Definitions
programRun = 1 # "True/False" for if code/program is running

doc1 = 50      # Clinician Charges
doc2 = 90
doc3 = 120
doc4 = 160

docPrice = 0

# User-Defined Information Storage
patient4Proc = input("Is there a Patient to Process? (Say 'Yes', 'Finish', 'No', or 'Stop') ")
patientName = " "     # Space for temporary value, "Variable" type
clinicianInput = "0" # Space for temporary value, "Variable" type
clinicianReq = 0
healthCard = " "

rxCount = 0
itemCount = 0
itemCosts = 0

# User-Interactive
while programRun == 1:

    if patient4Proc[0].lower() == 'r':
        patient4Proc = input("Is there another Patient to Process? (Say 'Yes', 'Finish', 'No', or 'Stop') ") 

    if patient4Proc[0].lower() == 'y':
        patientName = input("Please enter the patient's name: ")
        clinicianInput = input("How many Clinicians will the patient require? (Range of 1 to 4) ")
        patient4Proc = "reask"
        print(patient4Proc)

        if clinicianInput == '1' or clinicianInput[0:2].lower() == 'on':
            clinicianReq = 1 # Ensures that "on" is changed to 1 for the "while not" below.
            docPrice = docPrice + doc1
            #int(clinicianInput) + 1

        elif clinicianInput == "2" or clinicianInput[0:2].lower() == 'tw':
            int(clinicianReq) == 2
            docPrice + doc2
            #int(clinicianInput) = 1

        elif clinicianInput == "3" or clinicianInput[0:2].lower() == 'th':
            int(clinicianReq) == 3
            docPrice + doc3
            #int(clinicianInput) = 1

        elif clinicianInput == "4" or clinicianInput[0:2].lower() == 'fo':
            int(clinicianReq) == 4
            docPrice + doc4
            #int(clinicianInput) = 1

        while not clinicianReq <= 4 and clinicianReq >= 1:
            print("Error - Please enter a valid number entry for clinicians required.")
            clinicianInput = input("How many Clinicians will the patient require? (Range of 1 to 4) ")

# Calculation Sectors
    itemCosts = rxCount * itemCount
    print(itemCosts)

    #if healthCard[0:2].lower() == "ns":

    #if healthCard[0:2].lower() == "nb" or "pe" or "nl":

    #if healthCard[0:2].lower() == "us":
    
    #if healthCard[0:2].lower() == "on" or "qc" or "mb":

    #if healthCard[0:2].lower() == "bc" or "ab" or "sk":

    #if healthCard[0:2].lower() == "nt" or "nu" or "yt":

    #elif healthCard[0:2].lower():

# Continuation from "if" statements above the calculation sector
    if patient4Proc[0].lower() == 'n' or 's' or 'f':
        print("Thank you! Shutting down...")
        programRun = 0
    
    else:
        print("Error - Please enter one of the following answers: 'Yes', 'Finish', 'No', or 'Stop'.")
        clinician4Proc = input("Is there a Patient to Process? ")


# Testing Sector - REMEMBER TO REMOVE BEFORE FINAL COMMIT!!
print("patient4Proc " + str(patient4Proc))
print("patientName " + str(patientName))
print("clinicianReq " + str(clinicianReq))
print("docPrice " + str(docPrice))