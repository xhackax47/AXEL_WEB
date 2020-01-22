from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Gestionnaire perso d'utilisateurs  où email est l'unique identifiant
    pour l'authentification à la place de username
    """

    def create_user(self, email, password, **extra_fields):
        # Crée et sauvegarde un utilisateur avec le couple email/password
        if not email:
            raise ValueError(_('L\'adresse électronique doit être définie'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        # Crée et sauvegarde un super-utilisateur avec le couple email/password
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Le super-utilisateur doit avoir is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Le super-utilisateur doit avoir is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)
