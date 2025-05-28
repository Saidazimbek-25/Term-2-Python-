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
