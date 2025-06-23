
#1 Age calculator
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta

def age(birth_date):
    dob = dt.strptime(birth_date, '%Y-%m-%d')
    today = dt.today()
    diff = relativedelta(today, dob)
    return f"You a are {diff.years} year(s), {diff.months} month(s) and {diff.days} day(s) old"
#2 Next Birtday calculator
from datetime import datetime as dt, date
def next_bd(dob):
    dob = dt.strptime(dob, '%Y-%m-%d')
    today = dt.today().date()
    next_bd = None
    if (dob.month < today.month) or (dob.month == today.month and dob.day < today.day):
        next_bd = date(today.year + 1, dob.month, dob.day)
    else:
        next_bd = date(today.year, dob.month, dob.day)
    diff = next_bd - today
    diff = diff.days
    if diff == 0:
        return "Today is your Birthday!"
    else:
        return f"Your next Birthday is in {diff} day(s)"
#3
current = input('Please, enter the current date and time(YYYY-mm-dd HH:MM): ')
current = datetime.strptime(current, '%Y-%m-%d %H:%M')
duration = input('How long does the meeting last (HH-MM)?: ')
duration = datetime.strptime(duration, '%H:%M')
hours = duration.hour
minutes = duration.minute
time_to_add = timedelta(hours=hours, minutes=minutes)
end_time = current + time_to_add
print(end_time)
#4
import pytz
from datetime import datetime

def timezone_converter(date_and_time, current_timezone, target_timezone):
    dt = datetime.strptime(date_and_time, '%Y-%m-%d %H:%M:%S')
    current_zone = pytz.timezone(current_timezone)
    current_dt = current_zone.localize(dt)
    target_zone = pytz.timezone(target_timezone)
    target = current_dt.astimezone(target_zone)

    return target
#5
def countdown(fdate):
    future_date = datetime.strptime(fdate, '%Y-%m-%d %H:%M:%S')
    while True:
        now = datetime.now().replace(microsecond=0)
        diff = future_date - now

        print(diff)
        t.sleep(1)
        if not diff:
            print("Time is up!")
            break
#6
import re



def email_validator(email: str):
    
    try:
        pattern = r'\b[\w._%+-]+@[\w._-]+\.[A-Za-z._%+-]+\b'
        result = re.match(pattern, email.strip())

    except (AttributeError, TypeError):
        print('The input is of wrong data type')
        return

    if result:
        print(f"Your email '{email}' is valid")
    else:
        print(f"Your email '{email}' is NOT valid")

email_validator(123)

#7
def format_number(digits):
    if len(digits) != 10:
        return "Invalid phone number. Must contain exactly 10 digits."

    formatted_number = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"

    return formatted_number

#8
import re
password = '0!98a-sA'

def pass_checker(password):
    upper_case_pattern = ".*?[A-Z]+.*?" # pattern for uppercase letters
    lower_case_pattern = ".*?[a-z]+.*?" # pattern for lowercase letters 
    digit_pattern = ".*?[0-9]+.*?" # pattern for digits
    special_pattern = "^.*[,.!/<>?|':\\\"=+-_&^%$#`~]+.*$" # pattern for special characters like @ & - _
    
    if len(password) < 8: # checks the length of the password> If the length is less than 8 characters, notifies the user that it must be at least 8 and ends the function
        print('The password is too short. It must me at least 8 characters long')
        return
    if not re.match(upper_case_pattern, password): # chechs whether any uppercse letters are present in the password using the match function from re module and if it does not exists print the text and stops the function
        print('The password must contain at least one uppercase letter')
        return
    if not re.match(lower_case_pattern, password): # the same as for uppercase letters but for lowercase
        print('The password must contain at least one lowercase letter')
        return
    if not re.match(digit_pattern, password): # checks whether any digits are present
        print('The password must contain at least one digit')
        return
    if not re.match(special_pattern, password): # checks for special chracters
        print('The password must contain at least one special character')
        return
    print('Your password is secure') # Informs the user htat the password is secure if it satisfies (or rather does NOT satisfy) all the above conditions
        
#9
import re  # import the module

# A random text to look for a word
text = '''Bob was an ordinary guy, except for the fact that his toaster had developed sentience after a lightning strike and now demanded to be called Sir Toastalot. Every morning, Bob would wake up, walk into the kitchen, and be greeted with, “Kneel before your carb overlord!” before being allowed to make breakfast.

One day, Bob tried to unplug Sir Toastalot. Big mistake.

The toaster screamed, shot out two flaming bagels, and declared martial law in the kitchen. The microwave surrendered immediately, the blender joined the rebellion, and the fridge went into lockdown mode. Bob now lives in the garage and barters with the appliance regime using AA batteries and kind words.

The moral of the story?
Never insult a toaster with a superiority complex. Especially not one that knows how to make grilled cheese and wage psychological warfare.'''


def word_finder(word): # get a word to be searched from a user as input

    try:
        pattern = str(word) # cast the input to a string in case non_string argument is given. Text is a string, so, logically, we should look for a string
    except ValueError:
        return "The looking value must be a string" # if the argument is not convertable to str, then prints a warning

    result = re.findall(pattern, text) # finds all occurences of the word in the text

    if not result:
        return f"There are no occurences of the word '{word}' in the text" # if no words there are in the text, it says so
        
    return result # returns the result

#10
def find_date(text):
    
    pattern = '[0-9]{4}-[0-9]{,2}-[0-9]{,2}'
    
    result = re.findall(pattern, text)

    return result
