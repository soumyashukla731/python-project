from textblob import TextBlob

txt = TextBlob("I love programming, it makes me happy!")
print(txt.sentiment)
