clients = 'andres,jose,'
def create_client(client_name):
	global clients

	clients += client_name
	_add_comma()


def _add_comma():
	global clients

	clients += ','


def list_client():
	global clients

	print(clients)


if __name__ == '__main__':
	list_client()

	create_client('pedro')

	list_client()

