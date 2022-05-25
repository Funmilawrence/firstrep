# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


#def find_anagram(word, anagram):
    # [assignment] Add your code here

    #return True

word1= input("first word:")
word2= input("second word:")
sortresult1 = sorted(word1)
sortresult2 = sorted(word2)

if sortresult1 == sortresult2:
    print("True")
else:
    print("False")
