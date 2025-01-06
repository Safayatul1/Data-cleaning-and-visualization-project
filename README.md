# Data Cleaning and Visualization Project

## Overview
This project demonstrates data cleaning, manipulation, and visualization techniques using Python. The dataset contains metrics related to exercise routines, such as duration, pulse rate, maximum pulse, and calories burned. The goal is to clean the data, uncover patterns, and present insights through visualizations.

---

## Features
1. **Data Cleaning**:
   - Filled missing values in the `Calories` column using the mode.
   - Standardized the `Date` column to a consistent `datetime` format.
   - Removed duplicate entries to ensure data integrity.
   - Capped extreme values in the `Duration` column to handle outliers.

2. **Data Visualization**:
   - Scatter plots for analyzing relationships:
     - `Duration` vs. `Calories`
     - `Pulse` vs. `Calories`
   - Correlation heatmap to identify key variable relationships.
   - Line plots to explore trends over time.

3. **Polynomial Regression**:
   - Modeled the non-linear relationship between pulse rate and calories burned.
   - Visualized the regression fit and evaluated model performance using the R² score.

---

## Technologies Used
- **Pandas**: Data cleaning and manipulation.
- **NumPy**: Numerical operations.
- **Matplotlib**: Data visualization.
- **Seaborn**: Advanced visualizations.
- **Scikit-learn**: Polynomial regression and model evaluation.

---

## Installation
1. Clone the repository or download the files.
   ```bash
   git clone https://github.com/your-username/data-cleaning-visualization.git
   ```
2. Navigate to the project directory.
   ```bash
   cd data-cleaning-visualization
   ```
3. Install the required dependencies.
   ```bash
   pip install -r requirements.txt
   ```

---

## How to Run
1. Place the dataset file (`data.csv`) in the project directory.
2. Run the script:
   ```bash
   python data_analysis_code.py
   ```
3. View the generated visualizations and console outputs.

---

## Outputs
1. **Visualizations**:
   - Scatter plots and line charts to explore relationships and trends.
   - Correlation heatmap for variable analysis.
   - Polynomial regression fit to uncover non-linear relationships.
2. **Insights**:
   - Identified key drivers of calorie burn (pulse rate and intensity).
   - Highlighted trends in exercise metrics over time.

---

## Key Insights
- **Intensity Matters**: Higher pulse rates are strongly correlated with increased calorie burn.
- **Optimal Range**: Polynomial regression suggests diminishing returns at extreme pulse rates, indicating an optimal range for efficiency.
- **Duration vs. Calories**: Duration alone is a weaker predictor of calorie burn compared to pulse rate.

---

## Contribution
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push to your branch.
4. Create a pull request for review.

---

## License
This project is licensed under the MIT License. Feel free to use, modify, and share.

