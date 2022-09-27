from turtle import up


print("Enter your height.")

#Input variables
feet = input("Feet: ")
inch = input("Inches: ")

#Evaluating inputs
feetcm = float(feet) * 30.48
inchcm = float(inch) * 2.54

#Adding up
cm = feetcm + inchcm
suggestcm = cm * 0.88
#Print result
print("Suggested board length: " + str(suggestcm) + " cm")