
from collections import Counter   #引入Counter
import itertools
from compute_iou import compute_iou

def compare_scores(n, s, a):

    b = dict(Counter(n))
    c = [key for key,value in b.items()if value > 1]


    print (c)  #只展示重复元素
    scores_num = []
    rest_item = []
    # print ({key:value for key,value in b.items()if value > 1})
    for val in c:
        rest_item = s
        items = [i for i, x in enumerate(n) if x == val]
        print(items)
        for i in items:
            scores_num.append(s[i])
        print(scores_num)
        # max_num = max(scores_num)
        # max_key = a[s.index(max_num)]
        # print(max_key)
        # scores_num.remove(max_num)
        # print(scores_num)
        cc = list(itertools.combinations(scores_num, 2))
        print(cc)
        for i in cc:
            x, y = i
            rec1 = a[s.index(x)]
            rec2 = a[s.index(y)]
            IOU = compute_iou(rec1, rec2)
            if IOU > 0.5:
                if x > y :
                    del a[s.index(y)]
                    del n[s.index(y)]
                else:
                    del a[s.index(x)]
                    del n[s.index(x)]

        print(a)
        print(n)
        return a, n

    # for var in scores_num:
    #     x = a[s.index(var)]
    #     print(x)
    #     IOU = compute_iou(max_key, x)
    #     print(IOU)

if __name__ == '__main__':
    n = ['Aqua', 'Chartreuse', 'Chartreuse', 'Chartreuse']
    a = [(0.1504717469215393, 0.3192671537399292, 0.7737396359443665, 0.7255864143371582), (0.2575419545173645, 0.7287904620170593, 0.40175914764404297, 0.8005940318107605), (0.2083992213010788, 0.2431357204914093, 0.3656202554702759, 0.33222541213035583), (0.19882851839065552, 0.20809637010097504, 0.3971494436264038, 0.3327826261520386)]
    s = [0.9999914, 0.6982285, 0.6716356, 0.5245897]
    res1, res2 = compare_scores(n, s, a)
    box_to_color_map = []
    res1, res2 = compare_scores(n, s, a)
    for i in range(len(res1)):
        box_to_color_map.append((res1[i], res2[i]))

    print(box_to_color_map)

#     if len(id1) == 2:
#         print("IOU")
#     else:
#         for i in range(len(id1)):
#
#
#
#
#
# id1 = [i for i, x in enumerate(a) if x==15]
# print(id1)

i = 0
j = 0
# for j in range(len(c)-1):
#     idx = [i for i, x in enumerate(X) if x == 1]
#     for i in range(len(a)-1):
#         if a[i] == c[j]:
#             iou =
#             i++
#         else