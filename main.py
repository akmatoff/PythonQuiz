import csv, authorize
from colored import fg, attr

red = fg('red')
green = fg('green')
yellow = fg('yellow')
reset = attr('reset')

question_list = []
answer1_list = []
answer2_list = []
answer3_list = []
correct_answer_list = []

question_num = 1
count_correct_answers = 0

mark = ''
score = []
result = []

with open('quiz.csv', newline='') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=";")
  for row in csv_reader:
    question = row[0]
    answer1 = row[1]
    answer2 = row[2]
    answer3 = row[3]
    correct_answer = row[4]

    question_list.append(question)
    answer1_list.append(answer1)
    answer2_list.append(answer2)
    answer3_list.append(answer3)
    correct_answer_list.append(correct_answer)

auth = input("Введите цифру " + yellow + "1 " + reset + "для авторизации, или цифру" + green + " 2 " + reset + "для регистрации: ")

if auth == "1":
  authorize.login_form()
elif auth == "2":
  authorize.register_form()
while auth != "1" and auth != "2":
  auth = input("Введите цифру 1 для авторизации, или цифру 2 для регистрации")
  
while question_num < len(question_list):
  print(yellow + 'Вопрос №' + str(question_num) + ':' + reset + question_list[question_num])
  print(yellow + 'a) ' + reset + answer1_list[question_num])
  print(yellow + 'b) ' + reset + answer2_list[question_num])
  print(yellow + 'c) ' + reset + answer3_list[question_num])
  user_option = input("Выберите вариант ответа(a,b,c): ")

  if user_option == 'a': 
    a = answer1_list[question_num]
    if a == correct_answer_list[question_num]:
      print(green + "Ответ верный! Вы заработали 5 баллов!" + reset)
      score.append(5)
      count_correct_answers += 1
    else:
      print(red + "Ответ неверный! Вы не заработали баллы за этот вопрос." + reset)
  elif user_option == 'b':
    b = answer2_list[question_num]
    if b == correct_answer_list[question_num]:
      print(green + "Ответ верный! Вы заработали 5 баллов!" + reset)
      score.append(5)
      count_correct_answers += 1
    else:
      print(red + "Ответ неверный! Вы не заработали баллы за этот вопрос." + reset)
  elif user_option == 'c':
    c = answer3_list[question_num]
    if c == correct_answer_list[question_num]:
      print(green + "Ответ верный! Вы заработали 5 баллов!" + reset)
      score.append(5)
      count_correct_answers += 1
    else:
      print(red + "Ответ неверный! Вы не заработали баллы за этот вопрос." + reset)
  else:
    print("Такого варианта ответа не существует!")

  question_num += 1

totalscore = sum(score)

print("Поздравляю! Вы завершили тест по Python. Количество набранных баллов: " + green + str(totalscore) + reset)
print("Количество правильных ответов: " + green + str(count_correct_answers) + reset + " из " + green + str(len(question_list) - 1) + reset)

if totalscore == 100:
  print("Ваша оценка: A")
  mark += 'A'
elif totalscore >= 95:
  print("Ваша оценка: A-")
  mark += 'A-'
elif totalscore >= 90:
  print("Ваша оценка: B+")
  mark += 'B+'
elif totalscore >= 87:
  print("Ваша оценка: B")
  mark += 'B'
elif totalscore >= 85:
  print("Ваша оценка: B-")
  mark += 'B-'
elif totalscore >= 80:
  print("Ваша оценка: C+")
  mark += 'C+'
elif totalscore >= 77:
  print("Ваша оценка: C")
  mark += 'C'
elif totalscore >= 75:
  print("Ваша оценка: C-")
  mark += 'C-'
elif totalscore >= 70:
  print("Ваша оценка: D+")
  mark += 'D+'
elif totalscore >= 67:
  print("Ваша оценка: D")
  mark += 'D'
elif totalscore >= 65:
  print("Ваша оценка: D-")
  mark += 'D-'
else:
  print("Ваша оценка: F")
  mark += 'F'

result.append(authorize.login)
result.append(str(totalscore))
result.append(mark)
      
with open('results.csv', 'a', newline = '') as  write_result:
  writer = csv.writer(write_result)
  writer.writerow(result)

print("")
print("Логин \t Количество баллов \t Оценка")

with open('results.csv', newline = '') as read_result:
  reader = csv.reader(read_result, delimiter = ",")
  for res in reader:
    print('\t'.join(res))
