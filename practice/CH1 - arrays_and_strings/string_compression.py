# O(N)

def compress_string(string):
    output_string = ""
    prev = ""
    counter = 0
    for i in range(len(string)):
        if string[i] == prev:
            counter += 1
        elif (prev != "" and string[i] != prev):
            output_string += prev
            output_string += str(counter)
            prev = string[i]
            counter = 1
        elif prev == "":
            prev = string[i]
            counter = 1
        
    output_string += prev # this appends for the last repeated characters
    output_string += str(counter) 
    
    if len(output_string) >= len(string):
        return string
    
    return output_string
            
print(compress_string("xxxxyytttt"))
        