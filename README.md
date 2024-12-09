# ✉️ E-mail Tone Analyzer

This project is a Natural Language Processing (NLP) application designed to analyze email text for sentiment and formality. It leverages state-of-the-art models, including fine-tuned Large Language Models (LLMs), to provide insightful analysis. This repository includes the tools and processes for data preparation, model fine-tuning, evaluation, and deployment.

## Demo App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://emailanalyzer.streamlit.app)

Link to presentation: https://drive.google.com/file/d/1R88iLop4k_Jzgga7ahSq3VLD1_J2E7W4/view?usp=share_link
Dataset link: https://www.cs.cmu.edu/~enron/

## Introduction

The development of the **E-mail Tone Analyzer** is organized into three main phases:

### 1. Data Preparation and Labeling
- **Objective**: Build a robust dataset to train and evaluate the model.
- **Steps**:
  - Load email data from a tab-separated file or other structured formats.
  - Process raw text data, including cleaning and removing unnecessary columns.
  - Apply sentiment analysis to label emails as `positive`, `neutral`, or `negative` using pre-trained models like `cardiffnlp/twitter-roberta-base-sentiment`.
  - Introduce additional labeling for `formality`, classifying each email as `formal` or `informal` using a fine-tuned model or custom logic.
  - Map and clean labels to ensure consistency, such as merging variations of `Formal`/`Informal`.
  - Save the processed data for downstream tasks in CSV format.

### 2. Model Fine-Tuning and Application Development
- **Objective**: Optimize the model's performance and provide a user-friendly interface for real-time analysis.
- **Steps**:
  - **Fine-Tuning**:
    - Combine sentiment and formality labels to create a unified dataset for training.
    - Fine-tune the LLM on this dataset to improve its ability to detect nuanced email tones.
  - **Application Development**:
    - Develop a Python-based API function (`email_analyzer`) to interact with the fine-tuned LLM.
    - Configure generation parameters such as `temperature`, `top_p`, and `max_output_tokens` for controlled and meaningful responses.
    - Build an interactive application using **Streamlit** to allow users to input email text and receive instant tone analysis.

### 3. Evaluation and Validation
- **Objective**: Quantify the model's accuracy and reliability using rigorous metrics.
- **Steps**:
  - Construct a labeled evaluation dataset, representing various email styles and tones.
  - Use metrics such as:
    - **Precision**: How accurate are the positive predictions?
    - **Recall**: How many actual positives are correctly identified?
    - **F1 Score**: The harmonic mean of precision and recall.
    - **Confusion Matrix**: Evaluate true positives, false positives, true negatives, and false negatives.
    - **ROC-AUC Score**: Assess the model’s ability to distinguish between classes.
  - Generate detailed classification reports and visualize results to identify areas for improvement.

## Key Features
- **Sentiment Analysis**: Classifies email tone as positive, neutral, or negative.
- **Formality Detection**: Distinguishes between formal and informal emails.
- **Interactive Application**: Provides real-time analysis through an easy-to-use Streamlit app.
- **Comprehensive Metrics**: Evaluates the model’s performance using precision, recall, F1-score, and more.

## Future Work
- Enhance the model to detect additional tones, such as urgency or professionalism.
- Expand datasets with multilingual support for broader applicability.
- Integrate advanced visualizations in the Streamlit app for better user insights.

