🚨 911 Calls Data Analysis (MontcoAlert)

This project analyzes 911 emergency calls data from Montgomery County, PA, sourced from Kaggle. The objective is to explore trends in emergency calls, identify peak hours, and visualize geographical distributions.

📃 Dataset Information

Source: MontcoAlert 911 Calls on Kaggle

Records: Over 260,000 emergency calls

Key Columns:

lat, lng → Geographical location of the call

desc → Description of the emergency

zip → ZIP code where the call was placed

title → Category and specific reason for the call

timeStamp → Date and time of the emergency call

twp → Township where the call originated

addr → Address details

📊 Key Insights

Peak call hours: Emergency calls are most frequent during work hours (8 AM - 6 PM).

Most common emergency type: Medical emergencies make up the highest percentage of calls.

Geographical patterns: Certain townships experience more emergency calls than others.

🚀 Project Structure

📂 911-calls-analysis/
   ├️ 📄 README.md  (Project documentation)
   ├️ 📂 data/  (Sample dataset files, avoid large raw files)
   ├️ 📂 notebooks/  (Jupyter notebooks for EDA & visualization)
   ├️ 📄 analysis.py  (Python script for analysis)
   ├️ 📂 plots/  (Images and graphs from analysis)
   ├️ 📄 requirements.txt  (List of dependencies)
   └️ 📄 .gitignore  (To exclude unnecessary files)

🛠️ How to Run the Project

1. Install Dependencies

pip install -r requirements.txt

2. Run Analysis

Jupyter Notebook:

jupyter notebook

Python Script:

python analysis.py

📝 Libraries Used

Pandas for data manipulation

Plotly for interactive visualization

NumPy for numerical computations

📚 License

This project is licensed under the MIT License. Feel free to use and modify it with attribution.

🔎 Additional Notes

Data preprocessing steps include handling missing values and extracting time-based features.

Further improvements can involve predictive modeling to forecast emergency call trends.

📈 Happy Analyzing! 💡

