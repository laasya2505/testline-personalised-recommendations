# testline-personalised-recommendations
Student Persona Analysis and Insights
This project leverages student performance data to define personalized student personas, highlight strengths, and identify weaknesses with creative labels and actionable insights. By analyzing patterns in the data, this tool offers a comprehensive view of individual learning styles and areas for improvement.

Features
Student Persona Analysis: Categorizes students into personas like "High Achiever," "Balanced Learner," or "Steady Improver."
Strengths Identification: Highlights topics where students excel with creative insights.
Weakness Detection: Identifies areas that need improvement with targeted recommendations.
Customizable Performance Metrics: Easily adjust thresholds for scores and accuracy to match specific use cases.
Project Structure
src/: Contains the core analysis scripts and helper functions.
analyze_performance.py: Main script for calculating student personas, strengths, and weaknesses.
dash1.py: Streamlit-based dashboard for visualizing insights and recommendations.
recommendations.py: Gives recommendations
utils.py: Calculates performance metrics
data/: Sample datasets for testing and demonstration purposes.
README.md: Project documentation.

Installation
Clone the repository:
git clone https://github.com/laasya2505/testline-personalised-recommendations.git
cd testline-personalised-recommendations

Usage
Add your student performance data in a CSV format with columns like topic, score, accuracy, and duration_minutes.
Run the analysis script or launch the Streamlit dashboard:
streamlit run src/dash1.py
View the output, which includes:
Defined student personas
Strengths and weaknesses

License
This project is licensed under the MIT License. See the LICENSE file for details.


