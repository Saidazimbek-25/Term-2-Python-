from datetime import date
def age_calculator(birthdate):
    today= date.today() 
    age= today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day)
    )
    return age

year = int(input("Enter your birth year: "))
month = int(input("Enter your birth month: "))
day = int(input("Enter your birth day: "))
name=input('Enter your name:')

birthdate = date(year, month, day)
print(f"Hello  {name}! You are {age_calculator(birthdate)} years old.")
#task-2
txt = 'LMaasleitbtui'
print(txt[::2]) #output is Lasetti
print(txt[1::2]) #output is Malibu
#task-3
txt = 'MsaatmiazD'
print(txt[::2]) #output is Matiz
print(txt[-1::-2]) #output is Damas
#task-3
txt = "I'am John. I am from London" 
print(txt[-6:]) #output is London
#task-4
a = input('Enter the word you want, I will make it reverse: ')
reversed = a[::-1]
print(f'Result: {reversed}')
