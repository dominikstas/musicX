from django.shortcuts import render

def news(request):
    return render(request, "news/news.html")

def add_preorder(request):
    if request.method == 'POST':
        form = PreorderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news.html')
    else:
        form = PlytaForm()
    
    context = {'form': form}
    return render(request, 'news/add_preorder.html', context)