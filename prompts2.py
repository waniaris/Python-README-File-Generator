from InquirerPy import prompt

# Get user input for README file
def user_input():
    questions = [
        {
            'type': 'input', 
            'name': 'title', 
            'message': 'Title:'
        },
                {
            'type': 'input', 
            'name': 'description', 
            'message': 'Description:'
        },
        {
            'type': 'input', 
            'name': 'installation', 
            'message': 'Installation Instructions:'
        },
        {
            'type': 'input', 
            'name': 'usage', 
            'message': 'Usage Information:'
        },        
        {
            'type': 'list', 
            'name': 'license', 
            'message': 'Choose a license:', 
            'choices': ['MIT', 'Apache 2.0', 'Boost Software', 'None'] # reference: https://choosealicense.com/licenses/
        },
        {
            'type': 'input', 
            'name': 'author', 
            'message': 'Author Name:'
        },
        {
            'type': 'input', 
            'name': 'contact', 
            'message': 'Contact:'
        }
    ]
    return prompt(questions)