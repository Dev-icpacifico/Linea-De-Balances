from django.contrib.admin import site
from django.views.generic import TemplateView

class Report(TemplateView):
    template_name = 'admin/reportbi.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agrega el contexto del admin
        context.update(site.each_context(self.request))
        context['title'] = 'Reportes BI'  # Título personalizado
        return context
