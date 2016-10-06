import random
fortune = ['yes', 'no', 'perhaps', 'maybe', 'uncertain', 'the square root of pi', 'answer the question yourself', 'find the answer within your heart', 'never', 'that is funny', 'I do not know', ' I do not care', 'unfortunately', 'who knows?', 'when pigs fly']
print 'Ask me a question'
option = random.choice(fortune)
answer = option
text = raw_input("\nAsk me a question ")
print answer
