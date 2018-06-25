
# -*- encoding: utf8 -*-

def capitalize(value) :
    """
    人民币金额大写
    """
    units = u'元角分'
    levels = u'仟佰拾'
    grades = u'亿万'
    numbers = u'零壹贰叁肆伍陆柒捌玖'
    truncation = u'整'

    # 支持的金额不大于1兆兆
    assert(value < 10 ** (1 + 4 * 2 ** len(grades)))

    def number_and_units(number_list, unit_list) :
        assert(len(number_list) <= len(unit_list))
        s = u''
        z = None
        for i, c in enumerate(number_list) :
            v =  int(c)
            if v == 0 :
                z = True
            else :
                if z != None :
                    s += numbers[0]
                    z = None
                s += numbers[v] + unit_list[i + len(unit_list) - len(number_list)]
        return s

    # 整数部分
    def head_string(head) :
        # 将整数串以万/亿/兆分开
        # '12345678901234567890' ->  ['1234', '56789012', '3456', '7890']
        def split(s) :
            right_index = lambda x : - 4 * 2 ** x if x >= 0 else len(s)
            return filter(lambda x : len(x) > 0,
                          [s[right_index(i) : right_index(i-1)] for i in reversed(range(len(grades)+1))])
                
        heads = split(head)
        assert(len(grades) + 1 >= len(heads) > 0)

        s = u''
        # 兆/亿/万
        for i, h in enumerate(heads[:-1]) :
            hs = head_string(h)
            if len(hs) != 0 :
                s += hs + grades[i - len(heads) + 1]                
        # X仟X佰X拾X
        s += number_and_units(heads[-1], list(levels) + [u''])
        return s
    
    # 小数部分：X角X分
    def tail_string(tail) :
        s = number_and_units(tail, units[1:])

        if tail[1] == '0' :
            s += truncation
        return s
    
    head, tail = ('%#.2f' % value).split('.')
    s = head_string(head) + units[0] + tail_string(tail)
    print s
    return s
