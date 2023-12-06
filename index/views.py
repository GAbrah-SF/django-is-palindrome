from django.views.generic import TemplateView


# Create your views here.
class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context_index = {
            "title": "Palabras palíndromas",
            "h1": "Escribe una palabra"
        }

        return context_index
