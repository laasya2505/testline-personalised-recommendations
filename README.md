

# 📊 Student Persona Analysis and Insights  

This project provides a comprehensive framework to analyze student performance data, identify personalized personas, highlight specific strengths, and detect areas for improvement with creative labels and actionable insights.  



## 🌟 Features  

- **Student Persona Analysis**  
  Categorizes students into personas like "High Achiever," "Balanced Learner," or "Steady Improver."  
- **Strength Identification**  
  Pinpoints topics or areas where students excel, offering creative and positive feedback.  
- **Weakness Detection**  
  Highlights areas for improvement with targeted and actionable recommendations.  
- **Customizable Metrics**  
  Allows customization of score thresholds, accuracy levels, and other parameters for a tailored analysis.  


## 🗂️ Project Structure  

```
|-- testline-performance/
    |-- data/
        |-- sample_current_quiz.json  
        |-- sample_historical_quiz.json  
    |-- src/
        |-- analyze_performance.py
        |-- recommendations.py
        |-- utils.py
        |-- dash1.py
        |-- persona.py
    |-- README.md


```  



## 🚀 Installation  

Follow these steps to set up and run the project locally:  

1. **Clone the Repository**  
   ```bash  
   git clone https://github.com/laasya2505/testline-personalised-recommendations.git  
   cd testline-personalised-recommendations 
   ```  

2. **Add Your Data**  
   Replace or edit the sample dataset in the `data` folder to include your own student performance data. Ensure it includes columns like `topic`, `score`, `accuracy`, and `duration_minutes`.  



## 🛠️ Usage  

1. **Run the Dashboard**  
   Use Streamlit to launch the interactive dashboard:  
   ```bash  
   streamlit run src/dashboard.py  
   ```  

2. **Analyze Results**  
   View outputs directly on the dashboard, including:  
   - Defined student personas  
   - Key strengths and weaknesses  
   - Recommendations  




## 📜 License  

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.  






