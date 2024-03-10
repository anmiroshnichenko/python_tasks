# def vote(votes):
#     unique_vote = set(votes)
#     dict_vote = {}
#     for num in unique_vote:
#         dict_vote[num] = votes.count(num)
#     return max(dict_vote, key=dict_vote.get)

# Решение эксперта
def vote(votes):
    d = {}
    for v in votes:
        d.setdefault(v, 0)        
        d[v] += 1    
    sorted_by_count = sorted(d.items(), key=lambda a: a[1], reverse=True)
    return sorted_by_count[0][0]

if __name__ == '__main__':
    print(vote([1,1,1,2,3]))
    print(vote([1,2,3,2,2]))

# dic = {}
# v = 1 
# dic.setdefault(v, 0)
# dic[v] += 1
# v = 1 
# dic.setdefault(v, 0)
# dic[v] += 1
# v = 1 
# dic.setdefault(v, 0)
# dic[v] += 1
# v = 2
# dic.setdefault(v, 0)
# dic[v] += 1
# v = 3 
# dic.setdefault(v, 0)
# dic[v] += 1
# print(dic)

#В результате корректного выполнения задания будет выведен следующий результат:
#1 1
#2 2