import sys, pickle

def function():

        svm_clf = pickle.load(open("/home/shreyansh/GSoC/Spamassassin-GSoC/svm_pickle", "rb"))
        tfidf_pickle = pickle.load(open("/home/shreyansh/GSoC/Spamassassin-GSoC/tfidf_pickle", "rb"))

        text_file = open("test.txt", "r")
        s=''
        for line in text_file:
                s+=''+line.rstrip()
        text_file.close()

        mail_itr = [s,]
        X = tfidf_pickle.transform(mail_itr)

        mail_status = svm_clf.predict(X)

        text_file = open("test.txt", "w+")
        if mail_status==1:
                text_file.write("spam")
        else:
                text_file.write("ham")
        text_file.close()

if __name__ == "__main__":
        function()
