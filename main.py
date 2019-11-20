import csv, authorize

question_list = []
answer1_list = []
answer2_list = []
answer3_list = []
correct_answer_list = []

score = []

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

authorize.login_form()




