"""Your task is to complete the function commonElements() which take the 3 arrays A[], B[], C[] and their respective sizes n1, n2 and n3 as inputs and returns an array containing the common element present in all the 3 arrays in sorted order.

If there are no such elements return an empty array. In this case the output will be printed as -1."""

class common():
    def commonElements(self):
        a = [1, 5, 10,20, 40, 80]
        b = [6, 7, 20, 80, 100]
        c = [3, 4, 15, 20, 30, 70, 80, 120]
        common = []
        for i in a:
            for j in b:
                for k in c:
                    if i==j and j==k:
                        common.append(i)
        if len(common)==0:
            print("-1")
        else:
            print(common)

c = common()
c.commonElements()
