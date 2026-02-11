from django.shortcuts import render
from django.http import (
    HttpResponse,
    HttpResponseNotFound,
    HttpResponseRedirect,
    Http404,
)
from django.urls import reverse
from django.template.loader import render_to_string

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
    # "december": "Learn Django for at least 20 minutes every day! in December",
    "december": None,
}


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {"months": months})


def monthly_challenge_by_number(request, month):
    if month < 13:
        months = list(monthly_challenges.keys())
        redirect_month = months[month - 1]
        redirect_path = reverse("month-challenge", args=[redirect_month])

        return HttpResponseRedirect("/challenges/" + redirect_month)
    else:
        response_data = render_to_string("404.html")  # render(request, "404.html")
        return HttpResponseNotFound(response_data)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(
            request,
            "challenges/challenge.html",
            {"text": challenge_text, "month": month.capitalize()},
        )
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        response_data = render_to_string("404.html")  # render(request, "404.html")
        return HttpResponseNotFound(response_data)
        # raise Http404()  # automatically shows 404.html page but only when debug is false in settings.py
