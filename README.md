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

### Hypotheses and Validation
* Hypothesis 1: Powdery mildew creates visible white spots or patches on cherry leaves
  * Validation: Image visualization study comparing healthy and infected leaves
  
* Hypothesis 2: Machine learning can detect subtle patterns that differentiate healthy from infected leaves
  * Validation: Development and evaluation of an image classification model

## Project Structure
```
cherry-leaf-detection/
│
├── app_pages/            # Streamlit pages
│   ├── home.py
│   ├── visualization.py
│   ├── prediction.py
│   └── about.py
│
├── src/                  # Source code
│   ├── data_management.py
│   ├── machine_learning/
│   │   └── predictive_analysis.py
│   └── visualization.py
│
├── notebooks/           # Jupyter notebooks
│   ├── data_collection.ipynb
│   ├── ml_modeling.ipynb
│   └── data_analysis.ipynb
│
├── requirements.txt     # Project dependencies
├── Procfile            # Heroku deployment
├── setup.sh            # Setup configuration
├── runtime.txt         # Python runtime
└── README.md
```

## ML Business Case
### Objective
Create a binary classification model to detect the presence of powdery mildew in cherry leaf images.

### Model Output
* Binary output: "Healthy" or "Powdery Mildew Detected"
* Confidence level for the prediction

### Success Metrics
* Accuracy score > 97%
* Precision and recall scores > 95%
* Low false positive rate to minimize incorrect diagnoses

### Training Data
* Balanced dataset of healthy and infected cherry leaf images
* 80-20 train-validation split
* Data augmentation techniques applied to prevent overfitting

## Dashboard Design
### Home Page
* Project summary and background
* Key facts about powdery mildew in cherry leaves
* Quick links to prediction and visualization tools

### Visualization Page
* Side-by-side comparison of healthy vs infected leaves
* Statistical analysis of leaf characteristics
* Visual aids to help understand infection patterns

### Prediction Page
* Image upload functionality
* Real-time prediction results
* Confidence scores display
* Image preprocessing information

### About Page
* Project information
* Dataset details
* Model performance metrics
* Usage instructions

## Technical Details
### Image Classification Model
* CNN architecture optimized for leaf disease detection
* Image preprocessing pipeline
* Data augmentation strategy
* Model evaluation metrics

### Deployment
* Streamlit cloud deployment
* Version control via GitHub
* Continuous integration setup

## Future Improvements
* Expand dataset with more diverse examples
* Implement multi-class classification for different diseases
* Add mobile support for field diagnosis
* Integrate weather data for predictive analytics
