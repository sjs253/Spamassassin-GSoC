# Spamassassin-GSoC
I am currently a GSoC student under ASF working on the project Spamassassin. Apache Singa will be used in this project for the development of neural nets for spam detection. </br> 

![alt text](https://github.com/sjs253/Spamassassin-GSoC/blob/master/spam.png)
### Repo description</br>
#### Dataset</br>
This directory contains separate folders for sample spam/ham mbox mails which the user can use to train the Svm and Neural network model.</br>
#### Jupyter_Notebooks</br>
It contains the jupter notebooks for Svm and Keras model. For better visualisation and parameter tweaking users are sdvised to run jupyter notebooks.</br>
#### Pickled_models</br>
Sample pickled models which can directly be used for classification.</br>
#### Spamassassin_files</br>
This is the heart of the project. It contains a number of files,
1. svm.cf - This is the configuration file needed for the plugin. Add this to /etc/mail/spamassassin directory.</br>

2. svm.pre - This file is added before .cf files. Used to lead the plugin. Place it in /etc/mail/spamassassin/directory</br>
3. svm.pm - This file has the Perl plugin code. Add in /usr/local/share/perl5 directory.</br>
4. svm_learn.py - The python script which taked the path of dataset as argument and dumps the pickled models which will be used by the plugin for classification.</br>
5. svm_python_call.py - This script is called by the .pm file. It takes the mail as an argument and returns the spamminess of the mail.</br>
### Project status</br>
#### Original Goals</br>
1. Development of an effective SA plugin with various statistical classifiers for spam classification.</br>

2. Integration of the plugins in SA.</br>
3. Proper documentation and relevant tests for the plugin.</br>

#### Achieved Goals</br>
1. A basic Plugin with two classifiers ( SVM and neural net ) is developed.</br>

2. Plugin was successfully integrated locally with SA.</br>
3. Documentation of the code is done.</br>

#### Future goals</br>
1. Extend the scope of classifiers to other sections of MIME format mail namely, attachments  and relevant headers.</br>

2. Adding dynamic functionality of making the plugin learn the correct classification of incorrectly classified mails.</br>
3. Extend the functionality which will make the plugin classify the incoming mail in shades of spamminess.</br>
4. Code an effective test file which covers the “perl calling python” aspect of the plugin. </br>
5. Decide on the best score range which the plugin should provide once the rule gets hit.</br>
6. Add a functionality which lets the user test the plugin on a given dataset for the model’s effectiveness.</br>
7. Make the neural net compatible with CPU only machines.</br>
8. Hopefully merge the code in the next major release of SA.</br>


