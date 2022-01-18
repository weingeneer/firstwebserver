from tinyhtml import html, h

html_string = html()(
    h('table')(h('tr')(h('td')(idx*incr) for idx in range(1, 11)) for incr in range(1, 11))
)
print(html_string)