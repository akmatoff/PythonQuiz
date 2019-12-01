import csv
from colored import fg, attr

red = fg('red')
green = fg('green')
blue = fg('blue')
yellow = fg('yellow')
reset = attr('reset')

usernames = []
logpass = []

def login_form():
  print("- Авторизация - ".center(70))

  global login
  login = input("Введите логин: ")
  password = input("Введите пароль: ")

  with open('users.csv', newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    while login == '' and password == '':
      login_form()

    for row in csv_reader:
      username = row[0]
      usernames.append(username)
  if login in usernames:
    with open('users.csv', newline = '') as read_csv:
      reader = csv.reader(read_csv, delimiter = ',')
      for r in reader:
        if login == r[0] and password == r[1]:
          print(green + "Добро пожаловать в тесты по Python!" + reset)
          break
      if password != r[1]:
        print(red + "Неверный логин или пароль! Повторите попытку!" + reset)
        login_form()
  else:
    print(yellow + "Пользователь не найден, пройдите регистрацию." + reset)
    register_form()

def register_form():
  print("- Регистрация - ".center(70))

  login = input("Введите логин: ")
  password = input("Введите пароль: ")
  confirm = input("Повторите пароль для подтверждения: ")
  
  if confirm == password:
    logpass.append(login)
    logpass.append(password)
    with open('users.csv', 'a') as users_csv:
      writer = csv.writer(users_csv)
      writer.writerow(logpass)
  else:
    print(red + "Пароли не совпадают! Попробуйте еще раз!" + reset)
    register_form()
    
  print(green + "Регистрация успешно завершена!" + reset)
  