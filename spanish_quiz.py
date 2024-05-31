def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }

    #declaring usefull variables
    questions_number = len(translations)
    correct_counter = 0

    #looping over the dictionary
    for word, translation in translations.items():
        #ask the user for the input
        response = input('What is the Spanish translation for ' + word + '? ')
        if response == translation:
            # if correct print and increment counter
            print('That is correct!')
            correct_counter += 1
        else:
            print('That is incorrect, the Spanish translation for ' + word + ' is ' + translation + '.')
        # using print to add an empty line
        print('')
        # showing the score to the user
    print('You got ' + str(correct_counter) + '/' + str(questions_number) + ' words correct, come study again soon!')


if __name__ == '__main__':
    main()
