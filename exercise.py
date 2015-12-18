#coding=UTF-8
# 아이파이썬 노트북 관련 모듈을 로딩하고,
from bokeh.io import output_notebook, show

# 결과를 아이파이썬 노트북으로 출력할 플롯 엔진을 뛰운다.
output_notebook()

# 테스트용 데이터를 만든다.
import math,numpy as np

X = np.arange(1,10,.1)
Y = [ math.sin(x) for x in X ]
Ym = [ - math.sin(x) for x in X ]

# 데이터를 플롯팅 한다.
from bokeh.plotting import figure

p = figure(height=300,title='파이썬(Python)')
p.title_text_font = 'PilGi'
p.circle(x=X,y=Y,size=X)
p.triangle(x=X,y=Ym,size=X[::-1],color='orange')
p.line(x=X,y=0,line_width=10,color='red',alpha=.3)
show(p)
