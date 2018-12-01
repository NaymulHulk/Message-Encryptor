import check
## Constants to refer the index from( 0 to 25)

up_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
low_alpha = "abcdefghijklmnopqrstuvwxyz"

def index_counter(text, step):
    '''
    index_counter is a helper function, which counts the index for the encrypted 
    letter. 
    
    requires: text to be Str, step = Nat
    
    index_counter: Str Nat -> Nat    
    '''    
    if (text[0]).isupper():
        if (up_alpha.index(text[0]) + (step % 26)) >= 26:
            return ((step % 26) - (26 - up_alpha.index(text[0])))
        else: 
            return (up_alpha.index(text[0]) + (step % 26))
        
    elif (text[0]).islower():
        if (low_alpha.index(text[0]) + (step % 26)) >= 26:
            return ((step % 26) - (26 - low_alpha.index(text[0])))
        else: 
            return (low_alpha.index(text[0]) + (step % 26))     
        
        
def caesar_encrypt(text, step):
    '''
    caesar_encrypt is a function which consumes a text as a string,
    and step as a natural number. Each of the letters inside the string 
    steps ahead by that number of "steps"
    and step% 26 ensures if the step is more than 26, then the remainder is used
    
    requires: text to be Str, step = Nat
    
    caesar_encrypt: Str Nat -> Str
    
    examples:
    caesar_encrypt("Nice", 7) => "Upjl" 
    caesar_encrypt("xYz", 3) => "aBc" 
    caesar_encrypt("", 10) => "" 
    caesar_encrypt("Wow", 113) => "Fxf" 
    caesar_encrypt("Wow", 0) => "Wow"
    '''
    if len(text) == 0:
        return ""
    elif text[0].isupper():
        return up_alpha[(index_counter(text, (step % 26) ))] +\
               (caesar_encrypt(text[1:], (step % 26)))      
    elif text[0].islower():
        return low_alpha[(index_counter(text, (step % 26)))] +\
               (caesar_encrypt(text[1:], (step % 26))) 
    
## Tests:
check.expect("Test1", caesar_encrypt("ABC", 1), "BCD")
check.expect("Test2", caesar_encrypt("xYz", 3), "aBc")
check.expect("Test3", caesar_encrypt("", 10), "")
check.expect("Test4", caesar_encrypt("Wow", 113), "Fxf")
check.expect("Test5", caesar_encrypt("Wow", 0), "Wow")     
    
    

def zinzi_helper(lst_of_sentence, pos):
    '''
    this function encrypts the lst_of_sentence, which is basically the sentence 
    is being fed as a list with (sentence).split(" "), and started with the pos(ition)
    as 0.
    it converts using the caesar encrypt, but I made this encryption to my own,
    where the steps for each word is independent, and based on the length of the 
    word
    '''
    if pos == len(lst_of_sentence) :
        return []
    else:
        return [(caesar_encrypt((lst_of_sentence[pos]), (len(lst_of_sentence[pos]))))]\
            + zinzi_helper(lst_of_sentence, (pos+1))






def zinzi_encryptor():
    '''
    is the main function which wraps all the other helper functions to 
    take in input and also ecrypt the sentence
    '''
    sentence_input = input("Write the sentence you want to encrypt: ") 
    output= zinzi_helper(((sentence_input).split(" ")), 0)
    output = " ".join(output)
    print(output)
    
    
    
    
    
    
        
    

                              
