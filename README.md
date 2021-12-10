## Lending Club | Predicting Applicant Loan
# Final Project / Northwestern University Data Science

# Project Summary:
Lending Club is America's largest online credit marketplace, and the first 
marketplace bank connecting borrowers and investors. We wanted to 
explore the factors going into their  applicant grade (risk) assessments.
Lending Club had two data files (loan applicants and approved applicants / 
loan status) covering 2007 to 2018 which we downloaded from Kaggle.  

Since there were limited common fields / comparability between the files 
we focused our efforts on predicting future applicant grades (risk) based on
the grades that Lending Club had assigned to approved loans and resolved
loans (A-G).

Our ML model makes grade (risk) predictions for new prospective 
borrowers based on various borrower criteria they input on our website.

DATA: https://www.kaggle.com/rikdifos/credit-card-approval-prediction

# Understanding the Data / ETL:

The downloaded database was large and slow to work with, and 
included information that did not contribute to our model

# Tools Used: 

Jupyter Notebook, Python Pandas, Numpy

# Database: 

**Initial database: ** 2.2m records, 151 columns

**Final database: ** 824k records, 8 columns

# Activities:

**Clean-up**

-Drop non-essential and duplicate columns 

-Drop records including NaN values


**Selection**

-Drop records for open / active loans (we only included 
loans that were either “fully paid” or “charged off”) 

-Drop loans for people employed more than 10 years


**Conversion / Manipulation**

-Convert certain columns from string to binary values 

-Convert date ranges to integers


# Training our ML Model:

To predict a potential borrower’s loan approval grade (risk) from 
inputs entered on our website

# Tools Used: 

Jupyter Notebook, Python Pandas, TensorFlow, SkLearn, Numpy, Pickle


# Modeling criteria:  
1. Employment Length (10 years or less)
2. FICO Score (Range High) 
3. Application Type (Joint or Individual)
4. Income (Annual)
5. Loan Amount (USD)
6. Term (36 or 60 months)
7. Loan Status (Fully Paid or Charged Off) 


# Models considered:  

We tested several different models (Random Forest, Logistic Regression, Neural Network) to find which would generate the best results 


# Website

**Tools Used: ** HTML, CSS, JS, Tableau, Flask, Bootstrap

**Model Used:**  Random Forest


# Functionality:

-Predict the user’s loan grade based on their inputs to our model

-Allow the user to better understand grading criteria and 
outcomes by providing visualizations of historical grading data 

-Allow the user to see the relationship between the historical 
grading data and loan repayment status 


# Considerations – Learnings:

**Dataset Choice**

-There was no way to compare the two initial datasets related
to approved vs. rejected loans

-Incomplete data dictionary / column definitions - we may not
have included the best columns  

-Set had inconsistent sorting / categorizations (e.g. date 
ranges for length of employment)

-Set was very large for this type of project and our hardware 
and difficult  to work with related to modeling (17 hours), we 
should have looked at a smaller number of years 


**Modeling**

-Have a more rigorous initial discussion of which method / 
model would be the best approach

-More initial discussion about how to work with such a large 
dataset and related limitations

-Did we overtrain our models, did it memorize our data

-Should we have used a live server instead of our local 
machines


**Website**

-Making sure we translated all our data back into “plain 
English” from binary code

-Making sure that all the different web components 
effectively communicated with each other 


# Generalizations about our Model:

Our model seemed to work well predicting grades, compared to past data
but ... we didn’t understand why Lending Club was approving loans for 
certain grades (E, F, G) where the historical default rates were over 40%


