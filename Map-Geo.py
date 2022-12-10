from pyecharts.globals import GeoType
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.datasets import register_files,register_coords,register_url
import json

try:
    register_url("https://echarts-maps.github.io/echarts-china-counties-js/") #C:\ProgramData\Miniconda3\Lib\site-packages\echarts_china_counties_pypkg\resources\echarts-china-counties-js

except Exception:
    import ssl

    ssl._create_default_https_context = ssl._create_unverified_context
    register_url("https://echarts-maps.github.io/echarts-china-counties-js/")



data=[
    ('杨柳青镇镇政府', 1),

]

# 批量导入位置信息
test_data_=[

    ('杨柳青镇镇政府', 117.01409339904785, 39.128473396269634),


]

address_ = []
json_data = {}
for ss in range(len(test_data_)):
    json_data[test_data_[ss][0]] = [test_data_[ss][1], test_data_[ss][2]]
    address_.append(test_data_[ss][0])

json_str = json.dumps(json_data, ensure_ascii=False, indent=4)
with open('map-geo.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_str)

city='西青区'
g = Geo()

g.add_schema(
    maptype=city,
    itemstyle_opts=opts.ItemStyleOpts(color="#323c48", border_color="#111") #设置背景颜色
)

g.add_coordinate_json(json_file='map-geo.json') # 经度在前，维度在后
#g.add_coordinate('杨柳青镇镇政府', 117.01409339904785, 39.128473396269634)  # 逐个导入位置


# 定义数据
data_pair = data
#data_pair = [('杨柳青镇镇政府', 80), ('张家窝镇镇政府', 19)]

# Geo 图类型，有scatter,effectScatter,heatmap,lines 4种，建议使用
# from pyecharts.globals import GeoType
# GeoType.EFFECT_SCATTER,GeoType.HEATMAP,GeoType.LINES
# 将数据添加在地图上

g.add('点位分布图', data_pair, type_=GeoType.EFFECT_SCATTER,symbol_size=20) # 空的时候默认为散点图，加上type_=GeoType.EFFECT_SCATTER为涟漪图
g.set_series_opts(label_opts=opts.LabelOpts(is_show=False)) #False去除维度标识，True为显示维度表示


# 自定义分段color，可用取色器取色
pieces = [
    {'max': 99,'label':'杨柳青','color':'blue'},

]

# is_piecewise 是否自定义分段，变为True才能生效
g.set_global_opts(
    visualmap_opts=opts.VisualMapOpts(is_piecewise=True, pieces=pieces, orient='vertical',
                                      textstyle_opts=opts.ItemStyleOpts('rgb(51,75,92)') and opts.TextStyleOpts(
                                          font_size=25),
                                      item_width=[30], item_height=[30],
                                      pos_top='100px', pos_bottom='bottom', pos_left=[0],
                                      max_=33),
    title_opts=opts.TitleOpts(title="{}-按街镇分布(涟漪图)".format(city)),
    legend_opts=opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(font_size=35)),
)





g.render("Map-Geo.html")
#g.render_notebook()