# -*-encoding:utf-8 -*-

from pywinauto.application import Application
from login import LoginComan
from calcXY import dealWithString
import time
import autoit


def main():
    # 登录COMAN
    name = 'qyl'
    passwd = 'skyship'
    LoginComan(name, passwd).login()

    # 通过pywinauto连接COMAN程序
    app_uia = Application(backend='uia')
    app_uia.connect(path='SkyMngerServer.exe')
    coman_worker = app_uia[r'天舟COMAN Worker  当前用户: 戚延磊 (qyl)']

    # 进入COMAN Professional起始页
    # coman_worker.['button8'].click()
    coman_worker.child_window(auto_id="btnCOMAN", control_type="Button").click()

    # 进入项目目录
    app_api = Application()
    app_api.connect(path='SkyMngerServer.exe')
    coman_pro_api = app_api[r'天舟COMAN多学科设计/仿真协同系统 - 起始页']
    coman_pro_api['项目目录Button'].click()
    time.sleep(2)

    # 进入项目目录所在列表
    coman_pro_uia = app_uia[r'天舟COMAN多学科设计/仿真协同系统 - 起始页']
    coman_pro_uia.child_window(auto_id="59648", control_type="Pane")
    # 获取项目目录的信息
    prjCat = coman_pro_uia.child_window(title="演示验证", control_type="TreeItem")
    # 选中项目目录
    prjCat.select()

    # 进入命令行区域
    commandLine = coman_pro_uia.child_window(auto_id="1043", control_type="List")
    # 获取所有命令行命令
    commandLine.get_items()
    # 获取要执行的命令
    createPrj = commandLine.child_window(title="创建新项目", control_type="ListItem")
    # 先选中项目，然后在执行单击响应
    createPrj.select()
    createPrj.click_input()

    # 得到项目信息窗口
    prjInfos = app_api[r'项目基本信息']
    # 输入项目名称
    prjInfos['项目名称Edit'].type_keys(r'喷管气动方案设计')
    # 单击下一步，进入设置项目关联的顶级对象
    prjInfos.child_window(title="下一步(&N) >", class_name="Button").click()

    # 确定项目关联的顶级对象对话框
    setTopObjinfosForPrj = app_api[r'项目关联的项目类型及设计对象类型']
    topp = setTopObjinfosForPrj.child_window(title="项目关联的项目类型及设计对象类型", class_name="#32770")
    # 选择项目关联的项目类型及设计对象类型对话框中的第7个控件
    topp.children()[7].click()

    time.sleep(2)
    # 选择顶级对象类型
    checkTopObject = app_api[r'选择项目关联的顶级对象类型']

    # 获得所有对象类型库所在的列表
    # 得到选择原理对象类型库的对象列表，下标为1，结构对象类型库的下标为4
    objectLibs = checkTopObject.children()[1]
    print(objectLibs)

    # 选中某个对象类型库
    objectLibs.items()[1].select()

    # 获得对象类型库的对象类型的树状列表对象
    treeViews = checkTopObject.child_window(title="Tree1", class_name="SysTreeView32")

    # 选择对象类型
    treeViews.roots()[0].select()

    # 获得当前窗口的位置并计算顶级对象类型的坐标
    ax1 = str(treeViews.rectangle())
    left, hight = dealWithString(ax1)
    x = left + 35
    y = hight + 13
    time.sleep(2)
    # 移动鼠标到某个位置，并执行单击
    autoit.mouse_move(x, y)
    autoit.mouse_click()

    # 确定，完成顶级对象类型选择
    checkTopObject.child_window(title="确定", class_name="Button").click()

    # 完成项目顶级对象类型的设置
    setTopObjinfosForPrj.child_window(title="完成", class_name="Button").click()

    time.sleep(3)
    # 退出定义项目成员对话框
    prjPersion = app_api[r'定义项目成员']
    prjPersion.close_alt_f4()

    time.sleep(2)

    # 打开建模器
    chickOpen = app_api[r'选择项目打开方式']

    chickOpen['打开设计仿真建模器'].click()



if __name__=="__main__":
    main()


