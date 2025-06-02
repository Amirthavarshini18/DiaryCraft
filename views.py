# # diary_app/views.py
# from django.shortcuts import render
# from .groq_utils import format_diary

# def home(request):
#     diary_entry = ""
#     if request.method == "POST":
#         hints = request.POST.get("hints")
#         diary_entry = format_diary(hints)
#     return render(request, "home.html", {"diary": diary_entry})


from django.shortcuts import render
from .groq_utils import format_diary
from .models import DiaryEntry

def home(request):
    generated_entry = None
    if request.method == "POST":
        hints = request.POST.get("hints")
        generated_entry = format_diary(hints)
        
        # Save to database
        DiaryEntry.objects.create(hints=hints, entry=generated_entry)

    # Show all entries ordered by latest
    all_entries = DiaryEntry.objects.all().order_by('-date_created')

    return render(request, "index.html", {
        "generated_entry": generated_entry,
        "all_entries": all_entries,
    })
