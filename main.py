import json
import habit


def my_handler(event, context):
    print("Hello, lambda")
    try:
        ret = habit.habit_word()
    except Exception as e:
        print("error -> " + str(e))
        return {
            'statusCode': 500,
            'body': json.dumps("habit.py error")
        }
    return {
        'statusCode': 200,
        'body': json.dumps(ret)
    }
