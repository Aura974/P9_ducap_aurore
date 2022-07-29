from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from authentication.models import User
from followers import models, forms


@login_required
def follow_users(request):
    unfollows = forms.UnfollowsForm()
    requested_user = request.POST.get("search")
    if request.method == "POST":
        if "unfollows" in request.POST:
            unfollows = forms.UnfollowsForm(request.POST)
            followed = request.POST.get("followed_user")
            if unfollows.is_valid():
                models.UserFollows.objects.get(user=request.user, followed_user=followed).delete()
        else:
            if User.objects.filter(username=requested_user).exists():
                requested_user = User.objects.get(username=requested_user)
                unique_relation = models.UserFollows.objects.filter(user=request.user, followed_user=requested_user)

                if unique_relation.exists():
                    messages.info(request, "Vous suivez déjà cet utilisateur")
                elif request.user == requested_user:
                    messages.warning(request, "Vous ne pouvez vous suivre vous-même !")
                else:
                    models.UserFollows.objects.create(user=request.user, followed_user=requested_user)
                    messages.success(request, "Utilisateur ajouté avec succès !")
            else:
                messages.error(request, "Nom d'utilisateur invalide")

    following_list = models.UserFollows.objects.filter(user=request.user)
    followed_by_list = models.UserFollows.objects.filter(followed_user=request.user)
    context = {
        "following_list": following_list,
        "followed_by_list": followed_by_list,
        "unfollows": unfollows
    }

    return render(request, "followers/follow_users.html", context=context)
