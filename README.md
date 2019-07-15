# Spamassassin-GSoC
I am currently a GSoC student under ASF working on the project Spamassassin. Apache Singa will be used in this project for the development of neural nets for spam detection. </br> 
This readme will be constantly updated over the course of programme.</br>
### Current status</br>
#### SVM.ipynb</br>
1. Removal of punctuation did'nt help in increasing the F1 score.Although a python script is ready and can be used if needed.</br>
2. As stop words are language specific, thry are not removed either.</br>
3. Stemming is used for Data cleaning</br>
4. TFIDF is used for feature extraction. Message length was also considered as a feature but proved to be disastrous.</br>
5. K-fold Cross validation along with Random search is used for parameter tuning.</br>
6. F1 score and confusion matrix is used as performance metric.</br></br>
F1 score of 98% is achieved as of now. See the confusion matrix for further details.</br>
#### Open Svm.pm to see the Perl code of the plugin.This is under development right now.</br>
1. A constructor (Calls register_eval_rule() of Plugin.pm which calls register_eval_rule() of Conf.pm to register the rule)</br>
2. A check_svm() sub which calls scan() and finally returns the status of the mail.</br>
3. A svm_learn() sub which trains the model using user's mbox file as the dataset.</br>

#### Keras neural net.ipynb</br> 
1. A Keras neural network for spam detection is developed.</br>
2. GLOVE pre-train is used for word embeddings.</br>
3. Bidirectional GRU is added.</br></br>
F1 score of 95.2% is achieved. Refer the confusion matrix for further details.</br>

#### SINGA neural net.ipynb
1. A neural network using Apache's machine learning library SINGA is developed.
