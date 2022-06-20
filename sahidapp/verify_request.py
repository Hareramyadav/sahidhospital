from django.shortcuts import redirect
from .models import *
from django.contrib.auth.models import User

def validate_request_for_admin(f):
    def wrap(request, *args, **kws):
        admin_name = request.session.get('user', None)
        print("admin_name_is", admin_name)
        if admin_name is None:
            return redirect("/admin_login")
        else:
            is_admin = validate_admin(admin_name)
            print("admin_name", is_admin)
            if is_admin:
                return f(request, *args, **kws)
            else:
                return redirect("/admin_login")

    return wrap

def validate_admin(email):
    check_user = User.objects.filter(email=email).filter(is_superuser=True).exists()
    if check_user:
        return True
    else:
        return False