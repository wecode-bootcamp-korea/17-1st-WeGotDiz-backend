<<<<<<< HEAD
import  jwt
import  json
import  requests

from django.http  import JsonResponse
from django.conf  import settings
from my_settings  import SECRET_KEY, ALGORITHM
from user.models  import User
=======
import    jwt
import    json
import    requests

from django.http              import JsonResponse
from django.conf              import settings

from my_settings              import SECRET_KEY, ALGORITHM
from .models                  import User
>>>>>>> 905d93f2f515526447b3313e371e3c669fa8e59f

def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        try:
<<<<<<< HEAD
            access_token = request.headers['Authorization']
            payload      = jwt.decode(access_token, SECRET_KEY, algorithms=ALGORITHM)
            user         = User.objects.get(id=payload['id'])
            request.user = user

        except jwt.exceptions.DecodeError:
            return JsonResponse({"message" : "INVALID_TOKEN"}, status=401)

        except User.DoesNotExist:
            return JsonResponse({"message" : "INVALID_USER"}, status=401)
=======
            access_token  = request.headers['Authorization']
            payload       = jwt.decode(access_token, SECRET_KEY, algorithms=ALGORITHM)
            user          = User.objects.get(id=payload['id'])
            request.user  = user
        
        except jwt.exceptions.DecodeError:
            return JsonResponse({"message" : "INVALID_TOKEN"}, status=400)

        except User.DoesNotExist:
            return JsonResponse({"message" : "INVALID_USER"}, status=400)
>>>>>>> 905d93f2f515526447b3313e371e3c669fa8e59f

        return func(self, request, *args, **kwargs)

    return wrapper