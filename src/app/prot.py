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
    # @brief 单次字符串帧格式解析。
    # @details 无
    # @param self 对象指针。
    # Wparam Msg 解析内容。
    # @return
    #   - StrFrm 字符串帧解码结果。
    #   - SurMsg 解析剩余内容。
    # @note 帧格式为："<Str>: Num1, Num2, Num3...\n"
    #   1.<Str>为任意标识字符串；
    #   2.Numx为数据；
    #   3.\n为结束符；
    #   例：printf("chA: 1, 2, 3\nchB: 4, 5, 6\n")
    # @attention 无
    #
    def DecOnce(self, Msg):
        LogTr("Enter cStrFmtProt.DecOnce().")
        StrFrm = {}
        SurMsg = Msg

        if len(Msg):
            MtchRst = match(r"(\w+)(\s*):(\s*)(\d(\s*),(\s*))*(\d)(\s*)[\n\r|\r\n|\n]", Msg)

            if MtchRst:
                Idx = MtchRst.span()[1]
                SurMsg = Msg[Idx:]
                Msg = Msg[:Idx]
                Msg = sub(r"[\n\r|\r\n|\n].*$", "", Msg)
                Id = sub(r":.*$", "", Msg)
                Dat = [int(x) for x in findall(r"\d+", Msg)]

                if len(Id) and len(Dat):
                    StrFrm = {"Id":Id, "Dat":Dat}

        LogTr("Exit cStrFmtProt.DecOnce().")
        return StrFrm, SurMsg

    ##
    # @brief 字符串帧格式解析。
    # @details 无
    # @param self 对象指针。
    # Wparam Msg 解析内容。
    # @return
    #   - StrFrm 字符串帧解码结果。
    #   - SurMsg 解析剩余内容。
    # @note 无
    # @attention 无
    #
    def Dec(self, Msg):
        LogTr("Enter cStrFmtProt.Dec().")
        StrFrm = {}
        SurMsg = ""

        ExtrRst, Msg = self.DecOnce(Msg)
        if ExtrRst:
            StrFrm[ExtrRst["Id"]] = ExtrRst["Dat"]
            SurMsg = Msg

        while ExtrRst:
            ExtrRst, Msg = self.DecOnce(Msg)
            if ExtrRst:
                if ExtrRst["Id"] in StrFrm: #若Id已存在则追加数据。
                    StrFrm[ExtrRst["Id"]] += ExtrRst["Dat"]
                else:
                    StrFrm[ExtrRst["Id"]] = ExtrRst["Dat"]

                SurMsg = Msg

        LogTr("Exit cStrFmtProt.Dec().")
        return StrFrm, SurMsg
