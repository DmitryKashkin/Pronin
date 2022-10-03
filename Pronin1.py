def normalize_email(email: str) -> str:
    if not '@' in email:
        return 'а где же @???'
    if '@yandex.ru' in email:
        email=email[:email.find('@yandex.ru')]+'@ya.ru'
    return email.lower()


if __name__ == '__main__':
    print(normalize_email(input('enter email ')))
