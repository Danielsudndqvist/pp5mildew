# Cherry Leaf Mildew Detection

## Business Understanding

### Dataset Content
* The dataset contains images of cherry leaves divided into two classes:
   * Healthy cherry leaves
   * Cherry leaves infected with powdery mildew
* The dataset was sourced from Kaggle and contains 2104 images of cherry leaves
   * Training set: approximately 1682 images (80% of the dataset)
   * Validation set: approximately 422 images (20% of the dataset)

### Business Requirements
1. The client is interested in conducting a study to visually differentiate between healthy and powdery mildew infected cherry leaves.
   * Success Criteria: Create a visual analysis tool that highlights the differences between healthy and infected leaves
2. The client wants to predict if a cherry leaf is healthy or contains powdery mildew.
   * Success Criteria: Create a ML model that accurately predicts the condition of a cherry leaf with at least 97% accuracy

### User Stories
1. As a farmer
   I want to visually differentiate healthy cherry leaves from infected ones
   So that I can identify infected trees early and prevent disease spread

2. As a farm manager
   I want to receive predictions about leaf health from leaf images
   So that I can make quick decisions about treatment and crop management

3. As an agricultural technician
   I want to understand the visual patterns of mildew infection
   So that I can train field workers on early detection

4. As a quality control specialist
   I want to batch process multiple leaf images
   So that I can efficiently screen large numbers of samples

### Rationale to Map Business Requirements to ML Tasks

1. Visual Difference Analysis
   * Purpose: Enable clear identification of infection patterns
   * Implementation: 
     - Average image comparison shows typical infection characteristics
     - Difference highlighting reveals key distinguishing features
     - Image montage provides multiple examples for pattern recognition
   * Business Value:
     - Helps train staff in visual inspection
     - Enables early detection of infection
     - Supports quality control processes

2. Automated Detection System
   * Purpose: Provide quick, accurate leaf health assessment
   * Implementation:
     - CNN-based binary classification
     - High accuracy model (>97%)
     - Confidence score for predictions
   * Business Value:
     - Reduces inspection time
     - Ensures consistent assessment
     - Enables large-scale screening

## Dashboard Design

### Page 1: Project Summary
* Purpose: Provide project overview and context
* Contents:
   * Brief project description
   * Dataset information
   * Business requirements
   * Quick start guide
* Business Requirement Mapping: Provides context for both requirements

### Page 2: Leaf Visualizer
* Purpose: Address Business Requirement 1
* Contents:
   * Side-by-side comparison of healthy vs infected leaves
   * Average image analysis
   * Difference highlight visualization
   * Statistical analysis of features
* Interpretation:
   * Clear explanation of visual patterns
   * Highlight of key differences
   * Guidance on identifying infection

### Page 3: Mildew Detector
* Purpose: Address Business Requirement 2
* Contents:
   * Image upload interface
   * Prediction results with confidence scores
   * Batch processing capability
   * Model performance metrics
* Interpretation:
   * Clear prediction results
   * Confidence level explanation
   * Model performance context

## ML Business Case
* Type: Binary Classification
* Objective: Predict whether a cherry leaf is healthy or infected with powdery mildew
* Success Metrics:
   * Accuracy > 97%
   * Precision > 95%
   * Recall > 95%
* Model Output:
   * Label: "Healthy" or "Powdery Mildew Detected"
   * Probability score
* Training Data:
   * 2104 images split 80/20
   * Balanced classes
   * Data augmentation applied

## Hypotheses and Validation
* Hypothesis 1: Powdery mildew creates visible white spots or patches on cherry leaves
   * Validation: Image visualization study comparing healthy and infected leaves
* Hypothesis 2: Machine learning can detect subtle patterns that differentiate healthy from infected leaves
   * Validation: Development and evaluation of an image classification model

## Technical Details
* Platform: Streamlit
* Model: CNN with transfer learning
* Deployment: Heroku
* Libraries: TensorFlow, OpenCV, Streamlit