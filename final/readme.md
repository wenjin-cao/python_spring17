
# MovieLens Dataset Analysis

> ## Analysis 01 General Feature Analysis

### Original dataframe:
![drawing](https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/movies.png =10x5)
![drawing](https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/ratings.png)
<img src="https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/movies.png" height="10">

###  I. What are the release dates like for the movies?
#### Extract 'release_year' from 'release_date'. The range of 'release_year' is from 1920 to 2000.
#### Use pandas cut() function to convert 'year' to 'year group'. The width of each bin is 10 years.
#### Count numbers of movies grouped by 'year group' and plot.
![alt text](https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/01MovieDistributionByYear.png)
#### As shown in the image, the majority of the movies were released between the year 1970 and 2000. 

###  II. What are the 5 MOST RATED movies?
#### Merge the original dataframes to get movies and their ratings.
![alt text](https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/moviesRated.png)
#### Group by 'movie_title' to count how many ratings each movie has and sort.
#### The movies in the dataset that have most ratings are : 
![alt text](https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/01mostRated.png)
#### Get an api key from https://www.themoviedb.org and use the 'IMDB url' of the above movies to request and display their posters. e.g.
![alt text](https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/01poster1.png)

### III. What are the 5 MOST HIGHLY RATED movies?
#### Group by 'movie_title' and apply aggregate functions to get average ratings of each movie.
#### Filter the movies by count of ratings and only look at 'qualified' movies that have been rated at least 150 times.
#### The movies in the dataset that have the highest ratings are : 
![alt text](https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/01highlyRated.png)
#### Display the posters of these movies. e.g.
![alt text](https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/01poster2.png)

---

> ## Analysis 02 Divisive Rating Analysis

### I.


- 
