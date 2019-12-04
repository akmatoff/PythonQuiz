import csv
from colored import fg, attr

red = fg('red')
green = fg('green')
blue = fg('blue')
yellow = fg('yellow')
reset = attr('reset')

usernames = []
logpass = []

# Авторизоваться или зарегистрироваться
def auth_or_reg():
  auth = input("Введите цифру " + yellow + "1 " + reset + "для авторизации, или цифру" + green + " 2 " + reset + "для регистрации: ")

  if auth == "1":
    login_form()
  elif auth == "2":
    register_form()
  while auth != "1" and auth != "2":
    auth = input("Введите цифру " + yellow + "1 " + reset + "для авторизации, или цифру" + green + " 2 " + reset + "для регистрации: ")
    if auth == "1":
      login_form()
    elif auth == "2":
      register_form()

# Логин форма
def login_form():
  print("- Авторизация - ".center(70))

  global login
  login = input("Введите логин: ")

  with open('users.csv', newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    for row in csv_reader:
      username = row[0]
      usernames.append(username)
  if login in usernames:
    password = input("Введите пароль: ")
    with open('users.csv', newline = '') as read_csv:
      reader = csv.reader(read_csv, delimiter = ',')
      for r in reader:
        if login == r[0] and password == r[1]:
          print(green + "Добро пожаловать!" + reset)
          break
      if password != r[1]:
        print(red + "Неверный логин или пароль! Повторите попытку!" + reset)
        login_form()
  else:
    print(yellow + "Пользователь не найден!" + reset)
    login_form()

# Форма регистрации
def register_form():
  print("- Регистрация - ".center(70))

  login = input("Введите логин: ")
  if login != '':
    with open('users.csv', newline='') as reader:
      csv_reader = csv.reader(reader, delimiter=",")
      for row in csv_reader:
        if login != row[0]:
          password = input("Введите пароль: ")
          confirm = input("Введите пароль еще раз для подтверждения: ")
          if confirm == password:
            logpass.append(login)
            logpass.append(password)
            # Запись в csv файл
            with open('users.csv', 'a') as userswrite:
              writer = csv.writer(userswrite)
              writer.writerow(logpass)
            print(green + "Регистрация успешно завершена!" + reset)
          else: # Если пароли не совпадают
            print(red + "Пароли не совпадают! Попробуйте еще раз!" + reset)
            register_form()
        else:
          print(yellow + "Пользователь уже существует!" + reset)
          auth_or_reg()
  else: # Если логин не введен
    print(red + "Вы не ввели логин!" + reset)
    register_form()
      