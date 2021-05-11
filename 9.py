from time import sleep
group=['디랩', 'chloe', 'daddy']

#로그인
print('로그인하기 위해 닉네임을 입력하세요.')
currentUser=input("닉네임: ")
group.append(currentUser)
print (currentUser, "님 로그인 되었습니다.")
print ("현재 접속자: ", group)

sleep(5)

#로그아웃
print("로그아웃할 사용자의 닉네임을 입력하세요.")
outUser=input("닉네임: ")
group.remove(outUser)
print (outUser, "님, 로그아웃 되었습니다.")
print ("현재 접속자: ", group)