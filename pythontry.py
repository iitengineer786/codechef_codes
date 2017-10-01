def allsubstr(str):
    return [str[i:j+1] for i in range(len(str)) for j in range(i, len(str))]

def getpalindromes_trincot(aList):

    def collectLeft(common, needle, i, j):
        if i > j:
            return [common + needle + common[::-1]] if needle == needle[::-1] else []
        results = []
        for seq in aRevList[j]:
            if seq.startswith(needle):
                results += collectRight(common+needle, seq[len(needle):], i, j-1)
            elif needle.startswith(seq):
                results += collectLeft(common+seq, needle[len(seq):], i, j-1)
        return results

    def collectRight(common, needle, i, j):
        if i > j:
            return [common + needle + common[::-1]] if needle == needle[::-1] else []
        results = []
        for seq in aList[i]:
            if seq.startswith(needle):
                results += collectLeft(common+needle, seq[len(needle):], i+1, j)
            elif needle.startswith(seq):
                results += collectRight(common+seq, needle[len(seq):], i+1, j)
        return results

    aRevList = [[seq[::-1] for seq in seqs] for seqs in aList]
    return collectRight('', '', 0, len(aList)-1)

# sample input and call:
t=int(raw_input())
while(t>0):
    n,k=map(int,raw_input().split())
    ls=[0]*n
    for i in range(k):
        a,b=map(int,raw_input().split())
        ls[a-1]=b
    count=0
    input1=''.join(map(str,ls))
    input=[]
    input.append(input1)
    aList = [allsubstr(word) for word in input]
    result = getpalindromes_trincot(aList)
    for i in range(len(result)):
        if(len(result[i])%2!=0 ):
            count=count+1
    print(count)
    t=t-1