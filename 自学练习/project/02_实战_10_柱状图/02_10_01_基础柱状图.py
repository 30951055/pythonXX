from pyecharts.charts import Bar
from pyecharts.options import LabelOpts

bar = Bar()
bar.add_xaxis(['中国','美国','英国'])
# label_opts=LabelOpts(position='right')    表示数字标签显示的方向，如果不写这句，则默认是中间。
bar.add_yaxis('GDP',[30,20,10],label_opts=LabelOpts(position='right'))
# 反转x和y轴 的角度。就是让x和y轴各旋转90度。
# bar.reversal_axis()
bar.render('基础柱状图.html')