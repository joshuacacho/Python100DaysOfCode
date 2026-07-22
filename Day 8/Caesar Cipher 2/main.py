alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.


# Test data of qnuux fxaum! should return Hello World!

def decrypt(original_text, shift_amount):

    decoded_string = ""

    for letter in original_text:
        if letter in alphabet:
            alphabet_position = alphabet.index(letter) - int(shift_amount)  # the shift will be int of X to the right

            # Apply shift, wrap around using % 26, then convert back to letter
            # example 20 / 26 means 26 goes into 20 a total of 0 times and the remainder is 20
            # so new index of 20 is still in the range of 0-25 for the alphabet (26 length/letters) so NO out of bounds exception
            new_index = alphabet_position % len(alphabet)
            decoded_string = decoded_string + alphabet[new_index]
            # print(new_index, alphabet[new_index])
        else:
            decoded_string = decoded_string + letter

    # print encoded string
    print(f"Here is the decoded result: {decoded_string}")


# decrypt(original_text=text, shift_amount=shift)


#------------------------------ENCRYPT------------------------------#


# Now putting it all together
def encrypt(original_text, shift_amount):

    encoded_string = ""

    for letter in original_text:
        if letter in alphabet:
            alphabet_position = alphabet.index(letter) + int(shift_amount) # the shift will be int of X to the left

            # Apply shift, wrap around using % 26, then convert back to letter
            # example 20 / 26 means 26 goes into 20 a total of 0 times and the remainder is 20
            # so new index of 20 is still in the range of 0-25 for the alphabet (26 length/letters) so NO out of bounds exception
            new_index = alphabet_position % len(alphabet)
            encoded_string = encoded_string + alphabet[new_index]
            # print(new_index, alphabet[new_index])
        else:
            encoded_string = encoded_string + letter

    #print encoded string
    print(f"Here is the encoded result: {encoded_string}")


# encrypt(original_text = text, shift_amount = shift)


# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

# Reusing the above
def caesar():

    directions = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    while directions != "encode" and directions != "decode":
        directions = input("Invalid selection, type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if directions == "encode":
        encrypt(original_text=text, shift_amount=shift)
    else:
        decrypt(original_text=text, shift_amount=shift)


# Combining all re-useable  above
def caesar_combined():

    directions = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    while directions != "encode" and directions != "decode":
         directions = input("Invalid input, type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    original_text = input("Type your message:\n").lower()
    shift_amount = int(input("Type the shift number:\n"))

    encode_decode_string = ""

    for letter in original_text:

        if letter in alphabet:
            if directions == "encode":
               alphabet_position = alphabet.index(letter) + int(shift_amount)  # the shift will be int of X to the left
            else: # decode
               alphabet_position = alphabet.index(letter) - int(shift_amount)
               # Apply shift, wrap around using % 26, then convert back to letter
               # example 20 / 26 means 26 goes into 20 a total of 0 times and the remainder is 20
               # so new index of 20 is still in the range of 0-25 for the alphabet (26 length/letters) so NO out of bounds exception
            new_index = alphabet_position % len(alphabet)
            encode_decode_string = encode_decode_string + alphabet[new_index]
            # print(new_index, alphabet[new_index])
        else:
            encode_decode_string = encode_decode_string + letter

    # print encoded string
        # encode and decode both end with a d so we can lump both results into one output string passing the directions
        # and leaving the d since both are in the past
    print(f"Here is the {directions}d result: {encode_decode_string}")


caesar_combined()

