from django.views import generic


class ComponentLibraryView(generic.base.TemplateView):
    template_name = 'a4test_contrib/component_library.html'
