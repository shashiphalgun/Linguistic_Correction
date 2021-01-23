# Linguistic_Correction
**TABLE OF CONTENTS**

| SL.NO | CONTENTS | 
| --- | --- |
| 1 | INTRODUCTION | 
| 2 | PROPOSED METHODOLOGY | 
| 3 | RESULT &amp; ANALYSIS | 
| 4 | CONCLUSION | 
| 5 | REFERENCES | 

**INTRODUCTION:**

Linguistic Correction has the most vital use in our modern-day technology, where we rely more on sentence framing and formation.

Technology is so intertwined with our lives that we need technology to pass in our life at each and every step and try to maintain that ability to know our grammar right or wrong. In order to have a proper basic ideology on the purpose of the proper sentence we have to have this type of technology where we can know what is right and what is wrong, what kind of a sentence is good and what kind of a sentence is bad in order to revaluate and reiterate the sentences which we write in our essays, letters to officials, or any other occasion.

Considering the fact that English and its importance in modern day has a path breaking impact in our lives we have to handle our mishaps and make sure to have a proper impact on the things we write, to whom we write and what we write.

**PROPOSED METHODOLOGY:**

**DATA ACQUISITION AND DATA CLEANING:**

- We used CoLa Dataset, it is an open source dataset.
  - [https://nyu-mll.github.io/CoLA/cola\_public\_1.1.zip](https://nyu-mll.github.io/CoLA/cola_public_1.1.zip)
- Sentence
- Label: Whether the sentence is right or wrong defined as 1 or 0 respectively.
- Label notes
- Sentence Source
- Tokens
- The public version provided here contains 9594 sentences belonging to training and development sets, and excludes 1063 sentences belonging to a held-out test set.

**DATA CLEANING:**
- From all these sentences we removed the Null values of label notes and sentence sources and create a clean data set with only sentences, tokens and labels

**METHODOLOGY:**

- We create a dataset which is clean and start to using BERT modelling technique.


Modified Dataset:

- We will fine-tune the model using the train set and the validation set, and make predictions for the test set.

- Train our classification model and Test on the test set.
  - Fine-tune the BERT model:
  - We used BertForSequenceClassification, since we are trying to classify query and document pairs into two distinct classes (right, wrong).


**MODELLING:**

- We create a dataset with sentences and tokens with labels and we import BERT tokenizer from transformers.

- Now we will split this dataset into three sets – train, validation, and test.

Original: Our friends won&#39;t buy this analysis, let alone the next one we propose.

Tokenized: [&#39;our&#39;, &#39;friends&#39;, &#39;won&#39;, &quot;&#39;&quot;, &#39;t&#39;, &#39;buy&#39;, &#39;this&#39;, &#39;analysis&#39;, &#39;,&#39;, &#39;let&#39;, &#39;alone&#39;, &#39;the&#39;, &#39;next&#39;, &#39;one&#39;, &#39;we&#39;, &#39;propose&#39;, &#39;.&#39;]

Token IDs: [2256, 2814, 2180, 1005, 1056, 4965, 2023, 4106, 1010, 2292, 2894, 1996, 2279, 2028, 2057, 16599, 1012]

- If we look closely each word including punctuations of the sentence is tokenized and given a distinctive token id.

- Maximum sentence length: 47

- Tokenize all of the sentences and map the tokens to their word IDs.

Original: Our friends won&#39;t buy this analysis, let alone the next one we propose.

Token IDs: tensor([ 101, 2256, 2814, 2180, 1005, 1056, 4965, 2023, 4106, 1010,

2292, 2894, 1996, 2279, 2028, 2057, 16599, 1012, 102, 0,

0, 0, 0, 0, 0, 0, 0, 0, 0, 0,

0, 0, 0, 0, 0, 0, 0, 0, 0, 0,

0, 0, 0, 0, 0, 0, 0, 0, 0, 0,

0, 0, 0, 0, 0, 0, 0, 0, 0, 0,

0, 0, 0, 0])

Training of Classification model:

- There are:
  - 7,695 training samples
  - 856 validation samples

Using bertforsentenceclassification of pre trained model

  - Number of training epochs. The BERT authors recommend between 2 and 4.
  - We chose to run for 4, but we&#39;ll see later that this may be over-fitting the training data.
  - At epochs 1/4 accuracy is 0.83, epochs 2/4, 3/4, 4/4 accuracy is 0.86.



Training and Validation loss:

- Training loss epochs 1: 0.50, epochs 2: 0.31, epochs 3: 0.19 and epochs 4: 0.13
- Number of test sentences: 516
- Positive samples: 354 of 516 (68.60%)

Matthews Correlation Coefficient: Total MCC: 0.540

**RESULT &amp; ANALYSIS:**

The model is tested on test set of 516 sentences.

The average training loss is 0.282.

The average validation loss is 0.442.

An interface is also created where the user can give input and get to the input sentence is gramatically correct or in-correct.

**DISCUSSION:**

- We have a problem of checking whether the sentences are right or wrong, this was and is encountered by many people in their daily lives and we have created an opportunity to check whether the sentence they are using is right or wrong.
- by knowing that they are wrong they are correct and reiterate their sentence and make it right. This solves many major issues while writing any official mails, letters or essays.
- This is a smart move in the way of achieving right or wrong classification using the technology we have.


**REFERENCES:**

[1] [https://nyu-mll.github.io/CoLA/](https://nyu-mll.github.io/CoLA/)

[2] [https://huggingface.co/transformers/model\_doc/bert.html](https://huggingface.co/transformers/model_doc/bert.html)

[3] [https://huggingface.co/transformers/](https://huggingface.co/transformers/)

[4] [https://huggingface.co/transformers/pretrained\_models.html](https://huggingface.co/transformers/pretrained_models.html)

[5] [https://github.com/huggingface/transformers](https://github.com/huggingface/transformers)

[6] [https://huggingface.co/bert-base-uncased](https://huggingface.co/bert-base-uncased)
