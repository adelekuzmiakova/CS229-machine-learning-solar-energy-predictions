## Predicting solar energy using machine learning: CS 229 project

<img src="assets/cs229-project-poster.png" width="756" height="500" />

[Poster](https://github.com/adelekuzmiakova/CS229-machine-learning-solar-energy-predictions/blob/master/assets/cs229-project-poster.png), [Report](https://github.com/adelekuzmiakova/CS229-machine-learning-solar-energy-predictions/blob/master/cs229-final-report.pdf)

by Adele Kuzmiakova, Gael Colas, and Alex McKeehan, graduate students at Stanford University. This repo contains all project files used for CS229 class in Autumn quarter 2017. Course notes are available from the course website at http://cs229.stanford.edu/ or https://see.stanford.edu/course/cs229. 

**Goal:** Predict the solar energy output from a solar power plant at the University of Illinois using weather features and local meta-data, for instance, the month or the hour of the day.

**tl;dr:** LSTM networks performed the best for the prediction of the solar energy due to their abilities to connect recent features to perform present day predicitions.

The project had 3 main parts:

* **Data pre-processing:** we processed the raw weather data inpuits from the National Oceanographic and Atmospheric Administration and the solar energy output files from Urbana-Champaign solar farm in order to get meaningful numeric values with hourly and daily resolutions. 

* **Feature selection:** we run the correlation analysis between the weather features and the energy output to discard useless features. Additionally, we implemented Principal Component Analysis (PCA) to reduce the dimensionality of our dataset. Finally, using gradient boosting, we obtained estimates of feature importance from a trained predictive model.

* **Machine learning:** We started with simple models, such as weighted linear regression and PCA. Additionally, we used generalized boosting methods, which build an ensemble of shallow and week successive trees where each tree is learning and improving from the previous ones. Finally, we experimented with implementation of neural networks with and without vanishing temporal gradient.

One thing that probably would be very important is not randomizing examples. In our project we shuffled all examples and randomly split them into train/dev/test sets (60/20/20). It might be better to use sequences of data to advantage of short-term weather dependence. For instance, weather conditions yesterday would dictate weather conditions today to some extent (e.g. we do not expect to encounter a significant temperature gradient overnight). As a result, instead of randomizing our examples, we could have considered them sequentially and attempted to predict the solar output for next day ahead from its immediately preceding one or two neighbors.

## Updating/Contributing 👋

This project was done in autumn 2017 and hasn't been updated since then. If anything feels off or looks outdated (which is very likely!), feel free to open an issue or submit a pull request to the project. Thanks! :)
