from django.shortcuts import redirect, render

from .forms import ContactForm

# Create your views here.

"""CONTACT VIEWS"""


# class ContactView(FormView):
#     template_name = 'contact/contact.html'
#     form_class = ContactForm
#     success_url = reverse_lazy('index')
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
#
#
# @csrf_protect
# def my_view(request):
#     # Your view logic here
#     pass

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print("Saving database")
            form.save()
            return redirect('index')
    else:
        form = ContactForm()
        print("Is not saving")

    return render(request, 'contact/contact.html', {'form': form})
