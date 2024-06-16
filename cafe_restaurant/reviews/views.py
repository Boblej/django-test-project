from django.shortcuts import render, redirect
from .models import Review, ContactInfo
from .forms import ReviewForm

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/review_list.html', {'reviews': reviews})

def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review_list')
    else:
        form = ReviewForm()
    return render(request, 'reviews/review_form.html', {'form': form})

def contact_info(request):
    contact_info = ContactInfo.objects.first()
    return render(request, 'reviews/contact_info.html', {'contact_info': contact_info})
