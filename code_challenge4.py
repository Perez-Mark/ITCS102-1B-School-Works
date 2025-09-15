print("Welcome to the manga Reader Recommender!")
print("Answer a few questions for your recommeded manga")

selection_genre = input("what genere do you like (action,romance,horror): ")
selection_decade = input("Which decade (2000s,2010s): ")
selection_duration = input("How long is it gonna be (short,medium,long): ")

if selection_genre == 'action':
    if selection_decade == '2000s':
        if selection_duration == 'short':
            print("We recommend short-action-manga-2000s")
        elif selection_duration == 'medium':
            print("We recommend medium-action-manga-2000s")
        elif selection_duration == 'long':
            print("We recommend long-action-manga-2000s")
    elif selection_decade == '2010s':
        if selection_duration == 'short':
            print("We recommend short-action-manga-2010s")
        elif selection_duration == 'medium':
            print("We recommend medium-action-manga-2010s")
        elif selection_duration == 'long':
            print("We recommend long-action-manga-2010s")

if selection_genre == 'romance':
    if selection_decade == '2000s':
        if selection_duration == 'short':
            print("We recommend short-romance-manga-2000s")
        elif selection_duration == 'medium':
            print("We recommend medium-romance-manga-2000s")
        elif selection_duration == 'long':
            print("We recommend long-romance-manga-2000s")
    elif selection_decade == '2010s':
        if selection_duration == 'short':
            print("We recommend short-romance-manga-2010s")
        elif selection_duration == 'medium':
            print("We recommend medium-romance-manga-2010s")
        elif selection_duration == 'long':
            print("We recommend long-romance-manga-2010s")

if selection_genre == 'horror':
    if selection_decade == '2000s':
        if selection_duration == 'short':
            print("We recommend short-horror-manga-2000s")
        elif selection_duration == 'medium':
            print("We recommend medium-horror-manga-2000s")
        elif selection_duration == 'long':
            print("We recommend long-horror-manga-2000s")
    elif selection_decade == '2010s':
        if selection_duration == 'short':
            print("We recommend short-horror-manga-2010s")
        elif selection_duration == 'medium':
            print("We recommend medium-horror-manga-2010s")
        elif selection_duration == 'long':
            print("We recommend long-horror-manga-2010s")   
