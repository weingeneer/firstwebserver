from tinyhtml import html, h

html_string = html()(
    h('body')(
        h('table')(h('tr')(h('td')(h('a', href_=f'http://{idx*incr}.ru')(idx*incr)) for idx in range(1, 11)) for incr in range(1, 11))
    )
)
print(html_string)