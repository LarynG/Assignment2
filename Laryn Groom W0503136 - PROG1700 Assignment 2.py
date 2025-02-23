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
taxCalc = 0.07
taxTotal = 0
addCharge = 0

itemCostChrg = 0
docPriceChrg = 0

# User-Interactive
while programRun == 1:

    while patient4Proc[0].lower() == 'y':
        patientName = input("Please enter the patient's name: ")
        clinicianInput = input("How many Clinicians will the patient require? (Range of 1 to 4) ")
        patient4Proc = "reask"

        if clinicianInput == '1' or clinicianInput[0:2].lower() == 'on':
            clinicianReq = 1 # Ensures that "on" is changed to 1 for the "while not" below.
            docPrice = docPrice + doc1

        elif clinicianInput == "2" or clinicianInput[0:2].lower() == 'tw':
            clinicianReq = 2
            docPrice = docPrice + doc2

        elif clinicianInput == "3" or clinicianInput[0:2].lower() == 'th':
            clinicianReq = 3
            docPrice = docPrice + doc3

        elif clinicianInput == "4" or clinicianInput[0:2].lower() == 'fo':
            clinicianReq = 4
            docPrice = docPrice + doc4

        while not clinicianReq <= 4 and clinicianReq >= 1:
            print("Error - Please enter a valid number entry for clinicians required.")
            clinicianInput = input("How many Clinicians will the patient require? (Range of 1 to 4) ")

    rxCount = input("How many Prescriptions for " + patientName + "? ")
    itemCount = input("How many individual Prescription Items in total? ")
    healthCard = input("Please enter " + patientName + "'s Health Card Number: ")

# Calculation Sectors

    #  Prescription Calculation  #
    itemCosts = int(rxCount) * int(itemCount)

    #  HealthCard Calculations Below  #
    if healthCard[0:2].lower() == "ns":
        itemCosts = itemCosts + 0
        docPrice = docPrice + 0

    if healthCard[0:2].lower() == "nb" or "pe" or "nl":
        addCharge = 0.10
        itemCostChrg = itemCosts * addCharge
        docPriceChrg = docPrice * addCharge
        itemCosts = itemCosts + itemCostChrg
        docPrice = docPrice + docPriceChrg

    if healthCard[0:2].lower() == "us":
        addCharge = 1
        itemCostChrg = itemCosts * addCharge
        docPriceChrg = docPrice * addCharge
        itemCosts = itemCosts + itemCostChrg
        docPrice = docPrice + docPriceChrg

    if healthCard[0:2].lower() == "on" or "qc" or "mb":
        addCharge = 0.20
        itemCostChrg = itemCosts * addCharge
        docPriceChrg = docPrice * addCharge
        itemCosts = itemCosts + itemCostChrg
        docPrice = docPrice + docPriceChrg

    if healthCard[0:2].lower() == "bc" or "ab" or "sk":
        addCharge = 0.25
        itemCostChrg = itemCosts * addCharge
        docPriceChrg = docPrice * addCharge
        itemCosts = itemCosts + itemCostChrg
        docPrice = docPrice + docPriceChrg

    if healthCard[0:2].lower() == "nt" or "nu" or "yt":
        addCharge = 0.20
        itemCostChrg = itemCosts * addCharge
        docPriceChrg = docPrice * addCharge
        itemCosts = itemCosts + itemCostChrg
        docPrice = docPrice + docPriceChrg

    elif healthCard[0:2].lower():
        addCharge = 0.50
        itemCostChrg = itemCosts * addCharge
        docPriceChrg = docPrice * addCharge
        itemCosts = itemCosts + itemCostChrg
        docPrice = docPrice + docPriceChrg


    docTax = docPrice * taxCalc
    rxTax = itemCosts * taxCalc
    taxTotal = docTax + rxTax
    staySubtotal = itemCosts + docPrice
    stayTotal = staySubtotal + taxTotal

    print("Clinic Charges for " + patientName + ": $" + str(docPrice))
    print("Prescription costs: $" + str(itemCosts))
    print("Provincial Tax: $" + str(taxTotal))
    print("Total Charges for " + patientName + ": $" + str(stayTotal))

# Continuation from "if" statements above the calculation sector

    if patient4Proc[0].lower() == 'r':
        patient4Proc = input("Is there another Patient to Process? (Say 'Yes', 'Finish', 'No', or 'Stop') ") 

    if patient4Proc[0].lower() == 'n' or 's' or 'f':
        print("Thank you! Shutting down...")
        programRun = 0
    
    else:
        print("Error - Please enter one of the following answers: 'Yes', 'Finish', 'No', or 'Stop'.")
        clinician4Proc = input("Is there a Patient to Process? ")