
#1  ToDo List Application
class Task:
    def __init__(self, title, description, due_date, status = "Incomplete"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f'{self.title}, {self.description}, {self.due_date}, {self.status}'

    def mark_complete(self):
        self.status ='Completed'

class ToDoList:
    
    def __init__(self):
        self.list_of_tasks = []

    def add_task(self, task: Task):
        self.list_of_tasks.append(task)
        print(f"\nNew task'{task.title}' was created")

    def complete_task(self, index):
        self.list_of_tasks[index-1].mark_complete()
        print(f"\nTask '{self.list_of_tasks[index-1].title}' was marked complete")

    def list_all(self):
        if self.list_of_tasks:
            for index, task in enumerate(self.list_of_tasks):
                print(f"{index+1}. {task}")
        else:
            print("\nThere are no tasks in your to-do list, yet.")
        
    def list_incomplete(self):
        for index, task in enumerate(self.list_of_tasks):
            if task.status == 'Incomplete':
                print(f"{index}. {task}")
        else:
            print("\nYou don't have any uncompleted tasks")


def print_menu():
    print('\nTo-Do List Menu: ')
    print('1. Add a task')
    print('2. Mark a task as complete')
    print('3. List all tasks')
    print('4. Display incomplete tasks')  
    print('5. Exit')  

def main():
    task1 = Task('Reading', 'Finishing 13th chapter of "Demon haunted world"', '2025-06-05', 'Incomplete')
    To_Do = ToDoList()
    To_Do.add_task(task1)


    while True:
        
        print_menu()
        choice = input('Enter your choice (1-5): ')

        if choice == '1':
            title = input('Please, enter the title of your task: ')
            description = input('Please, enter the description of your task: ')
            due_date = input('Please, enter the deadline of your task: ')
            new_task = Task(title, description, due_date)
            To_Do.add_task(new_task)

        elif choice == '2':
            print('\n')
            To_Do.list_all()
            print('\n')
            ind = int(input('Select the number of the task you want to mark as complete: '))
            To_Do.complete_task(ind)

        elif choice == '3':
            print('\nYour tasks:')
            To_Do.list_all()

        elif choice == '4':
            print('\nIncomplete tasks:')
            To_Do.list_incomplete()

        elif choice == '5':
            print('\nGoodbye!\n')
            break
        
        else:
            print('Invalid choice')

if __name__=="__main__":
    main()

#Blog system
class Post:


    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"\nAbout: {self.title}.\nContent: {self.content}.\nBy: {self.author}\n"
    
    
class Blog:


    def __init__(self):
        self.all_posts = []

    def add_post(self, post: Post):
        self.all_posts.append(post)
    
    def list_posts(self):
        if self.all_posts:
            for num, post in enumerate(self.all_posts, 1):
               print(f"{num}. {post}")
        else:
            print("\nThere are no posts in the blog")
    
    def list_by_author(self, author):
        for i in self.all_posts:
            if i.author == author:
                print(i)
        else:
            print(f"\nThere are no posts by this author '{author}'.")

    def delete_post(self, post_ind):
        if 1 <= post_ind <= len(self.all_posts):
            deleted_post = self.all_posts.pop(post_ind - 1)
            print(f"\nPost '{deleted_post.title}' by {deleted_post.author} was deleted.")
        else:
            print('\nInvalid post number.')

    def edit_post(self, post_ind, new_title, new_content):
        if 1 <= post_ind <= len(self.all_posts):
            post = self.all_posts[post_ind - 1]
            post.title = new_title
            post.content = new_content
            print(f"\nThe post '{post.title}' by {post.author} was updated succesfully.")
        else:
            print('\nInvalid post number.')

    def display_latest(self, count = 3):
        if not self.all_posts:
            print('\nThere are no posts in this blog, yet')
            return
        if count > len(self.all_posts):
            print(f'There are only {len(self.all_posts)} posts!')
            
        print(f'The latest {min(count, len(self.all_posts))} posts:')
        latest_posts  = self.all_posts[-count:]
        for ind, post in enumerate(reversed(latest_posts), 1):
            print(f'{len(self.all_posts) - (ind - 1)}. {post}')


def print_menu():
    print('\nBlog management manu:')
    print('1. Add a post')
    print('2. List all posts')
    print('3. Display posts by an author')
    print('4. Delete a post')
    print('5. Edit a post')
    print('6. View recent posts')
    print('7. Exit')

def main():

    post = Post('Aliens among us!', 'blah blah blah blah blah', 'Psychopath')
    blog = Blog()
    blog.add_post(post)

    while True:
        print_menu()
        try:
            choice = int(input('\nEnter your choice (1-7): '))
        except ValueError:
            print('Invalid input. Please enter a number between 1 and 4.')
            continue  # skip to the next loop iteration

        if choice == 1:
            title = input('Please, enter the title of the post: ')
            contents = input('Please, enter the contents of the post: ')
            author = input('Please, enter the author of the post: ')
            new_post = Post(title, contents, author)
            blog.add_post(new_post)
            print(f"\nNew post '{new_post.title}' was added!")
        
        elif choice == 2:
            print('\nAll posts:')
            blog.list_posts()
        
        elif choice == 3:
            author = input('\nWhose posts do you want to see?: ')
            print(f'\nPosts by {author}:\n')
            blog.list_by_author(author)

        elif choice == 4:
            blog.list_posts()
            try:
                ind = int(input('\nPlease enter the number of the post you want to delete: '))
                blog.delete_post(ind)
            except ValueError:
                print('\nInvalid input. Please enter a valid post number.')
        elif choice == 5:
            blog.list_posts
            try:
                ind = input('\nPlease enter the number of the post you want to edit: ')
                new_title = input('\nPlease enter the new title for the post: ')
                new_content = input('\nPlease enter the new content for the post: ')
                blog.edit_post(ind, new_title, new_content)
            except ValueError:
                print('\nInvalid input. Please enter a valid post number')

        elif choice == 6:
            try:
                count = int(input('\nHow many latest posts do you want to see?: '))
                blog.display_latest(count)
            except ValueError:
                print('\nInvalid input. Please, enter a number')

        elif choice == 7:
            print('\nGoodbye!👋👋\n')
            break

        else:
            print('Invalid option. Please choose a number between 1 and 4')

if __name__ == '__main__':
    main()
#Simple Banking System
class Account:


    def __init__(self, account_number: int, account_holder_name: str, balance: float):

        self.account_number = account_number
        self.holder_name = account_holder_name.capitalize()
        self.balance = balance


    def __str__(self):

        return f"\n'{self.account_number}' account holder '{self.holder_name}' has ${self.balance}"
    

    def deposit(self, amount):

        self.balance += amount*0.9 # 1% Interest rate
        print(f"\n${amount} has been successfully deposited to {self.account_number}.")


    def withdraw(self, amount):
        if self.balance < amount:
            ans = input('\nThe user has less money in his balance than you want to withdraw. Are you sure you want to carry out the withdrawal? (Y/N): ')
            if ans == 'Y':
                self.balance -= amount
                print(f"\n${amount} has been successfully withdrawn from {self.account_number}.")
                print(f"\nThe user now owes ${self.balance*(-1)} to the Bank")
            elif ans == 'N':
                print('\nThe withdrawal was cancelled')
                return
            
            else:
                print("\nPlease, enter either 'Y' or 'N'")
                return
        else:
            self.balance -= amount
            print(f"\n${amount} has been successfully withdrawn from {self.account_number}.")
        


    def check_balance(self):
        return self.balance



class Bank:


    dict_of_accounts = dict()

    def __init__(self):
        pass


    def add_account(self, new_account: Account):
        if new_account.account_number not in self.dict_of_accounts.keys():
            self.dict_of_accounts[new_account.account_number] = new_account
            print(f"\nAccount {new_account.account_number} added.")
        else:
            print("T\nhere's already a user with this number. Please choose another one")

    
    def get_account(self, account_number):
        return self.dict_of_accounts.get(account_number)

    def list_all(self):
        for account in self.dict_of_accounts.values():
            print(account)


    def check_balance(self, account_num):
        
        account = self.get_account(account_num)
        if account:
            print(f"\nAccount {account_num} has ${account.check_balance()} in balance.")
        else:
            print(f"\nAccount {account_num} not found.")


    def deposit_money(self, account_num, amount):

        account = self.get_account(account_num)
        if account:
            account.deposit(amount)
        else:
            print(f"\nAccount {account_num} not found.")
            

    def withdraw_money(self, account_num, amount):

        account = self.get_account(account_num)
        if account:
            account.withdraw(amount)
        else:
            print(f"\nAccount{account_num} not found.")

    
    def transfer(self, from_account, to_account, amount):
        sender = self.get_account(from_account)
        receiver = self.get_account(to_account)
        if sender.balance >= amount:
            sender.balance -= amount
            receiver.balance += amount
        else:
            ans = input(f"\nThe sender has less money in his balance than you want to withdraw. Are you sure you want to carry out the withdrawal? (Y/N): ")
            if ans == 'Y':
                sender.balance -= amount
                receiver.balance += amount
                print(f"\nThe tansfer was successfully carried out")
                print(f"\nThe sender now owes ${sender.balance*(-1)} to the Bank")


            elif ans == 'N':
                print('\nThe withdrawal was cancelled')
                return
        
            else:
                print("\nPlease, enter either 'Y' or 'N'")
                return


    def account_details(self, account_number):
        account = self.get_account(account_number)
        print(account)

def print_menu():
    print('\n1. Add an account.')
    print('2. Check balance.')
    print('3. Deposit money.')
    print('4. Withdraw money.')
    print('5. List all account holders.')
    print('6. Transfer money.')
    print('7. See account details.')
    print('8. Exit.')


def main():

    acc = Account(1, 'Shohruh', 1000)
    bnk = Bank()
    bnk.add_account(acc)

    while True:
        
        print_menu()
        choice = input('\nPlease, enter your option (1-8): ')

        if choice == '1':
            
            try:
                id = int(input("\nPlease, enter the account number: "))
                if bnk.get_account(id):
                    print(f'\nThere is already an account with this number. Please, choose another one')
                    continue
                user = input("\nPlease, enter the name of the user: ")
                balance = float(input("\nPlease, enter the balance: "))
                new_account = Account(id, user, balance)
                bnk.add_account(new_account)
            except ValueError:
                print('\nInvalid input. Please enter valid values')
                continue

        elif choice == '2':
            try:
                number = int(input("\nPlease, enter the account number you want to see the balance of: "))
                bnk.check_balance(number)
            except ValueError:
                print('\nPlease, enter a positive integer')

        elif choice == '3':
            try:
                number = int(input("\nPlease, enter the account number you want to deposit money to: "))
                if not bnk.get_account(number):
                    print(f'\nAccount {number} not found')
                    continue
                amount = float(input('\nPlease, enter the amount you want to deposit: '))
                bnk.deposit_money(number, amount)
            except ValueError:
                print('\nPlease, enter valid numbers')

        elif choice == '4':
            try:
                number = int(input("\nPlease, enter the account number you want to withdraw money from: "))
                amount = float(input('\nPlease, enter the amount you want to withdraw: '))
                bnk.withdraw_money(number, amount)
            except ValueError:
                print('\nPlease, enter valid numbers')

        elif choice == '5':
            bnk.list_all()

        elif choice == '6':
            try:
                send = int(input('\nPlease enter the account number of the sender: '))
                if not bnk.get_account(send):
                    print(f'\nAccount {send} not found')
                    continue
                receive = int(input('\nPlease enter the account number of the receiver: '))
                if not bnk.get_account(receive):
                    print(f'\nAccount {receive} not found')
                    continue
                if send == receive:
                    print('\nWhat is the point of transferring money to yourself, bro?')
                    continue
                amount = float(input('\nPlease, enter the amount you want to transfer: '))

                bnk.transfer(send, receive, amount)
            except ValueError:
                print('\nPlease, enter valid values')


        elif choice == '7':
            try:
                acc_num = int(input('\nPlease enter the account number: '))
                if not bnk.get_account(acc_num):
                    print(f'\nAccount {acc_num} not found')
                    continue
                bnk.account_details(acc_num)
            except ValueError:
                print('\nPlease, enter a valid account number')

        elif choice == '8':
            print('\nGoodbye👋\n')
            break

        else:
            print("\nPlease, enter a valid number(1-8)")

    
if __name__ == '__main__':
    main()

