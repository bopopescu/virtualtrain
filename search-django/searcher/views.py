from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post,Comment
from rest_framework import authentication, permissions
from rest_framework import generics
from django.http import JsonResponse
from .models import Shepp
import json
from django.core import serializers

# Create your views here.


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post_list.html'


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post_detail.html'

    def  get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comments.all()
        print(self.request.POST)
        return context

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        content = request.POST.get('content')
        self.object = self.get_object()
        comment = Comment.objects.create(post=self.object,username=username,content=content)
        array = []
        obj = {}
        obj['username'] = comment.username
        obj['content'] = comment.content
        array.append(obj)
        return JsonResponse(array,safe=False)


    
    



def test(request):
    males = Shepp.objects.filter(male=1)
    female = Shepp.objects.filter(male=2)
    context={
        'male':males,
        'female':female
    }
    return render(request,'test.html',context)


