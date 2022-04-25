#Bmap-散点图、热力图和涟漪图
import pandas as pd
from pyecharts.charts import BMap
from pyecharts import options as opts
from pyecharts.globals import ChartType

data = pd.read_excel('GDP.xlsx')
province = list(data["province"])
gdp = list(data["2019_gdp"])
list = [list(z) for z in zip(province,gdp)]
print(list)
c = (
    BMap(init_opts=opts.InitOpts(width="1000px", height="600px"))
    .add_schema(baidu_ak="你的AK", center=[120.13066322374, 30.240018034923])
    .add(
        "GDP",
        list,
        type_="heatmap",  #scatter为散点图，heatmap为热力图，ChartType.EFFECT_SCATTER为涟漪图
        label_opts=opts.LabelOpts(formatter="{b}")
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="2019年各省GDP热力图"), visualmap_opts=opts.VisualMapOpts(max_=110000)
    )
    .render("Bmap1.html")
)
