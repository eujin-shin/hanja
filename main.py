import random

class hanja:

  def __init__(self, num, character, sound, mean):
    self.num = num
    self.character = character
    self.sound = sound
    self.mean = mean
    self.score = 0

  def printhanja(self):
    print(self.character)

hanja_list = []


# hanja list 입력 받기 (파일명 전달 받음)
def Input_data(filename, size):
  file = open(filename, "r")
  input_list = file.readlines()
  for data in input_list:
    character, mean, sound = data.split(',')
    if '\n' in sound:
      sound = sound.split('\n')[0]
    newhanja = hanja(size, character, sound, mean)
    hanja_list.append(newhanja)
    size += 1
  file.close();
  return hanja_list

def Make_Quiz(n):
  quiz_index = []
  while(len(quiz_index)!=4):
    x = random.randint(0, n-1)
    if x in quiz_index:
      continue
    else:
      quiz_index.append(x)
  x = random.randint(0, 3)
  return quiz_index[x], quiz_index

# 뜻을 맞히는 퀴즈 (출제~결과 기록 & 오답출력)
def Quiz_mean(quizlist, n):
  quiz_wronglist = []
  for i in range(n):
    ans, quiz = Make_Quiz(len(quizlist))
    ans_code = quizlist[ans].num

    print("다음 한자의 뜻을 고르시오 : ", quizlist[ans].character)
    print("-------------------------")
    for j in range(4):
      print(j+1, ":", quizlist[quiz[j]].mean)
    print("-------------------------")
    input_ans = int(input())

    if input_ans==quiz.index(ans)+1:
      print("맞았습니다!")
      print(len(hanja_list))
      print(ans_code, hanja_list[ans_code].score)
      hanja_list[ans_code].score += 1
    else:
      print("틀렸습니다.")
      print("**", quizlist[ans].character, quizlist[ans].mean, quizlist[ans].sound)
      hanja_list[ans_code].score -= 1
      quiz_wronglist.append(quizlist[ans])
    del quizlist[ans]

  print("퀴즈가 종료되었습니다.")
  print("총 %d 문제 중 %d 문제를 맞혔습니다." % (n, n-len(quiz_wronglist)))
  if(len(quiz_wronglist)>0):
    print("틀린 문제는 다음과 같습니다.")
    print("-------------------------")
    for i in range(len(quiz_wronglist)):
      print(quiz_wronglist[i].character, quiz_wronglist[i].mean, quiz_wronglist[i].sound)


# 음을 맞히는 퀴즈 (출제~결과 기록 & 오답출력)
def Quiz_sound(quizlist, n):
  quiz_wronglist = []
  for i in range(n):
    ans, quiz = Make_Quiz(len(quizlist))
    ans_code = quizlist[ans].num

    print("다음 한자의 음을 고르시오 : ", quizlist[ans].character)
    print("-------------------------")
    for j in range(4):
      print(j+1, ":", quizlist[quiz[j]].sound)
    print("-------------------------")
    input_ans = int(input())

    if input_ans==quiz.index(ans)+1:
      print("맞았습니다!")
      hanja_list[ans_code].score += 1
    else:
      print("틀렸습니다.")
      print("**", quizlist[ans].character, quizlist[ans].mean, quizlist[ans].sound)
      hanja_list[ans_code].score -= 1
      quiz_wronglist.append(quizlist[ans])
    del quizlist[ans]

  print("퀴즈가 종료되었습니다.")
  print("총 %d 문제 중 %d 문제를 맞혔습니다." % (n, n-len(quiz_wronglist)))
  if(len(quiz_wronglist)>0):
    print("틀린 문제는 다음과 같습니다.")
    print("-------------------------")
    for i in range(len(quiz_wronglist)):
      print(quiz_wronglist[i].character, quiz_wronglist[i].mean, quiz_wronglist[i].sound)


# 한자 모양을 맞히는 퀴즈 (출제~결과 기록 & 오답출력)
def Quiz_character(quizlist, n):
  quiz_wronglist = []
  for i in range(n):
    ans, quiz = Make_Quiz(len(quizlist))
    ans_code = quizlist[ans].num

    print("다음 한자의 모양을 고르시오 : ", quizlist[ans].mean, quizlist[ans].sound)
    print("-------------------------")
    for j in range(4):
      print(j+1, ":", quizlist[quiz[j]].character)
    print("-------------------------")
    input_ans = int(input())

    if input_ans==quiz.index(ans)+1:
      print("맞았습니다!")
      hanja_list[ans_code].score += 1
    else:
      print("틀렸습니다.")
      print("**", quizlist[ans].character, quizlist[ans].mean, quizlist[ans].sound)
      hanja_list[ans_code].score -= 1
      quiz_wronglist.append(quizlist[ans])
    del quizlist[ans]

  print("퀴즈가 종료되었습니다.")
  print("총 %d 문제 중 %d 문제를 맞혔습니다." % (n, n-len(quiz_wronglist)))
  if(len(quiz_wronglist)>0):
    print("틀린 문제는 다음과 같습니다.")
    print("-------------------------")
    for i in range(len(quiz_wronglist)):
      print(quiz_wronglist[i].character, quiz_wronglist[i].mean, quiz_wronglist[i].sound)

# wrong list 작성하여 파일로 출력
def List_wrong(hanja_list, filename):
  wrong_hanja_file = open(filename, "w")
  count = 0
  for i in range(len(hanja_list)):
    if hanja_list[i].score<0:
      data = hanja_list[i].character + ',' + hanja_list[i].mean + ',' + hanja_list[i].sound + '\n'
      wrong_hanja_file.write(data)
      count+=1
  if count==0:
    print("틀린 한자가 없습니다.")
  else:
    wrong_hanja_file.close()
    print("%s에 %d개의 오답이 저장되었습니다." % (filename, count))


print("*** 한자 학습 프로그램입니다. ***")
print("학습을 위해 한자 데이터가 저장된 파일 명을 입력해 주세요.")
filename = input("(0 입력 시 기본 파일을 불러옵니다.) : " )
if int(filename)==0:
  filename = "hanja.csv"
hanja_list = Input_data(filename, len(hanja_list))
size = len(hanja_list)

while(1):
  print("1. 퀴즈 풀기")
  print("2. 오답 목록 저장하기")
  print("3. 종료하기")
  order = int(input("실행할 기능을 입력하세요 : "))
  
  if order==1:
    while(1): 
      n = int(input("퀴즈의 문제 수를 입력하세요 : "))
      if n<=size:
        break
      else:
        print(size, "보다 작은 수를 입력해 주세요")
    
    while(1):
      print("1. 음 맞추기 퀴즈")
      print("2. 뜻 맞추기 퀴즈")
      print("3. 한자 모양 맞추기 퀴즈")
      order_quiz = int(input("퀴즈의 유형을 선택하세요 : "))
      if order_quiz>3 or order_quiz<1:
        print("다시 입력해 주세요.")
      else:
        break
    quizlist = hanja_list.copy()

    if order_quiz==1:
      Quiz_sound(quizlist, n)
    elif order_quiz==2:
      Quiz_mean(quizlist, n)
    elif order_quiz==3:
      Quiz_character(quizlist, n)
  elif order==2:
    wrong_filename = input("오답을 저장할 파일명을 입력해 주세요. (csv, txt 확장자 등) : ")
    List_wrong(hanja_list, wrong_filename)
  elif order==3:
    print("프로그램을 종료합니다.")
    break;