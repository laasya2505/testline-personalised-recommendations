import datetime
import json

def parse_date(date_str):
    """Convert string date to datetime object."""
    return datetime.datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f%z")

from datetime import datetime

def calculate_time_difference(start_time, end_time):
    """Calculate the time difference in minutes between two timestamps."""
    try:
        start = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
        end = datetime.fromisoformat(end_time.replace("Z", "+00:00"))
        return (end - start).total_seconds() / 60  # Convert to minutes
    except Exception as e:
        raise ValueError(f"Invalid timestamp format: {start_time} or {end_time}. Error: {e}")


def calculate_accuracy(correct, incorrect):
    """Calculate accuracy percentage."""
    total_attempted = correct + incorrect
    return round((correct / total_attempted) * 100, 2) if total_attempted > 0 else 0

data='/Users/srinivas/Desktop/testline/data/sample_historical_quiz.json'
def calculate_performance_metrics(data):
    """Calculate performance metrics from the data."""
    started_at = data.get("started_at")
    ended_at = data.get("ended_at")

    if not started_at or not ended_at:
        print("Warning: Missing 'started_at' or 'ended_at' in the data.")
        duration_minutes = None  # Set to None or a default value
    else:
        duration_minutes = calculate_time_difference(started_at, ended_at)

    performance = {
        "quiz_id": data.get("quiz_id", "N/A"),
        "score": data.get("score", 0),
        "accuracy": float(data.get("accuracy", "0%").strip('%')),
        "final_score": float(data.get("final_score", 0)),
        "duration_minutes": duration_minutes,
        "topic": data.get("topic", "Unknown")  # Default to "Unknown" if the topic is missing
    }
    return performance



file_path='/Users/srinivas/Desktop/testline/data/sample_historical_quiz.json'
def load_data(file_path):
    """Load JSON data from a file."""
    with open(file_path, "r") as file:
        data = json.load(file)
        if isinstance(data, list):
            return data
        return [data]


data='/Users/srinivas/Desktop/testline/data/sample_current_quiz.json'
def summarize_performance(data):
    """Summarize the performance of the user."""
    performance = calculate_performance_metrics(data)

    summary = {
        "Quiz ID": performance["quiz_id"],
        "Score": performance["score"],
        "Accuracy": f"{performance['accuracy']}%",
        "Final Score": performance["final_score"],
        "Duration (minutes)": (
            round(performance["duration_minutes"], 2) if performance["duration_minutes"] is not None else "N/A"
        ),
        "Topic": performance.get("topic", "Unknown")
    }
    return summary


sample_data = {
    "quiz_id": "123",
    "score": 85,
    "accuracy": "90%",
    "final_score": "85.5",
    "started_at": "2023-01-01T12:00:00.000+0000",
    "ended_at": "2023-01-01T12:30:00.000+0000"
}

print(calculate_performance_metrics(sample_data))

# Complete data
sample_data_complete = {
    "quiz_id": "123",
    "score": 85,
    "accuracy": "90%",
    "final_score": "85.5",
    "started_at": "2023-01-01T12:00:00.000+0000",
    "ended_at": "2023-01-01T12:30:00.000+0000",
    "topic": "Math"
}


print(summarize_performance(sample_data_complete))


