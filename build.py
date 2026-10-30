# Собирает две версии из index.html: тёмные акценты (index) и светлую (light.html).
import re,pathlib
p=pathlib.Path(__file__).parent
src=(p/'index.html').read_text()
def sw(active):
    a=lambda f,n,t:f'<a href="{f}"{" class=\"on\" aria-current=\"page\"" if f==active else ""}><b>{n}</b>{t}</a>'
    return ('<nav class="cswitch" aria-label="Версии концепта"><div class="cs-in"><span class="cs-lbl">Версия</span>'
            +a('./','01','С тёмными акцентами')+a('light.html','02','Светлая')+'<a class="cs-kp" href="#kp">Было / стало ↓</a></div></nav>')
def put(s,body):
    s=re.sub(r'<!--@SWITCHER:start-->.*?<!--@SWITCHER:end-->','<!--@SWITCHER-->',s,flags=re.S)
    return s.replace('<!--@SWITCHER-->',f'<!--@SWITCHER:start-->{body}<!--@SWITCHER:end-->')
dark=put(src,sw('./'))
(p/'index.html').write_text(dark)
light=put(src,sw('light.html')).replace('<body>','<body class="theme-light">',1).replace('<title>Окна Houselux — концепт</title>','<title>Окна Houselux — светлая версия</title>',1)
(p/'light.html').write_text(light)
print('ok')
