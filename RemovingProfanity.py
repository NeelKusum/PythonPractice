from better_profanity import profanity

if __name__=='__main__':
    profanity.load_censor_words()
    x=input("enter the sentence : ")
    output=profanity.censor(x)
    print(output)
