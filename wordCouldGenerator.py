import wordcloud
from matplotlib import pyplot as plot

def replace_punctuation(word, punctuation):
    newWord = ""
    for c in word:
        if c not in punctuation:
            newWord += c
    return newWord

def calculate_frequencies(file_data):
    #List of punctuations and uninteresting words to be excluded from the wordcloud
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just", "for", "in", "not", "gutenbergtm"]
    
    wordCount = {}
    for word in file_data.split():
        lowercase = word.lower()
        lowercase = replace_punctuation(lowercase, punctuations)
        if lowercase.isalpha():
            if lowercase in uninteresting_words:
                continue
        if lowercase in wordCount:
            wordCount[lowercase] += 1
        else:
            wordCount[lowercase] = 1
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(wordCount)
    return cloud.to_array()

with open('The Project Gutenberg EBook of Mewanee.txt', encoding='utf8') as file:
    file_data = file.read()
    myimage = calculate_frequencies(file_data)
    plot.imshow(myimage, interpolation = 'nearest')
    plot.axis('off')
    plot.show()