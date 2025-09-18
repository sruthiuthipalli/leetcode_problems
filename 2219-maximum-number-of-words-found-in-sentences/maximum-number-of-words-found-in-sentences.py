class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        l=0
        for i in range(len(sentences)):
            w=sentences[i].split()
            s=len(w)
            l=max(s,l)
        return l    

        