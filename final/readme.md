
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
<img src="https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/0203RatingDifferenceByGender.png" height="550">

---

> ## Analysis 03 User Occupation Analysis

###  I. How are occupations distributed amongst the users?
#### Group the users by occupations and count the numberbs. As shown in the pie chart below, the users in the dataset comes from 19 specified occupations. Students account for 20% of the users, which makes the biggest occupation group. Nearly half of the users are students or educators or administrators.
<img src="https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/0301OccupationPercentage.png" height="200">

### II. How is the gender bias like in each profession?
#### For each occupation, count the number the female users and the number of male users. As we can see in the stacked bar char below, in most of the occupations, there are more male users than female users. And this difference tends to be more remarkable when it comes to occupations with less people totally, such as the occupation 'technician', 'scientist', 'retired', 'entertainment'.
<img src="https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/0302UsersCountOfEachOccupation.png" height="200">

#### To observe the difference in gender more clearly, calculate the percentage of males and females for each occupation. As is shown below, 'librarian', ' artist' and 'adminitrator' have the most balanced users with respect to gender, while 'doctor', 'engineer', 'technician' the least. 
<img src="https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/0303Female&MalePercentageOfEachOccupation.png" height="200">

### III. How 'old' is each profession?
#### For each occupation, calculate the average age. As we can see, the 'oldest' occupations are 'retired', 'doctor', 'educator'. The 'youngest' occupations are 'student', 'entertainment', 'artist'. And the majority of the occupations are in age range 20-40.
<img src="https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/0304AvgAge.png" height="200">

#### The violin plot shows the age distribution for each occupation more vividly.
<img src="https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/0305AgeDistributionAmongOccupations.png" height="200">

### IV. Do users from different professions tend to rate movies differently?
#### Use a violin plot to depict the distribution of ratings among professions.
<img src="https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/0306RatingDistributionAmongOccupations.png" height="200">

#### For each occupation, calculate the average rating using groupby() and aggregation function.
<img src="https://github.com/wenjin-cao/python_spring17/blob/master/final/pics/0307AvgRatingOfEachOccupation.png" height="200">

#### According to the graphs, there's only slight differences in avg. ratings with respect to occupations. Yet we can still tell that healthcare people tend to rate movies the lowest and lawyers tend to rate the highest. 

---

> ## Analysis 03 User Occupation Analysis






















