import json
import pandas as pd
historical_data='/Users/srinivas/Desktop/testline/data/sample_historical_quiz.json'
def analyze_performance(historical_data):
    results = []
    for entry in historical_data:
        performance = {
            "user_id": entry["user_id"],
            "quiz_id": entry["quiz_id"],
            "score": entry["score"],
            "accuracy": float(entry["accuracy"].strip('%')) / 100,
            "speed": int(entry["speed"]),
            "final_score": float(entry["final_score"]),
            "correct_answers": entry["correct_answers"],
            "incorrect_answers": entry["incorrect_answers"],
            "total_questions": entry["total_questions"],
            "negative_score": float(entry["negative_score"]),
            "duration": entry["duration"],
            "better_than": entry["better_than"],
            "rank_text": entry["rank_text"]
        }
        results.append(performance)
    
    return results
data='/Users/srinivas/Desktop/testline/data/sample_current_quiz.json'
def calculate_accuracy(data, group_by):
    """Calculate the accuracy by grouping data."""
    # Convert the list of dictionaries to a DataFrame if it's a list
    if isinstance(data, list):
        data = pd.DataFrame(data)
    
    # Ensure the DataFrame contains the necessary columns
    if 'correct_answers' not in data.columns:
        raise ValueError("The DataFrame does not contain 'correct_answers' column.")
    
    # Group by the specified column and calculate accuracy
    grouped = data.groupby(group_by).apply(lambda x: (x['correct_answers'].sum() / len(x)))
    return grouped
historical_data='/Users/srinivas/Desktop/testline/data/sample_historical_quiz.json'
def analyze_trends(historical_data):
    """Analyze trends in historical data by quiz_id."""
    # Convert the list to a DataFrame if it's a list
    if isinstance(historical_data, list):
        historical_data = pd.DataFrame(historical_data)
    
    # Ensure that the DataFrame contains the required columns
    if 'quiz_id' not in historical_data.columns or 'score' not in historical_data.columns:
        raise ValueError("The DataFrame must contain 'quiz_id' and 'score' columns.")
    
    # Perform the groupby operation
    trends = historical_data.groupby('quiz_id')['score'].mean().reset_index()
    return trends

def identify_weak_areas(historical_data):
    """
    Identify weak topics and difficulty levels.
    """
    accuracy_by_time = calculate_accuracy(historical_data, 'duration')
    accuracy_by_difficulty = calculate_accuracy(historical_data, 'better_than')
    weak_topics = accuracy_by_time[accuracy_by_time < 0.6]
    weak_difficulty = accuracy_by_difficulty[accuracy_by_difficulty < 0.6]
    
    print("Weak Topics:", weak_topics)  # Debugging
    print("Weak Difficulty Levels:", weak_difficulty) 
    return weak_topics, weak_difficulty
if __name__ == "__main__":
    # Replace 'historical_data.json' with your actual data file path
    with open('/Users/srinivas/Desktop/testline/data/sample_historical_quiz.json', 'r') as file:
        historical_data = json.load(file)
    
    performance_analysis = analyze_performance(historical_data)
    print(json.dumps(performance_analysis, indent=2))
