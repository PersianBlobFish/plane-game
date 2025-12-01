tweet = input("Enter your tweet: ")
def vowel(char):
    return char.lower() in 'aeiou'
def shorten_tweet(tweet):
    words = tweet.split()
    shortened_words = []
    for word in words:
        if len(word) > 1:
            new_word = ''.join([char for char in word if not vowel(char)])
            shortened_words.append(new_word)
        else:
            shortened_words.append(word)
    return ' '.join(shortened_words)
shortened_tweet = shorten_tweet(tweet)
print(shortened_tweet)