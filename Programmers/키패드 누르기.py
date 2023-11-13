'''
[카카오 인턴] 키패드 누르기 Lv1

문제
https://school.programmers.co.kr/learn/courses/30/lessons/67256

>> 문제요구사항을 잘 읽자
   딕셔너리 활용
   
'''
pos={1:(0,0),2:(1,0),3:(2,0),4:(0,1),5:(1,1),6:(2,1),7:(0,2),8:(1,2),9:(2,2),0:(1,3)}

def solution(numbers, hand):
    answer = ''
    left=(0,3)
    right=(2,3)
    
    for n in numbers:
        x,y=pos[n]
         
        if x==0:  # 1 4 7 
            answer+="L"
                
        elif x==2:  # 3 6 9
            answer+="R"
                      
        else:
            # 2 5 8 0
            dist_l= abs(x-left[0])+ abs(y-left[1])
            dist_r= abs(x-right[0])+ abs(y-right[1])

            # print("n:%d L:%d R:%d"%(n,dist_l,dist_r))
            # print(left,right)
            
            if dist_l<dist_r:
                answer+="L"               
            elif dist_l>dist_r:
                answer+="R"   
            else:
                answer+=hand[0].upper()
        
        if answer[-1]=="R":
            right=(x,y)
        else:
            left=(x,y)
            
    return answer