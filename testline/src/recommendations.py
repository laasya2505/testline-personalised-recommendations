import json
import pandas as pd
current_quiz='/Users/srinivas/Desktop/testline/data/sample_current_quiz.json'
def generate_recommendations(historical_performance, current_quiz):
    recommendations = []

    for performance in historical_performance:
        if performance["accuracy"] < 0.8:
            recommendations.append({
                "user_id": performance["user_id"],
                "message": "Focus on improving accuracy for better results in future quizzes.",
                "suggested_topic": current_quiz["quiz"]["topic"]
            })

        if performance["speed"] < 80:
            recommendations.append({
                "user_id": performance["user_id"],
                "message": "Try to increase your speed to answer more questions within the given time.",
                "suggested_topic": current_quiz["quiz"]["topic"]
            })

        if performance["incorrect_answers"] > 5:
            recommendations.append({
                "user_id": performance["user_id"],
                "message": f"Revise concepts from {current_quiz['quiz']['topic']} to reduce mistakes.",
                "suggested_topic": current_quiz["quiz"]["topic"]
            })
    
    return recommendations
accuracy_by_difficulty = pd.Series({
    'easy': 0.9,
    'medium': 0.55,
    'hard': 0.85
})
accuracy_by_time = pd.Series({
    'easy': 0.9,
    'medium': 0.55,
    'hard': 0.85
})
def define_persona(accuracy_by_time, accuracy_by_difficulty):
    """
    Define student persona based on accuracy patterns.
    """
    persona = {}
    print(accuracy_by_difficulty)  # Debug print statement

    # Safe access
    if accuracy_by_difficulty.get('hard', 0) > 0.8 and accuracy_by_difficulty.get('medium', 0) < 0.6:
        persona = "Confident Explorer"
    elif accuracy_by_time.max() > 0.9 and accuracy_by_time.min() < 0.5:
        persona = "Topic Specialist"
    else:
        persona = "Balanced Learner"
    return persona

if __name__ == "__main__":
    # Replace 'performance_analysis.json' and 'current_data.json' with your actual data file paths
    with open('/Users/srinivas/Desktop/testline/src/perfomance_analysis.json', 'r') as perf_file:
        historical_performance = json.load(perf_file)
    
    with open('/Users/srinivas/Desktop/testline/data/sample_current_quiz.json', 'r') as curr_file:
        current_quiz = json.load(curr_file)
    
    recommendations = generate_recommendations(historical_performance, current_quiz)
    print(json.dumps(recommendations, indent=2))
