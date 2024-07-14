with open("Story.txt", "r") as f:
    Story = f.read()
    
words = set()
start_of_word = -1

target_start = "<"
target_stop = ">"

    

for i, char in enumerate(Story):
    if char == target_start:
        start_of_word = i
        
    if char == target_stop and start_of_word != -1:
        word = Story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1
        
answers = {}
for word in words:
    answer = input("Enter a word " + word + ": ")
    answers[word] = answer
    
for word in words:
    Story = Story.replace(word, answers[word])
    

print(Story)