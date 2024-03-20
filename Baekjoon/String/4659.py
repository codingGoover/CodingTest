'''
4659번 비밀번호 발음하기 실버5

문제

1. 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
2. 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
3. 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.

입력
입력은 여러개의 테스트 케이스로 이루어져 있다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 테스트할 패스워드가 주어진다.

마지막 테스트 케이스는 end이며, 패스워드는 한글자 이상 20글자 이하의 문자열이다. 또한 패스워드는 대문자를 포함하지 않는다.

출력
각 테스트 케이스를 '예제 출력'의 형태에 기반하여 품질을 평가하여라.

예제 입력 1 
a
tv
ptoui
bontres
zoggax
wiinq
eep
houctuh
end

예제 출력 1 
<a> is acceptable.
<tv> is not acceptable.
<ptoui> is not acceptable.
<bontres> is not acceptable.
<zoggax> is not acceptable.
<wiinq> is not acceptable.
<eep> is acceptable.
<houctuh> is acceptable.

'''
import sys
input=sys.stdin.readline

while True:
    pw= input().rstrip()
    if pw=='end':
        break
    flag=False
   
    if pw.find('a')!=-1 or pw.find('e')!=-1 or pw.find('i')!=-1 or pw.find('o')!=-1 or pw.find('u')!=-1:
        flag=True
        aeiou=['a','e','i','o','u']
        for i in range(0,len(pw)-2):
            if pw[i] in aeiou and pw[i+1] in aeiou and pw[i+2] in aeiou:
                flag=False
                break
            if pw[i] not in aeiou and pw[i+1] not in aeiou and pw[i+2] not in aeiou:
                flag=False
                break
            
        if flag:    
            for i in range(len(pw)-1):
                if pw[i]=='e' or pw[i]=='o':
                    pass
                elif pw[i]==pw[i+1]:
                    flag=False
                    break
    
    if flag:
        print(f'<{pw}> is acceptable.')
    else:
        print(f'<{pw}> is not acceptable.')

        
# 찾아본코드 우아 깔끔하다
vowel = {'a','e','i','o','u'}
while (1):
	test = sys.stdin.readline().rstrip()
	if test == 'end':
		break
	pw = list(test)
	v_flag = 0 # 모음 존재하는지 확인
	v_cnt = 0  # 모음 3개 연속인지 확인
	c_cnt = 0  # 자음 3개 연속인지 확인
	err = 0  # 같은 문자 연속 2개 or 자음/모음 연속 3개인 경우 1
	for i in range(len(pw)):
		if i > 0:
			if pw[i] == pw[i-1]:
				if pw[i] != 'e' and pw[i] != 'o':
					err = 1
					break
		if pw[i] in vowel:
			v_flag = 1
			v_cnt += 1
			c_cnt = 0
			if v_cnt == 3:
				err = 1
				break
		else:
			v_cnt = 0
			c_cnt += 1
			if c_cnt == 3:
				err = 1
				break
	
	if (err != 1) and (v_flag == 1):
		print("<"+ test +"> is acceptable.")
	else:
		print("<" + test + "> is not acceptable.")    