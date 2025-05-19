"""Simple calculator with no fancy GUI"""
import sys
from importlib.metadata import version

from prompt_toolkit import Application
from prompt_toolkit.shortcuts import yes_no_dialog, radiolist_dialog, message_dialog, input_dialog


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'

def get_package_version(package_name: str) -> str:
	return version(package_name)

def get_operation() -> str:
    while True:
        result = radiolist_dialog(
            title='Choose operation',
            text='Which operation do you want to perform?',
            values=[
                ('+', 'add'),
                ('-', 'subtract'),
                ('*', 'multiply'),
                ('/', 'divide')
            ]

        ).run()
        if result is not None:
            break
        message_dialog(title='Invalid choice', text='You must select a valid operations').run()
    print(f'{result=}')
    return result


def get_number(prompt: str) -> float:
    while True:
        text = input_dialog(title='Input number',
                            text=prompt).run()
        try:
            value = float(text)
        except ValueError:
            message_dialog(title='Invalid number', text='Please enter a number').run()
        else:
            return value
            break


def perform_operation(n1, n2, opr) -> float:
    match opr:
        case '+':
            return n1 + n2
        case '-':
            return n1 - n2
        case '*':
            return n1 * n2
        case '/':
            return n1 / n2
        case _:
            return None


def perform_one_calculation():
    num1 = get_number('Enter first number')
    num2 = get_number('Enter second number')
    operation = get_operation()
    result = perform_operation(num1, num2, operation)
    msg = f'{num1} {operation} {num2} = {result}'
    message_dialog(title='Result', text=msg).run()


def main():
    keep_calculating = True
    while keep_calculating:
        perform_one_calculation()
        keep_calculating = yes_no_dialog(title='Another calculation?', text='Perform another calculation?').run()

    message_dialog(title='Thanks', text='Thanks for using my calculator').run()
    print('Thanks for using my calculator')


if __name__ == '__main__':
    print(f'Python version: {get_python_version()}')
    print(f'prompt_toolkit version: {get_package_version("prompt_toolkit")}')
    main()
