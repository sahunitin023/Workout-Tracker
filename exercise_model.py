class ExerciseModel:

    def __init__(self, exerciseData):
        self.name = exerciseData['name']
        self.duration_min = exerciseData['duration_min']
        self.calories = exerciseData['nf_calories']
