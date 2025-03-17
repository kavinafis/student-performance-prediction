from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def predict(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        age = data.get('age')
        study_hours = data.get('study_hours')
        previous_scores = data.get('previous_scores')

        # Implement your prediction logic here
        predicted_score = (study_hours * 10) + (previous_scores * 0.5)  # Example logic
        notification_message = f'Prediction for {name} with age {age} is successful! Predicted score: {predicted_score}'
        
        response_data = {
            'message': notification_message,
            'notification': notification_message
        }
        return JsonResponse(response_data, status=200)

    return JsonResponse({'error': 'Invalid request method.'}, status=400)
