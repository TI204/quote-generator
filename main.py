from quotes import *

def menu():
    print("\n==== Programming Quotes ====")
    print("1. Random quote")
    print("2. All quotes")
    print("3. Exit")

def main():
    while True:
        menu()

        choice = input("Choose your an action (1-3): ")
        
        if choice == "1":
            print_quote(random_quote())
        elif choice == "2":
            view_quotes()
        elif choice == "3":
            print("Good bye...")
            break
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()
