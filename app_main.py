# coding=utf-8

import wx


class App(wx.App):

    def OnInit(self):
        # 创建窗口对象

        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()  # 进入主事件循环
