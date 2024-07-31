from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import ContactForm
from django.views.decorators.csrf import csrf_protect
# Create your views here.

"""CONTACT VIEWS"""


class ContactView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


@csrf_protect
def my_view(request):
    # Your view logic here
    pass
