# Supervised Contrastive Image Classification

#### Novel Image classification competition

# Description

## Background

Traditional image classification approaches typically rely on softmax cross-entropy loss which doesn't explicitly optimize the structure of the feature space. This competition focuses on the emerging paradigm of supervised contrastive learning , which combines the strengths of contrastive representation learning with label information to create more robust and discriminative features.

## Problem Description

Your challenge is to implement and improve upon supervised contrastive learning for image classification. Unlike self-supervised contrastive learning which only treats augmentations of the same image as positives, supervised contrastive learning leverages class labels to treat all samples from the same class as positives.

## The Mathematical Foundation

The supervised contrastive loss in outer summation form is defined as:

![Outer Loss](https://latex.codecogs.com/png.image?\dpi{110}L_{sup}=\sum_{i\in%20I}%20\frac{-1}{|P(i)|}%20\sum_{p\in%20P(i)}%20\log\frac{\exp(z_i\cdot%20z_p/\tau)}{\sum_{a\in%20A(i)}\exp(z_i\cdot%20z_a/\tau)})


An equivalent but computationally optimized inner summation form is:

![Inner Loss](https://latex.codecogs.com/png.image?\dpi{110}L_{sup}=\sum_{i\in%20I}%20\log\left(\frac{\sum_{a\in%20A(i)}%20\exp(z_i\cdot%20z_a/\tau)}{\sum_{p\in%20P(i)}%20\exp(z_i\cdot%20z_p/\tau)}\right))

This version flips the numerator and denominator to emphasize the contrast between all samples and positive pairs.

## Key Properties

### The supervised contrastive approach offers several advantages:

- **Multiple Positives**:  
  Unlike traditional contrastive learning, it handles multiple positive examples per anchor.

- **Implicit Hard Mining**:  
  The gradient structure naturally emphasizes hard positives and negatives without explicit mining.

- **Scaling with Negatives**:  
  Performance improves as the number of negative examples increases.

- **Robust Clustering**:  
  Creates more coherent class clusters in the embedding space.

## Challenge

### Your task is to:
- Implement a supervised contrastive learning framework for image classification
- Explore modifications to the base loss function to improve performance
- Investigate the impact of different architectural choices on representation quality
- Develop techniques to effectively balance positive and negative examples
- Analyze the resulting embedding space and classification performance

## Evaluation
## The solutions will be judged based on F1-scores.
