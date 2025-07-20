from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth.decorators import user_passes_test, login_required, permission_required
from django.utils.decorators import method_decorator
from .models import Book, Library, UserProfile
from django.http import HttpResponse

@login_required
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

@method_decorator(login_required, name='dispatch')
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

@user_passes_test(lambda u: u.userprofile.role == 'Admin')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(lambda u: u.userprofile.role == 'Librarian')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(lambda u: u.userprofile.role == 'Member')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

@permission_required('relationship_app.can_add_book')
def add_book(request):
    return HttpResponse("Permission to add book granted.")

@permission_required('relationship_app.can_change_book')
def edit_book(request):
    return HttpResponse("Permission to edit book granted.")

@permission_required('relationship_app.can_delete_book')
def delete_book(request):
    return HttpResponse("Permission to delete book granted.")
