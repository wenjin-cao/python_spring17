
# MovieLens Dataset Analysis

> ## Analysis 01 General Feature Analysis

###  I. What are the release dates like for the movies?
#### Extract 'release_year' from 'release_date'. The range of 'release_year' is from 1920 to 2000.
#### Use pandas cut() function to convert 'year' to 'year group'. The width of each bin is 10 years.
<img src="https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/01yearGroup.png" height="150">

#### Count numbers of movies grouped by 'year group' and plot.
#### As shown in the graph below, the majority of the movies were released between the year 1970 and 2000. 
<img src="https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/01MovieDistributionByYearGroup.png" height="250">

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
<img src="https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/0202RatingDifferenceByAgeGroup.png" height="600">

### II. Which movies are the most divisive among different genders?
#### Pivot the table below to user 'sex' as columns.
<img src="https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/movielens.png" height="150">

#### Find out the avg. rating difference of each movie (avg. rating from females - avg. rating from males)
<img src="https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/02genderDiff.png" height="150">

#### Now we only look at the 100 most rated movies. Plot a 'barh' graph depicting the rating difference by gender of each movie. As we can see, the differences in rating by gender are less notable than by age group. Among these movies, Sound Of Musice is particularly prefered by females, and 2001 A Space Odyssey is particularly prefered by males.
<img src="https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/0203RatingDifferenceByGender.png" height="600">

---

> ## Analysis 03 User Occupation Analysis

###  I. How are occupations distributed amongst the users?
#### Group the users by occupations and count the numberbs. As shown in the pie chart below, the users in the dataset comes from 19 specified occupations. Students account for 20% of the users, which makes the biggest occupation group. Nearly half of the users are students or educators or administrators.
<img src="https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/0301OccupationPercentage.png" height="400">

### II. How is the gender bias like in each profession?
#### For each occupation, count the number the female users and the number of male users. As we can see in the stacked bar char below, in most of the occupations, there are more male users than female users. And this difference tends to be more remarkable when it comes to occupations with less people totally, such as the occupation 'technician', 'scientist', 'retired', 'entertainment'.
<img src="https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/0302UsersCountOfEachOccupation.png" height="550">

#### To observe the difference in gender more clearly, calculate the percentage of males and females for each occupation. As is shown below, 'librarian', ' artist' and 'adminitrator' have the most balanced users with respect to gender, while 'doctor', 'engineer', 'technician' the least. 
<img src="https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/0303Female&MalePercentageOfEachOccupation.png" height="550">

### III. How 'old' is each profession?
#### For each occupation, calculate the average age. As we can see, the 'oldest' occupations are 'retired', 'doctor', 'educator'. The 'youngest' occupations are 'student', 'entertainment', 'artist'. And the majority of the occupations are in age range 20-40.
<img src="https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/0304AvgAge.png" height="550">

#### The violin plot shows the age distribution for each occupation more vividly.
<img src="https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/0305AgeDistributionAmongOccupations.png" height="550">

### IV. Do users from different professions tend to rate movies differently?
#### Use a violin plot to depict the distribution of ratings among professions.
<img src="https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/0306RatingDistributionAmongOccupations.png" height="550">

#### For each occupation, calculate the average rating using groupby() and aggregation function.
<img src="https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/0307AvgRatingOfEachOccupation.png" height="550">

#### According to the graphs, there's only slight differences in avg. ratings with respect to occupations. Yet we can still tell that healthcare people tend to rate movies the lowest and lawyers tend to rate the highest. 

---

> ## Analysis 04 Movie Genre Analysis
### I. How do the movies vary with respect to genres?
#### For each genre, count the number of movies beloging to it. As we can see from the graph below, counts of movies of each genre vary greatly. The genre 'drama' has the most movies while 'fantasy' has the least. According the count of movies, the 3 most popular genres are 'drama', 'comedy', ' thriller', and the 3 least popular genres are 'fantasy', 'film noir', 'western'. P.S. Movies in the data may have multiple genres.
<img src="https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/0401MoviesCountOfEachGenre.png" height="550">

#### For each genre, count the average rating of movies beloging to it. Plot and compare the avg. ratings. Then in order to be convincible, we only consider genres of which movies have at least 100 ratings.As we can see from the image below, 'drama' has the highest average rating, while 'children' the lowest. Yet, generally speaking, ratings don't differ much among different genres.
<img src="https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/0403AvgRatingOfEachGenre(IgnoringSmallSampleSizes).png" height="550">

### II. How does the gender affect the rating of movies in each genre?
#### For each genre, count the average ratings of movies beloging to it with respect to gender. Only consider popular genres of which movies have at least 100 ratings in order to exclude very small samples.
#### The graph below shows avg. rating of female, male and both for different genres. As we can see, the difference between male and female in rating is not very big. But we may still reckon that women tend to love some genres better such as 'romance' and 'children's', while men 'crime' and 'sci-fi'.
<img src="https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/0404GenderDifferenceInAvgRatingOfEachGender.png" height="550">

### III. Does the profession matter to movie genre preference?
#### For each genre, count number of users from each occupation.
#### The heatmap below shows the different ratings of movies of different genres with respect to users' occupations. 
#### Users of some occupations tend to rate higher such as 'lawyer', 'artist', 'salesman' and 'administrator', while some tend to rate lower such as 'healthcare', 'homemaker', 'writer' and 'retired'. 
#### Some genres tend to be prefered by certain occupations. E.g., 'adventure' and 'thriller' movies are more welcome among lawyers, 'sci-fi' are liked better by artists. Likewise, certain occupations have certain preference. E.g., besides the commonly popular genres, salespeople also like 'adventure', doctors 'thriller', executives 'sci-fi'.
<img src="https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/0405AvgRatingHeatmap.png" height="550">

---

> ## Analysis 05 Movie Recommendation Analysis
### I. What are the recommended movies given a certain movie?
#### To compute similarities between movies, find the correlation between movies and then use that correlation to find similar movies to those the users have liked.
#### Calculate the correlation coefficient between each movie pair based on the ratings.
#### Build a recommender system using collaborative filtering to get the top 5(or less) recommended movies in the dataset. For each movie, return top 5 similar movies that have a high correlation coefficent with it. These recommendations can also be used to recommend movies to users.
<img src="https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/05recommendation.png" height="200">

### II. How to recommend movies to a given user?
#### Based on the ratings of the movies, create a matrix with a user per row and a movie per column
<img src="https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/05ratingMatrix.png" height="200">

#### To find similarities between movies, use the built-in function numpy.corrcoef() to calculates the Pearson Product Moment Correlation Coefficient between each movie pair. 
#### To provide recommendations to a user, take the list of movies that user has rated. Sum the correlations of those movies with all the other ones and return a list of those movies sorted by their total correlation with that user.
#### Below shows how the recommender system works.
<img src="https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/05moviesForUser.png" height="200">






