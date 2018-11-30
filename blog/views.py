from django.shortcuts import render


posts = [
	{
		'author': 'Азамат',
		'title': 'Первый пост',
		'content': 'Контент первого поста',
		'date_posted': 'Август 22, 2018'
	},
	{
		'author': 'Морфеус',
		'title': 'Две таблетки',
		'content': 'Ты как Алиса в крольичей норе',
		'date_posted': 'Август 28, 2018'
	}
]


def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'Обо мне'})