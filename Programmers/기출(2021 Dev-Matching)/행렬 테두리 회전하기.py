'''
2021 Dev-Matching: 웹 백엔드 개발자(상반기) 
Lv2 행렬 테두리 회전하기
>> 바로 4방향 경우따라 구현하는게 더 편할지도 모름 
   cur, next을 저장 
   다음턴에는 next가 cur로 이게 왜 생각이 안났을까!!

'''

# 45점 코드 나머지는 시간초과  -> 같은 방식이 C++로는 돌아간다.....  원인: deepcopy가 오래걸림
import copy


def solution(rows, columns, queries):
    
    #동남서북
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
     
    
    answer = []
    matrix=[[i+(j*columns) for i in range(1,columns+1)] for j in range(rows)]
    mm=copy.deepcopy(matrix)
    
    if len(queries)<2:
        answer.append(matrix[queries[0][0]-1][queries[0][1]-1])  
    else:
        
        for y1,x1,y2,x2 in queries:
            my,mx=y1,x1
            temp=[]
            DIR =0 
            while(1):

                temp.append(mm[my-1][mx-1])

                mx+=dx[DIR]
                my+=dy[DIR]

                matrix[my-1][mx-1]=temp[-1]

                if  (mx==x2 and my==y1) or (mx==x2 and my==y2) or (mx==x1 and my==y2):
                    DIR+=1
                    #print(DIR,temp)

                if mx==x1 and my==y1:
                    mm=copy.deepcopy(matrix)
                    answer.append(min(temp))
                    break

    return answer


# 100점 copy 없이 이전수 다음수를 저장한 방법으로 다시 구현 

def solution(rows, columns, queries):
    
    # 동서남북
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
     
    answer = []
    matrix=[[i+(j*columns) for i in range(1,columns+1)] for j in range(rows)]
    
        
    for y1,x1,y2,x2 in queries:
        my,mx=y1,x1
        DIR =0 
        cur=ans=matrix[my-1][mx-1]

        while(1):

            mx+=dx[DIR]
            my+=dy[DIR]
            next = matrix[my-1][mx-1]
            
            if ans> next :
                ans= next

            matrix[my-1][mx-1]= cur
            cur=next

            if  (mx==x2 and my==y1) or (mx==x2 and my==y2) or (mx==x1 and my==y2):
                DIR+=1
                # print(DIR,temp)

            if mx==x1 and my==y1:
                answer.append(ans)
                #print(*matrix,sep='\n')
                break

    return answer