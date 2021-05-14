import time
import random
print ("Welcome to")
time.sleep (1)
print ("PHRASE")
time.sleep (1)
print ("HUNTER!!!!!!!!!!")
time.sleep(1)
firstname = input ("What is your first name: ")
lastname = input ("What is your last name: ")
spoilers = input ("Do you want a catalog of words so that you won't be too far off?, y/n: ")
words = ["hosting","python","network","server","virus","application","music","directory","protocol","domain", "registration","secure","shell","certificate","cpanel"]
if spoilers == "y":
  print ("These are the words:")
  time.sleep(0.5)
  for w in words:
    print (w)
    time.sleep (1)
else:
  print ("OK, I guess you like playing fair.")
randomword = random.choice (words)
randomword = randomword.lower()
print ("Let's play!")
guesses = ""

while True:

  current_guess = ""
  
  for char in randomword:
    if char in guesses:
      current_guess = current_guess + char + " "
    else:
      current_guess = current_guess + "_ "
  
  print(current_guess)

  if "_" not in current_guess:
    break
  
  letterguess = input ("Your letter please.... ").lower()
  
  if letterguess in randomword:
    guesses = guesses + letterguess
  else:
    print ("That is wrong. Please try again!")
print (f"YAY!! You got the word. It was {randomword}!")