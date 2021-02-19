import json
import re
import bcrypt

from django.http                       import JsonResponse, HttpResponse
from django.views                      import View

from user.models                       import (
    User
)

email_regex              = re.compile(r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
password_regex           = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$')
MINIMUM_PASSWORD_LENGTH  = 8

class SignUpView(View):

    def post(self,request):
        try:
            data         = json.loads(request.body)

            email        = data['email']
            fullname     = data['fullname']
            password     = data['password']
            maker_info   = data.get('maker_info', None)

            if User.objects.filter(email=email).exists():
                return JsonResponse({"message" : "EMAIL_EXISTS"}, status=400)

            if not email:
                return JsonResponse({"message" : "EMAIL_REQUIRED"}, status=400)

            if not fullname:
                return JsonResponse({"message" : "FULLNAME_REQUIRED"}, status=400)

            if not password:
                return JsonResponse({"message" : "PASSWORD_REQUIRED"}, status=400)

            if len(password) < MINIMUM_PASSWORD_LENGTH:
                return JsonResponse({"message" : "PASSWORD_MUST_BE_LONGER_THAN_EIGHT_LETTERS"}, status=400)

            if not email_regex.search(email):
                return JsonResponse({"message" : "EMAIL_VALIDATION"}, status=400)

            if not password_regex.search(password):
                return JsonResponse({"message" : "PASSWORD_VALIDATION"}, status=400)

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            User.objects.create(
                fullname=fullname,
                email=email,
                password=hashed_password,
                maker_info=maker_info
            )

            return JsonResponse({"message" : "SUCCESS"}, status=200)
            
        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)