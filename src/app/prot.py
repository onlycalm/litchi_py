##
# @file prot.py
# @brief 通讯协议模块。
# @details 无
# @author Calm
# @date 2021-09-03
# @version v1.0.0
# @copyright Calm
#

import re

##
# @class cStrFmtProt
# @brief 字符串格式通讯协议类。
# @details 该类用于解析字符串格式帧。
# @note 帧格式为："<Str>: Num1, Num2, Num3...\n"
#       1、<Str>为任意标识字符串；
#       2、Numx为数据；
#       3、\n为结束符；
#       例：printf("chA: 1, 2, 3\nchB: 4, 5, 6\n")
# @attention 无
#
class cStrFmtProt:
    def __init__(self):
        pass

    def Dec(self, Msg):
        Idx = re.search(r"\n", Msg).span()[0]
        print(Idx)
        StrFmt = re.sub(r"\n.*$", "", Msg)
        Msg = Msg[Idx:]
        print(StrFmt) #还带有\n
        print(Msg)
        print(re.sub(r":.*$", "", StrFmt))
        print(re.findall(r"\d+", StrFmt))

        if len(Msg) != 0:
        else:

        return []
