from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from feeds import forms, models
from followers import models as fmodels
from itertools import chain


@login_required
def home(request):
    user_follows = [
        follows.followed_user for follows in fmodels.UserFollows.objects.filter(user=request.user)
    ]
    user_tickets = models.Ticket.objects.filter(Q(user__in=user_follows) | Q(user=request.user))
    user_reviews = models.Review.objects.filter(Q(user__in=user_follows) | Q(user=request.user))
    tickets_and_reviews = sorted(
        chain(user_tickets, user_reviews),
        key=lambda instance: instance.time_created,
        reverse=True,
    )

    reviewed_tickets = [
        review.ticket for review in models.Review.objects.filter(user=request.user)
    ]

    paginator = Paginator(tickets_and_reviews, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "feeds/home.html",
        context={"page_obj": page_obj, "reviewed_tickets": reviewed_tickets},
    )


@login_required
def create_ticket(request):
    ticket_form = forms.TicketForm()
    if request.method == "POST":
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect("home")
    return render(request, "feeds/create_ticket.html", context={"ticket_form": ticket_form})


@login_required
def create_review(request):
    ticket_form = forms.TicketForm()
    review_form = forms.ReviewForm()
    if request.method == "POST":
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        review_form = forms.ReviewForm(request.POST)
        if (ticket_form.is_valid()) and (review_form.is_valid()):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review = review_form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()
            return redirect("home")
    context = {
        "ticket_form": ticket_form,
        "review_form": review_form
    }
    return render(request, "feeds/create_review.html", context=context)


@login_required
def create_answer_review(request, ticket_id):
    ticket = models.Ticket.objects.get(id=ticket_id)
    review_form = forms.ReviewForm()
    if request.method == "POST":
        review_form = forms.ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()
            return redirect("home")
    context = {
        "review_form": review_form,
        "ticket": ticket
    }
    return render(request, "feeds/create_answer_review.html", context=context)


@login_required
def posts(request):
    tickets = models.Ticket.objects.filter(user=request.user)
    reviews = models.Review.objects.filter(user=request.user)
    tickets_and_reviews = sorted(
        chain(tickets, reviews),
        key=lambda instance: instance.time_created,
        reverse=True,
    )

    paginator = Paginator(tickets_and_reviews, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "feeds/posts.html",
        context={"page_obj": page_obj},
    )
