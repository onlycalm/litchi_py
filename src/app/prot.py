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
    ##
    # @brief 构造函数。
    # @details 无
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
    def __init__(self):
        pass

    ##
    # @brief 单次字符串帧格式解析。
    # @details 无
    # @param self 对象指针。
    # Wparam Msg 解析内容。
    # @return
    #         - StrFrm 字符串帧解码结果。
    #         - Msg 解析剩余内容。
    # @note 无
    # @attention 无
    #
    def DecOnce(self, Msg):
        StrFrm = {}

        if len(Msg):
            Srch = re.search(r"\n", Msg)
            if Srch:
                Idx = Srch.span()[0]
                if Idx > 0:
                    ExtStr = Msg[:Idx]
                    Msg = Msg[Idx + 1:]

                    if len(ExtStr):
                        Id = re.sub(r":.*$", "", ExtStr)
                        Dat = [int(x) for x in re.findall(r"\d+", ExtStr)]

                        if len(Id) and len(Dat):
                            StrFrm = {"Id":Id, "Dat":Dat}

        return StrFrm, Msg

    ##
    # @brief 字符串帧格式解析。
    # @details 无
    # @param self 对象指针。
    # Wparam Msg 解析内容。
    # @return
    #         - StrFrm 字符串帧解码结果。
    #         - Msg 解析剩余内容。
    # @note 无
    # @attention 无
    #
    def Dec(self, Msg):
        StrFrm = {}
        DecRst, Msg = self.DecOnce(Msg)
        if DecRst:
            StrFrm[DecRst["Id"]] = DecRst["Dat"]
        while DecRst:
            DecRst, Msg = self.DecOnce(Msg)
            if DecRst:
                StrFrm[DecRst["Id"]] = DecRst["Dat"]

        return StrFrm, Msg
