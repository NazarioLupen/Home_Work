# color_gost

# Create a class Ghost
# Ghost objects are instantiated without any arguments.
# Ghost objects are given a random color attribute of white" or "yellow" or "purple" or "red" when instantiated
import random
class Ghost():
    def __init__ (self,my_color_list = ['white', 'yellow', 'purple', 'red']):
        self.my_color_list = random.choice(my_color_list)
    
    def color (self):
        print  (self.my_color_list)
        
ghost = Ghost()
ghost.color()
