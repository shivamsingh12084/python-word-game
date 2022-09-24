import string
from unittest import result
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
alphabet = "abcdefghijklmnopqrstuvwxyz"
input_list = list(alphabet)
result = []
string_result = ""
for i in range(len(lettersGuessed)):
    if lettersGuessed[i] in input_list:
        input_list.remove(lettersGuessed[i])


print(string_result.join(input_list))
print(input_list)