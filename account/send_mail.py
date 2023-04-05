from django.core.mail import send_mail


def send_confirmation_email(user, code):
    send_mail(
        'Здравствуйте, активируйте ваш аккаунт!',
        f'Что активировать ваш аккаунт нужно ввести код:'
        f'\n{code}'
        f'\nне передавайте этот код никому!',
        'johnsnowtest73@gmail.com',
        [user],
        fail_silently=False,
    )
