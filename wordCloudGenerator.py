#wordCloudGenerator.py

import wordcloud
from matplotlib import pyplot as plot
import tkinter
#from tkinter.filedialog import askopenfile

#Reads the selected file and then draws the wordcloud
def readFileAndDrawPlot():
    file = tkinter.filedialogue.askopenfile(mode = 'rb', filetypes = [("Text Files", "*.txt")])
    fileContents = ""
    for i in file:
        fileContents += str(i, 'utf-8')
    drawPlot(fileContents)

def drawPlot(fileContents):
    myimage = calculate_frequencies(fileContents)
    plot.imshow(myimage, interpolation = 'nearest')
    plot.axis('off')
    plot.show()
    
#Removes punctuation from words
def omit_punctuation(word, punctuation):
    newWord = ""
    for c in word:
        if c not in punctuation:
            newWord += c
    return newWord

#Calculates how many times each word appears in the text file
def calculate_frequencies(fileContents):
    #List of punctuations and uninteresting words to be excluded from the wordcloud
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just", \
    "for", "in", "not", "into", "so"]
    
    wordCount = {}
    for word in fileContents.split():
        lowercase = word.lower()
        lowercase = omit_punctuation(lowercase, punctuations)
        if not lowercase.isalpha() or lowercase in uninteresting_words:
            continue
        if lowercase in wordCount:
            wordCount[lowercase] += 1
        else:
            wordCount[lowercase] = 1
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(wordCount)
    return cloud.to_array()

def main():
    #GUI
    root = tkinter.Tk()
    root.title("Word Cloud Generator")
    root.geometry("300x100")
    textFrame = tkinter.Frame(root)
    textFrame.pack()
    label = tkinter.Label(textFrame, text = "Please open a text file", foreground="black",font=("Calibri", 20))
    label.pack(side = tkinter.TOP)
    button = tkinter.Button(textFrame, text = "Browse...", command = readFileAndDrawPlot)
    button.pack(side = tkinter.BOTTOM)
    root.mainloop()
    
if __name__ == "__main__":
    main()