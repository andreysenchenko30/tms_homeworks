zen_of_python_text = '''The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''
my_email = 'a.senchenko30@gmail.com'
joined_text = zen_of_python_text + my_email
number_of_vowels = 0
number_of_letters = 0
for symbol in joined_text:
    if symbol.isalpha():
        number_of_letters += 1
        if symbol == 'a' or symbol == 'o' or symbol == 'i' or symbol == 'u' or symbol == 'e':
            number_of_vowels += 1
print(f'Количество букв в тексте: {number_of_letters}')
print(f'Количество гласных букв в тексте: {number_of_vowels}')
string_length = len(joined_text)
index = 18
while index < string_length:
    if joined_text[index].islower():
        print(f'{index}{joined_text[index].upper()}')
    else:
        print(f'{index}{joined_text[index].lower()}')
    index += 18
