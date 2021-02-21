import json
import re
import bcrypt

from django.http              import JsonResponse, HttpResponse
from django.views             import View
from django.core.validators   import validate_email
from django.core.exceptions   import ValidationError

from user.models              import User

password_regex           = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$')
MINIMUM_PASSWORD_LENGTH  = 8

class SignUpView(View):

    def post(self,request):
        try:
            data         = json.loads(request.body)

            email        = data['email']
            fullname     = data['fullname']
            password     = data['password']
            maker_info   = data.get('maker_info')

            if User.objects.filter(email=email).exists():
                return JsonResponse({"message" : "EMAIL_EXISTS"}, status=400)

            if not (email and fullname and password):
                return JsonResponse({"message" : "REQUIRED_FIELD"}, status=400)

            if len(password) < MINIMUM_PASSWORD_LENGTH:
                return JsonResponse({"message" : "PASSWORD_MUST_BE_LONGER_THAN_EIGHT_LETTERS"}, status=400)

            validate_email(email)

            if not password_regex.search(password):
                return JsonResponse({"message" : "INVALID_PASSWORD"}, status=400)

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            User.objects.create(
                fullname    = fullname,
                email       = email,
                password    = hashed_password,
                maker_info  = maker_info
            )

            return JsonResponse({"message" : "SUCCESS"}, status=201)
            
        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)

        except ValidationError:
            return JsonResponse({"message" : "VALIDATION_ERROR"}, status=400)