from django.shortcuts import render, redirect

posts = [
    {
        'author': 'rohid_islam',
        'user-full-name': 'Rohidul Islam',
        'discription': 'This is my first post!',
        'image': 'images/insta_pics/pic-1.jpg',
        'views': 301,
        'profile_pic': 'images/profile-3.jpg',
    },
    {
        'author': 'jasika_rr',
        'user-full-name': 'Jasika',
        'discription': 'This is my first post also :-)!',
        'image': 'images/insta_pics/pic-2.jpg',
        'views': 458,
        'profile_pic': 'images/profile-2.jpg',
    },
    {
        'author': 'jon_301',
        'user-full-name': 'Jon',
        'discription': 'this is so cool!!!!',
        'image': 'images/insta_pics/pic-3.jpg',
        'views': 1003,
        'profile_pic': 'images/profile-4.jpg'
    },
]


def home(request):
    context = {
        'title': 'Instagram',
        'posts': posts
    }
    return render(request, 'home.html', context)
