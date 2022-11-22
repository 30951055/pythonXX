import json

from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts

f_us = open('D:\\BaiduNetdiskWorkspace\\PG_XX\\python\\自学练习\\project\\02_实战_07_生成网页版折线图\\折线图数据\\美国.txt','r',encoding='utf-8')
f_jp = open('D:\\BaiduNetdiskWorkspace\\PG_XX\\python\\自学练习\\project\\02_实战_07_生成网页版折线图\\折线图数据\\日本.txt','r',encoding='utf-8')
f_in = open('D:\\BaiduNetdiskWorkspace\\PG_XX\\python\\自学练习\\project\\02_实战_07_生成网页版折线图\\折线图数据\\印度.txt','r',encoding='utf-8')
us_data = f_us.read()
jp_data = f_jp.read()
in_data = f_in.read()

us_data = us_data.replace('jsonp_1629344292311_69436(','')
jp_data = jp_data.replace('jsonp_1629350871167_29498(','')
in_data = in_data.replace('jsonp_1629350745930_63180(','')

# 切掉末尾的两个字符
us_data = us_data[:-2]
jp_data = jp_data[:-2]
in_data = in_data[:-2]

# Json数据转python字典数据
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)
us_trend_data = us_dict['data'][0]['trend']
jp_trend_data = jp_dict['data'][0]['trend']
in_trend_data = in_dict['data'][0]['trend']

# 获取日期数据，用于x轴，取2020年 到下标314结束（不包括314）
u_x_data = us_trend_data['updateDate'][:314]
j_x_data = jp_trend_data['updateDate'][:314]
i_x_data = in_trend_data['updateDate'][:314]
# 获取新冠确诊数据，用于y轴，取2020年 到下标314结束（不包括314）
u_y_data = us_trend_data['list'][0]['data'][:314]
j_y_data = jp_trend_data['list'][0]['data'][:314]
i_y_data = in_trend_data['list'][0]['data'][:314]

line = Line()
# 美国，日本，印度共用一个x时间轴
line.add_xaxis(u_x_data)
# 分别添加到y轴，并为其命名。label_opts 控制数字标签的显示。
line.add_yaxis('美国确诊人数',u_y_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis('日本确诊人数',j_y_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis('印度确诊人数',i_y_data,label_opts=LabelOpts(is_show=False))

# 设置标题  详情见 https://pyecharts.org/#/
line.set_global_opts(
    # 标题设置  pos_left:position_left，左侧距的意思。
    title_opts=TitleOpts(title='2020年美日印三国确诊人数对比折线图',pos_left='center',pos_bottom='1%')
)

line.render()

f_us.close()
f_jp.close()
f_in.close()
