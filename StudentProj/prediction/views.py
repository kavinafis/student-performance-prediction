from django.shortcuts import render
import joblib
import numpy as np
from .models import Student

model = joblib.load("StudentProj/prediction/model.pkl")


def predict_performance(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = int(request.POST.get("age"))
        study_hours = float(request.POST.get("study_hours"))
        previous_scores = float(request.POST.get("previous_scores"))

        prediction = model.predict(np.array([[study_hours, previous_scores]]))[0]

        student = Student(name=name, age=age, study_hours=study_hours, previous_scores=previous_scores)
        student.save()

        return render(request, "result.html", {"student": student, "prediction": round(prediction, 2)})

    return render(request, "index.html")
