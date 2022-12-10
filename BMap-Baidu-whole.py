import pyecharts.options as opts
from pyecharts.charts import BMap,Map
from pyecharts.globals import ChartType,SymbolType,BMapType,JsCode
import json
from pyecharts.datasets import COORDINATES
data=[
    ('碧泉花园社区<br>联系人：XXX<br>联系电话:12345678900<br>社区范围：碧泉花园、成发花苑、成发馨苑、水岸华庭<br>背街小巷：欣杨道、御河道', 4),
    ('碧泉花园社区新时代文明实践站', 5),
]
# 批量导入位置信息
test_data_=[

('碧泉花园社区\联系人：XXX\联系电话:12345678900\社区范围：碧泉花园、成发花苑、成发馨苑、水岸华庭\背街小巷：欣杨道、御河道', 117.031178, 39.140916),
('碧泉花园社区新时代文明实践站', 117.030087, 39.141962),
]

pieces=[

        {'min': 4, 'max': 4, 'label': '城市社区','color':'MediumPurple'},
        {'min': 5, 'max': 5, 'label': '社区新时代文明实践站','color':'Aqua'},

]
address_ = []
json_data = {}
for ss in range(len(test_data_)):
    json_data[test_data_[ss][0]] = [test_data_[ss][1], test_data_[ss][2]]
    address_.append(test_data_[ss][0])

json_str = json.dumps(json_data, ensure_ascii=False, indent=4)
with open('BMap-Baidu-whole.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_str)


b=BMap(init_opts=opts.InitOpts(width="1200px", height="2250px"),)
b.add_coordinate_json(json_file='BMap-Baidu-whole.json')
# cd=b.get_coordinate(name='张家窝镇')  #
# print(cd)

b.add(
    type_="scatter", #Geo 图类型，有 scatter, effectScatter, heatmap, lines 4 种，建议使用
    series_name="BMap",
    data_pair=data,
    symbol_size=100,
    effect_opts=opts.EffectOpts(),
    label_opts=opts.LabelOpts(formatter="{b}", position="right", is_show=False),
    itemstyle_opts=opts.ItemStyleOpts(color="purple"),

)
b.add_schema(
    baidu_ak="ikDcUGDtb60wei2Hnzi8NueIqUSXp7qB",
    center=[117.031178, 39.140916],
    zoom=20,
    is_roam=True,

)
b.set_global_opts(
    title_opts=opts.TitleOpts(
        title="点位分布图手机版",

        #subtitle_link="http://www.ollo100.cn/cms2021/",
        #subtitle_target="blank",

        pos_left="center",

        title_textstyle_opts=opts.TextStyleOpts(color="blue",font_size=60),
        subtitle_textstyle_opts=opts.TextStyleOpts(color="red",font_size=35),
    ),
    legend_opts=opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(font_size=20)),
    tooltip_opts=opts.TooltipOpts(trigger="item",
                                  formatter=JsCode("function(params){return params.data.name;}"),
                                  textstyle_opts=opts.TextStyleOpts(font_size=40), #return params.name + ' : ' + params.value[2];
                                  hide_delay=15000, # 浮层隐藏的延时，单位ms,在alwaysShowContent为true时，无效。
                                  position="inside", #固定参数配置：'inside'，'top'，'left'，'right'，'bottom'
    ),


    visualmap_opts=opts.VisualMapOpts(
        is_piecewise=True,pieces=pieces,
        pos_top="10%", pos_left="0",
        pos_bottom='bottom', max_=33,
        is_inverse=True,

        dimension=2,
        #brush_link=[0,1,2]
        #series_index='all',  # 指定取哪个系列的数据，默认取所有系列。
        #border_color="#ccc", # 设置控件工具边框和背景
        #border_width=2,
        #background_color="#eee",
        range_text=['总数:361'],
        range_opacity=1,
        orient = 'vertical',
        textstyle_opts=opts.ItemStyleOpts('rgb(51,75,92)') and opts.TextStyleOpts(font_size=35),
        item_width=[50],item_height=[50],
    ),
)

b.add_control_panel(
    copyright_control_opts=opts.BMapCopyrightTypeOpts(position=3), #调整版权控件位置
    maptype_control_opts=opts.BMapTypeControlOpts(

        # 控件的停靠位置
        # ANCHOR_TOP_LEFT，控件将定位到地图的左上角，值为 0
        # ANCHOR_TOP_RIGHT，控件将定位到地图的右上角，值为 1
        # ANCHOR_BOTTOM_LEFT，控件将定位到地图的左下角，值为 2
        # ANCHOR_BOTTOM_RIGHT，控件将定位到地图的右下角，值为 3
        position = BMapType.ANCHOR_TOP_RIGHT,

        # 地图类型属性
        # MAPTYPE_CONTROL_HORIZONTAL，按钮水平方式展示，默认采用此类型展示。值为 0
        # MAPTYPE_CONTROL_DROPDOWN，按钮呈下拉列表方式展示，值为 1
        # MAPTYPE_CONTROL_MAP，以图片方式展示类型控件，设置该类型后无法指定 maptypes 属性，值为 2
        type_=BMapType.MAPTYPE_CONTROL_HORIZONTAL,

    ),
    scale_control_opts=opts.BMapScaleControlOpts(),
    overview_map_opts=opts.BMapOverviewMapControlOpts(is_open=True),
    #navigation_control_opts=opts.BMapNavigationControlOpts(),
    geo_location_control_opts=opts.BMapGeoLocationControlOpts(position=BMapType.ANCHOR_BOTTOM_RIGHT),


)



b.render("BMap-Baidu-whole.html")
