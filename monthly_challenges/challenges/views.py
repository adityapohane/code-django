from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "january": "Eat no meat for the entire month! in January",
    "february": "Walk for at least 20 minutes every day! in February",
    "march": "Learn Django for at least 20 minutes every day! in March",
    "april": "Learn Django for at least 20 minutes every day! ",
    "may": "Learn Django for at least 20 minutes every day! in May",
    "june": "Learn Django for at least 20 minutes every day! in June",
    "july": "Learn Django for at least 20 minutes every day! in July",
    "august": "Learn Django for at least 20 minutes every day! in August",
    "september": "Learn Django for at least 20 minutes every day! in August",
    "october": "Learn Django for at least 20 minutes every day! in October",
    "november": "Learn Django for at least 20 minutes every day! in November",
    "december": "Learn Django for at least 20 minutes every day! in December",
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    if month < 13:
        months = list(monthly_challenges.keys())
        redirect_month = months[month - 1]
        redirect_path = reverse("month-challenge", args=[redirect_month])

        return HttpResponseRedirect("/challenges/" + redirect_month)
    else:
        return HttpResponseNotFound(f"<h1>This month is not supported!</h1>")


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound(f"<h1>This month is not supported!</h1>")
