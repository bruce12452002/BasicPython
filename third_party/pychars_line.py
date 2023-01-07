from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, TooltipOpts, VisualMapOpts, ToolboxOpts

line = Line()
print(f"{line}, {type(line)}")
line.add_xaxis(["孫悟空", "牛魔王", "如來佛", "鐵扇公主", "東海龍王"])
line.add_yaxis("攻擊力", [90, 85, 1000, 70, 100])
# line.render()
print("=========== 設定全域 ============")
# https://pyecharts.org/#/zh-cn/global_options
line.set_global_opts(
    title_opts=TitleOpts(title="標題", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),  # 控制 y 軸的主題，中間最上面
    tooltip_opts=TooltipOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),  # 右上角多出工具選項
    visualmap_opts=VisualMapOpts(is_show=True)  # 左下角多出上下可調整的三角按鈕
)

line.render("line.html")  # 預設生成 render.html
