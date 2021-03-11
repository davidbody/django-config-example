# Use this to generate secret keys for each environment

from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())
