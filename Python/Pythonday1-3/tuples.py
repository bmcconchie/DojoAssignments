dog = ("canis Familiaris", "dog", "carnivore",12,)
    # print dog

for data in dog:
    # print data

    dog = dog + ("domestic",)
# print dog
dog = dog[:3] + ("man's best friend",) + dog[4:]
print dog
