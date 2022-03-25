from datetime import date, datetime
import re


def process_message(message, response_array, response):

    list_message = re.findall(r"[\w']+|[.,!?;]", message.lower())

    score = 0
    for word in list_message:
        if word in response_array:
            score += 1

    return[score, response]


def get_response(message):
    now = datetime.now()
    response_list = [
        process_message(message, ['hello', 'hi', 'hey'],
                        'Greetings, whatcha been up to?'),
        process_message(message, ['goodbye', 'bye'], 'Until we meet again!'),
        process_message(message, ['thank', 'thanks', ],
                        'No problem, happy to be of help!'),
        process_message(message, ['how', 'doing', 'been'],
                        'Feeling great today, thank you for asking'),
        process_message(message, [
                        'time', 'date'], f"The date and time are {now.strftime('%d/%m/%y, %H:%M')}")
    ]
    # Above is list of possible responses

    # Below is response chosing algorithm

    response_scores = []
    for response in response_list:
        response_scores.append(response[0])

    winning_response = max(response_scores)
    matching_response = response_list[response_scores.index(winning_response)]

    if winning_response == 0:
        bot_response = 'Sorry, I don\'t understand you...'
    else:
        bot_response = matching_response[1]

    return bot_response

# get_response('Hey wassup')
