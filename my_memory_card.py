from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from random import *

def click_OK():
    if btn.text() == 'Ответить':
        check_answer()
    else:
        next_question()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        win.score += 1

    else:
        show_correct('Неверно!')
    print('Статистика')
    print('Всего вопросов: ', win.total)
    print('Правильных ответов: ', win.score)
    print('Рейтинг: ', (win.score/win.total*100), '%')

def next_question():
    win.total += 1
    q = questions_list[randint(0, len(questions_list) - 1)]
    ask(q)

def show_correct(qw):
    lb_Result.setText(qw)
    show_result()

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer) 
    show_question()

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn.setText('Следующий вопрос')

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

app = QApplication([])
win = QWidget()

win.score = 0
win.total = 0

questions_list = [] 
questions_list.append(Question('Изучаемый язык', 'Python', 'C#', 'Pascal', 'JS'))
questions_list.append(Question('Земля какая по счёту от солнца?', '3', '1', '2', '4'))
questions_list.append(Question('Какой сейчас год?', '2023', '2032', '2302', '2002'))

btn = QPushButton('Ответить') 
lb_Question = QLabel('Вопрос!')

RadioGroupBox = QGroupBox("Варианты ответов") 

rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) 

RadioGroupBox.setLayout(layout_ans1) 

AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('правильно или нет?') 
lb_Correct = QLabel('ответ')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter)
AnsGroupBox.setLayout(layout_res)
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line2)
layout_card.addLayout(layout_line3)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
win.setLayout(layout_card)

btn.clicked.connect(click_OK)
next_question()

win.show()
app.exec()
