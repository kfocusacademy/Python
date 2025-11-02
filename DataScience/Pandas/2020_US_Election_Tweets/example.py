from textblob import TextBlob
text = TextBlob('the sun rises in east').sentiment.subjectivity
print(text)
text = TextBlob('blue berries are delicious').sentiment.subjectivity
print(text)

text = TextBlob('Trump is not a good guy').sentiment.polarity
print(text)
text = TextBlob('Modi is the best PM').sentiment.polarity
print(text)
