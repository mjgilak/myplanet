import numpy as np

def calculate_bmi(weight, height):
    """
    Calculates the BMI (Body Mass Index) using weight in kilograms (kg)
    and height in meters (m).
    """
    return weight / (height ** 2)

def bmi_advice(bmi):
    """
    Provides fake advice based on BMI to reach an "ideal" BMI.
    """
    if bmi < 18.5:
        return "Your BMI is below the healthy range. You should aim to gain weight. Try consuming more nutrient-dense foods like avocados, nuts, and olive oil."
    elif 18.5 <= bmi < 25:
        return "Congratulations! Your BMI is within the healthy range. Maintain your weight by eating a balanced diet and engaging in regular physical activity."
    elif 25 <= bmi < 30:
        return "Your BMI is in the overweight range. Consider incorporating more exercise into your routine and reduce your intake of high-calorie foods."
    else:
        return "Your BMI is in the obese range. It's important to prioritize your health by adopting a well-balanced diet and increasing physical activity. Consult a healthcare professional for personalized advice."

# Prompt the user for weight and height
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI and get advice
bmi = calculate_bmi(weight, height)
advice = bmi_advice(bmi)

print("BMI:", bmi)
print("Advice:", advice)
