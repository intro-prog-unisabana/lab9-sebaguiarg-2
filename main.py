from bank_account import BankAccount
from person import Person
from utils import person_data, balance_summary

def main():
    people = []  # List to store all Person objects

    while True:
        # Display menu
        print("Choose an option:")
        print("1. Add a new person")
        print("2. Add an account to a person")
        print("3. Show all balances")
        print("4. Quit")

        choice = input().strip()

        # Option 1: Add a new person
        if choice == "1":
            nueva_persona = person_data()
            people.append(nueva_persona)

        # Option 2: Add an account to an existing person
        elif choice == "2":
            name_to_find = input("Enter the person's name:\n")
            found_person = None
            for p in people:
                if p.name == name_to_find:
                    found_person = p
                    break
            
            if found_person:
                acc_num = int(input("Enter a 4-digit account number:\n"))
                balance = float(input("Enter the initial balance:\n"))
                
                new_acc = BankAccount(acc_num, balance)
                found_person.add_account(new_acc)
            else:
                print("Person not found.")

        # Option 3: Show all balances
        elif choice == "3":
            if not people:
                print("No data to show.")
            else:
                balance_summary(people)

        # Option 4: Quit
        elif choice == "4":
            print("Goodbye!")
            break

        # Invalid input
        else:
            print("Invalid option. Please choose 1-4.")

if __name__ == "__main__":
    main()

