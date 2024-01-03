import keys
import requests
from exercise_model import ExerciseModel
from sheety_logic import add_exercise


nutri_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
headers = {
    'x-app-id': keys.NUTRI_APP_ID,
    'x-app-key': keys.NUTRI_API_KEY
}
body = {
    'query': input("Tell me which exercises you did today: "),
    'gender': 'male',
    'age': 21,
    'weight_kg': 60,
    'height_cm': 169
}

response = requests.post(nutri_endpoint, headers=headers, data=body)
response.raise_for_status()
data = response.json()

exercises = [ExerciseModel(exerciseData=exercise) for exercise in data['exercises']]

for exercise in exercises:
    add_exercise(exercise)


