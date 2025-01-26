import pandas as pd
student_data='/Users/srinivas/Desktop/testline/data/sample_historical_quiz.json'
def analyze_student_persona(student_data):
    """
    Analyze and define the student persona based on patterns in the data.
    Highlight specific strengths and weaknesses with creative labels or insights.
    
    Args:
        student_data (pd.DataFrame): DataFrame containing student performance data.
                                     Expected columns: ['topic', 'score', 'accuracy', 'duration_minutes']

    Returns:
        dict: A dictionary containing the student persona, strengths, and weaknesses.
    """
    # Step 1: Define creative labels based on performance thresholds
    persona = {}
    strengths = []
    weaknesses = []
    
    # Check the average score and accuracy
    avg_score = student_data['score'].mean()
    avg_accuracy = student_data['accuracy'].mean()
    
    # Assign persona based on average performance
    if avg_score >= 85:
        persona['label'] = "High Achiever"
        persona['description'] = "Excels in academics and consistently delivers strong results."
    elif 70 <= avg_score < 85:
        persona['label'] = "Balanced Learner"
        persona['description'] = "Performs well across topics but has room for growth in certain areas."
    else:
        persona['label'] = "Steady Improver"
        persona['description'] = "Working steadily to improve performance with focused efforts."

    # Step 2: Identify strengths and weaknesses by topic
    avg_performance_by_topic = student_data.groupby('topic').agg({
        'score': 'mean',
        'accuracy': 'mean',
    })
    
    for topic, row in avg_performance_by_topic.iterrows():
        if row['score'] >= 85 and row['accuracy'] >= 90:
            strengths.append(f"{topic}: 'Master of Concepts'")
        elif row['score'] < 70 or row['accuracy'] < 75:
            weaknesses.append(f"{topic}: 'Needs Reinforcement'")
    
    # If no weaknesses are found, add a generic insight
    if not weaknesses:
        weaknesses.append("Keep pushing the limits! No major weaknesses identified.")
    
    # Step 3: Combine persona, strengths, and weaknesses
    student_analysis = {
        "persona": persona,
        "strengths": strengths,
        "weaknesses": weaknesses,
    }
    
    return student_analysis

# Sample Data
sample_data = pd.DataFrame([
    {'topic': 'biology', 'score': 90, 'accuracy': 90.0, 'duration_minutes': 30.0},
    {'topic': 'zoology', 'score': 95, 'accuracy': 95.0, 'duration_minutes': 25.0},
    {'topic': 'physics', 'score': 70, 'accuracy': 65.0, 'duration_minutes': 20.0},
    {'topic': 'chemistry', 'score': 75, 'accuracy': 70.0, 'duration_minutes': 15.0},
])

# Analyze Student Persona
result = analyze_student_persona(sample_data)

# Display Result
print("Student Persona:")
print(result['persona'])
print("\nStrengths:")
print("\n".join(result['strengths']))
print("\nWeaknesses:")
print("\n".join(result['weaknesses']))
