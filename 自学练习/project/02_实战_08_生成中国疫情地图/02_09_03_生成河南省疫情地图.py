import json

from pyecharts.charts import Map
from pyecharts.options import TitleOpts, VisualMapOpts

f = open('D:\BaiduNetdiskWorkspace\PG_XX\python\教程资料\资料\可视化案例数据\地图数据\疫情.txt','r',encoding='UTF-8')
data = f.read()     # 读取全部数据
f.close()

data_dict = json.loads(data)
cities_data = data_dict['areaTree'][0]['children'][3]['children']
data_list = []
for city_data in cities_data:
    city_name = city_data['name']+'市'                   # 获取市区名
    city_confirm = city_data['total']['confirm']     # 确诊人数
    data_list.append((city_name,city_confirm))
# 对于上述没有数据的城市可以手动添加
data_list.append(('济源市',5))
print(data_list)


map = Map()
# 添加数据
map.add('河南省确诊人数',data_list,'河南')
# 设置全局选项
map.set_global_opts(
    title_opts=TitleOpts(title='河南省疫情地图'),   # 设置该图标题
    # VisualMapOpts 视觉映射配置项
    visualmap_opts = VisualMapOpts(
        is_show=True,   # 是否显示
        is_piecewise=True,
        # 自定义的每一段的范围，以及每一段的文字，以及每一段的特别的样式
        pieces=[
            {'min': 1, 'max': 99, 'label': '1-99人', 'color': '#CCFFFF'},
            {'min': 100, 'max': 999, 'label': '100-999人', 'color': '#FFFF99'},
            {'min': 1000, 'max': 4999, 'label': '1000-4999人', 'color': '#FF9966'},
            {'min': 5000, 'max': 9999, 'label': '5000-9999人', 'color': '#FF6666'},
            {'min': 10000, 'max': 99999, 'label': '10000-99999人', 'color': '#CC3333'},
            # 最小10000，最大无上限
            {'min': 100000, 'label': '100000以上', 'color': '#990033'},
        ]
    )
)
# 如果这里不指定文件名字的话，则自动生成为render.html
map.render('河南省疫情地图.html')

