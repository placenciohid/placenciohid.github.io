---
layout: post
title: Building ML Models from Scratch (Decision Trees, kNN, and Logistic Regression)
description:
image: assets/images/pic18.jpg
---

<!-- Content -->
Implementing machine learning models from scratch is a challenging but rewarding endeavor. This project demonstrates the process of building three foundational ML models: Decision Trees, k-Nearest Neighbors (kNN), and Logistic Regression, using only NumPy and raw Python functions. By understanding the core concepts and manually coding these algorithms, we gain insight into their mechanics, strengths, and limitations. The models are evaluated using synthetic datasets, spam detection data, and visualized to showcase their decision-making process.

For a detailed exploration of the methodology and results, please visit the accompanying <a href="https://github.com/placenciohid/Resume/blob/e9eb9d1c9b14ff9e6f96128bf6783785336ef2a6/Building%20Machine%20Learning%20Models%20from%20Scratch%20-%20Decision%20Trees%2C%20kNN%2C%20and%20Logistic%20Regression.ipynb"><b>Jupyter notebook</b></a>.

<h3>Understanding the Problem</h3>

To understand how each model works, we implemented the algorithms step-by-step, starting with a simple 2D synthetic dataset for visual demonstration and gradually moving to more complex spam detection tasks. By implementing these models, we build a solid foundation in understanding the math behind decision boundaries, gradient optimization, and tree structures.

<h3>1-Nearest Neighbor (1NN) Classifier on a 2D Dataset</h3>

The first part of this project involved implementing a basic 1-Nearest Neighbor (1NN) classifier. Using a 2D synthetic dataset, the 1NN algorithm classified test points based on the class of their nearest training neighbor. This simple proximity-based approach helped illustrate the basic concept of distance metrics in classification problems.

We visualized the decision boundaries created by the 1NN classifier and observed how it partitioned the feature space based on the nearest neighbor’s label. This provided a hands-on experience in understanding decision boundaries and their dependence on Euclidean distance.

<h3>Spam Detection with Logistic Regression and kNN</h3>

For the second part, we tackled a binary classification problem: spam detection using word frequency data from emails. We manually implemented two models:
1. **Logistic Regression**: Built using gradient descent optimization to minimize the cost function. This approach helped us understand the role of gradient steps and convergence in optimization.
2. **k-Nearest Neighbors (kNN)**: Predicted labels using majority voting among the `k` nearest neighbors. We varied the value of `k` and evaluated the model's performance using cross-validation.

<h3>Evaluating the Models with 5-Fold Cross Validation</h3>

To ensure robustness, we applied 5-fold cross-validation on the email dataset, splitting it into five subsets and evaluating each model on different subsets. The performance was measured using metrics such as Accuracy, Precision, and Recall. Logistic Regression achieved higher accuracy compared to kNN, demonstrating the effectiveness of logistic functions for text-based classification.

<h3>Decision Tree Classifier from Scratch</h3>

In the final part, we implemented a Decision Tree classifier. This model uses recursive splitting to construct a tree that optimally partitions the feature space based on entropy and information gain. The decision tree was constructed step-by-step using:
- **Entropy**: Measured the uncertainty of the target variable.
- **Information Gain**: Calculated the reduction in entropy for each split.
- **Gain Ratio**: Used to handle bias towards features with a larger number of distinct values.

The resulting tree structure was printed to visualize the decision-making process, showing the sequence of splits and leaf nodes, which made the model's logic transparent and interpretable.

<h3>Visualizing the Decision Boundaries</h3>

For the 1NN and Decision Tree models, we visualized the decision boundaries to understand how each algorithm partitions the feature space. The visualizations highlight how the proximity-based 1NN algorithm creates boundaries based on Euclidean distance, while the Decision Tree partitions the space using a series of axis-aligned splits.

<h3>Conclusion</h3>

This project provided a hands-on understanding of how three fundamental machine learning models work: kNN, Logistic Regression, and Decision Trees. Implementing these models from scratch enhanced my comprehension of distance metrics, gradient-based optimization, and tree construction principles.

By exploring these models manually, we gained a deeper understanding of their strengths and limitations, as well as the nuances in implementing them for different types of data. Such a foundational grasp is crucial for building more complex models and selecting appropriate techniques for various machine learning tasks.

Overall, this exercise serves as a stepping stone to mastering advanced concepts in machine learning, equipping me with the skills needed to tackle real-world problems with confidence.
