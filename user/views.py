import json
from json.decoder import JSONDecodeError
import bcrypt
import jwt

from django.http                       import JsonResponse, HttpResponse
from django.views                      import View

from user.models                       import (
    User
)

from my_settings                       import SECRET_KEY, ALGORITHM

class SignInView(View):

    def post(self, request):
        data = json.loads(request.body)

        try:
            email       = data.get('email', None)
            password    = data.get('password', None)

            if not (email and password):
                return JsonResponse({"message" : "REQUIRED_FIELD"}, status=400)

            if User.objects.filter(email=email):
                user = User.objects.get(email=email)

                if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                    access_token = jwt.encode({"id" : user.id}, SECRET_KEY, algorithm=ALGORITHM)
                    return JsonResponse({"message" : "SUCCESS", "TOKEN" : access_token}, status=200)
                
                return JsonResponse({"message" : "UNAUTHORIZED_APPROACH"}, status=401)
            
            return JsonResponse({"message" : "INVALID_USER"}, status=401)

        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)
    
