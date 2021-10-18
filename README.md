# Political Sentiment on Social Media
The effect of social media on politics is a frequently discussed issue. Claims are often made by media outlets and regulators that social media has a generally negative effect on political sentiment in the US—that social media creates “echo chambers” of like-minded people which lead to polarization and increasingly extreme views.

In an effort to illustrate this phenomenon, I analyzed 400k reddit comments from Jan 23 - Sept 15, 2021 and attempted to build a regression model that would use these commments to predict a more statistically robust sampling of political sentiment in the US -- presidential approval ratings.

## Analysis of Reddit comments

Using TextBlob, I generated sentiment scores for each comment and compared general sentiment across subreddits:

![Sentiment by Subreddit](https://github.com/zelda4669/presidential-approval/blob/main/Images/Sentiment%20by%20Subreddit.jpg)

![Polarity by Subreddit](https://github.com/zelda4669/presidential-approval/blob/main/Images/Polarity%20of%20Comments%20by%20Subreddit.jpg)

![Subjectivity by Subreddit](https://github.com/zelda4669/presidential-approval/blob/main/Images/Subjectivity%20of%20Comments%20by%20Subreddit.jpg)


There is little variation in these scores across the various subreddits, indicating that despite differing viewpoints, the caliber of discussions being held is similar across subreddits.

## Modelling

I chose to use regression modelling instead of a time-series model because the target variable doesn't display seasonality. I ran several different regression models to find the best-fitting model for this dataset.

![Modelling Results](https://github.com/zelda4669/presidential-approval/blob/main/Images/Model%20Metrics.png)

R-squared values indicate an extremely low correlation between Reddit discourse and Presidential approval ratings. Plotting actual versus predicted values for the "best fitting" model demonstrate how little correlation there is.

![Actual vs Predicted Ratings](https://github.com/zelda4669/presidential-approval/blob/main/Images/Actual%20vs%20Predicted%20Approval%20Ratings.png)

Based on these results, we cannot reject the hypothesis that political echo chambers exist on Reddit, and that these communities have little in common with political sentiment in the US at large.

## Next Steps

Reddit is not the only social media site out there--to further explore this hypothesis, models using Twitter or Facebook data should be developed.