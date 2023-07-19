---
layout: post
title: Uncovering Google Play Store Reviews - A Data-Driven Analysis
description:
image: assets/images/pic22.jpg
---

User reviews on the Google Play Store offer valuable feedback for application developers, providing insights that drive app improvements and enhance user satisfaction. In this project, we embark on a data-driven journey to explore the fascinating world of topic modeling, sentiment analysis, and rating prediction using user feedback from the Google Play Store. The aim is to uncover the most common themes, sentiments, and preferences within the vast volume of unstructured user feedback.

<h3>Objectives</h3>

The objectives are to first, generate topic models and gain insights into common themes expressed in user reviews, and second, to build a rating prediction model based on the review text to assess overall user sentiment. Achieving these goals will empower developers to make data-driven decisions, enhancing their applications and better catering to user needs.

<h3>Data Cleaning and Preprocessing</h3>

Before delving into topic modeling, I performed necessary data cleaning and preprocessing on the dataset. This involves handling missing data, dropping irrelevant columns, and transforming the text through tokenization, lemmatization, and stop word removal. The resulting clean and processed reviews serve as the foundation for my analysis.

<h3>Topic Modeling</h3>

<h4>Topic Modeling using Latent Semantic Indexing (LSI)</h4>

I begin my topic modeling journey with Latent Semantic Indexing (LSI) from the gensim library. LSI is a statistical model that explores relationships between documents and the terms they contain. I iteratively optimize the number of topics by calculating coherence scores to select the model with the highest quality. The final optimal LSI model reveals three topics, primarily revolving around app functionality, task management, and calendar features.

<h4>Topic Modeling using Latent Dirichlet Allocation (LDA)</h4>

Continuing my exploration, I apply Latent Dirichlet Allocation (LDA) from the gensim library for topic modeling. LDA is a generative statistical model that assumes each document in a corpus is a mixture of topics. I optimize the number of topics using coherence scores and ultimately arrive at an LDA model with 13 topics. These topics provide insights into areas such as app features, task management, user sentiment, and app versions.

<h4>Topic Modeling using LDA with Spacy</h4>

For my final topic modeling approach, I leverage LDA with Spacy, harnessing the power of the Spacy NLP library and LDA algorithm. After preprocessing the text data with Spacy, I extract features and train the LDA model. The coherence score for this model is 0.47, indicating reasonable performance in identifying coherent topics. The resulting themes include app usability, calendar features, app versions, and user satisfaction.

<h3>Rating Prediction Model</h3>

In addition to topic modeling, I also delve into building a predictive model for determining review ratings based on their text using a combination of natural language processing and classification algorithms. This enables developers to gauge overall user sentiment and make data-driven decisions to enhance their applications. To achieve this, I fine-tune BERT (from Google Transformers) on a dataset of reviews and their corresponding ratings, showcasing the steps involved in training the model, such as data splitting, attention mask creation, and the training process. Sentiment analysis becomes a vital tool for developers to understand user satisfaction, identify pain points, and implement targeted enhancements. Now, with the trained model capable of predicting review ratings, developers can quickly assess incoming reviews' sentiment and take prompt action to address user concerns or appreciate positive feedback.

<h3>Conclusion</h3>

This work on topic modeling, sentiment analysis, and rating prediction on apps reviews could provide valuable insights for developers. By leveraging these powerful tools, developers can elevate their applications, improve user experiences, and stay competitive in the app market. The combination of NLP techniques and machine learning empowers developers to unlock the potential of user feedback and create impactful applications that cater to user needs.


