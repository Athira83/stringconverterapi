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
