import random


num = 0

def generate_random_number():
  return (random.randint(0,100))

def difference_from_answer(guess, answer = generate_random_number()):
  if guess < answer:
      print ("Too low")
  elif guess > answer:
      print("Too high")
  else:
    print("Correct")
   
      
    
difference_from_answer(67)
  