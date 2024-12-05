
import time as tm

class Calculator:
    def __init__(self):
        self.name = 'Bimscalculator'
    def home(self): 
          
        option = input(f'''
        loading.......
        Welcome to {self.name} 
        1. Addition
        2. Subtraction
        3. Division
        4. Multiplication
        5. Exit
 choose:- ''')
        if option == '1':
            self.Addition() 
        elif option == '2':
            self.Subtraction()
        elif option == '3':
            self.Division()
        elif option == '4':
            self.Multiplication()
        elif option == '5':
            self.exit()
           
        else:
            print('Inavlid code')
            self.home()
            
    def Addition(self):
        try:
           val1 = int(input('Value1: ')) 
           val2 = int(input('Value2: '))  
           result = val1 + val2
           print(f'Your result is {result}')
           self.home()
        except ValueError:
            print('code error')

    def Subtraction(self):
        try:
            val1 = int(input('Value1: ')) 
            val2 = int(input('Value2: '))  
            result = val1 - val2
            print(f'Your result is {result}')
            self.home()
        except ValueError:
            print('code error')

    def Division(self):
        try:
            val1 = int(input('Value1: ')) 
            val2 = int(input('Value2: '))  
            result = val1 / val2
            print(f'Your result is {result}')
            self.home()
        except TypeError:
            print('code error')

    def  Multiplication(self):
        try:
            val1 = int(input('Value1: ')) 
            val2 = int(input('Value2: '))  
            result = val1 * val2
            print(f'Your result is {result}')
            self.home()
        except ValueError:
            print('code error')

    def exit(self):
        print('loading........')
        tm.sleep(1)
        print(f'Thank you for using {self.name}👍')
        

app = Calculator()
app.home()