PASSWORD = '12345'


def password_required(func):
    def wrapper():
        password = input('Cual es tu contraseña: ')

        if password == PASSWORD:
            return func()
        else:
            print("Contraseña errada, intente de nuevo")
    
    return wrapper()


@password_required
def needs_password():
    print('La contraseña es correcta')


def upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        return result.upper()
    
    return wrapper


@upper
def say_my_name(name):
    return (f'Hola {name}')


if __name__ == '__main__':
    # needs_password()
    print(say_my_name("andres"))