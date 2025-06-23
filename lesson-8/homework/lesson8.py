
#1
try:
    1/0
except ZeroDivisionError:
    print("You can't divide by zero idiot")
#2
try:
    n = int(input('Please, enter an integer: '))

except ValueError:
    print('Only integers are allowed')

#3
try:
    f = open("D:\\Project\\categories.txt", 'r')
except FileNotFoundError:
    print('The file does not exist')
#4
a = input('Enter the first number: ')
b = input('Enter the second number: ')

if isinstance(a, int) and isinstance(b, int) :
    pass
else:
    print('Values must be numbers!')
#5
try:
    f = open("D:\\Project\\categories.txt", 'r')
except PermissionError:
    print("You don't have the necessary right to access this file")
#6
try:
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(lst[30])
except IndexError:
    print('The index is out of range')
#7
try:
    val = int(("Type a number: ")) # the user presses Ctrl + C
except KeyboardInterrupt:
    print('\nThe user has cancelled the input')
#8
def division(a, b):
    try:
        c = a / b
        print(f'The result of dividing {a} by {b} is: {c}')
    except ArithmeticError:
        print('An arithmetic error occured')
division(3, 0)
#9
def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            contents = file.read()
            print(contents)
    except UnicodeDecodeError as e:
        print(f'Unicode decoding error: {e}')
    except FileNotFoundError:
        print("The file you're looking for isn't found. Please assure that the file is in the correct path")
    except Exception as e:
        print(f'An unexpected error occured: {e}')
file_path = 'D:\\Project\\categories.csv'
read_file(file_path)
#10
def call_method(lst):
    try:
        lst.add()
        print(lst)
    except AttributeError:
        print('No such attribute exists')
my_list = [23, 53, 42, 2, 5]
call_method(my_list)
#11
contents = open('D:\\Project\\categories.txt', 'r')
print(contents)
#12
def read_line(n):
    with open('D:\\Project\\categories.txt', 'r') as file:
        contents = file.readlines()

    return contents[:n]
print(*read_line(2))
#13
def read_lines():
    with open("D:\\Project\\categories.txt", 'a+') as file:
        file.write('\n8,Starbucks')

        file.seek(0)
        contents = file.read()
        
    print(contents)
    
read_lines()
#14
def read_lines(n):
    try:
        with open("D:\\Project\\categories.txt", 'r') as file:
            contents = file.readlines()
            
        return contents[-n:]
    except FileNotFoundError as e:
        print("File doesn't exist in the given path")
        return []
    except Exception as e:
         print(f"An error occurred: {e}")
         return []
print(*read_lines(5))
#15
def read_lines():
    try:
        with open("D:\\Project\\categories.txt", 'r') as file:
            contents = file.readlines()
            
        return contents
    except FileNotFoundError as e:
        print("File doesn't exist in the given path")
    
print(read_lines())
#16
try:
    with open("D:\\Project\\categories.txt", 'r') as file:
        contents = file.readlines()
except FileNotFoundError as e:
    print("File doesn't exist in the given path")
    
print(contents)
#17
try:
    with open("D:\\Project\\categories.txt", 'r') as file:
        contents = tuple(file.readlines())
except FileNotFoundError as e:
    print("File doesn't exist in the given path")
    
print(contents)
#18
try:
    with open("D:\\Project\\categories.txt", 'r') as file:
        contents = list(file.readlines())
except FileNotFoundError as e:
    print("File doesn't exist in the given path")
    
print(contents)
#19
def find_longest_words(filename):
    try:
        with open(filename, 'r') as file:
            words = file.read().split()
        words = [word.strip(".,!?;:'\"()[]{}") for word in words]

        max_length = 0
        longest_text = list()

        for text in words:
            if len(text) > max_length:
                max_length = len(text)
                longest_text = [text]

            elif len(text) == max_length:
                if text not in longest_text:
                    longest_text.append(text)

        return longest_text, max_length
    except FileNotFoundError:
        print(f'The file "{filename}" not found')
    except Exception as e:
        print(f'An error occured. {e}')

longest, len = find_longest_words('D:\\Project\\categories.txt')
print(f'Longest word(s) of {len}: ')
for i in longest:
    print(i)
#20
def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.readlines()
        return len(contents)
    except FileNotFoundError:
        print(f"File not found in the path '{filename}'")
    except Exception as e:
        print("An unexpected error occured", e)
filepath = 'D:\\Project\\categories.txt'
print(count_lines(filepath))
#21
def count_words(filename):
    word_freq = dict()

    with open(filename, 'r') as file:
        words = file.read().split()
        for word in words:
            if word not in word_freq:
                word_freq[word] = 1
            else:
                word_freq[word] += 1
    return word_freq


print(count_words('test.txt'))
#22
import os
def get_file_size(filename):
    try:
        file_size =os.path.getsize(filename)
        return file_size
    except FileNotFoundError:
        print('File not found')
    except Exception as e:
        print('An unexpected error', e)
print(get_file_size('test.txt'))
#23
characters = ['Diluc', 'Barbara', 'Jean', 'Kaeya', 'Albedo', 'Qiqi', 'Hu Tao']
def write_list():
    try:
        with open('genshin.txt', 'w+') as file:
            for character in characters:
                file.write(f'{character}\n') 
            file.seek(0)
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print('File not found')
    except Exception:
        print('An unexpected error occured')
write_list()
#24
def copy_file():
    try:

        with open('new_file.txt', 'w+') as file:
            with open('genshin.txt', 'r+') as gen:
                for i in gen:
                    file.write(i)
            file.seek(0)
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print('File not found')
    except Exception:
        print('An unexpected error occured')

copy_file()
#25
def copy_file():
    try:
        with open('first_names.txt', 'r') as fn:
            fnames = fn.readlines()
        with open('last_names.txt', 'r') as ln:
            lnames = ln.readlines()

        combined = []

        for f, l in zip(fnames, lnames):
            combined.append(f.strip() + ' ' + l.strip() + '\n')

        with open('full_names.txt', 'w') as file:
            file.writelines(combined)

    except FileNotFoundError:
        print('File not found') 
    except Exception as e:
        print('An unexpected error occured', e)

copy_file() 
#26
import random
def read_random_line():
    try:
        with open('full_names.txt', 'r') as file:
            lines = file.read().splitlines()
        return random.choice(lines)
    except FileNotFoundError:
        print('File Not Found')
    except Exception as e:
        print('An unexpected error popped up', e)
print(read_random_line())
#27
def is_closed(filename):
    if filename.closed == True:
        print('The file is closed')
    else:
        print("The file is open")  


file = open('full_names.txt')

is_closed(file)
#28
def remove_new_line(filename):
    with open(filename, 'r') as file:
        contents = file.read().replace('\n', '')
    with open(filename, 'w') as outfile:
        outfile.write(contents)
    return contents
    
print(new_line('full_names.txt'))
#29
def num_of_words(filename):
    with open(filename, 'r') as file:
        contents = file.read().replace(',', ' ')
    words = contents.split()
    return len(words)


print(num_of_words('full_names.txt'))
#30
#31
def create_file():
    try:
        for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            with open(f'{i}.txt', 'w'):
                pass
    except FileNotFoundError:
        print('File not found')
    except Exception:
        print('An unexpected error occured')

create_file()
#32
with open('Alphabet.txt', 'w+') as file:
    counter = 0 # To count how many character there are currently in line
    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        file.write(letter)
        counter += 1 # Adds 1 after each write, which is one letter
        if counter == 4: # Number of letters per line
            file.write('\n') #Goes to a new line once the limit is reached
            counter = 0 #Sets counter back to zero, and then counts again
