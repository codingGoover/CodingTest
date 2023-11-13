'''
성격 유형 검사하기 Lv1

문제
https://school.programmers.co.kr/learn/courses/30/lessons/118666

>> 문제 잘 읽기

'''

kind={"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}

def solution(survey, choices):
    answer = ''
    
    for i,s in enumerate(survey):
        k1,k2=s[0],s[1]
        score= choices[i]-4
        if score<0:
            kind[k1]+=abs(score)
        else:
            kind[k2]+=score
      
    kl= list(kind.items())
    for i in range(0,8,2):
        kitem= kl[i:i+2] 
        kitem.sort(key=lambda x:x[1],reverse=True)
        answer+=kitem[0][0]
    
    # 다른 코드 같은 방식
    kl= list(kind.items())
    for i in range(0,8,2):
        if kl[i+1][1]> kl[i][1]:
            answer+=kl[i+1][0]
        else:
            answer+=kl[i][0]
        
   
    return answer


# 강사 코드
def solution(survey, choices):
    answer = ''
    CHARS=['RT','CF','JM','AN']
    D_IDX={'R':0,'T':0,'C':1,'F':1,'J':2,'M':2,'A':3,'N':3}
    D_REVERSE={'R':False,'T':True,'C':False,'F':True,'J':False,'M':True,'A':False,'N':True}

    scores=[0]*4
    for t,c in zip(survey,choices):
        if D_REVERSE[t[0]]:
            c=8-c
        c= 4-c
        scores[D_IDX[t[0]]]+=c
        
        for idx,s in enumerate(scores):
            if s>=0:
                answer+=CHARS[idx][0]
            else:
                answer+=CHARS[idx][1]
    
    return answer
    