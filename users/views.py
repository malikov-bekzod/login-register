from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User
# Create your views here.

class LoginPageView(View):
    def get(self,request):
        return render(request, "users/login.html")

    def post(self, request):
        username = request.POST["username"]
        users = User.objects.filter(username = username)

        if len(users) == 0:
            return redirect("login-page")
        else:
            return redirect("profile-page")


class RegisterPageView(View):
    def get(self, request):
        return render(request, "users/register.html")

    def post(self,request):
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        user = User(
            first_name = first_name,
            last_name = last_name,
            email = email,
            username = username
        )
        user.set_password(password)
        user.save()
        print("<<<<<<<<<<<<<<<<<<<<<<CREATED>>>>>>>>>>>>>>>>>>>>")
        return redirect("login-page")

class UserListView(View):
    def get(self,request):
        users = User.objects.all()
        context = {"users":users}
        return render(request, "users/user_list.html",context)