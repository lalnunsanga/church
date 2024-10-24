from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader


from django.shortcuts import render, get_object_or_404, redirect  
from .models import Post, Comment  ,Category, Staff
from .form import CommentForm  

import plotly.graph_objs as go
import plotly.offline as pyo
import pandas as pd


# Create your views here.

def methodist(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def template(request):
    template = loader.get_template('template.html')
    return HttpResponse(template.render())



def post_detail(request, post_id):  
    post = get_object_or_404(Post, id=post_id)  
    comments = post.comments.all()  # Get all comments for the post  
    
    if request.method == 'POST':  
        form = CommentForm(request.POST)  
        if form.is_valid():  
            comment = form.save(commit=False)  
            comment.post = post       # Associate comment with the post  
            comment.user = request.user  # Get the current user  
            comment.save()            # Save the comment to the database  
            return redirect('post_detail', post_id=post.id)  # Redirect to post detail page  
    else:  
        form = CommentForm()  

    return render(request, 'post_detail.html', {  
        'post': post,  
        'comments': comments,  
        'form': form,  
    })  

def home(request):
    record = Post.objects.all().values()
    template = loader.get_template('home.html')
    context = {
        'record': record,
    }
    return HttpResponse(template.render(context,request))

def category(request):
    news = Category.objects.all()
    context = {
        'news' : news,
    }
    return render(request, 'home.html', context)

def staff_list(request):  
    staff_members = Staff.objects.all()  # Fetch all staff members  
    return render(request, 'staff_list.html', {'staff_members': staff_members})  


def plot_view(request):  
    # Load example dataset  
    tips = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")  
    
    # Create a Plotly bar plot  
    data = [  
        go.Bar(  
            x=tips['day'],  
            y=tips.groupby('day')['total_bill'].sum(),  
            marker=dict(color='blue')  
        )  
    ]  
    
    layout = go.Layout(title='Total Bill by Day', xaxis=dict(title='Day'), yaxis=dict(title='Total Bill'))  
    
    fig = go.Figure(data=data, layout=layout)  
    
    # Convert the plot to HTML  
    plot_div = pyo.plot(fig, auto_open=False, include_plotlyjs=False, output_type='div')  

    return render(request, 'plot.html', {'plot_div': plot_div}) 

