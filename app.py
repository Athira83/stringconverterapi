from chalice import Chalice
# import json
app = Chalice(app_name='stringconverterapi')

@app.route('/fizzbuzz/{number}')   
 def fizzbuzz(number):
     number = int(number)
     if number % 3 == 0 and number % 5 == 0:
        answer = "FizzBuzz    elif number % 5 == 0:
        answer = "Buzz"
     elif number % 3 == 0:
        answer = "Fizz"
     else:
        answer = number
     return {'answer': answer}

# @app.route('/test/text=<enter text>')
# # def index():
# #     return {'hello': 'world'}

# def process_string(text):
#     ''' The  function takes as input a string and adds a copy right symbol
#     after the names of the companies as specified in keywords '''
    
#     import re
#     keywords=['deloitte','oracle','google','microsoft','amazon']                # List of words which has to be replaced
#     response_text=''                                                            # Creating an empty response text
#     text=text.split(' ')                                                        # Splitting the string by spaces
#     for word in text:                                                           # Recreating the text with new words
#         if word.lower() in keywords:                                                
#             word=word+u"\u00a9"
#         else:
#             pass
#         response_text+=word+' '
#     return response_text
    

# def lambda_handler(event, context):
#     """ The lambda function will take a text as input from the user and add the 
#     copyrighted symbol after the given     keywords. 
#     Eg : Google : Google©
#          Oracle : Oracle©
#          Amazon : Amazon©
#          Deloitte: Deloitte©
#          Microsoft: Microsoft©
#     """

#     user_input=event['queryStringParameters']["text"]                            # To get text input from the event handler
#     user_output=process_string(user_input)
   
#     return {
#         'statusCode': 200,
#         'headers': {"Content-Type" : 'application/json ; charset:utf-8'},
#         'body': json.dumps(user_output)
#     }


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
