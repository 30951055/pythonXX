from pyecharts.charts import Bar, Timeline
from pyecharts.globals import ThemeType
from pyecharts.options import LabelOpts

'''各个bar相当于各个帧'''
bar1 = Bar()
bar1.add_xaxis(['中国','美国','英国'])
# label_opts=LabelOpts(position='right')    表示数字标签显示的方向，如果不写这句，则默认是中间。
bar1.add_yaxis('GDP',[30,30,20],label_opts=LabelOpts(position='right'))
# 反转x和y轴 的角度。就是让x和y轴各旋转90度。
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(['中国','美国','英国'])
# label_opts=LabelOpts(position='right')    表示数字标签显示的方向，如果不写这句，则默认是中间。
bar2.add_yaxis('GDP',[50,50,50],label_opts=LabelOpts(position='right'))
# 反转x和y轴 的角度。就是让x和y轴各旋转90度。
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(['中国','美国','英国'])
# label_opts=LabelOpts(position='right')    表示数字标签显示的方向，如果不写这句，则默认是中间。
bar3.add_yaxis('GDP',[70,60,60],label_opts=LabelOpts(position='right'))
# 反转x和y轴 的角度。就是让x和y轴各旋转90度。
bar3.reversal_axis()

'''  构建时间线对象 
        {'theme':ThemeType.LIGHT} 变换主题风格（包括颜色）
            其他的风格：
                默认 ( WHITE )
                明亮风格 ( LIGHT )
                暗黑风 ( DARK )
                粉笔风 ( CHALK )
                厄索斯大陆 ( ESSOS )
                信息风 ( INFOGRAPHIC )
                马卡龙 ( MACARONS )
                紫色风情 ( PURPLE-PASSION )
                罗马风 ( ROMA )
                浪漫风 ( ROMANTIC )
                闪耀风 ( SHINE )
                复古风 ( VINTAGE )
                瓦尔登湖 ( WALDEN )
                维斯特洛大陆 ( WESTEROS )
                仙境 ( WONDERLAND )
                万圣节风 ( HALLOWEEN )      '''
timeline = Timeline({'theme':ThemeType.LIGHT})
# 在时间线内添加柱状图对象
timeline.add(bar1,'点1')
timeline.add(bar2,'点2')
timeline.add(bar3,'点3')
# 自动播放设置
timeline.add_schema(
    # 自动播放的时间间隔 单位（毫秒）
    play_interval=1000,
    # 是否显示时间线
    is_timeline_show=True,
    # 是否自动播放
    is_auto_play=True,
    # 是否循环播放
    is_loop_play=True

)

timeline.render('变换基础柱状图.html')