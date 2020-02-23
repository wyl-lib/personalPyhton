list ="""[
<li>
<a href="https://tianqi.moji.com/today/china/shandong/penglai">今天</a>
</li>,

<li>
<span><img alt="今天" src="https://h5tq.moji.com/tianqi/assets/images/weather/w1.png"/>
</span>
多云
</li>,

<li>
8°/16°
</li>, 

<li>
<em>南风</em>
<b>5-6级</b>
</li>,

<li>
<strong class="level_2">
    65 良
</strong>
</li>]

"""
html = """
[<li>
<a href="https://tianqi.moji.com/today/china/shandong/penglai">今天</a>
</li>, <li>
<span>
<img alt="多云" src="https://h5tq.moji.com/tianqi/assets/images/weather/w31.png"/>
</span>

                        多云                    </li>, <li>8° / 19°</li>, <li>
<em>南风</em>
<b>5-6级</b>
</li>, <li><strong class="level_2">

                    81 良  

                    </strong>
</li>]
"""

print(type(list))
print(type(html))