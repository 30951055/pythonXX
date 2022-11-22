"""
使用python轻松生成世界各国地图
    参考：https://pyecharts.org/#/zh-cn/geography_charts?id=map%ef%bc%9a%e5%9c%b0%e5%9b%be
"""
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

map = Map()
data = [
    ('北京', 40),
    ('天津', 400),
    ('上海', 500),
    ('重庆', 600),
    ('河北', 1000),
    ('河南', 496),
    ('云南', 372),
    ('辽宁', 666),
    ('黑龙江', 512),
    ('湖南', 218),
    ('安徽', 862),
    ('山东', 900),
    ('新疆', 10020),
    ('江苏', 10000),
    ('浙江', 20000),
    ('江西', 200010),
    ('湖北', 522),
    ('广西', 20),
    ('甘肃', 13),
    ('山西', 168),
    ('内蒙古', 500),
    ('陕西', 670),
    ('吉林', 280),
    ('福建', 370),
    ('贵州', 246),
    ('广东', 950),
    ('青海', 222),
    ('西藏', 145),
    ('四川', 652),
    ('宁夏', 325),
    ('海南', 854),
    ('台湾', 666),
    ('香港', 215),
    ('澳门', 315)
]
# 添加数据 即使不写'china'，也会默认为china
map.add('测试地图',data,'china')

# 设置全局选项
map.set_global_opts(
    # VisualMapOpts 视觉映射配置项
    visualmap_opts=VisualMapOpts(
        # 是否开启
        is_show=True,
        # 手动校正分段内容
        is_piecewise=True,
        # 自定义分段内容，自定义每一段的范围，以及每一段的文字，以及每一段的特别的样式
        pieces = [
            {'min':1,'max':9,'label':'1-9人','color':'#AEEEEE'},
            {'min':10,'max':99,'label':'10-99人','color':'#2F4F4F'},
            {'min':100,'max':499,'label':'100-499人','color':'#FF9966'},
            {'min':500,'max':999,'label':'500-999人','color':'#FF6666'},
            {'min':1000,'max':9999,'label':'1000-9999人','color':'#CC3333'},
            # 最小10000，最大无上限
            {'min':10000,'label':'10000以上','color':'#B22222'},
        ]
    )
)

# 如果这里不指定文件名字的话，则自动生成为render.html
map.render()