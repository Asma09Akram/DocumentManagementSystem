from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import DocumentForm
from .models import Document
import os
from django.conf import settings
from django.http import Http404
import mimetypes
from django.http import HttpResponse
from docx import Document as DocxDocument


# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        return redirect('login')
    return render(request, 'signup.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

def logout_user(request):
    messages.error(request,"")
    logout(request)    

    return redirect('login')


@login_required
def dashboard(request):
    if request.method == 'POST':
        if 'upload' in request.POST:
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                document = form.save(commit=False)
                document.user = request.user
                document.save()
                return redirect('dashboard')
        elif 'delete' in request.POST:
            document_id = request.POST.get('document_id')
            document = get_object_or_404(Document, id=document_id, user=request.user)

            # Delete the file from the filesystem
            if document.file:
                file_path = os.path.join(settings.MEDIA_ROOT, document.file.name)
                if os.path.exists(file_path):
                    os.remove(file_path)
            
            # Delete the document record from the database
            document.delete()
            return redirect('dashboard')
        elif 'view' in request.POST:
            document_id = request.POST.get('document_id')
            document = get_object_or_404(Document, id=document_id, user=request.user)
    
            # Get the document file path
            file_path = document.file.path

            # For text-based files, read and display the content
            if file_path.endswith('.txt') or file_path.endswith('.csv'):
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        file_content = file.read()
                    return render(request, 'view_document.html', {'document': document, 'file_content': file_content})
                except IOError:
                    raise Http404("File not found or can't be opened")
                except UnicodeDecodeError:
                    raise Http404("Unable to decode file content")
            
            # For .docx files, read and display the content
            elif file_path.endswith('.docx'):
                try:
                    doc = DocxDocument(file_path)
                    doc_content = []
                    for para in doc.paragraphs:
                        doc_content.append(para.text)
                    file_content = "\n".join(doc_content)
                    return render(request, 'view_document.html', {'document': document, 'file_content': file_content})
                except IOError:
                    raise Http404("File not found or can't be opened")
        
        # For other file types (e.g., PDFs, images), return a download or view link
            else:
                file_url = document.file.url
                return redirect(file_url)
    

            
        elif 'download' in request.POST:
            document_id = request.POST.get('document_id')
            document = get_object_or_404(Document, id=document_id, user=request.user)

            # Serve the document as an HTTP response
            file_path = document.file.path
            if os.path.exists(file_path):
                with open(file_path, 'rb') as f:
                    response = HttpResponse(f.read(), content_type="application/octet-stream")
                    response['Content-Disposition'] = f'inline; filename={os.path.basename(file_path)}'
                    return response
            else:
                messages.error(request, 'File not found')
                return redirect('dashboard')
    else:
        form = DocumentForm()  # Initialize the form for GET requests
    
        documents = Document.objects.filter(user=request.user)
        return render(request, 'dashboard.html', {'form': form, 'documents': documents})
