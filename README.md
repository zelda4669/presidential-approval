# Political Sentiment on Social Media
The effect of social media on politics is a frequently discussed issue. Claims are often made by media outlets and regulators that social media has a generally negative effect on political sentiment in the US—that social media creates “echo chambers” of like-minded people which lead to polarization and increasingly extreme views.

In an effort to illustrate this phenomenon, I analyzed 400k reddit comments from Jan 23 - Sept 15, 2021 and attempted to build a regression model that would use these commments to predict a more statistically robust sampling of political sentiment in the US -- presidential approval ratings.

## Analysis of Reddit comments

Using TextBlob, I generated sentiment scores for each comment and compared general sentiment across subreddits:

(sentiment graph bar graph)
(sentiment graph violin plot)

There is little variation in the 