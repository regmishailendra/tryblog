from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from stories.models import Story
from .forms import StoryForm, LoginForm, RegisterForm


@login_required(login_url='login')
def list(request):
    storylist = Story.objects.all().order_by('-publish')
    query=request.GET.get('q')
    if query:
       storylist = storylist.filter(title__icontains=query)
       storylist=storylist.filter(
           Q(title__icontains=query)|
           Q(content__icontains=query)|
           Q(user__first_name__icontains=query)|
           Q(user__last_name__icontains=query)






       ).distinct()
    context = {

        'storylist': storylist,
    }

    return render(request, 'list.html', context)


@login_required(login_url='login')
def create(request):
    form = StoryForm(request.POST or None, request.FILES or None)
    context = {
        'form': form,

    }
    if form.is_valid():
        instance = form.save(commit=False)

        # for analyzing data
        title = instance.title
        content = instance.content
        image = instance.image

        story = Story()
        story.title = title
        story.content = content
        story.image = image

        #
        story.save()
        return redirect('list')

    return render(request, 'create.html', context)


@login_required(login_url='login')
def details(request, id):
    # story=Story.objects.all().get(pk=id)
    story = get_object_or_404(Story, pk=id)

    context = {
        'story': story

    }

    return render(request, 'details.html', context)


@login_required(login_url='login')
def edit(request, id):
    story = get_object_or_404(Story, pk=id)
    form = StoryForm(request.POST or None ,request.FILES or None, instance=story)

    context = {
        'form': form,

    }
    if form.is_valid():
        instance = form.save(commit=False)

        # for analyzing data
        title = instance.title
        content = instance.content

        if story.user == request.user:

            story.title = title
            story.content = content
            print(request.user)
            story.save()
            return redirect('list')

        else:
            print('This is not your post and you cannot edit this.')

    return render(request, 'update.html', context)


@login_required(login_url='login')
def delete(request, id):
    story = get_object_or_404(Story, pk=id)
    if story.user==request.user:
       story.delete()
    else:
        print('You cannot delete other people\'s post')
    return redirect('list')


def login_view(request):
    print(request.user.is_authenticated)
    form = LoginForm(request.POST or None)
    next = request.GET.get('next')
    if form.is_valid():
        # instance=form.save(commit=False)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        if not user:
            print('Credentials do not match')

        else:
            print('Credientials match')

            login(request, user)

            if request.user.is_authenticated():
             print('user is authendicated')
             if next:
                return redirect(next)

             return redirect('list')



    context = {
    'form': form

}

    return render(request, 'login.html', context)


def register_view(request):
    form = RegisterForm(request.POST or None)
    next = request.GET.get('next')
    context = {

        'form': form
    }

    if form.is_valid():
        print('on view function it came here')
        password = form.cleaned_data.get('password')
        user = form.save(commit=False)
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)

        return redirect('list')

    return render(request, 'register.html', context)


def logout_view(request):
    logout(request)
    return redirect('list')

