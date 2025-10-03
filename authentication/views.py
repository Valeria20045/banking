from django.shortcuts import render, get_object_or_404, redirect
from .models import Countries
from .forms import CountriesForm

def country_list(request):
    countries = Countries.objects.all()
    return render(request, 'authentication/country_list.html', {'countries': countries})

def country_edit(request, pk):
    country = get_object_or_404(Countries, pk=pk)
    if request.method == 'POST':
        form = CountriesForm(request.POST, instance=country)
        if form.is_valid():
            form.save()
            return redirect('authentication:country_list')
    else:
        form = CountriesForm(instance=country)
    return render(request, 'authentication/country_form.html', {'form': form, 'country': country})
