import contractions
import string
import re

def clean_text(text):
    # remove '
    text = contractions.fix(text)
    print(text)
    text = text.lower()
    print(text)
    #remove comma or !
    text = re.sub('[%s]' % re.escape(string.punctuation), '',text)
    print(text)
    #remove number
    text = re.sub(r'\w*\d\w*','',text)
    print(text)

    # stopwords = []
    # for word in open('stopwords_en.txt','r'):
    #     #strip() remove \n \n 
    #     stopwords.append(word.strip())

    stopwords = [word.strip() for word in open('stopwords_en.txt','r')]

    #print(text.split())
    # text_list = [word for word in text.split() if word not in stopwords]
    # text= ' '.join(text_list)
    text= ' '.join([word for word in text.split() if word not in stopwords])
    print(text)

    return text

def main():
    text = "I read this book for the time first time in 1987, and it's still one of my favourites!"
    #print(contractions.fix("that's "))
    print(clean_text(text))

if __name__ == '__main__':
    main()