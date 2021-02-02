#!/usr/bin/env python
# -*- coding: utf-8 -*-

def is_even_len(string: str) -> bool:  # nb caractères est pair ? cad si len Divisible par 2 sans reste (modulo) => pair
    if len(string) % 2 == 0:
        return True
    return False


def remove_third_char(string: str) -> str:  # str[0:2]+[3:]
    return string[0:2] + string[3:]


def replace_char(string: str, old_char: str, new_char: str) -> str:
    position_of_old_char = string.index(old_char)  # donne position/l'index qui est un int, alternative for loop and if statement pcq comme c'est pas capable d'identifier pls old_char
    string = string[:position_of_old_char] + new_char + string[position_of_old_char + 1:]
    return string

def get_number_of_char(string: str, char: str) -> int:
    number_of_char = 0
    for i in string:
        if i == char:
            number_of_char += 1
    return number_of_char

    # Solution that didn't work
    # positions_of_char = (string.index(char))
    # number_of_char = len(f'{positions_of_char}')
    # return number_of_char


def get_number_of_words(sentence: str, word: str) -> int:
    number_of_word = 0
    sentence = sentence.split()
    for i in sentence:  # pourquoi ecq for word in sentence: ne fonctionne pas
        if i == word:
            number_of_word += 1
    return number_of_word


def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caractère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caractère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans 'hello world' est : {get_number_of_char(chaine, 'l')}")  # hello ou hello zworld

    chaine = "Baby shark doo doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()

# complet 2
