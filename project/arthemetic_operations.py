from InquirerLib import prompt
from add import add
from sub import sub
from mul import mul
from div import div


def main():
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    questions = [
        {
            "type": "list",
            "message": "Please select an operation to perform?",
            "choices": [
                
                "add",
                "sub",
                "div",
                "mul"
            ],
            "multiselect": False,
            "name": "output"
        },
    ]

    result = prompt(questions)["output"]

    if result == 'add':
        print(f"The result is: {add(x, y)}")
    elif result == 'sub':
        print(f"The result is: {sub(x, y)}")
    elif result == 'mul':
        print(f"The result is: {mul(x, y)}")
    elif result == 'div':
        print(f"The result is: {div(x, y)}")
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()

