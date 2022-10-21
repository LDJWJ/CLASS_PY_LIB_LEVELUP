# tkinter 기본 학습 내용
# 01. 기본창 사이즈 지정
# 02. 각종 클래스 객체 사용
# 03. 버튼 클릭시의 동작 함수 설정

from tkinter import *

window = Tk()
window.geometry("300x200")  # 기본 창 사이즈 지정
window.title("My Program")

def program_quit():
    print("버튼 선택!")
    window.destroy()  # 종료

def Text_Clear():
    print("버튼 선택!")
    output.delete(0.0, END) # 텍스트 박스 내용을 지운다.


# 01. 입력 상자 설명 레이블
label = Label(window, text="프로그램 시작")
label.grid(row=0, column=0, sticky=W)

# 02. 텍스트 입력이 가능한 상자(Entry)
entry = Entry(window, width=15, bg="dark orange")
entry.grid(row=1, column=0, sticky=W)

label = Label(window, text="내용 입력 Text 상자")
label.grid(row=2, column=0, sticky=W)

# 03. 텍스트 박스 입력 상자
output = Text(window, width=50, height=6, wrap=WORD, background="light green")
output.grid(row=3, column=0, columnspan=2, sticky=W)

# 04. 버튼 추가
label = Button(window, text="CLEAR", command=Text_Clear)
label.grid(row=4, column=0, sticky=W)

# 05. 버튼 추가
label = Button(window, text="프로그램 종료", command=program_quit)
label.grid(row=4, column=1, sticky=W)

window.mainloop()

# 실습. 6행, 7행에 레이블과 버튼을 각각 추가해 보기