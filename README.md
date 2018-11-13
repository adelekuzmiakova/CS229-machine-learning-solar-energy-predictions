# CS229 Project Files

by Adele Kuzmiakova, Gael Colas, and Alex McKeehan, graduate students at Stanford University. This repo contains all project files used for the class. Course notes are available from the course website at http://cs229.stanford.edu/ or https://see.stanford.edu/course/cs229. 

**Goal:** Predict the solar energy output from a solar power plant at the University of Illinois using weather features and local meta-data, for instance, the month or the hour of the day.

**tl;dr:** LSTM networks performed the best for the prediction of the solar energy due to their abilities to connect recent features to perform present day predicitions.

The project had 3 main parts:

* **Data pre-processing:** we processed the raw weather data inpuits from the National Oceanographic and Atmospheric Administration and the solar energy output files from Urbana-Champaign solar farm in order to get meaningful numeric values with hourly and daily resolutions. 

* **Feature selection:** we run the correlation analysis between the weather features and the energy output to discard useless features. Additionally, we implemented Principal Component Analysis (PCA) to reduce the dimensionality of our dataset. Finally, using gradient boosting, we obtained estimates of feature importance from a trained predictive model.

* **Machine learning:** We started with simple models, such as weighted linear regression and PCA. Additionally, we used generalized boosting methods, which build an ensemble of shallow and week successive trees where each tree is learning and improving from the previous ones. Finally, we experimented with implementation of neural networks with and without vanishing temporal gradient.
