import re

from django.http              import JsonResponse

def validate_password(password):
    password_regex = re.compile(r'^(?=.*[!$?])(?=.*[a-z])(?=.*[A-Z]).{8}$')
    if not password_regex.search(password):
        return JsonResponse({"message" : "INVALID_PASSWORD"}, status=400)
