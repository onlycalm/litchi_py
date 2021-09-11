##
# @file prot.py
# @brief 通讯协议模块。
# @details 无
# @author Calm
# @date 2021-09-03
# @version v1.0.0
# @copyright Calm
#

from re import *
from log import *

##
# @class cStrFmtProt
# @brief 字符串格式通讯协议类。
# @details 该类用于解析字符串格式帧。
# @note 帧格式为："<Str>: Num1, Num2, Num3...\n"
#   1.<Str>为任意标识字符串；
#   2.Numx为数据；
#   3.\n为结束符；
#   例：printf("chA: 1, 2, 3\nchB: 4, 5, 6\n")
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
        LogTr("Enter cStrFmtProt.__init__().")
        pass
        LogTr("Exit cStrFmtProt.__init__().")


    ##
    # @brief 解析指令。
    # @details 有效指令为字符串帧格式。
    # @param self 对象指针。
    # Wparam Msg 解析内容。
    # @return
    #   - StrFrm 字符串帧解码结果。
    # @note 帧格式为："<Str>: Num1, Num2, Num3...\n"
    #   1.<Str>为任意标识字符串；
    #   2.Numx为数据；
    #   3.\n为结束符；
    #   例：printf("chA: 1, 2, 3\nchB: 4, 5, 6\n")
    # @attention 无
    #
    def DecInstr(self, Msg):
        LogTr("Enter cStrFmtProt.DecInstr().")
        StrFrm = {}

        if len(Msg):
            MtchRst = match(r"(\w+)(\s*):(\s*)(\d(\s*),(\s*))*(\d)(\s*)[\n\r|\r\n|\n]", Msg)

            if MtchRst:
                SrchRst = search(":", Msg)
                Idx = SrchRst.span()
                DatMsg = Msg[Idx[1]:]
                Id = Msg[:Idx[0]]
                Dat = [int(x) for x in findall(r"\d+", DatMsg)]

                if Id and Dat:
                    StrFrm = {"Id":Id, "Dat":Dat}

        LogTr("Exit cStrFmtProt.DecInstr().")
        return StrFrm

    ##
    # @brief 解析数据。
    # @details 以'\n'作为指令的结束符。
    # @param self 对象指针。
    # Wparam Msg 字符串类型，解析内容。
    # @return
    #   - StrFrm 字符串帧解码结果。
    #   - SurMsg 解析剩余内容。
    # @note 无
    # @attention 无
    #
    def Dec(self, Msg):
        LogTr("Enter cStrFmtProt.GetInstr().")
        StrFrm = {}

        if len(Msg):
            SrchRst = search("\n", Msg)
            while SrchRst:
                Idx = SrchRst.span()
                Instr = Msg[:Idx[1]]
                Msg = Msg[Idx[1]:]
                InstrRst = self.DecInstr(Instr)

                if InstrRst:
                    if InstrRst["Id"] in StrFrm: #若Id已存在则追加数据。
                        StrFrm[InstrRst["Id"]] += InstrRst["Dat"]
                    else:
                        StrFrm[InstrRst["Id"]] = InstrRst["Dat"]

                SrchRst = search("\n", Msg)

        LogTr("Exit cStrFmtProt.GetInstr().")
        return StrFrm, Msg
