#ffalta o favorito
def add_contact(contacts, name, telephone, email):
  contact = {"nome": name, "telefone": telephone, "email": email, "favorita": False }
  contacts.append(contact)
  print(f"O seguinte contato foi adicionado a sua lista:\nNome: {name}\nTelefone: {telephone}\nEmail: {email}")
  return

def show_contacts(contacts):
  print("\nLista de contatos: ")
  for index, contact in enumerate(contacts, start=1):
    contact_name = contact["nome"]
    contact_telephone = contact["telefone"]
    contact_email = contact["email"]
    contact_favorite = "Sim" if contact["favorita"] else "Não"
    print(f"{index}. Nome: {contact_name}, Email: {contact_email}, Telefone: {contact_telephone}, Favorita: {contact_favorite}")
  return

def update_contacts(contacts, contact_index, updated_contact_name, updated_contact_telephone, updated_contact_email):
  adjusted_contact_index = int(contact_index) - 1
  if adjusted_contact_index >= 0 and adjusted_contact_index < len(contacts):
    contacts[adjusted_contact_index]["nome"] = updated_contact_name
    contacts[adjusted_contact_index]["telefone"] = updated_contact_telephone
    contacts[adjusted_contact_index]["email"] = updated_contact_email
    print(f"Os dados foram atualizados para: \nNome: {updated_contact_name}\nTelefone: {updated_contact_telephone}\nEmail: {updated_contact_email}")
  else:
    print("Indice do contato invalido")
  return

def mark_as_favorite(contacts, contact_index):
  adjusted_contact_index = int(contact_index) - 1
  if contacts[adjusted_contact_index]["favorita"] == False:
    contacts[adjusted_contact_index]["favorita"] = True
    print(f"\ncontato {contact_index} marcado como favorito")
  else:
    print(f"\nNão é possivel realizar essa ação, pois o contato {contact_index} ja esta marcado como favorito")
  return

def unmark_favorite(contacts, contact_index):
  adjusted_contact_index = int(contact_index) - 1
  if contacts[adjusted_contact_index]["favorita"] == True:
    contacts[adjusted_contact_index]["favorita"] = False
    print(f"\ncontato {contact_index} desmarcado como favorito")
  else:
    print(f"\nNão é possivel realizar essa ação, pois o contato {contact_index} não é um contato favorito")
  return

def show_favorite_contacts(contacts):
  print("\nLista de contatos favoritos: ")
  for index, contact in enumerate(contacts, start=1):
    if contact["favorita"]:
      contact_name = contact["nome"]
      contact_telephone = contact["telefone"]
      contact_email = contact["email"]
      print(f"{index}. Nome: {contact_name}, Email: {contact_email}, Telefone: {contact_telephone}")
  return 

def delete_contact(contacts, contact_index):
  adjusted_contact_index = int(contact_index) - 1
  delete_contact = contacts[adjusted_contact_index]
  contacts.remove(delete_contact)
  print(f"\nO contato {contact_index} foi removido da lista de contato")
  return
    

contacts = []

while True:
  print("\nAgenda de contatos")
  print("1. Adicionar contato")
  print("2. Visualizar lista de contatos")
  print("3. Editar contato")
  print("4. Marcar contato como favorito")
  print("5. Desmarcar contato como favorito")
  print("6. Visualizar contatos marcados como favorito")
  print("7. Deletar contato")
  print("8. Sair")

  option = input("Escolha a opção desejada: ")

  if option == '1':
    contact_name = input("Digite o nome do contato: ")
    contact_telephone = input("Digite o telefone do contato: ")
    contact_email = input("Digite o email do contato: ")
    add_contact(contacts, contact_name, contact_telephone, contact_email)

  if option == '2':
    show_contacts(contacts)

  if option == '3':
    show_contacts(contacts)
    contact_index = input("Confirme o contato que deseja atualizar: ")
    new_contact_name = input("Confirme o nome: ")
    new_contact_telephone = input("Confirme o telefone: ")
    new_contact_email = input("Confirme o email: ")
    update_contacts(contacts, contact_index, new_contact_name, new_contact_telephone, new_contact_email)

  if option == '4':
    show_contacts(contacts)
    contact_index = input("Confirme o contato que deseja marcar como favorito: ")
    mark_as_favorite(contacts, contact_index)

  if option == '5':
    show_contacts(contacts)
    contact_index = input("Confirme o contato que deseja desmarcar como favorito: ")
    unmark_favorite(contacts, contact_index)

  if option == '6':
    show_favorite_contacts(contacts)
  
  if option == '7':
    show_contacts(contacts)
    contact_index = input("Confirme o contato que deseja deletar: ")
    delete_contact(contacts, contact_index)  

  if option == '8':
    break

print("Programa finalizado.")