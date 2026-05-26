class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
            
        l1, l2 = len(num1), len(num2)
        # 两个数相乘，结果的位数最多是 l1 + l2 位
        result = [0] * (l1 + l2)
        
        # 从后往前遍历
        for i in range(l1 - 1, -1, -1):
            for j in range(l2 - 1, -1, -1):
                # 当前两位数对应的单步乘积
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                
                # 乘积加到对应的低位上（注意：i+j+1 是低位，i+j 是高位）
                p1 = i + j
                p2 = i + j + 1
                total = mul + result[p2]
                
                # 更新当前低位和它的进位
                result[p2] = total % 10
                result[p1] += total // 10
                
        # 去掉数组前面多余的 0（比如 9 * 9 = 81，占满 2 位；但 1 * 1 = 1，前面会剩一个 0）
        start = 0
        while start < len(result) and result[start] == 0:
            start += 1
            
        # 用 join 一口气转成字符串，避开 str(大整数) 的大坑
        return "".join(str(x) for x in result[start:])