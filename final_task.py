# write an application that checks the strength of a password.
# Requirements:
# 
# Write a class that has a method that checks the password strength.
# Use factors like length, upper/lower case and if it has a number and special character.
# ratings should be very weak - weak - moderate - strong - very strong 
# Check against a list of common passwords 10-20 common password = very weak
# User input that loops until the user quits

# 1st stretch goal: A dictionary that returns a history of passwords/strengths whilst in the loop.

# 2nd Stretch goal:
# write tests and achieve a high score in pylint.

# Code must be pushed to a repo or emailed to me. 

# Deadline is 12.30

class PasswordChecker:
  def __init__(self):
    self.common_passwords = ["password", "123456", "qwerty", "abc123", "abcdef", "111111", "222222", "333333", "444444", "555555", "666666", "777777", "888888", "999999"]
    self.password_history = {}
  def check_password(self):
    while True:
        password = input("Please enter your Password (Quit/quit to exit):")
        if password.lower == "quit"or password == "Quit" or password == "Q":
          break

        self.score = 0
      
        if password in self.common_passwords:
          print("Very Weak")
          
  
        
        if len(password) > 8:
          self.score += 1
        elif len(password) > 12:
          self.score += 2
        elif len(password) > 16:
          self.score += 3
  
  
        if any(character.isupper() for character in password):
          self.score += 1
  
        if any (character.islower() for character in password):
          self.score += 1
  
        if any (character.isdigit() for character in password):
          self.score += 1
  
        if any (character in "!@#$%^&*()_+-=[]{}|;':,./<>?£€" for character in password):
          self.score += 1
        
        if self.score < 2:
          print("Very Weak")
        
        elif self.score == 3:
          print ("Weak")
  
        elif self.score == 4 or self.score == 5:
          print ("Moderate")
          
        elif self.score == 6:
          print ("Strong")
        elif self.score >= 7:
          print ("Very Strong")

        if self.score > 4:
          self.password_history[password] = password
          c = self.password_history.values
          print(f"Password History: {self.password_history.values()}")
                


      
        
enter = PasswordChecker()
enter.check_password()
      