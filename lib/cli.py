# lib/cli.py
import ipdb

from helpers import (
    exit_program,
    create_question,
    create_animal_type,
    delete_question,
    delete_animal_type,
    find_animal_type_by_id,
    find_question_by_id,
    view_all_animal_types,
    view_all_questions,
    play_game
)


def main():
    while True:
        menu()
        choice = input(">")
        if choice == "0":
            exit_program()
        elif choice == "1":
            create_question()
        elif choice == "2":
            create_animal_type()
        elif choice == "3":
            delete_question()
        elif choice == "4":
            delete_animal_type()
        elif choice == "5":
            find_animal_type_by_id()
        elif choice == "6":
            find_question_by_id()
        elif choice == "7":
            view_all_animal_types()
        elif choice == "8":
            view_all_questions()
        elif choice == "9":
            play_game()
        else:
            print("Invalid choice")
            input("\nPress 'return' to continue... \n")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Create a question")
    print("2. Create a animal type")
    print("3. Delete a question")
    print("4. Delete an animal type")
    print("5. Find an animal by id")
    print("6. Find a question by id")
    print("7. View all animal types")
    print("8. View all questions")
    print("9. Play game")


if __name__ == "__main__":
    main()
   
