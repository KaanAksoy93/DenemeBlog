from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages
# Create your views here.

def post_index(request):

    posts=Post.objects.all()

    return render(request,'post/index.html',{'posts': posts})


def post_detail(request,id):

    post=get_object_or_404(Post,id=id)
    context={
        'post':post,
    }
    return render(request,'post/detail.html',context)


def post_create(request):



    # if request.method == "POST":
    #     print(request.POST)

    # title=request.POST.get('title')
    # content=request.POST.get('content')
    # Post.objects.create(title=title,content=content)

    # if request.method == "POST":
    #     #save info came from form
    #     form = PostForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    # else:
    #     #show form to user
    #     form = PostForm()

    form = PostForm(request.POST or None)
    if form.is_valid():
        post=form.save()
        messages.success(request,'Completed Successfully.')
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
            'form': form,
        }

    return render(request,'post/form.html',context)


def post_update(request,id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None,instance=post)
    if form.is_valid():
        form.save()
        messages.success(request,'Updated Successfully.',extra_tags='msg success')
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
            'form': form,
        }
    return render(request,'post/form.html',context)


def post_delete(request,id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('post:index')

