
# MovieLens Dataset Analysis

> ## Analysis 01 General Feature Analysis

###  I. What are the release dates like for the movies?
#### Extract 'release_year' from 'release_date'. The range of 'release_year' is from 1920 to 2000.
#### Use pandas cut() function to convert 'year' to 'year group'. The width of each bin is 10 years.
<img src="https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/01yearGroup.png" height="150">

#### Count numbers of movies grouped by 'year group' and plot.
<img src="https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/01MovieDistributionByYearGroup.png" height="250">

#### As shown in the image, the majority of the movies were released between the year 1970 and 2000. 

###  II. What are the 5 MOST RATED movies?
#### Merge the original dataframes to get movies and their ratings.
<img src="https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/moviesRated.png" height="150">

#### Group by 'movie_title' to count how many ratings each movie has and sort.
#### The movies in the dataset that have most ratings are : 
<img src="https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/01mostRated.png" height="150">

#### Get an api key from https://www.themoviedb.org and use the 'IMDB url' of the above movies to request and display their posters. E.g.
<img src="https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/01poster1.png" height="200">

### III. What are the 5 MOST HIGHLY RATED movies?
#### Group by 'movie_title' and apply aggregate functions to get average ratings of each movie.
#### Filter the movies by count of ratings and only look at 'qualified' movies that have been rated at least 150 times.
#### The movies in the dataset that have the highest ratings are : 
<img src="https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/01highlyRated.png" height="150">

#### Display the posters of these movies. E.g.
<img src="https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/01poster2.png" height="200">

---

> ## Analysis 02 Divisive Rating Analysis

### I. Which movies are the most divisive among different ages?
#### Find out how ages are distributed among the users. As shown in the histogram below, the age range is 0 - 80. And most of the users are between age 20 - 40.
<img src="https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/0201UserAgeDistribution.png" height="250">

#### Find out how ratings differ among age groups. As shown in the table below, the lowest rating comes from the age group 'Adolescence' and the highest rating 'Late Adulthood'. So we can reckon the youngest and the oldest have the most divisive opinions.
<img src="https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/02ageGroup.png" height="150">

#### Now we only look at the 100 most rated movies. For each movie, calculate the average ratings from different age groups, and get the difference between the two most divisive age groups.
<img src="https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/02ageGroup2.png" height="150">

#### Based on the above table, plot a graph showing the differences. As shown in the graph below, the most divisive movies are the ones with the biggest differences. Among the 100 most rated movies, Chasing Amy is specially prefered by people older than 60, Speed is specially prefered by people under 20.
<img src="https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/0202RatingDifferenceByAgeGroup.png" height="550">

### II. Which movies are the most divisive among different genders?
#### Pivot the table below to user 'sex' as columns.
<img src="https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/movielens.png" height="150">

#### Find out the avg. rating difference of each movie (avg. rating from females - avg. rating from males)
<img src="https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/02genderDiff.png" height="150">

#### Now we only look at the 100 most rated movies. Plot a 'barh' graph depicting the rating difference by gender of each movie. As we can see, the differences in rating by gender are less notable than by age group. Among these movies, Sound Of Musice is particularly prefered by females, and 2001 A Space Odyssey is particularly prefered by males.
<img src="https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/02genderDiff.png" height="550">

---








