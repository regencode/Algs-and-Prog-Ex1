#Inputs
force, mass = input("Enter the mass in kg and the force in N: ").split()

#Eval
force = float(force)
mass = float(mass)

#not correct equation but whatever, 
#supposed to be accel = force/mass
accel = mass/force

#Print
print("The acceleration is " + str(accel))