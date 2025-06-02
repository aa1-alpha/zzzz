import login
import signup
import users
import delete

def main():
    while True:
        print("\nWelcome to the Vault")
        choice = input("What would you like to do?\n"
                       "1. Create account\n"
                       "2. Sign in to Account\n"
                       "3. Delete account\n"
                       "4. Exit\n")

        if choice == "4":
            print("Bye!")
            break
        elif choice == "3":
            username = input("What is your username? ")
            delete.delete_account(username)
            
        elif choice == "2":
            user_name = input("What is your username ")
            pass_word = input("What is your password ")
            login.login(user_name, pass_word)
          
            # login.sign_in()  # Placeholder
        elif choice == "1":
            username =  input("what do you choose as you username ")
            password = input("what do you choose as your password ")         
            signup.signup(username, password)
          
           
          
        else:
            print("Try again")

# Run the main function
main()
