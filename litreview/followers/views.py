from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from authentication.models import User
from followers.models import UserFollows


@login_required
def follow_users(request):
    message = ""
    if request.method == "POST":
        requested_user = request.POST.get("search")
        if User.objects.filter(username=requested_user).exists():
            requested_user = User.objects.get(username=requested_user)
            unique_relation = UserFollows.objects.filter(Q(user=request.user) & Q(followed_user=requested_user))

            if unique_relation.exists():
                message = "Already followed"
            elif request.user == requested_user:
                message = "Can't follow yourself"
            else:
                UserFollows.objects.create(user=request.user, followed_user=requested_user)
                message = "successful !"
        else:
            message = "Invalid username"

    return render(request, "followers/follow_users.html", context={"message": message})
