word_list = {
    'JavaScript': '''It is most well-known  lightweight, 
        interpreted programming language/scripting 
        language for Web pages''',
    'Force': '''A force is any interaction that, when unopposed, 
        will change the motion of an object.''',
    'Program': '''A collection of instructions that can be 
         executed by a computer to perform a specific task''',
    'Synergy': 'A synergy is where the whole is greater than the sum of its parts.'
}
continueOrNot = 'y'
while continueOrNot.lower() == 'y':
    print('''
           Welcome To My Dictionary:
           1. javascript 2. force 3. program 4. synergy
       ''')
    word = int(input('Type the option number to choose a word from dictionary: '))
    flag = 0
    for index, words in enumerate(word_list):
        if word-1 == index:
            print(f'{words.capitalize()}: {word_list[words]} ')
            flag = 1
            break
    if flag == 0:
        print('Word not found in the dictionary')
    continueOrNot = input('Do you want to continue? (Y/N)')
else:
    print('Thanks for Playing :)')
