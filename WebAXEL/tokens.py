from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six


# Création de jeton unique pour la confirmation d'adresse mail à l'inscription
class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
                six.text_type(user.pk) + six.text_type(timestamp) +
                six.text_type(user.is_active)
        )


account_activation_token = TokenGenerator()
