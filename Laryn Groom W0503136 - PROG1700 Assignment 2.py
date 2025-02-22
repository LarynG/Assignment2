# Program Title: Hinterland Clinic Patient Console (PROG1700 Assignment 2)
#     Objective: "Receive input from user, process multiple ‘strings’ based on their values, perform appropriate calculations on numeric data, and output results."
#        Author: Laryn Groom (W0503136)
#          Date: 02-21-2025
#         Notes: Flowchart should be passed in on Brightspace AND the Git Repository. (Not included yet. Will remove this part of the note when available)

# Introduction Print Statement
print("Hinterland Clinic - Patient Servicing Console")

# Hard-Coded Definitions
programRun = 0 # "True/False" for if code/program is running

doc1 = 50      # Clinician Charges
doc2 = 90
doc3 = 120
doc4 = 160

docPrice = 0

# User-Defined Information Storage
patient4Proc = input("Is there a Patient to Process? (Say 'Yes', 'Finish', 'No', or 'Stop') ")
patientName = " "  # Space for temporary value, "Variable" type
clinicianReq = " " # Space for temporary value, "Variable" type

# User-Interactive
int(programRun) + 1
while programRun = 1
    if patient4Proc[0].lower() == 'y':
        patientName = str(input("Please enter the patient's name: "))
        clinicianReq = str(input("How many Clinicians will the patient require? (Range of 1 to 4) "))
        if clinicianReq == 1 or clinicianReq[0:2].lower() == 'on':
            docPrice + doc1
        if clinicianReq == 2 or clinicianReq[0:2].lower() == 'tw':
            docPrice + doc2
        if clinicianReq == 3 or clinicianReq[0:2].lower() == 'th':
            docPrice + doc3
        if clinicianReq == 4 or clinicianReq[0:2].lower() == 'fo':
            docPrice + doc4
        else:
            print("Error - Please enter a valid number entry for doctors required. (Between 1 and 4)")

    if patient4Proc[0].lower() == 'n' or 's' or 'f':
        int(programRun) - 1
        print("Thank you! Shutting down...")

    else:
        print("Error - Please enter one of the following answers: 'Yes', 'Finish', 'No', or 'Stop'.")


# Testing Sector - REMEMBER TO REMOVE BEFORE FINAL COMMIT!!
print(patient4Proc)
print(patientName)
print(clinicianReq)