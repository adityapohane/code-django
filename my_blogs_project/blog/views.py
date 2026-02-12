from datetime import date
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponseNotFound

# Create your views here.

all_posts = [
    {
        "slug": "my-first-post",
        "title": "The Mountain Hiking",
        "image": "mountains.jpg",
        "author": "Ketaki",
        "date": date(2023, 1, 1),
        "excerpt": " Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.",
        "content": """Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo.
         
           Odio.Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.""",
    },
    {
        "slug": "my-second-post",
        "title": "The Mountain Hiking",
        "image": "adii.jpg",
        "author": "Chaitainya",
        "date": date(2022, 1, 1),
        "excerpt": " Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.",
        "content": """Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo.
         
           Odio.Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.""",
    },
    {
        "slug": "my-third-post",
        "title": "Sky-Dive Thriller",
        "image": "coding.jpg",
        "author": "Yash",
        "date": date(2025, 1, 1),
        "excerpt": " Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.",
        "content": """Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo.
         
           Odio.Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.""",
    },
    {
        "slug": "my-fourth-post",
        "title": "Greenland Adventure",
        "image": "woods.jpg",
        "author": "Aditya",
        "date": date(2024, 1, 1),
        "excerpt": " Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.",
        "content": """Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo.
        
          Odio.Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.""",
    },
]


def get_date(post):
    return post["date"]


def starting_page(request):
    try:
        sorted_posts = sorted(all_posts, key=get_date)
        latest_posts = sorted_posts[-3:]
        return render(request, "blog/index.html", {"recent_posts": latest_posts})
    except:
        response_data = render_to_string("404.html")  # render(request, "404.html")
        return HttpResponseNotFound(response_data)


def posts(request):
    try:
        return render(request, "blog/all-posts.html", {"all_posts": all_posts})
    except:
        response_data = render_to_string("404.html")  # render(request, "404.html")
        return HttpResponseNotFound(response_data)


def post_details_page(request, slug):
    try:
        post_found = next(
            post for post in all_posts if post["slug"] == slug
        )  # filtering the post
        return render(request, "blog/post-details-page.html", {"post": post_found})
    except:
        response_data = render_to_string("404.html")  # render(request, "404.html")
        return HttpResponseNotFound(response_data)
