import csv

usernames = []
logpass = []

def login_form():
  print("- Авторизация - ".center(70))

  login = input("Введите логин: ")
  password = input("Введите пароль: ")

  with open('users.csv', newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    for row in csv_reader:
      username = row[0]
      usernames.append(username)
      if login in usernames:
        if password == row[1]:
          print("Добро пожаловать в тесты по Python!")
          break
        else:
          print("Неверный пароль! Попробуйте еще раз!")
          login_form()
    if not login in usernames:
      print("Пользователь не найден, пройдите регистрацию!")
      register_form()

def register_form():
  print("- Регистрация - ".center(70))

  login = input("Введите логин: ")
  password = input("Введите пароль: ")
  confirm = input("Повторите пароль для подтверждения: ")
  
  if confirm != password:
    print("Пароли не совпадают! Попробуйте еще раз!")
    register_form()
  else:
    logpass.append(login)
    logpass.append(password)
    with open('users.csv', 'a') as users_csv:
      writer = csv.writer(users_csv)
      writer.writerow(logpass)

  print("Регистрация успешно завершена!")


        


      






    

      
    





