import random

fruits = [
    "Apple", "Banana", "Orange", "Mango", "Grapes",
    "Pineapple", "Strawberry", "Blueberry", "Watermelon", "Cherry",
    "Peach", "Pear", "Kiwi", "Papaya", "Pomegranate"
]

animals = [
    "Lion", "Tiger", "Elephant", "Giraffe", "Zebra",
    "Kangaroo", "Panda", "Dolphin", "Eagle", "Wolf",
    "Rabbit", "Crocodile", "Bear", "Owl", "Horse"
]

cartoons = [
    "Mickey-Mouse", "SpongeBob-SquarePants", "Tom-and-Jerry", "Scooby-Doo", "Bugs-Bunny",
    "The-Simpsons", "Rick-and-Morty", "Looney-Tunes", "Popeye", "Dora-the-Explorer",
    "Teen-Titans", "Ben-10", "Avatar:-The-Last-Airbender", "Phineas-and-Ferb", "The-Flintstones"
]




selectedCategory = random.choice([fruits, animals, cartoons])
# selectedWord = random.choice(selectedCategory)

print(selectedCategory , selectedCategory)