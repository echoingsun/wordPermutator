from itertools import permutations

prompt_list = {

    'letters_input': {
        'prompt': 'Please enter some letters: ',
        'error': 'Please enter LETTERS only: '
    },
    'digit_input': {
        'prompt': 'How many digits is the word going to be? ',
        'error': 'Please enter a NUMBER within the length of the letters: '
    },
    'char_input': {
        'prompt': 'Does any letter need to be in any specific position?\nEnter the letter and its position and '
                  'separate them with a comma.\nFor example, enter "w,3".\nPress Enter to skip.',
        'error01': 'Format error',
        'error02': 'Char error',
        'error03': 'Length error'
    }

}

def is_in_dict(word):

    with open('/usr/share/dict/words') as f1:
        lex = f1.readlines()

    mydict = []

    for each_word in lex:
        mydict.append(each_word[:-1].lower())

    if word in mydict:
        return True
    else:
        return False


def letter_check(chars):
    return chars.isalpha()


def digit_input_check(digit, length):
    if not digit.isdigit():
        return False
    elif int(digit) <= 0:
        return False
    elif int(digit) > length:
        return False
    else:
        return True


def char_position_check(string, length, chars, digit):
    if string == "":
        return 'pass'
    if len(string) < 3:
        return 'error01'

    char = string[0]
    delimiter = string[1]
    position = string[2:len(string)]

    if not position.isdigit():
        return 'error01'
    elif not (char in chars):
        return 'error02'
    elif int(position) > length or int(position) > digit:
        return 'error03'
    else:
        conditions = [char.isalpha() == True, delimiter == ',']
        if all(conditions):
            return 'pass'
        else:
            return 'error01'


def permu_gen(string, digit, char, position):

    allperm = list(permutations(string, digit))

    parts = []

    if char == 0 and position == 0:
        parts = allperm
    else:
        for each_element in allperm:
            if each_element[int(position) - 1] == char:
                parts.append(each_element)


    for each_element in parts:
        result = ""
        for char in each_element:
            result += char
        if is_in_dict(result):
            print(result)


letters = input(prompt_list['letters_input']['prompt'])
while not letter_check(letters):
    letters = input(prompt_list['letters_input']['error'])
letterlen = len(letters)

digitinput = input(prompt_list['digit_input']['prompt'])
while not digit_input_check(digitinput, letterlen):
    digitinput = input(prompt_list['digit_input']['error'])
digit = int(digitinput)

charposition = input(prompt_list['char_input']['prompt'])
while char_position_check(charposition, letterlen, letters, digit) != 'pass':
    charposition = input(prompt_list['char_input'][char_position_check(charposition, letterlen, letters, digit)])

if charposition == "":
    char = 0
    position = 0
else:
    char = charposition[0]
    position = charposition[2:len(charposition)]

permu_gen(letters, digit, char, position)
