import json

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def temp_func():
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from ECR Test!')
    }

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('test')
    temp_func()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
