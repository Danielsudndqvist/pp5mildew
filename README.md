# Cherry Leaf Mildew Detection

## Project Overview
Detection of powdery mildew in cherry leaves using machine learning.

## Business Requirements
As defined by the client's needs:

1. As a farmer
   I want to visually differentiate healthy cherry leaves from infected ones
   So that I can quickly identify potential mildew infections in my orchards

2. As a farm manager
   I want to receive predictions about leaf health from leaf images
   So that I can make automated assessments of tree health status

## Rationale to Map Business Requirements to Data Science Tasks

* Business Requirement 1: Visual Differentiation Study
  * Average image study to identify typical infection patterns
  * Image montage to understand variability in healthy/infected leaves
  * Side-by-side comparison tool for comparative analysis
  * Statistical analysis of image characteristics

* Business Requirement 2: Predictive Classification
  * Binary classification model (healthy vs infected)
  * Image preprocessing pipeline for standardization
  * Model evaluation metrics focused on high accuracy
  * User-friendly interface for uploading and analyzing new images

## Dataset
* Source: Kaggle Cherry Leaves Dataset
* Contents: 2104 images total
  * Healthy Leaves: 1052 images
  * Infected Leaves: 1052 images
* Train-Test Split:
  * Training: 1682 images (80%)
  * Validation: 422 images (20%)

## ML Business Case
* Problem Type: Binary Classification
* Success Metrics:
  * Accuracy > 97%
  * Precision > 95%
  * Recall > 95%
* Output:
  * Label: "Healthy" or "Powdery Mildew Detected"
  * Probability score
* Model Features:
  * Processed leaf images (standardized size and format)
  * Image augmentation for training robustness
* Training Data:
  * Balanced dataset of healthy and infected leaves
  * Augmentation techniques:
    * Rotation
    * Horizontal flip
    * Brightness adjustment

## Dashboard Design

### Page 1: Project Summary
* Project overview and background
* Powdery mildew information
* Project dataset information
* Link to project repository
* Quick navigation to tools

### Page 2: Leaf Visualizer
* **Purpose**: Answers Business Requirement 1
* **Contents**:
  * Average image comparison (healthy vs infected)
  * Image variability analysis
  * Difference between average healthy and infected leaves
  * Image montage for both classes
  * Statistical analysis of image features
* **User Actions**:
  * Toggle between different visualization types
  * Select number of images for montage
* **Interpretations**: Clear text explanations for each visualization

### Page 3: Mildew Detector
* **Purpose**: Answers Business Requirement 2
* **Contents**:
  * Image upload interface
  * Prediction results display
  * Confidence score visualization
  * Model performance metrics
* **User Actions**:
  * Upload new images
  * Batch process multiple images
  * Download prediction reports
* **Interpretations**: 
  * Clear prediction results
  * Reliability indicators
  * Usage instructions

### Page 4: Project Hypotheses and Validation
* Hypothesis 1: Visible Patterns
  * Null: No visible differences exist between healthy and infected leaves
  * Alternative: Infected leaves show distinct visual patterns
  * Validation: Image analysis results
* Hypothesis 2: ML Detection
  * Null: ML cannot reliably detect mildew infection
  * Alternative: ML can detect mildew with >97% accuracy
  * Validation: Model performance metrics

## Technical Requirements
* Python 3.8+
* Key Dependencies:
  * streamlit
  * tensorflow
  * opencv-python
  * numpy
  * pandas

## Development Workflow
1. Set up development environment
2. Data collection and preparation
3. EDA and visualization
4. Model development and training
5. Dashboard implementation
6. Testing and validation
7. Deployment

## Deployment
* Platform: Heroku
* URL: [Your-App-URL]
* Deployment Files:
  * Procfile
  * requirements.txt
  * runtime.txt
  * setup.sh