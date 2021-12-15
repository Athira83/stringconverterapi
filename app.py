from chalice import Chalice
# import json
app = Chalice(app_name='stringconverterapi')
@app.route('/') 
def index(): 
    return {'hello': 'world'}


@app.route('/fizzbuzz/{number}')   
def fizzbuzz(number):
     number = int(number)
     if number % 3 == 0 and number % 5 == 0:
        answer = "FizzBuzz"    
     elif number % 5 == 0:
        answer = "Buzz"
     elif number % 3 == 0:
        answer = "Fizz"
     else:
        answer = number
     return {'answer': answer}    
@app.route('/apiconverter')
def process_string(text):
    ''' The  function takes as input a string and adds a copy right symbol
    after the names of the companies as specified in keywords '''
    
    import re
    keywords=['deloitte','oracle','google','microsoft','amazon']                # List of words which has to be replaced
    response_text=''                                                            # Creating an empty response text
    # text=str(text)                                                              # String of input
    text=text.split(' ')                                                        # Splitting the string by spaces
    for word in text:                                                           # Recreating the text with new words
        if word.lower() in keywords:                                                
            word = word + u"\u00a9"
        else:
            pass
        response_text +=word+' '
    return response_text
