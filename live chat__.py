import random
responses = [
    "hello",
    "what is your goal ",
    "what is your plan for today",
    'By the whoude like Tea Or Coffee',
    'by the way what does your father do ',
    "what r you doing right now",
    'if you have some helf from my side',
    'ok',
    "yes",
    "sure",
    'why not']

print("Hello, And welcome to my chat")
print("you can end this chat to type exit")
while 1:
    x=input('you:-')
    if x=="exit":
        print("end chat")
        break
    aa=random.choice(responses)
    print(aa)



