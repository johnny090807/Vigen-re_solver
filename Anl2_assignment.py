import english_quadgrams as eq
import random as r
import string

qs = eq.quadgram_score


def group_info():
    return [("0997774", "John Klees", "INF2a1"), ("0959331", "Reynethan Leon", "INF2a1")]


letter_arr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
              "v", "w", "x", "y", "z"]


def number_letter(letter):
    return letter_arr.index(letter.lower())


def encrypt_vigenere(plaintext, key):
    # Array for the encryption
    encrypted_arr = []
    # String to return the encrypted as a string
    encrypted_string = ""
    # Make index for only the key
    key_index = 0
    #
    # Start for loop for the plaintext
    #
    for i in plaintext:
        # Check if the char doesnt consist of a space or !
        if i != ' ' and i != "!":
            # Make the new number by adding the number of the plaintext and number of the key
            newNr = number_letter(i) + number_letter(key[key_index])
            # If both the numbers are bigger than the alphabet_arr do it minus the whole array
            if newNr > 25:
                newNr -= len(letter_arr)
            # If the plaintext char was a uppercase, add the letter with an uppercase
            if i.isupper():
                encrypted_arr.append(letter_arr[newNr].upper())
            # Enter a lowercase if it's not an uppercase letter
            else:
                encrypted_arr.append(letter_arr[newNr])
            # If the key index reached the total length of the key, set it to 0
            if key_index + 1 != len(key):
                key_index += 1
            else:
                key_index = 0
        # If the char is a space or ! then it will just add it to the array
        else:
            encrypted_arr.append(i)
    # Join all elements of the array to the string
    return encrypted_string.join([str(elem) for elem in encrypted_arr])


def decrypt_vigenere(ciphertext, key):
    # Array for the decryption
    decrypted_arr = []
    # String to return the encrypted as a string
    decrypted_string = ""
    # Make index for only the key
    key_index = 0
    #
    # Start for loop for the plaintext
    #
    for i in ciphertext:
        # Check if the char doesnt consist of a space or !
        if i != ' ' and i != "!" and i != ".":
            # Make the new number by adding the number of the plaintext and number of the key
            newNr = number_letter(i) - number_letter(key[key_index])
            # If both the numbers are lower than the 0 do it plus the length of the letters array
            if newNr < 0:
                newNr = newNr + len(letter_arr)
            # If the plaintext char was a uppercase, add the letter with an uppercase
            if i.isupper():
                decrypted_arr.append(letter_arr[newNr].upper())
            # Enter a lowercase if it's not an uppercase letter
            else:
                decrypted_arr.append(letter_arr[newNr])
            # If the key index reached the total length of the key, set it to 0
            if key_index + 1 != len(key):
                key_index += 1
            else:
                key_index = 0
        # If the char is a space or ! then it will just add it to the array
        else:
            decrypted_arr.append(i)
    # Join all elements of the array to the string
    return decrypted_string.join([str(elem) for elem in decrypted_arr])


def quadgram_fitness(text):
    letters = string.ascii_lowercase
    randomstring = ''.join(r.choice(letters) for _ in range(7))
    bestscore = 0
    for i in range(100):
        randomstring_arr = list(randomstring)
        randomint = r.randint(0,6)
        randomstring_arr[randomint] = r.choice(letters)
        newstring = ""
        randomstring = newstring.join([str(elem) for elem in randomstring_arr])
        decryptedstring = decrypt_vigenere(text, randomstring)
        score = 0
        for i in qs:
            if decryptedstring.replace(" ", "").lower().__contains__(i):
                score += qs.get(i)

        if score > bestscore:
            bestscore = score
        else:
            pass
        print(score)
    return bestscore

#
# Calculate the fitness.
#
def calculate_fitness(text):
    string_sentence = list(text.lower().replace(" ", "").replace("!", ""))
    fitness = 0
    for i in range(0, len(string_sentence) - 3):
        small_word = ""
        for j in range(4):
            small_word += string_sentence[i + j]
        old_fitness = fitness
        for x in qs:
            if x == small_word:
                fitness += qs.get(x)
        if fitness == old_fitness:
            fitness += 23
    return fitness

def solve_vigenere(text, length):
    for a in range(length):
        A_fitness = 0
        A_word = ""
        for b in range(length):
            B_fitness = 0
            B_word = ""
            for c in range(length):
                C_fitness = 0
                C_word = ""

# A:abc 50
# B:abc 50
# c:abc 50

print(encrypt_vigenere("Bokito and Einstein have the same birthday!", "ape"))
print(decrypt_vigenere("M abxock hnsp ge oycs rts akqc at n zpyzh.", "monkey"))
# print(quadgram_fitness("Wkh glh kdv ehhq fdvw!"))

print(calculate_fitness("Wkh glh kdv ehhq fdvw!", 7))
