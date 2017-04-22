
# MovieLens Dataset Analysis
> ## Analysis01 General Features

###  I. What are the release dates like for the movies?**

#### Original dataframe:
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")



> **II. What are the 5 MOST RATED movies?**

##### Collected data:

> **Analysis 3. Who communicated via emails the most**


---

### Analysis02

> **Collected data**


- 1000 articles about DONALD TRUMP since 20170101, stored in json file output1_donald_trump 
- 1000 articles about HILLARY CLINTON since 20170101, stored in json file output2_hillary_clinton 
- 1000 articles about BARACK OBAMA since 20170101, stored in json file output3_barack_obama
- All articles published in Jan, stored in json file output_archive_201701

--

> **Analysis 1. Were the articles neutral towards Trump?**

- **Sentiment analysis on the subjects of the articles**

##### Collected data:
The subjects extracted from the keywords of the articles about Donald Trump.(Using AFINN-en-165 as a sentiment dictionary in order to give the NLTK tokenized words sentiment scores)

##### Conclusion:
No negative words were found. One positive word 'asset' were found. According to that, the articles about trump were neutral in subjects.

--

> **Analysis 2. What did the articles talk about**

- **Create wordcloud on Trump, Hillary, Obama respectively**

##### Collected data:
The headlines of the articles about Trump/Hillary/Obama.

##### Conclusion:
Plotted a picture using wordcloud to visualize the important words. (See Q2_NYT.ipynb)

Words about Trump : donald trump new ban president immigration inauguration

Words about Hillary : trump russia new election say white house

Words about Obama : trump obama say new white house russia rule fact 

--

> **Analysis 3. Who were mentioned the most in Jan**

- **Count the keywords if they are described as 'persons'**

##### Collected data:
The names appearing in the keywords from articles of Jan.

##### Conclusion:
Top 3:

"Trump Donald J" were mentions 985 times.

"Obama, Barack" were mentions 148 times.

"Putin, Vladimir V" were mentions 41 times.
