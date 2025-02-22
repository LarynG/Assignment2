# Program Title: Hinterland Clinic Patient Console (PROG1700 Assignment 2)
#     Objective: "Receive input from user, process multiple ‘strings’ based on their values, perform appropriate calculations on numeric data, and output results."
#        Author: Laryn Groom (W0503136)
#          Date: 02-21-2025
#         Notes: Flowchart should be passed in on Brightspace AND the Git Repository. (Not included yet. Will remove this part of the note when available)

# Introduction Print Statement
print("Hinterland Clinic - Patient Servicing Console")

# Hard-Coded Definitions
doc1 = 50  #Clinician Charges
doc2 = 90
doc3 = 120
doc4 = 160

# User-Defined Information
patient4Proc = input("Is there a Patient to Process? (Say 'Yes', 'Finish', 'No', or 'Stop')")  # Storage for Patients Waiting
patientName = " " # Space for temporary value, "Variable" type
clinicianReq = " " # Space for temporary value, "Variable" type

if patient4Proc[0].lower() == 'y':
    patientName = str(input("Please enter the patient's name: "))
    clinicianReq = str(input("How many Clinicians will the patient require? (Number range between 1 and 4) "))

if patient4Proc[0].lower() == 'n' or 's' or 'f':
    print("Thank you! Shutting down...")

elif patient4Proc[0].lower():
    print("Error - Please enter one of the following answers: 'Yes', 'Finish', 'No', or 'Stop'.")


# Testing Sector - REMEMBER TO REMOVE BEFORE FINAL COMMIT!!
print(patient4Proc)
print(patientName)
print(clinicianReq)