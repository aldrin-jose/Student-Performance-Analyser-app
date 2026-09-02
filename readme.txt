Student Performance & Exam Outcome Predictor

The Student Performance & Exam Outcome Predictor is an intelligent web and mobile application designed to evaluate a student's academic standing and predict their probability of passing or failing an upcoming examination. By capturing key daily habits—such as daily study hours, historical academic results, and sleep duration—and evaluating them against a trained Machine Learning model sourced from Kaggle datasets, the application delivers instant, data-driven predictions alongside personalized behavioral insights.

Input Parameters: Users fill out a concise onboarding questionnaire covering primary academic indicators:

Study Duration: Average hours dedicated to independent study daily.

Prior Academic Performance: Percentage scored in previous exams.

Sleep & Well-being: Average nightly sleep duration.

Secondary Variables (Optional): Class attendance percentage, tutoring sessions, and extracurricular involvement.

Feature Engineering: Inputs are normalized using standard scaling techniques matching the schema derived from Kaggle's Student Performance Dataset (e.g., standardizing ranges for continuous variables like hours and percentages).
Model Training: Trained on historical Kaggle student data containing labeled outcomes (Pass vs. Fail or raw target grades mapped to threshold pass marks).

Algorithm: Implements classification models such as Logistic Regression (for baseline interpretability) or Random Forest / XGBoost (for high non-linear prediction accuracy).

Prediction Engine: Outputs both a binary classification (Pass / Fail) and a confidence score representing the probability distribution (e.g., 78% Likelihood of Passing).
Instant Risk Assessment: Generates an immediate prediction result upon questionnaire submission.

Feature Importance Insights: Identifies which habits are contributing most negatively or positively to the predicted outcome (e.g., highlighting that sleep deprivation lowers performance despite high study hours).

Interactive Scenario Simulator: Allows students to adjust variables dynamically (e.g., "What if I increase study time from 2 to 4 hours?") to visualize how habit changes impact their pass probability.
IF YOU WANT TO ADD CONSTRAINTS I HAVE UPLOADED FILES ABOVE SO DEVELOPER CAN MODIFY IT ACCORDINGLY.ORELSE TO USE THE APP JUST DOWNLOAD THE ZIP FILE AND OPEN IT WITH LOCAL HOST.FOR BUILTING TO A STANDALONE APP I HAVE ADDED FLUTTER LIBRARIES TOO.

Target Audience & Impact

Students: Serves as a diagnostic tool to build realistic study routines and spot potential academic risks early in a semester.

Educators & Counselors: Provides a baseline monitoring system to identify at-risk students who need targeted academic support.
