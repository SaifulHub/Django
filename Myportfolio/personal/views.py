from django.shortcuts import render

# Create your views here.
def home_sreen_view(request):
    context = {}
    # context['some_string'] = "I am passing this string from views.py to home.html"
    # context['some_num'] = 12345

    list_of_values = []
    list_of_values.append("first_entry")
    list_of_values.append("second_entry")
    list_of_values.append("third_entry")
    list_of_values.append("fourth_entry")
    context['list_of_values'] = list_of_values

    return render(request, "home.html", context)