# O(N^2) -> urlify
# O(N) -> urlify_raw, urlify_raw_single -> + 0(N) space complexity in both

def urlify(text):
    # text.replace(" ", "%20")
    return text.replace(" ", "%20") # don't forget to return this

def urlify_raw(text):
    output_text = "" # can't use append, have to use +=
    for i in range(len(text)):
        if text[i] == ' ':
            output_text += "%20"
        else:
            output_text += text[i]
    return output_text

def urlify_raw_single(text, true_length): # read carefully include all parameters
    new_index = len(text) - 1 # actual length of text
    text_n = [" "]*len(text) # have to use this, because https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference
    for i in reversed(range(true_length)): # put reversed(range(6)) to count reversely (5, 4, 3, 2, 1)
        if text[i] == " ":
            text_n[new_index - 2 : new_index + 1] = "%20" # be careful about the index slicing values
            new_index -= 3
        else:
            text_n[new_index] = text[i]
            new_index -= 1
            
    return text_n
            
        
test_string = "Mr John Smith    " # 4 spaces are sufficient
print(urlify_raw_single(test_string, 13))