"""   2.1    Write a function that takes in an input and checks to see if it’s an
             isogram. The function should return True or False.
"""
def is_isogram(input_string):
    # Convert the input string to lowercase to handle both uppercase and lowercase characters.
    input_string = input_string.lower()

    # Create an empty set to keep track of the letters in the input strinh variable
    seen_characters = set()

    # Iterate through each character in the string.
    for char in input_string:
        if char in seen_characters:
            return False
        seen_characters.add(char)
    # If it doesn't get any of the same letters,it returns true.
    return True


#Check if these words are idograms or not.
print(is_isogram("isogram"))
print(is_isogram("uncopyrightable"))
print(is_isogram("ambidextrously"))
print(is_isogram("Extraordinary"))

