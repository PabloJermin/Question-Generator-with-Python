import random

import random

# list of dictionary for all celibrities
celibrities = [{
    "name": "Christiano Ronaldo",
    "country": "portugal",
    "followers": 250000,
},
    {"name": "Didier Drogba",
     "country": "Cote d'voire",
     "followers": 12000
     },
    {"name": "Stephen Appiah",
     "country": "Ghana",
     "followers": 2900
     },
    {"name": "Fernando Torres",
     "country": "Spain",
     "followers": 6700
     },
    {"name": "Van DerSar",
     "country": "Netherland",
     "followers": 570
     }
]



def account(person):
    """takes a rperson and returns the name country """
    p_name = person["name"]
    p_country = person["country"]
    return f"{p_name} from {p_country}"

# comparing followers and answers
def chooser(answer, p1_followers, p2_followers):
    """tCompares the number of followers and returns the highest person with followers"""
    if p1_followers > p2_followers:
        return answer == 'A'
    else:
        return answer == 'B'


score = 0
game_continue = True

person2 = random.choice(celibrities)

while game_continue:
    # generating a random account
    person1 = person2
    person2 = random.choice(celibrities)
    while person1 == person2:
            person2 = random.choice(celibrities)

    print(f"Compare A: {account(person1)}")
    print(f"And B: {account(person2)}")

    answer = input(f"Who has more followers? A or B  ? ").upper()

    p1_followers = person1["followers"]
    p2_followers = person2["followers"]


    right = chooser(answer, p1_followers, p2_followers)

    if right:
        score += 1
        print(f"You are right! your score is: {score}")
    else:
        print(f"Sorry, you got it wrong. your final score is {score}")
        game_continue = False

