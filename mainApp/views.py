from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import *
 
def homePage(Request):
    blogData = BlogPost.objects.all().order_by("id").reverse()[:3]
    teamData = TeamMember.objects.all()
    return render(Request,"index.html",{"blogData":blogData,"teamData":teamData})

def callBackDetails(Request):
    if(Request.method=="POST"):
        cbd = CallBackDetail()
        cbd.name = Request.POST.get("name")
        cbd.phone = Request.POST.get("phone")
        cbd.email = Request.POST.get("email")
        cbd.message = Request.POST.get("message")
        cbd.save()
        messages.success(Request,"Your Form Submitted Successfuly!!!")
    return redirect("/")

def subscribtions(Request):
    if(Request.method=="POST"):
        sbc = Subscribtion()
        sbc.email = Request.POST.get("email")
        sbc.save()
        messages.success(Request,"Subscribed Successfuly!!!")
    return redirect("/")

def about(Request):
    blogData = BlogPost.objects.all().order_by("id").reverse()[:3]
    return render(Request,"about.html",{"blogData":blogData})

def blog(Request):
    blogData = BlogPost.objects.all().order_by("id").reverse()[:3]
    blogDataAll = BlogPost.objects.all()
    return render(Request,"blog-grid.html",{"blogDataAll":blogDataAll,"blogData":blogData})

def blogSingle(Request,id):
    blogData = BlogPost.objects.all().order_by("id").reverse()[:5]
    blogDataSingle = BlogPost.objects.get(id=id)
    blogComment = BlogComment.objects.filter(post=blogDataSingle)
    return render(Request,"blog-single-left.html",{"blogDataSingle":blogDataSingle,"blogData":blogData,"blogComment":blogComment})

# def blog_comment(request, id):
#     post = get_object_or_404(BlogPost, id=id)
#     if request.method == "POST":
#         username = request.POST.get("author")
#         phone = request.POST.get("comment_phone")
#         email = request.POST.get("comment_email")
#         message = request.POST.get("comment")

#         BlogComment.objects.create(
#             post=post,
#             username=username,
#             phone=phone,
#             email=email,
#             message=message
#         )
#         messages.success(request, "Your comment has been submitted successfully!")
#     return redirect("/blog-single-left", id=id)

def blogComment(Request):
    if(Request.method=="POST"):
        
        username = Request.POST.get("author")
        phone = Request.POST.get("comment_phone")
        email = Request.POST.get("comment_email")
        message = Request.POST.get("comment")
        postId = Request.POST.get("postId") 
        post = BlogPost.objects.get(id=postId)
        blc = BlogComment(username=username,phone=phone,email=email,message=message,post=post)
        blc.save()
        messages.success(Request,"Your Comment Submitted Successfuly!!!")
        return redirect(f"/blog-single-left/{post.id}")
    return redirect("/")

def contact(Request):
    blogData = BlogPost.objects.all().order_by("id").reverse()[:3]
    if(Request.method=="POST"):
        cnd = ContactDetail()
        cnd.name = Request.POST.get("name")
        cnd.phone = Request.POST.get("phone")
        cnd.email = Request.POST.get("email")
        cnd.subject = Request.POST.get("subject")
        cnd.message = Request.POST.get("message")
        cnd.save()
        messages.success(Request,"Your Form Submitted Successfuly!!!")
    return render(Request,"contact.html",{"blogData":blogData})

def services(Request):
    blogData = BlogPost.objects.all().order_by("id").reverse()[:3]
    return render(Request,"services.html",{"blogData":blogData})

def website(Request):
    blogData = BlogPost.objects.all().order_by("id").reverse()[:3]
    return render(Request,"website.html",{"blogData":blogData})

def mobileApp(Request):
    blogData = BlogPost.objects.all().order_by("id").reverse()[:3]
    return render(Request,"mobile-app.html",{"blogData":blogData})

def graphicsDesigning(Request):
    blogData = BlogPost.objects.all().order_by("id").reverse()[:3]
    return render(Request,"graphics-designing.html",{"blogData":blogData})

def digitalMarketing(Request):
    blogData = BlogPost.objects.all().order_by("id").reverse()[:3]
    return render(Request,"digital-marketing.html",{"blogData":blogData})

def seo(Request):
    blogData = BlogPost.objects.all().order_by("id").reverse()[:3]
    return render(Request,"seo.html",{"blogData":blogData})

def socialMedia(Request):
    blogData = BlogPost.objects.all().order_by("id").reverse()[:3]
    return render(Request,"social-media.html",{"blogData":blogData})

