from django.views.generic import TemplateView


class NotFoundView(TemplateView):
    template_name = 'AdminAXEL\\404.html'


class BlankView(TemplateView):
    template_name = 'AdminAXEL\\blank.html'


class ButtonsView(TemplateView):
    template_name = 'AdminAXEL\\buttons.html'


class CardsView(TemplateView):
    template_name = 'AdminAXEL\\cards.html'


class ChartsView(TemplateView):
    template_name = 'AdminAXEL\\charts.html'


class ForgotPasswordView(TemplateView):
    template_name = 'AdminAXEL\\forgot-password.html'


class IndexView(TemplateView):
    template_name = 'AdminAXEL\\index.html'


class LoginView(TemplateView):
    template_name = 'AdminAXEL\\login.html'


class RegisterView(TemplateView):
    template_name = 'AdminAXEL\\register.html'


class TablesView(TemplateView):
    template_name = 'AdminAXEL\\tables.html'


class UtilitiesAnimationView(TemplateView):
    template_name = 'AdminAXEL\\utilities-animation.html'


class UtilitiesBorderView(TemplateView):
    template_name = 'AdminAXEL\\utilities-border.html'


class UtilitiesColorView(TemplateView):
    template_name = 'AdminAXEL\\utilities-color.html'


class UtilitiesOtherView(TemplateView):
    template_name = 'AdminAXEL\\utilities-other.html'
