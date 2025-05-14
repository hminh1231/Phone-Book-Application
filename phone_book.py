class PhoneBook:
    def menu(self):
        print('Welcome to your phone book \n What can I help you today?')
        print('1. Add new contact')
        print('2. Look up contact')
        print('3. Delete contact') #Under construction
        print('4. Browse all of your contact')
        print('5. Exit')
        
    def add(self):
        name = input('Please enter the name: ')
        number = input('Please enter the phone number:')
        with open('Phone_Book.txt','r') as info:
            check_info = info.readlines()
            for i,inf in enumerate(check_info):
                if number in inf:
                    print('The number is already in your contact list')
                    break
            else:                  
                with open('Phone_Book.txt','a') as book:
                    book.write(f'Name: {name}\n')
                    book.write(f'Telephone: {number}\n\n')
                
    def look_up(self):
        lkup = input('Please enter information (name or phone number): ')
        print('Here are all of the information that you need:')
        with open('Phone_Book.txt','r') as lk:
            lines = lk.readlines()
            for i,line in enumerate(lines):
                if lkup in line and 'Name:' in line:
                    print(line.strip())
                    print(lines[i+1])
                    break
                elif lkup in line and 'Telephone:' in line:
                    print(lines[i-1].strip())
                    print(line())
                    break
            else:
                print("Can't find the information that you need")
                
    def browse(self):
        print('Here is all of your contacts in Phone Book')
        with open('Phone_Book.txt','r') as br:
            print(br.read())
     
    # Work below here is still under construction, will update soon       
    '''def delete(self):
        name_del = input('Please enter the name that you want to delete: ')
        with open('Phone_Book.txt','r') as show:
            inf = show.readlines()
            for i, line in enumerate(inf):
                if name_del in line:
                    print(line.strip())
                    print(inf[i+1])
        number_del = input('Please enter the number of the contact that you want to delete: ')
        with open('Phone_Book.txt','r') as show:
            inf = show.readlines()
            for i,line in enumerate(inf):
                if number_del in line:
                    print(inf[i-1].strip())
                    print(line)
        choice = input('Do you want to delete this contact? (Y/N): ')
            '''
            
    def option(self):
        while True:
            while True:
                try:
                    user = int(input('Please choose your option: '))
                    if user not in range(1,6):
                        print('Your choice must be from 1-5')
                    else:
                        break
                except ValueError:
                    print('Your choice is invalid, please try again')
            if user == 1:
                self.add()
            elif user == 2:
                self.look_up()
            elif user == 3:
                print('This function is still under construction, so sorry about it')
            elif user == 4:
                self.browse()
            else:
                print('Thank you for using me')
                break

    def display(self): #Still under construction but can use it temporary now
        self.menu()
        print('')
        self.option()
        
user = PhoneBook()
user.display()
        