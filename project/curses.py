from InquirerLib import prompt


questions = [
    {
        "type": "list",
        "message": "Please select an operation to perform?",
        "choices": [
            "add",
            "sub",
            "div"
        ],
        "multiselect": False,
        "name": "class_name"
    },
]

result = prompt(questions)
print("So, you are a:",result["class_name"])