from textblob import TextBlob

text = open('abc.txt')
text = text.read()
text = text = text[0:20]
blob = TextBlob(text)

print(blob.translate(to='hi'))