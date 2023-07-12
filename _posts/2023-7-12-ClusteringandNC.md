---
layout: post
title: Unveiling Insights from Clustering and Non-Compliance in Experimental Data
description: 
image: assets/images/pic17.jpg
---

<!-- Content -->
<p>In the realm of data analytics, two crucial concepts, clustering and non-compliance, hold significant importance. These concepts provide valuable insights into understanding patterns within data and analyzing the impact of interventions or treatments. In this article, we delve into the world of clustering and non-compliance, exploring their applications and implications in experimental data analysis.
<h3>Clustering</h3>
Clustering, a technique widely employed in experimental design, involves grouping experimental units or subjects into homogeneous subsets based on specific attributes. The objective of clustering is to create internally similar and externally dissimilar groups, enhancing the efficiency and accuracy of experiments. By clustering similar units together, researchers can reduce variability within each group, leading to more precise comparisons and analysis of treatment effects. In essence, clustering aids in creating a balanced and representative sample, yielding insightful conclusions from experimental studies.
To demonstrate the application of clustering, let's consider a hypothetical randomized controlled trial (RCT) conducted on 200 stores within a company. These stores were randomly assigned to treatment and control groups to evaluate the impact of in-store advertisements on sales. Data was collected from the first 1,000 customers who visited the stores after the experiment's launch, recording the amount they purchased.
To analyze the average treatment effect (ATE) on sales using the aggregated store-level data, we can calculate the ATE and its confidence interval (CI) to gauge the impact of in-store advertisements on sales.
To delve deeper into the analysis, and check the methodology and results, please visit the accompanying <a href="https://github.com/placenciohid/Resume/blob/main/Clustering%20and%20Non-Compliance.ipynb"><b>Jupiter notebook</b></a>.
<h3>Non-Compliance</h3>
In experimental design, non-compliance refers to situations where participants do not adhere to the assigned treatment or fail to comply with the experimental protocol. Non-compliance can introduce bias and affect the validity of experimental results. Addressing non-compliance is crucial to obtain accurate conclusions from experimental studies. Researchers employ various strategies such as monitoring participant adherence, implementing incentives or reminders, and adopting specific analytical approaches like intention-to-treat or complier average causal effect methods.
To illustrate the concept of non-compliance, we consider a company's randomized controlled trial to increase flu shot participation among employees. The trial consists of two treatment groups:
<ul>
    <li>Treatment 1: Employees were sent an email encouraging them to take an online "flu awareness quiz" with the chance to win a $100 prize.</li>
    <li>Treatment 2: Similar to Treatment 1, employees were sent an email but received an automated call if they had not taken the quiz within a week.</li>
</ul>
The company tracked the fraction of participants taking the quiz and the flu shot rates across the control and treatment groups. By examining the intention-to-treat (ITT) estimates and treatment-on-the-treated (TOT) effects, we gain insights into the impact of the survey on flu shot rates.
To delve deeper into the analysis, and check the methodology and results, please visit the accompanying <a href="https://github.com/placenciohid/Resume/blob/main/Clustering%20and%20Non-Compliance.ipynb"><b>Jupiter notebook</b></a>.
<h3>Conclusion</h3>
Clustering and non-compliance play pivotal roles in analyzing experimental data. Clustering aids in identifying patterns and creating balanced samples, while non-compliance analysis helps address biases and enhance the accuracy of experimental findings. Understanding these concepts provides researchers and analysts with powerful tools to draw insightful conclusions from their data.
By leveraging clustering and addressing non-compliance, researchers can uncover valuable insights that shape the success of experimental studies and guide decision-making processes.</p>