from chalice import Chalice
# import json
app = Chalice(app_name='stringconverterapi')
def process_string(text):
    
    ''' The  function takes as input a string and adds a copy right symbol
    after the names of the companies as specified in keywords '''
    # from flask import request
    import re
    keywords=['deloitte','oracle','google','microsoft','amazon']                # List of words which has to be replaced
    response_text=''                                                            # Creating an empty response text
    text = text.replace('%20',' ')                                              # Replacing spaces
    text=text.split(' ')                                                        # Splitting the string by spaces
    for word in text:                                                           # Recreating the text with new words
        if word.lower() in keywords:                                                
            word = word + u"\u00a9"
        else:
            pass
        response_text +=word+' '
    return response_text
