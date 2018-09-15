# -*- coding: UTF-8 -*- 


###
# import sys
# reload(sys)
# sys.setdefaultencoding( "utf-8" )

# output_encoding = sys.stdout.encoding or "utf-8"
	


### python内部是unicode编码，cmd输出窗口默认是gbk编码
### st.decode('utf-8')，将utf-8编码的st转unicode编码
### st.encode('gbk')，将unicode编码的st转gbk编码
# 在cmd输出窗口乱码问题
def myprint(st):
	print(st.decode('utf-8').encode('gbk'))

#------------一些语言点-------------------
# int转String：str(数字)
# String转int：int(字串)
# py是弱类型语言，变量无需类型申明
# 缩进要严格统一，不能空格和TAB混用
# 若要在代码中直接写中文，需要加上一句# -*- coding: UTF-8 -*-
# continue和其他语言一样是跳过后面的代码，开始下一轮循环
# for循环的else是可选的，如果循环未被break终止，则执行else块中的语句


#------------- 1.for循环------------------
for v in range(1, 10, 3):   # 参数3可省略 默认为1
    if v>=6:
    	myprint("循环被break终止,不执行else块中的语句")
        break
    elif v%2==0 :
        myprint("偶数:" + str(v))
    elif v%2!=0 :
        myprint("奇数:" + str(v))
    else:
        myprint("其他")
else:
    myprint("for 循环结束")

#------------- 2.写文件------------------

# 需要引入库：			import os
# 新建或者打开文件：		file = open(路径,'w')
# 向文件中写入数据：		file.write('数据')（file为上一步新建的文件）
# 写入完毕，关闭文件：	file.close()

import os
file = open('/Users/RC-W/Desktop/hello.lua','w')
file.write("Hello lua")
file.close()
