# Midterm Exam - Spring 2017 
---
### Question 1

**`Dataset : The enron data-set`**
`Collected all the files under the directory enron/maildir and created a list with all the parsed emails`

--

> **Analysis 1. What did the emails talk about**

- **What did the emails say according to their subjects?**

##### Collected data:
The subjects of the emails.
##### Conclusion:
Plotted a picture using wordcloud to visualize the important words. (See Q1_Enron.ipynb)

- **What did the emails say according to their contents?**

##### Collected data:
The contents(payload) of the emails.
##### Conclusion:
Plotted a picture using wordcloud to visualize the important words. (See Q1_Enron.ipynb)

--

> **Analysis 2. When did people send emails**

- **In which years were the emails sent?**

##### Collected data:
The years extracted from date of the emails.
##### Conclusion:
As shown in the histogram, most of the emails were sent in year 2000 (196101 emails) and 2001 (272819 emails).

- **On which weekdays were the emails sent?**

##### Collected data:
The weekdays extracted from date of the emails.
##### Conclusion:
As shown in the histogram, most of the emails weren't sent on weekends.

- **In which months were the emails sent?**

##### Collected data:
The months extracted from date of the emails.
##### Conclusion:
As shown in the histogram, the top three months are Oct, Sep, Jan.

--

> **Analysis 3. Who communicated via emails the most**

- **Who had the most emails?**

##### Collected data:
The X-origin of the emails.
##### Conclusion:
Kaminski-V had the most emails (26995 emails).

- **Which two accounts communicated with each other the most?**

##### Collected data:
The 'from' and 'to' of the emails. (Neglecting the emails people sent to themselves)
##### Conclusion:
Top 1 sender/receiver pair : 4308 emails were sent from vince.kaminski@enron.com to vkaminski@aol.com

---

### Question 2


**`Dataset : The NYT data-set`**


> **Collected data**


- 1000 articles about DONALD TRUMP since 20170101, stored in json file output1_donald_trump 
- 1000 articles about HILLARY CLINTON since 20170101, stored in json file output2_hillary_clinton 
- 1000 articles about BARACK OBAMA since 20170101, stored in json file output3_barack_obama- All articles published in Jan, stored in json file output_archive_201701

--

> **Analysis 1. Were the articles neutral towards Trump?**

- **Sentiment analysis on the subjects of the articles**

##### Collected data:
The subjects extracted from the keywords of the articles about Donald Trump.(Using AFINN-en-165 as a sentiment dictionary in order to give the NLTK tokenized words sentiment scores)

##### Conclusion:
No negative words were found. One positive word 'asset' were found. According to that, the articles about trump were neutral in subjects.

--

> **Analysis 2. What did the articles talk about**

- **Create WordCloud on Trump, Hillary, Obama Respectively**

##### Collected data:
The headlines of the articles about Trump/Hillary/Obama.

##### Conclusion:
Plotted a picture using wordcloud to visualize the important words. (See Q2_NYT.ipynb)

Words about Trump : donald trump new ban president immigration inauguration

Words about Hillary : trump russia new election say white house

Words about Obama : trump obama say new white house russia rule fact 

--

> **Analysis 3. Who were mentioned the most**

- **Count the keywords if they are described as 'persons'**

##### Collected data:
The names appearing in the keywords.

##### Conclusion:
Top 3:

"Trump Donald J" were mentions 985 times.

"Obama, Barack" were mentions 148 times.

"Putin, Vladimir V" were mentions 41 times.
