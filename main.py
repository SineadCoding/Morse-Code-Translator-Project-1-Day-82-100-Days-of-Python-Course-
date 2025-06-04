morse_alphabet = { 'a':'.- ', 'b':'-... ', 'c':'-.-. ', 'd':'-.. ',
                   'e':'. ', 'f':'..-. ', 'g':'--. ', 'h':'.... ',
                   'i':'.. ', 'j':'.--- ', 'k':'-.- ', 'l':'.-.. ',
                   'm':'-- ', 'n':'-. ', 'o':'--- ', 'p':'.--. ',
                   'q':'--.- ', 'r':'.-. ', 's':'... ', 't':'-' ,
                   'u':'..- ', 'v':'...- ', 'w':'.-- ', 'x':'-..- ',
                   'y':'-.-- ', 'z':'--.. ',

                   '1':'.----', '2':'..---',
                   '3':'...--', '4':'....-',
                   '5':'.....', '6':'-....',
                   '7':'--...', '8':'---..',
                   '9':'----.', '0':'-----',

                   ' ':'   '
                 }



print('Welcome to the Morse Code Calculator!')
intake = input('What would you like to translate to Morse Code?:').lower()

table = str.maketrans(morse_alphabet)
result = intake.translate(table)
print(f'Here is Your Morse Code!:'f'{result}')
