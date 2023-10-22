# AAI_520_Final

## Overview

This is the final project for AAI 520 - Natural Language Processing

Group Members:

* Zack Robertson
* Ryan Laxamana
* Shane Schipper

## Technical Details

We fine-tuned an instance of the BERT for Questions and Answers model from the Hugging Face transformers library on the SQUAD (Standord Question and Answer Dataset). Development took place largely on Google Colab, making use of its compute resources for training and inference. 


## Instructions for Running the Chatbot

As mentioned, this  bot was ddeveloped on google colab and as such will work best in that enviornment. The following are our recomended steps for running and interacting with this model. 

* Clone this repository
* Upload the "Chatbot_interact.ipynb" notebook to google colab
* Access this [google drive folder](https://drive.google.com/drive/folders/14a1oDJ8FPiU_NHx0gLkiijBlV1WeX2om?usp=sharing) which contains the data and saved model checkpoint. Then add a shortcut for it to your main drive directory. *Note: this shortcut is not mandatory but will make it so directories do not need to be changed in the script. 
* Open the notebook and connect to a runtime. For best performance, use a high-RAM runtime with a GPU. 
* Follow the instructions for chatting on the notebook!