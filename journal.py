from os import system
import sys
import os
import datetime


def menu():
    while True:
        clear_screen()
        print(
            """Welcome to your Journal! What would you like to do?
 1. Write
 2. Read
 3. Exit
 """
        )
        user_input = input("Input: ")
        if user_input in ["1", "2", "3"]:
            return user_input
        print("I don't know that command")
        input("Press Enter to try again...")


def write():
    while True:
        clear_screen()
        # Get entry
        entry = input("Entry:\n")

        # Creating current timestamp
        now = str(datetime.datetime.now())
        current_date, current_minute = now.split(" ", 1)

        # Write to file
        with open("journal.txt", "a") as file:
            file.write(current_date + "\n" + entry + "\n\n")

        clear_screen()
        # Ask about another entry
        if input("Would you like to write another entry? (y/n) ").lower() != "y":
            break


def read():
    clear_screen()
    try:
        with open("journal.txt", "r") as journal:
            content = journal.read()
            if content.strip():
                print(content)
            else:
                print("Journal is empty! Try writing an entry first.")
    except FileNotFoundError:
        print("No Journal found! Try writing an entry first.")

    input("Press Enter to return to menu...")

def clear_screen():
    _ = os.system('clear')

def main():
    while True:
        choice = menu()
        if choice == "1":
            write()
        elif choice == "2":
            read()
        elif choice == "3":
            sys.exit()

main()
