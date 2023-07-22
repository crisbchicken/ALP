'''
In these tasks you will be given one or more examples of code.

- Look at each example , study it carefully.
- Write a prediction of what it will do when it runs. Your prediction should be added to the code as comments. You should use the key terms list, item and index in your predictions.
- Run the code, compare what happens to your prediction.
- Add comments to note down and differences between your prediction and what actually happened.

'''

# Example Code 1

Sentence = ["Always", "look", "on", "the", "bright", "side", "of",]
print(Sentence)
#All of the words in the string would be printed
print(Sentence[1])
#the word with index 1 would be printed which would be look because it goes 0, 1, 2, 3, 4, 5, 6
Sentence.append("life")
#The word "life" would be attached to the existing list
Sentence[4] = "sunny"
# the variable is assigned to sunny
print(Sentence[4])
# sunny would be printed
print(Sentence[0] + " " + Sentence[3])
# The first word would be concetenated with the third word with a space
print(Sentence)
#the string would be printed again