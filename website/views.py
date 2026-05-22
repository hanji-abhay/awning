from django.shortcuts import render, redirect
from .models import ContactQuery, Feedback
from django.contrib import messages
from django.db.models import Avg
# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        message = request.POST.get("message")

        ContactQuery.objects.create(
            name=name,
            phone=phone,
            email=email,
            message=message
        )
        messages.success(request, "Your query has been sent successfully. We will contact you soon.")
        return redirect("contact")

    return render(request, "contact.html")

def feedback(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        rating = request.POST.get("rating")
        Feedback.objects.create(
            name=name,
            phone=phone,
            message=message,
            rating=rating
        )

        messages.success(request, "Thank you for your feedback!")
        return redirect("feedback")  # refresh page after submit
    
    average_rating = Feedback.objects.aggregate(avg=Avg("rating"))["avg"]

    # handle no ratings case
    if average_rating is None:
        average_rating = 0
        all_feedback = Feedback.objects.all().order_by("-created_at")
    context = {
        "average_rating": round(average_rating, 1),
        "feedbacks": all_feedback
    }

    return render(request, "feedback.html", context)

def work(request):
    return render(request, 'works.html')