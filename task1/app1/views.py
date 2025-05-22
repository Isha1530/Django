from django.shortcuts import render

# Create your views here.

def table(request):
    # Sample data for the table
    people = [
        {'name': 'Priya', 'age': 30, 'email': 'priya@example.com'},
        {'name': 'prachi', 'age': 25, 'email': 'prachi@example.com'},
        {'name': 'kavita', 'age': 35, 'email': 'kavita@example.com'},
    ]
    return render(request, 'table.html', {'people': people})