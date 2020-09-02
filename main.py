import sys
import csv
import os


CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
clients = []

def _initialize_clients_from_storage():
	with open(CLIENT_TABLE, mode='r') as f:
		reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

		for row in reader:
			clients.append(row)


def _save_client_to_storage():
	tmp_table_name = f'{CLIENT_TABLE}.tmp'
	with open(tmp_table_name, mode='w') as f:
		writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
		writer.writerows(clients)

	os.remove(CLIENT_TABLE)
	os.rename(tmp_table_name, CLIENT_TABLE)


def create_client(client):
	global clients

	if client not in clients:
		clients.append(client)
	else:
		print('CLient already in in the client\'s list')


def list_client():
	global clients
	print('uid |  name  | company  | email  | position ')
	print('*' * 50)
	
	for idx, client in enumerate(clients):
		print(f"{idx} : {client['name']} | {client['company']} | {client['email']} | {client['position']}")


def update_client(new_client_name, updated_client_name):
	global clients

	response = search_client(updated_client_name)
	print(response)

	if response["exists"]:
		response["client"].update(new_client_name)
	# for client in clients:
	# 	if updated_client_name in client['name']:
	# 		client.update({'name': new_client_name})
	# 		break


def delete_client(client_name):
	global clients

	response = search_client(client_name)

	if response["exists"]:
		clients.pop(response["idx"])
		return True
	return False
	# for idx, client in enumerate(clients):
	# 	# print(type(idx), client)
	# 	if client_name == client['name'].lower():
	# 		clients.pop(idx)
	# 		return True
	# return False 


def search_client(client_name):
	global clients

	for idx, client in enumerate(clients):
		if client['name'].lower() == client_name.lower():
			return {"idx": idx, "exists": True, "client": client}
	return {"idx": False, "exists": False, "client": None}


def _print_welcome():
	print('WELCOME TO PLATZI VENTAS')
	print('*' * 50)
	print('What would you like to do today?')
	print('[C]reate client')
	print('[L]ist client')
	print('[U]pdate client')
	print('[D]elete client')
	print('[S]earch client')


def _get_client_field(field_name):
	field = None

	while not field:
		field = input(f'What is the client {field_name}: ')
	
	return field


def _get_client_name():
	client_name = None

	while not client_name:
		client_name = {
			'name': _get_client_field('name'),
			'company': _get_client_field('company'),
			'email': _get_client_field('email'),
			'position': _get_client_field('position'),
		}

		if client_name == 'exit':
			client_name = None
			break
		
	if not client_name:
			sys.exit()

	return client_name


if __name__ == '__main__':
	_initialize_clients_from_storage()

	_print_welcome()

	command = input('').upper()

	if command == 'C':
		client = {
			'name': _get_client_field('name'),
			'company': _get_client_field('company'),
			'email': _get_client_field('email'),
			'position': _get_client_field('position')
		}
		create_client(client)
	elif command == 'L':
		list_client()

	elif command == 'D':
		client_name = _get_client_name()
		deleted = delete_client(client_name)

		if deleted:
			print("User deleted Successful")
		else:
			print("User not found")

	elif command == 'U':
		updated_client_name = input('Search by name: ')
		new_client_name = _get_client_name()
		update_client(new_client_name, updated_client_name)

	elif command == 'S':
		client_name = _get_client_name()
		found = search_client(client_name)

		if found["exists"]:
			print('The client is in the client\'s list')
		else:
			print(f'The client: {client_name} is not in our client\'s list')

	else:
		print('Invalid Command')

	_save_client_to_storage()