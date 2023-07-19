def reverse_string(string):
    # Initialize an empty string to store the reversed characters
    reversed_string = ""

    # Iterate through the string in reverse order and append each character to the new string
    for char in string[::-1]:
        reversed_string += char

    return reversed_string
