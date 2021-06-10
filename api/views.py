from django.shortcuts import render
from django.views.generic import FormView

from .forms import ContactForm
from django.shortcuts import redirect



class ContactView(FormView):
    template_name = 'api/index.html'
    form_class = ContactForm

    def form_valid(self, form):
        form.result()
        return redirect('home')

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['title'] = 'Контакты'
        return context
