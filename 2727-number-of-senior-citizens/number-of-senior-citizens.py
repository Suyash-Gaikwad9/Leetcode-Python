class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0

        

        for d in details:
            
            s = d[11] + d[12]

            if int(s) > 60:
                res += 1
        
        return res