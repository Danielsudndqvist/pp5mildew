# Cherry Leaf Mildew Detection

## Dataset Content
* The dataset contains 2104 images of cherry leaves:
   * 1052 healthy leaves
   * 1052 leaves infected with powdery mildew
* Dataset split:
   * Training: 1682 images (80%)
   * Validation: 422 images (20%)

## Business Requirements

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

3. As a quality control specialist
   I want to batch process multiple leaf images
   So that I can efficiently screen large numbers of samples

4. As a farm training coordinator
   I want to see clear visual examples of leaf infections
   So that I can train new staff on disease identification

### Rationale to Map Business Requirements to ML Tasks

1. Visual Study Requirement:
   * Image montage creation for visual comparison
   * Statistical analysis of image characteristics
   * Average image computation for both classes
   * Side-by-side comparison tools
   * Rationale: Enables clear understanding of visual infection markers

2. Automated Detection Requirement:
   * Binary classification model development
   * Image preprocessing pipeline
   * Model training with data augmentation
   * Performance metrics tracking
   * Rationale: Provides fast, accurate disease detection

## Dashboard Design

### Page 1: Project Summary
* Purpose: Provide overview of project goals and features
* Contents:
   * Project background
   * Dataset information
   * Model performance metrics
   * Quick start guide
* Business Requirement Mapping: Introduces both visual analysis and prediction capabilities

### Page 2: Leaf Visualizer
* Purpose: Address Business Requirement 1
* Contents:
   * Side-by-side leaf comparison
   * Image montage display
   * Statistical analysis
   * Feature distribution plots
* Interpretation: Each visualization includes clear explanation of patterns and findings

### Page 3: Mildew Detector
* Purpose: Address Business Requirement 2
* Contents:
   * Image upload interface
   * Real-time prediction results
   * Confidence scores
   * Treatment recommendations
* Features: Clear presentation of model predictions and appropriate actions

## ML Business Case
* Type: Binary Classification
* Success Metrics:
   * Accuracy > 97%
   * Precision > 95%
   * Recall > 95%
* Training Data:
   * 2104 images split 80/20
   * Balanced dataset
   * Data augmentation applied

## Hypotheses and Validation
* Hypothesis 1: Visual Differentiation
   * Null: No clear visual differences exist
   * Alternative: Infected leaves show distinct patterns
   * Validation: Image montage and statistical analysis

* Hypothesis 2: ML Detection
   * Null: ML cannot reliably detect infection
   * Alternative: ML can detect with >97% accuracy
   * Validation: Model performance metrics

## Project Development Lifecycle
1. Data Collection and Verification
2. Exploratory Data Analysis
3. Model Development and Training
4. Dashboard Implementation
5. Testing and Validation
6. Deployment

## Features and Tools Used
* Image Analysis:
   * Average image comparison
   * Statistical visualization
   * Feature distribution analysis

* ML Implementation:
   * TensorFlow/Keras model
   * Data augmentation
   * Cross-validation

* User Interface:
   * Streamlit dashboard
   * Interactive visualizations
   * Batch processing capability

## Future Improvements
* Mobile app development
* Additional disease detection
* Integration with farm management systems
* Automated monitoring system

## Credits
* Dataset sourced from Kaggle
* Code Institute project template
* Streamlit documentation