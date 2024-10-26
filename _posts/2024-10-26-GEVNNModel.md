---

layout: post
title: Predicting Imbalanced Events with GEV-NN
description:
image: assets/images/pic25.jpg

---

<!-- Content -->
<div class="row">
    <div class="col-12">
        <h3>Overview</h3>
        <p>Predicting rare events within imbalanced datasets is a significant challenge in machine learning. Whether it's fraud detection, medical diagnosis, or risk assessment, the minority class—the events of greatest interest—is often overshadowed by a vast majority of non-events. Traditional models tend to be biased towards the majority, leading to poor performance in detecting these critical occurrences.</p>
        <p>In this project, I implement the <b>Generalized Extreme Value Neural Network (GEV-NN)</b> to address this issue. By leveraging the unique properties of the Generalized Extreme Value distribution and combining it with an autoencoder for feature extraction, the model enhances its ability to predict minority class events effectively.</p>
        <p>To delve deeper into the methodology and view the detailed code implementation, please visit the accompanying <a href="https://github.com/placenciohid/Resume/blob/c0f227928c6062ab7c87691dbe841b8eebd985ec/GEV-NN-Model.py"><b>Python script</b></a>.</p>
    </div>
</div>

<div class="row">
    <div class="col-12">
        <h3>Objectives</h3>
        <ul>
            <li>Develop a model capable of accurately predicting rare events in an imbalanced dataset.</li>
            <li>Implement the GEV-NN architecture to handle class imbalance.</li>
            <li>Enhance feature extraction using an autoencoder.</li>
            <li>Evaluate the model using appropriate metrics to assess performance on the minority class.</li>
        </ul>
    </div>
</div>

<div class="row">
    <div class="col-12">
        <h3>Data Preprocessing</h3>
        <ul>
            <li><b>Feature Standardization</b>: All features are standardized using <code>StandardScaler</code> to ensure consistent scaling.</li>
            <li><b>Class Weight Calculation</b>: Class weights are computed to address the imbalance between majority and minority classes, influencing the loss function during training.</li>
        </ul>
    </div>
</div>

<div class="row">
    <div class="col-12">
        <h3>Model Architecture</h3>

        <h4>1. Generalized Extreme Value Activation Function</h4>
        <p>The GEV activation function is integrated into the model to focus on extreme values, which are often associated with rare events. This function helps the network prioritize instances that are critical for minority class prediction.</p>

        <h4>2. Autoencoder for Feature Extraction</h4>
        <p>An autoencoder is employed to learn compressed representations of the data:</p>
        <ul>
            <li><b>Encoder</b>: Reduces dimensionality by compressing input features into a lower-dimensional space.</li>
            <li><b>Decoder</b>: Reconstructs the input data from the encoded representation, ensuring essential information is retained.</li>
        </ul>

        <h4>3. Self-Organizing Fuzzy Neural Network (SOFNN)</h4>
        <p>The SOFNN dynamically assigns importance to input features:</p>
        <ul>
            <li>Evaluates the relevance of each feature.</li>
            <li>Enhances the model's focus on attributes that are more indicative of the minority class.</li>
        </ul>
    </div>
</div>

<div class="row">
    <div class="col-12">
        <h3>Training Process</h3>
        <ul>
            <li><b>Loss Functions</b>:
                <ul>
                    <li><b>Mean Squared Error (MSE)</b>: Used for training the autoencoder to reconstruct inputs accurately.</li>
                    <li><b>Weighted Binary Cross-Entropy Loss</b>: Employed for the classification task, incorporating class weights to penalize misclassification of the minority class more heavily.</li>
                </ul>
            </li>
            <li><b>Optimization</b>:
                <ul>
                    <li><b>Adam Optimizer</b>: Efficiently updates model parameters during training.</li>
                    <li><b>Learning Rate Scheduler</b>: Adjusts the learning rate based on validation loss to fine-tune the training process.</li>
                    <li><b>Early Stopping</b>: Prevents overfitting by halting training when validation performance stops improving.</li>
                </ul>
            </li>
        </ul>
    </div>
</div>

<div class="row">
    <div class="col-12">
        <h3>Evaluation Metrics</h3>
        <p>To assess the model's performance, several metrics are utilized:</p>
        <ul>
            <li><b>AUC-ROC</b>: Measures the model's ability to distinguish between classes across all thresholds.</li>
            <li><b>F1 Score</b>: Balances precision and recall, providing insight into the model's accuracy on the minority class.</li>
            <li><b>Brier Score</b>: Evaluates the accuracy of probabilistic predictions.</li>
            <li><b>Geometric Mean (G-Mean)</b>: Reflects the balance between sensitivity and specificity.</li>
        </ul>
        <p>Visualization tools like confusion matrices and ROC curves offer a clear picture of the model's performance.</p>
    </div>
</div>

<div class="row">
    <div class="col-12">
        <h3>Results and Insights</h3>
        <p>The GEV-NN model demonstrates promising results in predicting rare events:</p>
        <ul>
            <li><b>Improved Detection of Minority Class</b>: The model achieves higher recall for the minority class, indicating better detection of rare events.</li>
            <li><b>Balanced Performance</b>: High G-Mean scores show that the model maintains a balance between correctly identifying both classes.</li>
            <li><b>Robustness</b>: The integration of GEV activation and feature extraction through the autoencoder enhances the model's robustness against imbalanced data.</li>
        </ul>
    </div>
</div>

<div class="row">
    <div class="col-12">
        <h3>Conclusion</h3>
        <p>Predicting rare events in imbalanced datasets is challenging but critical. The GEV-NN model presents a powerful approach to tackle this issue, combining advanced neural network techniques with specialized activation functions. This implementation demonstrates the potential for improved detection of rare events, which can be invaluable in various domains such as finance, healthcare, and security.</p>
        <p>By leveraging these techniques, practitioners can develop models that are more sensitive to the minority class, leading to better decision-making and outcomes.</p>
    </div>
</div>

<div class="row">
    <div class="col-12">
        <h3>Citation</h3>
        <p>Munkhdalai, L., Munkhdalai, T., & Ryu, K. H. (2020). GEV-NN: A deep neural network architecture for class imbalance problem in binary classification. <em>Knowledge-Based Systems</em>, 194, 105534. <a href="https://doi.org/10.1016/j.knosys.2020.105534">https://doi.org/10.1016/j.knosys.2020.105534</a></p>
    </div>
</div>