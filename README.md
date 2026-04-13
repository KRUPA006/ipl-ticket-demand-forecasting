# IPL Ticket Demand Forecasting

## Project Overview
This project explores the factors that influence ticket sales for IPL matches using a synthetic dataset. The goal was to understand what drives attendance and to build a simple model that can estimate ticket demand based on match conditions.

---

## Problem Statement
For large sporting events like IPL matches, estimating ticket demand in advance can help organizers plan better — from scheduling matches to managing stadium capacity and resources. This project simulates that scenario and analyzes how different variables impact ticket sales.

---

## Approach
The project was carried out in the following steps:

- Created a synthetic dataset representing IPL match conditions  
- Performed basic data cleaning and validation  
- Explored the data using summary statistics and visualizations  
- Identified patterns between features and ticket sales  
- Built a linear regression model to predict ticket demand  
- Evaluated the model using standard performance metrics  

---

## Key Insights
- Weekend matches generally attract higher attendance than weekday matches  
- Matches involving more popular teams tend to sell more tickets  
- Higher combined team popularity strongly correlates with ticket sales  
- Weather conditions have some impact, but less compared to other factors  

---

## Model Performance
The regression model was evaluated using:

- Mean Absolute Error (MAE)  
- R² Score  

These metrics help measure how accurately the model predicts ticket sales based on the given inputs.

---

## Sample Prediction
For a high-demand scenario (popular teams, good weather, weekend), the model predicts approximately **50,000+ ticket sales**.

---

## Limitations
- The dataset is synthetically generated and may not reflect real-world IPL data  
- Some important factors like ticket pricing, team form, and location are not included  

---

## Future Improvements
- Use real IPL or sports datasets  
- Include additional features such as pricing, team rankings, and venue details  
- Build an interactive dashboard for better visualization  

---

## Tools and Technologies
- Python  
- Pandas  
- Matplotlib and Seaborn  
- Scikit-learn  
- Jupyter Notebook