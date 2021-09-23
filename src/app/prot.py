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
# @class cStrFmtOscProt
# @brief 字符串格式Osc通讯协议类。
# @details 该类用于解析字符串Osc格式帧。
# @note 帧格式为："<Str>: Num1, Num2, Num3...\n"
#   1.<Str>为任意标识字符串；
#   2.Numx为数据；
#   3.\n为结束符；
#   例：printf("chA: 1, 2, 3\nchB: 4, 5, 6\n")
# @attention 无
#
class cStrFmtOscProt:
    ##
    # @brief 构造函数。
    # @details 无
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
    def __init__(self):
        LogTr("Enter cStrFmtOscProt.__init__().")
        pass
        LogTr("Exit cStrFmtOscProt.__init__().")

    ##
    # @brief 解析指令。
    # @details 有效指令为字符串帧Osc格式。
    # @param self 对象指针。
    # @param Msg 解析内容。
    # @return
    #   - StrFrm 类型为字典，字符串帧Osc解码结果。
    # @note 帧格式为："<Str>: Num1, Num2, Num3...\n"
    #   1.<Str>为任意标识字符串；
    #   2.Numx为数据；
    #   3.\n为结束符；
    #   例：printf("chA: 1, 2, 3\nchB: 4, 5, 6\n")
    # @attention 无
    #
    def DecInstr(self, Msg):
        LogTr("Enter cStrFmtOscProt.DecInstr().")
        StrFrm = {}

        if len(Msg):
            MtchRes = match(r"(\w+)(\s*):(\s*)(\d(\s*),(\s*))*(\d)(\s*)[\n\r|\r\n|\n]", Msg)

            if MtchRes:
                SrchRes = search(":", Msg)
                Idx = SrchRes.span()
                DatMsg = Msg[Idx[1]:]
                Id = Msg[:Idx[0]]
                Dat = [int(x) for x in findall(r"\d+", DatMsg)]

                if Id and Dat:
                    StrFrm = {"Id":Id, "Dat":Dat}

        LogTr("Exit cStrFmtOscProt.DecInstr().")
        return StrFrm

    ##
    # @brief 解析数据。
    # @details 以'\n'作为指令的结束符。
    # @param self 对象指针。
    # @param Msg 字符串类型，解析内容。
    # @return
    #   - StrFrm 类型为字典，字符串帧Osc解码结果。
    #   - SurMsg 解析剩余内容。
    # @note 无
    # @attention 无
    #
    def Dec(self, Msg):
        LogTr("Enter cStrFmtOscProt.GetInstr().")
        StrFrm = {}

        if len(Msg):
            SrchRes = search("\n", Msg)
            while SrchRes:
                Idx = SrchRes.span()
                Instr = Msg[:Idx[1]]
                Msg = Msg[Idx[1]:]
                InstrRes = self.DecInstr(Instr)

                if InstrRes:
                    if InstrRes["Id"] in StrFrm: #若Id已存在则追加数据。
                        StrFrm[InstrRes["Id"]] += InstrRes["Dat"]
                    else:
                        StrFrm[InstrRes["Id"]] = InstrRes["Dat"]

                SrchRes = search("\n", Msg)

        LogTr("Exit cStrFmtOscProt.GetInstr().")
        return StrFrm, Msg

##
# @class cStrFmtLogProt
# @brief 字符串格式Log通讯协议类。
# @details 该类用于解析字符串Log格式帧。
# @note 帧格式为："[<Str>] <Msg>\n"
#   1.<Str>为Log等级字符串。有CRITICAL、ERROR、WARNING、SUCCESS、INFO、DEBUG、TRACE；
#   2.<Msg>为Log描述内容；
#   3.\n为结束符；
#   例：printf("[ERROR] Describe some information.\n")
# @attention 无
#
class cStrFmtLogProt:
    ##
    # @brief 构造函数。
    # @details 无
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
    def __init__(self):
        LogTr("Enter cStrFmtLogProt.__init__().")
        self.Lv = ("CRITICAL", "ERROR", "WARNING", "SUCCESS", "INFO", "DEBUG", "TRACE")
        pass
        LogTr("Exit cStrFmtLogProt.__init__().")

    ##
    # @brief 解析指令。
    # @details 有效指令为字符串帧Log格式。
    # @param self 对象指针。
    # @param Msg 解析内容。
    # @return
    #   - StrFrm 类型为字典，字符串帧Log解码结果。
    # @note 帧格式为："[<Str>] <Msg>\n"
    #   1.<Str>为Log等级字符串。有CRITICAL、ERROR、WARNING、SUCCESS、INFO、DEBUG、TRACE；
    #   2.<Msg>为Log描述内容；
    #   3.\n为结束符；
    #   例：printf("[ERROR] Describe some information.\n")
    # @attention 无
    #
    def DecInstr(self, Msg):
        LogTr("Enter cStrFmtLogProt.DecInstr().")
        StrFrm = {}

        if len(Msg):
            MtchRes = match(r"\[[CRITICAL|ERROR|WARNING|SUCCESS|INFO|DEBUG|TRACE]*\] .*\n", Msg)

            if MtchRes:
                SrchRes = search("] ", Msg)
                Idx = SrchRes.span()
                Des = Msg[Idx[1]:len(Msg) - 1]
                Lv = Msg[1:Idx[0]]

                if Lv and Des:
                    StrFrm = {"Lv":Lv, "Des":Des}

        LogTr("Exit cStrFmtLogProt.DecInstr().")
        return StrFrm

    ##
    # @brief 解析数据。
    # @details 以'\n'作为指令的结束符。
    # @param self 对象指针。
    # @param Msg 字符串类型，解析内容。
    # @return
    #   - StrFrm 字符串帧Log解码结果，类型为列表。
    #   - SurMsg 解析剩余内容。
    # @note 无
    # @attention 无
    #
    def Dec(self, Msg):
        LogTr("Enter cStrFmtLogProt.Dec().")
        StrFrm = []

        if len(Msg):
            SrchRes = search("\n", Msg)
            while SrchRes:
                Idx = SrchRes.span()
                Instr = Msg[:Idx[1]]
                Msg = Msg[Idx[1]:]
                InstrRes = self.DecInstr(Instr)

                if InstrRes:
                    StrFrm.append(InstrRes)

                SrchRes = search("\n", Msg)

        LogTr("Exit cStrFmtLogProt.Dec().")
        return StrFrm, Msg
