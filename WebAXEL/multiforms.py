from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.views.generic.base import ContextMixin, TemplateResponseMixin
from django.views.generic.edit import ProcessFormView


# Classe de base pour créer des vues contenant plusieurs formulaires
class MultiFormMixin(ContextMixin):
    form_classes = {}
    prefixes = {}
    success_urls = {}

    initial = {}
    prefix = None
    success_url = None

    # Récupération des valeurs de form_classes
    def get_form_classes(self):
        return self.form_classes

    # Récupération des formulaires dans un dictionnaire
    def get_forms(self, form_classes):
        return dict([
            (key, self._create_form(key, class_name)) for key, class_name in form_classes.items()])

    # Récupération des arguments de formulaire dans une liste
    def get_form_kwargs(self, form_name):
        kwargs = {}
        kwargs.update({'initial': self.get_initial(form_name)})
        kwargs.update({'prefix': self.get_prefix(form_name)})
        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
            })
        return kwargs

    # Validation des formulaires
    def forms_valid(self, forms, form_name):
        form_valid_method = '%s_form_valid' % form_name
        if hasattr(self, form_valid_method):
            return getattr(self, form_valid_method)(forms[form_name])
        return HttpResponseRedirect(self.get_success_url(form_name))

    # Invalidation des formulaires
    def forms_invalid(self, forms):
        return self.render_to_response(self.get_context_data(forms=forms))

    # Pré-remplissage des champs du formulaire via initial['nom_du_champ'] avec des valeurs
    def get_initial(self, form_name):
        initial_method = 'get_%s_initial' % form_name
        if hasattr(self, initial_method):
            return getattr(self, initial_method)()
        return {'action': form_name}

    # Récupération du préfixe
    def get_prefix(self, form_name):
        return self.prefixes.get(form_name, self.prefix)

    # Récupération de l'adresse en cas de succès du formulaire
    def get_success_url(self, form_name=None):
        return self.success_urls.get(form_name, self.success_url)

    # Fonction de création du formulaire
    def _create_form(self, form_name, form_class):
        form_kwargs = self.get_form_kwargs(form_name)
        form = form_class(**form_kwargs)
        return form


class ProcessMultipleFormsView(ProcessFormView):

    # Récupération des formulaires
    def get(self, request, *args, **kwargs):
        form_classes = self.get_form_classes()
        forms = self.get_forms(form_classes)
        return self.render_to_response(self.get_context_data(forms=forms))

    # Envoi des formulaires
    def post(self, request, *args, **kwargs):
        form_classes = self.get_form_classes()
        form_name = request.POST.get('action')
        return self._process_individual_form(form_name, form_classes)

    # Traitement individuel des formulaires
    def _process_individual_form(self, form_name, form_classes):
        forms = self.get_forms(form_classes)
        form = forms.get(form_name)
        if not form:
            return HttpResponseForbidden()
        if form.is_valid():
            return self.forms_valid(forms, form_name)

        return self.forms_invalid(forms)


class BaseMultipleFormsView(MultiFormMixin, ProcessMultipleFormsView):
    """
    Une vue de base pour l'affichage de plusieurs formulaires.
    """


class MultiFormsView(TemplateResponseMixin, BaseMultipleFormsView):
    """
    Une vue permettant d'afficher plusieurs formulaires, et de rendre une réponse modèle.
    """
