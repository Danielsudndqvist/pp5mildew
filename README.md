# Cherry Leaf Mildew Detection

## Dataset Content
* The dataset contains 2104 images of cherry leaves:
   * 1052 healthy leaves
   * 1052 leaves infected with powdery mildew
* The image data was sourced from Kaggle
* Dataset split:
   * Training: 1682 images (80%)
   * Validation: 422 images (20%)

## Business Requirements
As a consulting data analyst firm, we have been tasked with creating a solution that helps farmers detect powdery mildew in cherry leaves. The following requirements have been identified:

1. The client wants to visually differentiate between healthy and powdery mildew-infected cherry leaves
    * Success Criteria: Create a visual analysis tool that highlights the key differences between healthy and infected leaves

2. The client wants to predict if a cherry leaf is healthy or contains powdery mildew
    * Success Criteria: Create a ML model that accurately predicts the condition of a cherry leaf with at least 97% accuracy

## User Stories
1. As a farmer
   I want to visually differentiate healthy cherry leaves from infected ones
   So that I can understand what to look for during manual inspection

2. As a farm manager
   I want to receive predictions about leaf health from leaf images
   So that I can quickly identify infected trees and take action

3. As a quality control specialist
   I want to batch process multiple leaf images
   So that I can efficiently screen large numbers of samples

4. As a farm training coordinator
   I want to see clear visual examples of leaf infections
   So that I can train new staff on disease identification

## Rationale to Map Business Requirements to ML Tasks

### Business Requirement 1: Visual Differentiation Study
* Image montage displays to help users understand leaf appearances
* Side-by-side comparisons of healthy and infected leaves
* Average image analysis to identify typical infection patterns
* Difference analysis between healthy and infected leaves
* Statistical analysis of image characteristics

### Business Requirement 2: Mildew Detection System
* Binary classification using Convolutional Neural Networks
* Image preprocessing and augmentation pipeline
* High accuracy model (>97% target)
* User-friendly interface for upload and prediction
* Batch processing capability for multiple images

## ML Business Case
* Binary classification model to detect powdery mildew in cherry leaf images
* Output:
   * Label: "Healthy" or "Powdery Mildew Detected"
   * Probability score for prediction
* Success Metrics:
   * Accuracy > 97%
   * Precision > 95%
   * Recall > 95%
* Training Data:
   * 2104 images split 80/20 train/validation
   * Balanced dataset
   * Data augmentation applied

## Dashboard Design

### Page 1: Project Summary
* Purpose: Provide project overview and context
* Contents:
   * Brief project description
   * Dataset overview
   * Business requirements
   * Quick start guide
* User Benefit: Understand project scope and capabilities

### Page 2: Leaf Visualizer
* Purpose: Address Business Requirement 1
* Contents:
   * Difference between average healthy and infected leaves
   * Image montage of both classes
   * Statistical analysis of features
   * Downloadable example images
* Visualizations:
   * Average image comparison with interpretation
   * Image montage with size selection
   * Distribution plots of key features
   * Side-by-side healthy vs infected examples

### Page 3: Mildew Detector
* Purpose: Address Business Requirement 2
* Contents:
   * Upload interface for leaf images
   * Prediction results display
   * Probability scores
   * Performance metrics
* Features:
   * Single and batch upload options
   * Clear success/failure indicators
   * Downloadable prediction reports
   * Model performance statistics

## Hypotheses and Validation

### Hypothesis 1: Visual Differentiation
* Null: There are no clear visual differences between healthy and infected leaves
* Alternative: Infected leaves show distinct patterns visible to the human eye
* Validation: Average image study and difference analysis shows clear patterns

### Hypothesis 2: ML Detection
* Null: ML cannot reliably detect mildew infection from leaf images
* Alternative: ML can detect mildew with >97% accuracy
* Validation: Model achieves >97% accuracy on validation set

## Project Development

### Data Collection
* Leaf images downloaded from Kaggle
* Organized into healthy/infected classes
* Split into training and validation sets
* Verification of image quality and labeling

### Model Development
* CNN architecture with transfer learning
* Data augmentation to prevent overfitting
* Hyperparameter optimization
* Performance evaluation on validation set

### Dashboard Implementation
* Streamlit-based web interface
* Interactive visualizations
* Real-time prediction capability
* User-friendly design

## Future Improvements
* Mobile app development
* Additional disease detection
* Integration with farm management systems
* Automated monitoring system