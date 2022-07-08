from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from feeds import forms, models
from itertools import chain


@login_required
def home(request):
    tickets = models.Ticket.objects.all()
    reviews = models.Review.objects.all()
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
        "feeds/home.html",
        context={"page_obj": page_obj},
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

