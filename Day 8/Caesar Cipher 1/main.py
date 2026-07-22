
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt_two_inputs(original_text, shift_amount):
    print("Done")

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# HINT
# You can use the built-in Python index() function to find out the position of an item in a list. e.g.

# fruits = ["Apple", "Pear", "Orange"]
# fruits.index("Pear") #1

# e.g. If we have the following values:
# plain_text = "hello"
# shift_amount = 1
# The final encrypted output should be the below # Where each of the letters of 'hello' is shifted up by 1.:
    # Here is the encoded result: ifmmp


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


# TODO 3 - call the encrypt() function and pass in the user input, you should be able to test the code to encrypt a message
encrypt(original_text = text, shift_amount = shift)

# TODO-3a: What happens if you try to shift z forwards by 9? Can you fix the code?
    # this line makes it work new_index = alphabet_position % 26
    # so lets say we use the word zebra
        # z is 25th in the list and the shift is 9
        # alphabet_position = 25 + 9 = 34
            # before 34 > 25 so we would get out of range BUT with new_index = alphabet_position % 26
                # 34 % 26 meanings 26 goes into 34 once with a REMAINDER of 8 where the index(8) is i
                #     Type your message:
                #     zebra
                #     Type the shift number:
                #     9
                #     Here is the encoded result: inkaj

