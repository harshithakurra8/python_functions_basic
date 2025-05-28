#  Write a Python program to convert pressure in kilopascals
#  to pounds per square inch, a millimeter of mercury (mmHg) and
#  atmosphere pressure

kpa = float(input("Enter pressure in kilopascals (kPa): "))

psi = kpa * 0.145038
mmhg = kpa * 7.50062
atm = kpa / 101.325

print("Pressure in pounds per square inch (psi):", round(psi, 2))
print("Pressure in millimeters of mercury (mmHg):", round(mmhg, 2))
print("Pressure in atmospheres (atm):", round(atm, 4))