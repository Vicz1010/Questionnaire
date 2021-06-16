from django.shortcuts import render
from Myapp.forms import MyForm

# Create your views here.
def main(request):
    return render(request, 'home.html')

def forms(request):
    form = MyForm()

    if request.method == "POST":
        form = MyForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return main(request)
        else:
            print("Error. Form details is invalid!")

    return render(request,'form.html', {'form': form})

