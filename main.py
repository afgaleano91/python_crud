clients = 'andres,jose,'
def create_client(client_name):
	global clients

	if client_name not in clients:
		clients += client_name
		_add_comma()
	else:
		print('CLient already in in the client\'s list')


def _add_comma():
	global clients

	clients += ','


def list_client():
	global clients

	print(clients)

def _print_welcome():
	print('WELCOME TO PLATZI VENTAS')
	print('*' * 50)
	print('What would you like to do today?')
	print('[C]reate client')
	print('[D]elete client')


if __name__ == '__main__':
	_print_welcome()

	command = input('').upper()

	if command == 'C':
		client_name = input('What is the client name? ')
		create_client(client_name)
		list_client()
	elif command == 'D':
		pass
	else:
		print('Invalid Command')

