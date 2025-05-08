from django.shortcuts import render, redirect
from .models import Drug
from .forms import DrugForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def drug_list(request):
    drugs = Drug.objects.filter(added_by=request.user)
    return render(request, 'base/drug_list.html', {'drugs': drugs})


def add_drug(request):
    if request.method == 'POST':
        form = DrugForm(request.POST)
        if form.is_valid():
            drug = form.save(commit=False)
            drug.added_by = request.user
            drug.save()
            return redirect('drug_list')
    else:
        form = DrugForm()
    return render(request, 'base/drug_form.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


class DrugUpdateView(LoginRequiredMixin, UpdateView):
    model = Drug
    template_name = 'base/drug_edit.html'
    fields = ['name', 'quantity', 'status', 'remain']
    success_url = reverse_lazy('drug_list')


class DrugDeleteView(LoginRequiredMixin, DeleteView):
    model = Drug
    template_name = 'base/drug_delete.html'
    success_url = reverse_lazy('drug_list')
