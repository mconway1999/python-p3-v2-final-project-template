# Phase 3 Animal Trivia Project

## Introduction

Welcome to my Phase 3 project!

This is an animal trvia game.

There are five different animal types to start with. Each animal type has four questions. 

In this project, users have the ability to add questions and add the corrosponding animal types, if not already declared.
Users have the ability to delete questions and animal types, find them by their ID, and find all animal types and questions.


Take a look at the directory structure:

```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    │   ├── animals.py
    |   └── questions.py
    ├── cli.py
    ├── debug.py
    ├── helpers.py
    └── seed.py
```

---

## Generating Your Environment

 Run the commands:

```console
python lib/cli.py
```
---

## Generating Your CLI


When using the menu:

enter 0 to exit the program

enter 1 to create a question

enter 2 to create a animal type

enter 3 to delete a question

enter 4 to delete an animal type
    
enter 5 to find an animal by id

enter 6 to find a question by id

enter 7 to view all animal types

enter 8 to view all questions

enter 9 to play game

        enter 0 for if you think the answer is false
        enter 1 if you think the answer is true

## Conclusion

This project allows for an interactive approach to add, delete, and find different questions and animal types. 
While users have the ability to play a game and answer questions, they also have the ablity to customize the game to their liking. 

---


