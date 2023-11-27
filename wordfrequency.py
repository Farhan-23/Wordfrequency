#word frequency in a text by 2307

from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

def top(list_):
        return max(set(list_),key=list_.count)

def main():

    filename=input("\nenter the text file path: ")
    f=open(filename)
    string=""
    for i in f.read():
        if(i.isalpha()):
            string=string+i
        else:
            string=string+" "
    f.close()
    words_=string.split()
    words=[]
    for i in words_:
        i=i.lower()
        words.append(i)

    while(1):

        print("\nOPERATIONS:\n1.frequency of words\n2.top k frequent words\n3.wordcloud\n4.exit")
        b=int(input(": "))

        if(b==1):
            s=set(words)
            n=1
            print("\nFreuencies:")
            for i in s:
                print(f"{n}.{i}-{words.count(i)}")
                n=n+1
            print()

        elif(b==2):
            word_s=[]
            for i in words:
                word_s.append(i)
            k=int(input("\nenter how many frequrent words to display: "))
            newlist=[]
            for i in range(k):
                word=top(word_s)
                newlist.append(word)
                for i in range(words.count(word)):
                    word_s.remove(word)
            print(f"\nthe top {k} words are: \n")
            n=1
            for i in newlist:
                print(f"{n}.{i}-{words.count(i)}\n")
                n=n+1
            print()

        elif(b==3):
            c=int(input("\nwordcloud for how many frequent words: "))
            word_s=[]
            my_list=[]
            text=""
            for i in words:
                word_s.append(i)
            for i in range(c):
                word=top(word_s)
                for i in range(words.count(word)):
                    my_list.append(word)
                    word_s.remove(word)
            word_could_dict=Counter(my_list)
            wordcloud = WordCloud().generate_from_frequencies(word_could_dict)
            plt.imshow(wordcloud)
            plt.axis("off")
            plt.show()

        elif(b==4):
            print("\nbyee...\n")
            break

        else:
            print("invalid input ..try again")

if __name__=='__main__':
    main()