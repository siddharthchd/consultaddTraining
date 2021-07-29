from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import SignUpForm, CreateBlogForm
from .models import Blog
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required
def home(request):
    blogPosts = Blog.objects.all()
    context = {'blogposts' : blogPosts}
    return render(request, "secondapp/posts.html", context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            
        return redirect("home")
    else:
        form = SignUpForm()
    
    context = {'form' : form}
    return render(request, "registration/signup.html", context)
            

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            print('Error logging in : ', request)
    form = AuthenticationForm()
    context = {'form' : form}
    return render(request, "registration/login.html", context)
                
def logout_request(request):
    logout(request)
    return redirect('login')

@login_required
def createBlog(request):
    form = CreateBlogForm()
    if request.method == "POST":
        form = CreateBlogForm()
        blogPost = Blog()
        blogPost.blogTitle = request.POST['title']
        blogPost.user = request.user
        blogPost.content = request.POST['content']
        blogPost.save()
        return redirect('home')
    context = {'form' : form}
    return render(request, "secondapp/createBlog.html", context)

class UpdateBlog(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = "secondapp/updateBlog.html"
    success_url = reverse_lazy("home")
    fields = "__all__"

class DeleteBlog(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = "secondapp/deleteBlog.html"
    success_url = reverse_lazy("home")