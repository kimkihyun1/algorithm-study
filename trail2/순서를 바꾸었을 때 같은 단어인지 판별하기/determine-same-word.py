word1 = input()
word2 = input()

# Please write your code here.
word1 = sorted(word1)
word2 = sorted(word2)

def correct_word():
    if len(word1) != len(word2):
        return 'No'
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            return 'No'
    
    return 'Yes'

print(correct_word())