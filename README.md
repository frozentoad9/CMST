<!--- # Project Title --->
# Prabhupadavani: A Code-mixed Speech Translation Data for 25 languages
Code for the paper titled ["Prabhupadavani: A Code-mixed Speech Translation Data for 25 languages"](https://www.aclweb.org/anthology/W19-7503/) <br>

## File organization
* Preprocessing  : contains all files used to preprocess the data (Python 3.6)
* Data  : contains data required to run this code
* Statistics  : contains all files that contains statistics of the dataset

# Dataset
file name | discription
----|----
[train/test/dev.csv](https://drive.google.com/drive/folders/1mnCjP4woF0CrQfhXajj90xp13TW-moR1?usp=sharing)  | This is the dataset for code-mixed Speech Translation.  |
[chopped_audios](https://drive.google.com/drive/folders/1F_TM0EwlZG36ZbbqgzWdWagxsYR70cuN?usp=sharing)  | This contains all the audios, transcription and translation.

### Statistics of Corpora contained

| Languages                   | #types | #tokens | Types per line | Tokens per line | Avg. token length |
| --------------------------- | ------ | ------- | -------------- | --------------- | ----------------- |
| English\[100%\]             | 40,324 | 601889  | 10.58          | 11.27           | 4.92              |
| French (France)             | 50510  | 645651  | 11.38          | 12.09           | 5.08              |
| German\[100%\]              | 50748  | 584575  | 10.44          | 10.95           | 5.57              |
| Gujarati\[100%\]            | 41959  | 584989  | 10.37          | 10.95           | 4.46              |
| Hindi\[100%\]               | 29744  | 716800  | 12.36          | 13.42           | 3.74              |
| Hungarian\[100%\]           | 84872  | 506608  | 9.13           | 9.49            | 5.89              |
| Indonesian\[100%\]          | 39365  | 653374  | 11.54          | 12.23           | 6.14              |
| Italian\[100%\]             | 52372  | 512061  | 9.23           | 9.59            | 5.37              |
| Latvian\[100%\]             | 70040  | 477106  | 8.69           | 8.93            | 5.72              |
| Lithuanian\[100%\]          | 75222  | 491558  | 8.92           | 9.2             | 6.04              |
| Nepali\[100%\]              | 52630  | 570268  | 10.03          | 10.68           | 4.88              |
| Persian (Farsi)\[100%\]     | 51722  | 598096  | 10.61          | 11.2            | 4.1               |
| Polish\[100%\]              | 71662  | 494263  | 8.99           | 9.25            | 5.86              |
| Portuguese (Brazil)\[100%\] | 50087  | 608432  | 10.8           | 11.39           | 5.12              |
| Russian\[100%\]             | 72162  | 490908  | 8.96           | 9.19            | 5.79              |
| Slovak\[100%\]              | 73789  | 520465  | 9.39           | 9.75            | 5.37              |
| Slovenian\[100%\]           | 68619  | 516649  | 9.35           | 9.67            | 5.3               |
| Spanish\[100%\]             | 49806  | 608868  | 10.75          | 11.4            | 5.07              |
| Swedish\[100%\]             | 48233  | 581751  | 10.31          | 10.89           | 5                 |
| Tamil\[100%\]               | 84183  | 460678  | 8.37           | 8.63            | 7.65              |
| Telugu\[100%\]              | 72006  | 464665  | 8.34           | 8.7             | 6.56              |
| Turkish\[100%\]             | 78957  | 453521  | 8.27           | 8.49            | 6.35              |
| Bulgarian\[100%\]           | 60712  | 564150  | 10.1           | 10.56           | 5.24              |
| Croatian\[100%\]            | 73075  | 531326  | 9.58           | 9.95            | 5.28              |
| Danish\[100%\]              | 50170  | 587253  | 10.4           | 11              | 4.98              |
| Dutch\[100%\]               | 42716  | 595464  | 10.52          | 11.15           | 5.05              |


### Code-mixing

#### All languages in Code-mixing

| Language | Total Words | Unique Words | Percentage |
| -------- | ----------- | ------------ | ---------- |
| English  | 500136      | 6312         | 83.6       |
| Bengali  | 46933       | 3907         | 7.84       |
| Sanskrit | 51246       | 7202         | 8.56       |
| Total    | 598315      | 17421        | 100        |


#### Types of Code-mixing

|                  | English-Sanskrit | Sanskrit-English | English-Bengali | Bengali-English |
| ---------------- | ---------------- | ---------------- | --------------- | --------------- |
| Inter-Sentential | 2356             | 2366             | 339             | 339             |
| Intra-Sentential | 2338             | 851              | 124             | 0               |

<!---
<img src="images/vedabaseDF.png"> 

## Categorization of embeddings:

* Word level                            : Word2Vec, glove
* Subword level                         : FastText, Charagram, BPE, LexVec
* Character level                       : charcnn 
* contextual embeddings (Language model): ELMo, BERT, ULMFiT, openAI, FlairEmbeddings

## Evaluation

Parameter details are given in Fasttext ipython notebook in code directory.

To decide max_n parameter, histogram plot of no of characters in word plotted.
So value chosen for experimentation is max_n=10. 

<p align="center">
<img width="400" height="400" src="images/ave_word_plot.png">
</p>

To decide window parameter, histogram plot of, no of words per line plotted.
So window_size chosen is 11. 

<p align="center">
<img width="400" height="400" src="images/word_per_line.png">
  </p>
  
Variation of accuracy as the epoch is changing.

Other parameters were fixed as follows:

Emedding size =100, hidden_layer_sizes=(100),alpha=0.05,learning_rate='adaptive',max_iter=1000,max_n = 10

<p align="center">
<img width="400" height="400" src="images/epoch.png">
    </p>
 
Variation of accuracy as the embedding size is changing.

Other parameters were fixed as follows:

hidden_layer_sizes=(100),alpha=0.05,learning_rate='adaptive',max_iter=1000,max_n = 10 epochs = 5

<p align="center">
<img width="400" height="400" src="images/embedding.png">
</p>
--->
