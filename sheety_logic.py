import requests
from datetime import datetime
from exercise_model import ExerciseModel
import keys

sheety_post_endpoint = 'https://api.sheety.co/9d7e9fe17e6cd09cf7489b2c0737933d/workoutTracker/workouts'
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {keys.SHEETY_AUTH_KEY}'
}

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

def add_exercise(exercise: ExerciseModel):
    body = {
        'workout': {
            'date': today_date,
            'time': now_time,
            'exercise': exercise.name.title(),
            'duration': exercise.duration_min,
            'calories': exercise.calories,
        }
    }

    response = requests.post(sheety_post_endpoint, headers=headers, json=body)
    response.raise_for_status()