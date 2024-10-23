from models.__init__ import CONN, CURSOR
from models.animals import Animals
from models.questions import Questions 



def seed_database():
    Animals.drop_table()
    Questions.drop_table()

    Animals.create_table()
    Questions.create_table()

    Animals.create("dog")
    Animals.create("cat")
    Animals.create("bird")
    Animals.create("lizard")
    Animals.create("rabbit")

    Questions.create("English mastiff is the largest breed of dog? ENTER 1 FOR TRUE ---- ENTER 0 FOR FALSE",1,1)
    Questions.create("Dogs were the first animals to be domesticated by humans? ENTER 1 FOR TRUE ---- ENTER 0 FOR FALSE",1,1)
    Questions.create("Doberman pincher is the fastest breed of dog? ENTER 1 FOR TRUE ---- ENTER 0 FOR FALSE",0,1)
    Questions.create("Ollie  is the name of the terrier dog from the movie 'Wizard of Oz?' ENTER 1 FOR TRUE ---- ENTER 0 FOR FALSE",0,1)
    Questions.create("Cats are only right handed? ENTER 1 FOR TRUE ---- ENTER 0 FOR FALSE",0,2)
    Questions.create("In Ancient China sailors consider cats on the ship to be good luck? ENTER 1 FOR TRUE ---- ENTER 0 FOR FALSE",1,2)
    Questions.create("Felinophobia is a fear of cats? ENTER 1 FOR TRUE ---- ENTER 0 FOR FALSE",1,2)
    Questions.create("when a cat squints their eyes they feel fear and anxiety? ENTER 1 FOR TRUE ---- ENTER 0 FOR FALSE",0,2)
    Questions.create("Swan in a symbol of peace? ENTER 1 FOR TRUE ---- ENTER 0 FOR FALSE",0,3)
    Questions.create("An ostrich lays the biggest egg? ENTER 1 FOR TRUE ---- ENTER 0 FOR FALSE",1,3)
    Questions.create("Eastern bluebird is New York's state bird? ENTER 1 FOR TRUE ---- ENTER 0 FOR FALSE",1,3)
    Questions.create("A tucan is the breed of bird with the longest beak? ENTER 1 FOR TRUE ---- ENTER 0 FOR FALSE",0,3)
    Questions.create("Geckos are known for its ability to walk on vertical surfaces and even hang upside down using specialized toe pads? ENTER 1 FOR TRUE ---- ENTER 0 FOR FALSE",1,4)
    Questions.create("A Komodo dragon is the largest type of lizard? ENTER 1 FOR TRUE ---- ENTER 0 FOR FALSE",1,4)
    Questions.create("Lizards have bad eyesight? ENTER 1 FOR TRUE ---- ENTER 0 FOR FALSE",0,4)
    Questions.create("Earless Monitor Lizard is the most expensive lizard, ENTER 1 FOR TRUE ---- ENTER 0 FOR FALSE",1,4)
    Questions.create("Eight years is the average lifespan of a wild rabbit? ENTER 1 FOR TRUE ---- ENTER 0 FOR FALSE",0,5)
    Questions.create("According to superstition, carrying around a rabbit's foot will bring protection and good luck, ENTER 1 FOR TRUE ---- ENTER 0 FOR FALSE",1,5)
    Questions.create("Rabbits have a strong sense of smell to protect them from predators, ENTER 1 FOR TRUE ---- ENTER 0 FOR FALSE",1,5)
    Questions.create("The average rabbit rotate their ears 180 degrees? ENTER 1 FOR TRUE ---- ENTER 0 FOR FALSE",0,5)



seed_database()
print("animal type and question successfully seeded! ")


