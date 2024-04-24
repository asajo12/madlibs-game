with open("template.txt", "r") as file:
    template = file.read()
    
words = set()

start = -1

targetStart = "["
targetEnd ="]"

for i, char in enumerate(template):
    #"["
    if char == targetStart:
        start = i
    #"]"
    if char == targetEnd and start != -1:
        word = template[start:i +1]
        words.add(word) 
        
answers = {}

for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer
    
for word in words:
    template = template.replace(word, answers[word])
    
print(template)