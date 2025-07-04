from django.shortcuts import render

def indexView(request):
    """
    Render the index page.
    """
    page = 'index'
    page_title = 'Home'
    context = {
        'page': page,
        'page_title': page_title,
    }
    return render(request, 'employees/index.html', context)

def employeesView(request):
    """
    Render the employee page.
    """
    page = 'employee'
    page_title = 'Employee'
    context = {
        'page': page,
        'page_title': page_title,
    }
    return render(request, 'employees/employee.html', context)