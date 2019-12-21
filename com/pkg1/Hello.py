# coding=utf-8


import matplotlib.pyplot as plt

from com.pkg1.db.db_access import findall_hisq_data


def pot_hisvolume(dates, volumes):
    """苹果股票历史成交量折线图"""

    # 设置中文字体
    plt.rcParams['font.family'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    # 设置图表大小  x轴大一点，长一倍
    plt.figure(figsize=(16, 4))

    # 绘制线段
    plt.plot(dates, volumes)

    plt.title('苹果股票历史成交量')  # 添加图表标题
    plt.ylabel('成交量')  # 添加y轴标题
    plt.xlabel('交易日期')  # 添加x轴标题

    plt.show()  # 显示图形


def main():
    """主函数"""

    data = findall_hisq_data('AAPL')

    # 从data中提取成交量数据
    volume_map = map(lambda it: it['Volume'], data)
    # 将volume_map转换为交量列表
    volume_list = list(volume_map)

    # 从data中提取日期数据
    date_map = map(lambda it: it['Date'], data)
    # 将date_map转换为日期列表
    date_list = list(date_map)

    pot_hisvolume(date_list, volume_list)


if __name__ == '__main__':
    main()
