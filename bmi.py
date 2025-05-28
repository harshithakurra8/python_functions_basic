#  Write a Python program to calculate body mass index.

weight_pound = float(input("Enter your weight in pounds: "))   #pounds=0.45
height_cent = float(input("Enter your height in centimeters: ")) 
weight = weight_pound* 0.45
height = height_cent/ 100
bmi = weight / (height * height)
print("Your BMI is:", round(bmi, 2))
current=25*weight// bmi
#print(current)
difference=(current-weight)/0.45

#print(difference)
if bmi < 18.5:
    print("You are underweight.")
    if difference>0:
        print(f"the recommended weight you need to gain is:{difference}")
elif bmi < 25:                                                 #pounds=kilograms  #cm=meters
   print("You have a normal weight.")
elif bmi >25:
    print("You are overweight.")
    if difference<0:
        print(f"the recommended weight you need to lose is:{difference}")
    
else:
   print("You are obese.")



# def calculate_bmi(weight,height):
#     bmi = weight / (height ** 2)
#     return bmi

# def determine_bmi_category(bmi):
#     if bmi < 18.5:
#         return "Underweight"
#     elif 18.5 <= bmi<24.9:
#         return "Overweight"
#     else:
#         return "Obesity"