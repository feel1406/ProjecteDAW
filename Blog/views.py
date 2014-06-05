from django.shortcuts import render
from Blog.models import Post
from django.contrib import messages
from Blog.forms import NouPostForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils.datetime_safe import date
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def NouPost(request):
    if request.method == 'POST':
        formulariPost = NouPostForm(request.POST)
        if formulariPost.is_valid():
            autor = request.user
            data = str(date.today())
            tema = formulariPost.cleaned_data['tema']
            titol = formulariPost.cleaned_data['titol']
            entrada = formulariPost.cleaned_data['entrada']
            post = Post()
            post.autor = autor
            post.data_publicacio = data
            post.entrada = entrada
            post.tema = tema
            post.titol = titol
            post.save()
            messages.add_message(request, messages.INFO, 'Post publicat correctament.')
            return HttpResponseRedirect('/')
        else:
            messages.add_message(request, messages.INFO, 'Error publicant el post.')
    else:
        formulariPost = NouPostForm()
    return render(request,'Blog/nouPost.html', {'formulariPost' : formulariPost})

def VeureBlog(request):
    post = Post.objects.all().order_by('data_publicacio')
    page = request.GET.get('page')
    pagina = PaginarPosts(page, post, 2 )
    return render(request, 'Blog/blog.html', {'post': pagina})

def PaginarPosts(page, llista, num):
    paginador = Paginator(llista, num)
    try:
        entrada = paginador.page(page)
    except PageNotAnInteger:
        entrada = paginador.page(1)
    except EmptyPage:
        entrada = paginador.page(paginador.num_pages)
    return entrada
