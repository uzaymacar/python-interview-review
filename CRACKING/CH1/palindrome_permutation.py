# O(N)

MAX = 256
char_mapping = [0] * MAX

def is_palindrome_permutation(text):
    middle_element_count = 0 # could also be called odd count
    modified_text = text.lower() # do this so that ASCII values synch
    for character in modified_text:
        if character != " ":
            char_mapping[ord(character)] += 1
            if char_mapping[ord(character)] % 2 == 0:
                middle_element_count -= 1
            else:
                middle_element_count += 1
           
    return middle_element_count <= 1 #if middle element count is greater than 1, this can't be a palindrome permutation
    
    # UNNECESSARY / DUPLICATE WORK REPLICATED ABOVE WHILE ITERATING
    #print(char_mapping)
    #for i in range(MAX):
        #if char_mapping[i] > 0 and char_mapping[i] % 2 == 0:
            #char_mapping[i] = 0
        #elif char_mapping[i] > 0 and char_mapping[i] % 2 == 1:
            #char_mapping[i] = 1
    
    #middle_element_count = 0
    #for i in range(MAX):
        #if char_mapping[i] == 1 and middle_element_count < 1:
            #middle_element_count += 1
        #elif char_mapping[i] == 1 and middle_element_count >= 1:
            #return False 

# if even number of characters, then every character has to appear twice
# if odd number of characters, then every character has to appear twice but one character appears once
test = "Tact Coa"
print(is_palindrome_permutation(test))
    