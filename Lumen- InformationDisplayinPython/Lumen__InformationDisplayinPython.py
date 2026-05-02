
from ast import And


print("Welcome to the lumen information area, what would you like to know")

questions= ["Index 0?",
            "Who is lumen?",
            "What are lumen's interest?",
            "How many languages does lumen speak?",
            "Does lumen have a crush?",
            "Lumen's favorite videogame franchise?"]

answers = ["Zero :3",
           "A guy that is in his 20's",
           "Videogames, Computers and Weather to some extent :)",
           "Spanish (native language), English(quite basic) and Brazilian Portuguese(easy to understand and i can speak it to a lesser extent)",
           "No, i don't, and that's okay :)",
           "Sonic the Hedgehog"]

print("")
print("Choose which question you are curious about")

for i in questions:
    print(i)
    

choosing = int(input("type the number of which question sounds more interesting: "))

for i in answers:
    if choosing >=1 and choosing <= len(answers):
        print(answers[choosing])
        break
    else:
        print("Invalid Option")
        break
