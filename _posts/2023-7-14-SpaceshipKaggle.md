---
layout: post
title: Optimizing Predictive Performance for a Kaggle Competition
description:
image: assets/images/pic21.jpg
---

In the ever-evolving world of data science and machine learning, competitions provide an exciting opportunity to showcase skills and knowledge. Recently, I participated in a Titanic Survival Prediction competition, aiming to develop a robust model that accurately predicts the survival outcome of passengers aboard the ill-fated **Spaceship Titanic**. This article chronicles my journey and the steps I took to optimize the predictive performance of my submission.

To delve deeper into the analysis and explore the complete methodology and results, please visit the accompanying <a href="https://github.com/placenciohid/Resume/blob/d812b8d672441ae6edd5b8966baaeed5019ee2f0/Spaceship%20Titanic%20-%20Kaggle.ipynb"><b>Jupyter notebook</b></a>.

<h4>Exploratory Data Analysis (EDA)</h4>

The first crucial step was to gain a deep understanding of the dataset through exploratory data analysis. By meticulously examining the provided features, such as passenger origin, destination, age, and various expenditures, I unearthed meaningful insights and potential correlations. This process enabled me to make informed decisions when preprocessing and engineering the data for model training.

<h4>Data Preprocessing and Feature Engineering</h4>

To ensure the data was in a suitable format for model training, I embarked on a comprehensive data preprocessing journey. This involved handling missing values, encoding categorical variables, and scaling numerical features. Moreover, I strategically engineered new features, such as total expenditure and family size, to enhance the predictive power of the model.

<h4>Model Selection and Training</h4>

With the preprocessed data in hand, I ventured into selecting the most appropriate machine learning models for the task. I experimented with several popular algorithms, including Random Forest, Gradient Boosting, LightGBM, XGBoost, CatBoost, Support Vector Machines (SVM), and a deep Neural Network. Through rigorous evaluation and comparison, I identified the models that exhibited the highest predictive accuracy, precision, recall, and F1 score.

<h4>Hyperparameter Tuning</h4>

Realizing that fine-tuning the models could potentially yield further improvements, I delved into hyperparameter tuning. Leveraging techniques like `RandomizedSearchCV` and `GridSearchCV`, I explored various combinations of hyperparameters to optimize the performance of the Random Forest, XGBoost, and LightGBM models. This meticulous process led me to discover the best parameter configurations that significantly boosted the accuracy and robustness of my models.

<h4>Stacking Ensemble</h4>

Inspired by the concept of ensemble learning, I decided to combine the strengths of my top-performing models using a **Stacking Classifier**. By aggregating the predictions of the CatBoost, XGBoost, LightGBM, SVM, Neural Network, and Random Forest models, I aimed to create a more robust and accurate final prediction. The ensemble model exhibited excellent accuracy and precision, outperforming individual models.

<h4>Competition Performance</h4>

My final submission achieved an impressive position of **123 out of 1,603 participants**, placing me in the top **7.7%** of the competition. The ensemble model, which combined the strengths of CatBoost, XGBoost, LightGBM, SVM, Neural Network, and Random Forest, demonstrated exceptional accuracy, scoring **0.80710**. The precision, recall, and F1 scores were also consistently high, reflecting the robustness and effectiveness of the advanced techniques and models used.

Through various stages, including exploratory data analysis, feature engineering, model selection, hyperparameter tuning, and advanced ensemble techniques, I steadily enhanced the predictive performance of the model. Each step brought me closer to unlocking the full potential of the dataset and honing my understanding of the underlying principles. This experience has been invaluable in broadening my knowledge and refining my skills. I look forward to participating in more competitions and furthering my expertise in the field of data science and machine learning.
