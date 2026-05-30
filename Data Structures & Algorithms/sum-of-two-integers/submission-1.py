class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 这里首先符号位是啥 这是signed int吧
        # 然后 %2获得最低位 //2获得高一位 这样就获得了俩 i j ，然后看
        # 1 1 就变成0 add=1 01 10就变成1 00就变成0
        #最后 woc可是负数怎么整
        
        # 32位掩码，用来截断无限精度的数字
        mask = 0xFFFFFFFF

        while b != 0:
            # 1. 算出不带进位的和，并限制在 32 位内
            temp_sum = (a ^ b) & mask
            # 2. 算出进位，左移一位，同样限制在 32 位内
            carry = ((a & b) << 1) & mask

            # 滚动更新
            a = temp_sum
            b = carry

        # 此时 a 存储的是 32 位无符号整数的结果
        # 如果 a 大于 0x7FFFFFFF（32位正数的最大值），说明它在有符号下是个负数
        # 我们需要把它转换回 Python 的负数形式：~(a ^ mask)
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)