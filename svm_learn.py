import numpy as np
import io, string, warnings, os, glob, email, re, pickle, sys
from collections import Counter
from sklearn import feature_extraction, model_selection, naive_bayes, metrics, svm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import cross_val_score, GridSearchCV, train_test_split
# from nltk.tokenize import word_tokenize
# from keras.preprocessing.text import Tokenizer
# from keras.preprocessing.sequence import pad_sequences
# from keras.layers import Dense, Input, LSTM, Embedding, Dropout, Activation, CuDNNGRU, Conv1D
# from keras.layers import Bidirectional, GlobalMaxPool1D
# from keras.models import Model
# from keras import initializers, regularizers, constraints, optimizers, layers

def get_email_content(email_path):
    file = io.open(email_path, encoding='latin1')
    try:
        msg = email.message_from_file(file)
        for part in msg.walk():
            if part.get_content_type() == 'text/plain':
                return part.get_payload()
    except Exception as e:
        print(e)
                
def get_email_content_bulk(email_paths):
    email_contents = [get_email_content(o) for o in email_paths]
    return email_contents

def remove_hyperlink(word):
    return  re.sub(r"http\S+", "", word)

def to_lower(word):
    result = word.lower()
    return result

def remove_number(word):
    result = re.sub(r'\d+', '', word)
    return result

def remove_punctuation(word):
    result = word.translate(str.maketrans(dict.fromkeys(string.punctuation)))
    return result

def remove_whitespace(word):
    result = word.strip()
    return result

def replace_newline(word):
    return word.replace('\n','')

def clean_up_pipeline(sentence):
    cleaning_utils = [remove_hyperlink,
                      replace_newline,
                      to_lower,
                      remove_number,
                      remove_punctuation,remove_whitespace]
    for o in cleaning_utils:
        sentence = o(sentence)
    return sentence

def svm_model_learn(x_train,y_train):
    tfidf = TfidfVectorizer(stop_words = 'english')
    x_train_feature = tfidf.fit_transform()         # Pass x_train here somehow to extract the features
    
    list_C = np.arange(800,900,100)
    list_gamma = np.arange(0.001,0.006,0.001)
    parameters = [{'gamma': list_gamma, 'C': list_C}]

    svc = svm.SVC(kernel='rbf')
    svm_clf = GridSearchCV(svc, parameters, cv=2, scoring='f1', n_jobs=-1)
    svm_clf.fit(x_train_feature,y_train)

    pickle.dump(svm_clf, open('svm_pickle', 'wb'), protocol=2)
    pickle.dump(tfidf, open('tfidf_pickle', 'wb'), protocol=2)

def neural_model_learn():
    print ("We will do this!")


if __name__ == "__main__":

    ham = sys.argv[1]
    spam = sys.argv[2]

    ham_path = glob.glob(ham + '/*')
    spam_path = glob.glob(spam + '/*')

    ham_sample = np.array([train_test_split(o) for o in ham_path])
    ham_train = np.array([])
    ham_test = np.array([])
    for o in ham_sample:
        ham_train = np.concatenate((ham_train,o[0]),axis=0)
        ham_test = np.concatenate((ham_test,o[1]),axis=0)

    spam_sample = np.array([train_test_split(o) for o in spam_path])
    spam_train = np.array([])
    spam_test = np.array([])
    for o in spam_sample:
        spam_train = np.concatenate((spam_train,o[0]),axis=0)
        spam_test = np.concatenate((spam_test,o[1]),axis=0)

    ham_train_label = [0]*ham_train.shape[0]
    spam_train_label = [1]*spam_train.shape[0]
    x_train = np.concatenate((ham_train,spam_train))
    y_train = np.concatenate((ham_train_label,spam_train_label))

    ham_test_label = [0]*ham_test.shape[0]
    spam_test_label = [1]*spam_test.shape[0]
    x_test = np.concatenate((ham_test,spam_test))
    y_test = np.concatenate((ham_test_label,spam_test_label))

    train_shuffle_index = np.random.permutation(np.arange(0,x_train.shape[0]))
    test_shuffle_index = np.random.permutation(np.arange(0,x_test.shape[0]))
	
    x_train = x_train[train_shuffle_index]
    y_train = y_train[train_shuffle_index]

    x_test = x_test[test_shuffle_index]
    y_test = y_test[test_shuffle_index]

    x_train = get_email_content_bulk(x_train)
    x_test = get_email_content_bulk(x_test)

    x_train = [clean_up_pipeline(o) for o in x_train]
    x_test = [clean_up_pipeline(o) for o in x_test]

    svm_model_learn(x_train,y_train)

    # Figure out how will you call the neural network