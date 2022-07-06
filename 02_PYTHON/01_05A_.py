# 주소록 정보 확인 - 이름으로 검색하여 정보 보기
from tkinter import *
import pandas as pd
import os
# global dat

print(os.getcwd())
print(os.listdir())

#%%
dat = pd.read_excel("./address.xlsx", "두번째시트")
print(dat)


def click():
    # pass
    word = entry.get()  # 아래 엔트리 상자의 내용을 text로 넣는다.
    # END로 지정하면 문자열이 입력된 최종 입력 지점을 의미.
    # 특정 시작 지점부터 텍스트 엔트리 위젯의 끝까지 모두 지우기 위해 END를 쓴다.
    output.delete(0.0, END) # 텍스트 박스 내용을 지운다.

    try:
        def_word = dat.loc[dat['이름']==word, '전화번호'].values[0]
    except:
        def_word = "해당 이름을 찾을 수 없습니다."
        # dat = window_add(dat)

    print(def_word)
    output.insert(END, def_word)

# 메인 :
window = Tk()
window.title("전화번호부")

# 01 입력 상자 설명 레이블 
label = Label(window, text="찾을 사람 이름을 입력 후, 엔터 키 누르기")
label.grid(row=0, column=0, sticky=W)

# 02 텍스트 입력이 가능한 상자(Entry)
entry = Entry(window, width=15, bg="light green")
entry.grid(row=1, column=0, sticky=W)

# 03 제출 버튼 추가
btn = Button(window, text="검색", width=5, command=click)
btn.grid(row=2, column=0, sticky=W)

# 04 설명 레이블
lable2 = Label(window, text="\n전화번호:")
lable2.grid(row=3, column=0, sticky=W)

# 05 텍스트 박스 입력 상자
# columnspan=2 는 (4,0)~(4,1) 위치까지 분포
output = Text(window, width=30, height=2, wrap=WORD, background="light green")
output.grid(row=4, column=0, columnspan=2, sticky=W)

# 메인 반복문 실행
window.mainloop()