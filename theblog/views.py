from django.shortcuts import render


def error_404_view(request, exception):
    """
    Custom 404 page
    """
    return render(request, "404.html", status=404)
