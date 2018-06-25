# -*- coding: utf-8 -*-

def capitalize(value) :
    """
    人民币金额大写
    """
    
    # 日常用的仟佰拾元角分的顺序，并不方便处理，所以要倒过来
    # 序号：
    # -2  -1   0   1   2   3   4  ... 
    #  分  角  元   拾  佰   仟  万  ...
    units = u''.join(reversed(u'兆仟佰拾万仟佰拾亿仟佰拾万仟佰拾元角分'))
    
    numbers = u'零壹贰叁肆伍陆柒捌玖'
    truncation = u'整'

    def non_zero(num, level) :
        """
        非零位
        只是简单输出其数字值和单位
        """
        return numbers[num] + units[level + 2]

    def zero(start, end = -2) :
        """
        连续的零
        需要根据情况输出单位、"零"和最后的"整"
        """
        s = u''
        
        for p in range(start / 4 * 4, end - 1, -4) :
            if p == 4 and start >= 8 :   # 亿后不需要加万
                continue
            s += units[p + 2]
                
        if end == -2 :        # 零一直到最后，补“整”
            s += truncation
        else : 
            if end % 4 != 0 : # 零结束的地方不是亿/万/元，则补“零”
                s += numbers[0]
        return s
    
    # 去除小数点：
    # 1、将角/分和整值同样处理
    # 2、不需要考虑小数点的占位问题
    value = ''.join( ('%#.2f' % value).split('.') )
    lst = []
    for i, c in enumerate(value) :
        n = int(c)
        p = len(value) - i - 3
        if n == 0 :
            if p % 4 == 0 :
                lst.append( (units[p]) )
        else :
            lst.append( (numbers[n], units[p]) )
            
    print s
    return s
