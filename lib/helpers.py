# lib/helpers.py
from models.animals import Animals
from models.questions import Questions


def create_question():
    question = input("Enter the text for the question > ")
    correct_answer=input("Enter the correct answer here 1 for true, 0 for false")
    animal_id = input('Enter animal id here')
    
    try:
        new_question = Questions.create(str(question),int(correct_answer))
        print("New question successfully created")
        print(new_question, correct_answer, animal_id)
    except:
        print("Error: Unable to make a new question, information invalid")

def delete_question():
    id = input("Enter the id for the question that you want to delete > ")
    question = Questions.find_by_id(id)

    if question:
        question.delete()
        print(f"question # {id} was successfully deleted")
    else:
        print(f"Unable to delete question # {id}")

def find_question_by_id():
    id = input ('enter the id of the question you would like to see')
    question = Questions.find_by_id(id)

    if question:
        print(f"Here is the information for the Question #{id}:")
        print(question)
    else: print(f"error: Question {id} could not be found")


def view_all_questions():
    questions = Questions.get_all()

    if len(question) > 0:
        print("Here is the information for all of the questions:")
        for question in questions:
            print(question)
    else:
        print("There are no questions available")
    

def create_animal_type():
    animal_type = input('enter the animal type here')
    animal_id = input('enter animal id here')
    try:
        new_animal_type = Animals.create(str(animal_type))
        print("New animal type successfully created! View details:")
        print(new_animal_type, animal_id)
    except:
        print("Error: Unable to add new animal type")

def delete_animal_type():
    id = input("enter the id for the animal type you would like to delete")
    animal_type = Animals.find_by_id(id)

    if animal_type:
        animal_type.delete()
        print(f"animal type # {id} was successfully deleted")
    else:
        print(f"Unable to delete animal # {id}")

def find_animal_type_by_id():
    id = input("Enter the id for the animal that you want to retrieve > ")
    animal_type = Animals.find_by_id(id)

    if animal_type:
        print(f"Here is the information for the animal # {id}:")
        print(animal_type)
    else:
        print(f"Error: animal # {id} Not Found!")

def view_all_animal_types():
    animal_types = Animals.get_all()

    if len(animal_type) > 0:
        print("Here is the information for all of the animals:")
        for animal_type in animal_types:
            print(animal_type)
    else:
        print("There are no animals available")

def play_game():
    animal_id = input('enter the animal id for the type of animal questions you would like to answer' )
    animal = Animals.find_by_id(animal_id)

    if animal:
        score = 0
        for question in animal.questions():
            user_answer = input(question.text + '>') 
            try: 
                if (int(user_answer)) == question.correct_answer: 
                    print('correct answer!') 
                    score += 1
                else:
                     print('wrong answer')
            except:
                print('wrong answer')
        print(f'game over your final score is {score}')
    else:
        print('Please enter a valid animal type')
    

def exit_program():
    print("Goodbye")
    exit()