'''
[PCCP 모의고사 #1] 3번 - 유전법칙 Lv2
>> 재귀
재귀 규칙을 찾아야한다
숫자 번호에 따른 전세대의 숫자위치 찾기(몫 x//4), 그로 형질 알아내기(나머지 x%4)
'''

def solution(queries):
    answer = []
    child=['RR','Rr','Rr','rr']
    
    def back(gen,num):
        if gen==1:
            return 'Rr'
        
        parent=back(gen-1,num//4)
        
        if parent=='Rr':
            return child[num%4]
        else:
            return parent

    for q in queries:
        answer.append(back(q[0],q[1]-1))
    
    return answer


# 풀이 보기전, 전부 재귀로 만들었던 완두콩 형질
# def solution(queries):
#     bean={'RR':["RR","RR","RR","RR"],
#           'Rr':["RR","Rr","Rr","rr"],
#           'rr':["rr","rr","rr","rr"]}
		
#     def self_pollination(G,N,gen,kind):
#         if gen>G:
#             return
#         blist[gen-1]+=1
#     #print(G,N,gen,kind,blist[gen-1])
    
#         if gen==G and blist[G-1]==N:
#             answer.append(kind)
#             return

#         for i in range(4):
#             self_pollination(G,N,gen+1,bean[kind][i])     
            
#     for q in queries:
#         blist=[0]*16
#         self_pollination(q[0],q[1],1,'Rr')

#     return answer