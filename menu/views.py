from django.views import generic


class HomeView(generic.TemplateView):
    template_name = 'menu/index.html'
