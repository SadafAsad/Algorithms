def originalSize(in_string):
    n = len(in_string)
    return n*8

def fixSize(in_string):
    counter = 0
    char_string = list(in_string)
    while char_string!=[]:
        a = char_string[0]
        counter+=1
        j = 0 
        while j<len(char_string):
            if char_string[j]==a:
                char_string.pop(j)
                j=0
            else:
                j+=1
    i=0
    while 2*i<counter:
        i+=1
    table_bit = 8*counter + i*counter
    string_bit = len(in_string)*i
    return table_bit+string_bit

input_string = input("Enter string: ")
originalSize_n = originalSize(input_string)
fixSize_n = fixSize(input_string)
print("original size: " + str(originalSize_n) + "bit")
print("fix size format: " + str(fixSize_n) + "bit")
