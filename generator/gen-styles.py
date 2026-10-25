IDENT = "Akane — backend developer · AI models & agents · DevOps · self-hoster"
SVC_L1 = "Immich (photos) · Pocket ID (SSO) · Beszel (monitoring)"
SVC_L2 = "Miniflux (RSS) · Open WebUI (LLM chat) · Arcane (Docker management)"
STATUS = "Server status: monitor.akaneri.tech"
INTERESTS = ["backend development and DevOps", "AI models and agents — following how the field develops", "self-hosting"]
CURRENT = "handing routine ops to AI agents and supervising the results"
Otc = [("listening","Aya Hinata · Hitsujibungaku · Gen Hoshino — on Spotify"),
       ("reading","Japanese mystery novels · WeRead annual subscriber"),
       ("playing","Overwatch · Death Stranding")]
MONO = "'JetBrains Mono','Fira Code','Cascadia Code',Consolas,monospace"
SANS = "Inter,'Segoe UI',Helvetica,Arial,sans-serif"
SERIF = "Georgia,'Times New Roman',serif"
from xml.sax.saxutils import escape as xesc
IDENT = xesc(IDENT)
SVC_L1 = xesc(SVC_L1); SVC_L2 = xesc(SVC_L2); STATUS = xesc(STATUS)
CURRENT = xesc(CURRENT)
INTERESTS = [xesc(t) for t in INTERESTS]
Otc = [(k, xesc(v)) for k, v in Otc]

THEMES = {
  'dark': dict(stage=('#1a1238','#0d0820'), win='#11131c', bar='#1c1f2e', barline='#0a0c14',
               strip='#171a26', striptext='#5a5f7a', shadow=0.5,
               user='#a78bfa', sep='#7a7f99', tilde='#7ee787',
               cmd='#7ee787', arg='#fcd34d', file='#58a6ff', key='#fcd34d',
               txt='#e6edf3', mut='#8b949e', dim='#7a7f99',
               cursor='#c9d1d9', title='#7a7f99', conn='#7ee787'),
  'light': dict(stage=('#f2f4f8','#e2e6ec'), win='#ffffff', bar='#e8ebf0', barline='#d0d5dd',
               strip='#eef1f5', striptext='#8a919c', shadow=0.22,
               user='#6b21a8', sep='#57606a', tilde='#1a7f37',
               cmd='#1a7f37', arg='#9a6700', file='#0550ae', key='#9a6700',
               txt='#1f2328', mut='#6e7781', dim='#6e7781',
               cursor='#1f2328', title='#6e7781', conn='#1a7f37'),
}

def terminal(theme='dark'):
    T = THEMES[theme]
    rows=[]; y=112; LH=19; GAP=34
    def prompt(yy, parts):
        head = ('<text x="110" y="%d" fill="%s">akane</text>'
                '<text x="158" y="%d" fill="%s">:</text>'
                '<text x="165" y="%d" fill="%s">~</text>'
                '<text x="175" y="%d" fill="%s">$</text>') % (yy,T['user'],yy,T['sep'],yy,T['tilde'],yy,T['sep'])
        seg = ''.join('<tspan fill="%s">%s</tspan>' % (c, t) for t, c in parts)
        rows.append(head + '<text x="187" y="%d">%s</text>' % (yy, seg))
    def line(yy, parts, x=110):
        seg = ''.join('<tspan fill="%s">%s</tspan>' % (c, t) for t, c in parts)
        rows.append('<text x="%d" y="%d">%s</text>' % (x, yy, seg))
    SVC = [("Immich","photos"),("Pocket ID","SSO"),("Beszel","monitoring"),
           ("Miniflux","RSS"),("Open WebUI","LLM chat"),("Arcane","Docker management")]
    prompt(y,[('whoami',T['cmd']),(' --verbose',T['arg'])])
    line(y+24,[('\u21b3 ',T['dim']),('Akane',T['key']),(' \u2014 backend developer \u00b7 AI models &amp; agents \u00b7 DevOps \u00b7 self-hoster',T['txt'])])
    y+=24+GAP
    prompt(y,[('cat',T['cmd']),(' ',T['txt']),('selfhosted.txt',T['file'])])
    svc_parts=[]
    for i,(n,d) in enumerate(SVC):
        svc_parts.append((n,T['txt'])); svc_parts.append((' ('+d+')'+(' \u00b7' if i<5 else ''),T['mut']))
    line(y+24, svc_parts[:6]); line(y+24+LH, svc_parts[6:])
    line(y+24+2*LH,[('Server status: ',T['mut']),('monitor.akaneri.tech',T['file'])])
    y+=24+2*LH+GAP
    prompt(y,[('cat',T['cmd']),(' ',T['txt']),('interests.txt',T['file'])])
    for i,t in enumerate(INTERESTS):
        line(y+24+i*LH,[('- ',T['dim']),(t,T['txt'])])
    y+=24+(len(INTERESTS)-1)*LH+GAP
    prompt(y,[('cat',T['cmd']),(' ',T['txt']),('currently.txt',T['file'])])
    line(y+24,[(CURRENT,T['txt'])])
    y+=24+GAP
    prompt(y,[('tail',T['cmd']),(' -3',T['arg']),(' ',T['txt']),('off_the_clock',T['file'])])
    for i,(k,v) in enumerate(Otc):
        main, sep, tail = v.partition(' \u2014 ')
        parts=[(main,T['txt'])]
        if sep: parts.append((' \u2014 '+tail, T['mut']))
        line(y+24+i*LH,[(k,T['dim'])])
        line(y+24+i*LH, parts, 212)
    y+=24+2*LH+28
    body='\n'.join(rows)
    strip_top=y+4; win_h=strip_top-40+22; H=strip_top+22+40
    p=[]
    p.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 %d" width="1200" height="%d">'%(H,H))
    p.append('<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient>'%T['stage'])
    p.append('<filter id="sh" x="-10%%" y="-10%%" width="120%%" height="130%%"><feGaussianBlur in="SourceAlpha" stdDeviation="22"/><feOffset dy="14"/><feComponentTransfer><feFuncA type="linear" slope="%s"/></feComponentTransfer><feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>'%T['shadow'])
    p.append('<rect width="1200" height="%d" fill="url(#g)"/>'%H)
    p.append('<g filter="url(#sh)"><rect x="80" y="40" width="1040" height="%d" rx="14" fill="%s"/><rect x="80" y="40" width="1040" height="38" rx="14" fill="%s"/><rect x="80" y="60" width="1040" height="18" fill="%s"/><line x1="80" y1="78" x2="1120" y2="78" stroke="%s" stroke-width="0.6"/></g>'%(win_h,T['win'],T['bar'],T['bar'],T['barline']))
    p.append('<circle cx="106" cy="59" r="6.5" fill="#ff5f56"/><circle cx="128" cy="59" r="6.5" fill="#ffbd2e"/><circle cx="150" cy="59" r="6.5" fill="#27c93f"/>')
    p.append('<text x="600" y="63" text-anchor="middle" font-family="%s" font-size="11" fill="%s" letter-spacing="2">~/akane \u2014 zsh \u2014 124\u00d726</text>'%(MONO,T['title']))
    p.append('<g font-family="%s" font-size="14">'%MONO)
    p.append(body)
    p.append('<text x="110" y="%d" fill="%s">akane</text><text x="158" y="%d" fill="%s">:</text><text x="165" y="%d" fill="%s">~</text><text x="175" y="%d" fill="%s">$</text>'%(y,T['user'],y,T['sep'],y,T['tilde'],y,T['sep']))
    p.append('<rect x="191" y="%d" width="9" height="14" fill="%s"><animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.5;0.5;1" dur="1.1s" repeatCount="indefinite"/></rect>'%(y-12,T['cursor']))
    p.append('</g>')
    p.append('<rect x="80" y="%d" width="1040" height="22" rx="14" fill="%s"/><rect x="80" y="%d" width="1040" height="12" fill="%s"/><line x1="80" y1="%d" x2="1120" y2="%d" stroke="%s" stroke-width="0.6"/>'%(strip_top,T['strip'],strip_top,T['strip'],strip_top,strip_top,T['barline']))
    p.append('<g transform="translate(80,%d)" font-family="%s" font-size="10" fill="%s"><text x="30" y="0">UTF-8</text><text x="96" y="0">zsh</text><text x="156" y="0">ctrl-l \u00b7 clear</text><text x="1010" y="0" text-anchor="end" fill="%s">\u25cf connected</text></g>'%(strip_top+15,MONO,T['striptext'],T['conn']))
    p.append('</svg>')
    return ''.join(p)

def editorial():
    W=1200; H=680; x=110; y=96; e=[]
    e.append('<text x="%d" y="%d" font-family="%s" font-size="58" font-weight="700" fill="#111">AKANE</text>'%(x,y,SERIF))
    y+=34
    e.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#111" stroke-width="2"/>'%(x,y,W-110,y))
    y+=34
    e.append('<text x="%d" y="%d" font-family="%s" font-size="17" font-style="italic" fill="#444">backend developer · AI models &amp; agents · DevOps · self-hoster</text>'%(x,y,SERIF))
    y+=44
    def sect(title, lines):
        nonlocal y
        e.append('<text x="%d" y="%d" font-family="%s" font-size="12" letter-spacing="3" fill="#777">— %s</text>'%(x,y,SERIF,title))
        y+=24
        for ln,fill,sz,it in lines:
            style = ' font-style="italic"' if it else ''
            e.append('<text x="%d" y="%d" font-family="%s" font-size="%s" fill="%s"%s>%s</text>'%(x,y,SERIF,sz,fill,style,ln))
            y+=24
        y+=16
    sect("SELF-HOSTING", [(SVC_L1,"#111","15",False),(SVC_L2,"#111","15",False),(STATUS,"#111","15",False)])
    sect("INTERESTS", [("·  "+t,"#111","15",False) for t in INTERESTS])
    sect("CURRENTLY", [(CURRENT,"#444","16",False)])
    sect("OFF THE CLOCK", [(k+" — "+v,"#111","14.5",False) for k,v in Otc])
    e.append('<line x1="%d" y1="632" x2="%d" y2="632" stroke="#ddd" stroke-width="1"/>'%(x,W-110))
    out=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d">'%(W,H,W,H),
         '<rect width="%d" height="%d" fill="#fbfaf8"/>'%(W,H)] + e + ['</svg>']
    return ''.join(out)

def swiss():
    import textwrap
    W=1200; H=620; e=[]
    e.append('<rect width="%d" height="%d" fill="#f2f0eb"/>'%(W,H))
    e.append('<defs><pattern id="col" x="72" y="0" width="88" height="%d" patternUnits="userSpaceOnUse"><rect width="76" height="%d" fill="#0f0f0f" opacity="0.055"/></pattern></defs>'%(H,H))
    e.append('<rect x="72" y="0" width="1056" height="%d" fill="url(#col)"/>'%H)
    for by in (120,240,360,480):
        e.append('<line x1="72" y1="%d" x2="1128" y2="%d" stroke="#0f0f0f" opacity="0.08" stroke-width="1"/>'%(by,by))
    e.append('<text x="72" y="150" font-family="%s" font-weight="800" font-size="128" fill="#0f0f0f">AKA<tspan fill="#d0021b">NE</tspan></text>'%SANS)
    e.append('<line x1="760" y1="196" x2="1128" y2="196" stroke="#d0021b" stroke-width="4"/>')
    e.append('<text x="760" y="228" font-family="%s" font-size="15" fill="#0f0f0f">backend developer</text>'%SANS)
    e.append('<text x="760" y="250" font-family="%s" font-size="15" fill="#0f0f0f">AI models &amp; agents</text>'%SANS)
    e.append('<text x="760" y="272" font-family="%s" font-size="15" fill="#0f0f0f">DevOps · self-hoster</text>'%SANS)
    e.append('<text x="72" y="316" font-family="%s" font-size="12" letter-spacing="3" fill="#6d6a63">SELF-HOSTED INDEX</text>'%MONO)
    idx=[("01","Immich","photos"),("02","Pocket ID","SSO"),("03","Beszel","monitoring"),("04","Miniflux","RSS"),("05","Open WebUI","LLM chat"),("06","Arcane","Docker mgmt")]
    yy=342
    for n,s,d in idx:
        e.append('<text x="72" y="%d" font-family="%s" font-size="14" fill="#d0021b">%s</text><text x="118" y="%d" font-family="%s" font-weight="600" font-size="15" fill="#0f0f0f">%s</text><text x="300" y="%d" font-family="%s" font-size="14" fill="#6d6a63">%s</text>'%(yy,MONO,n,yy,SANS,s,yy,SANS,d))
        yy+=26
    e.append('<text x="72" y="%d" font-family="%s" font-size="13" fill="#0f0f0f">status → monitor.akaneri.tech</text>'%(yy+8,MONO))
    e.append('<text x="760" y="316" font-family="%s" font-size="12" letter-spacing="3" fill="#6d6a63">CURRENTLY</text>'%MONO)
    e.append('<text x="760" y="342" font-family="%s" font-size="14" fill="#0f0f0f">handing routine ops to AI agents</text>'%SANS)
    e.append('<text x="760" y="364" font-family="%s" font-size="14" fill="#0f0f0f">and supervising the results</text>'%SANS)
    e.append('<text x="760" y="412" font-family="%s" font-size="12" letter-spacing="3" fill="#6d6a63">OFF THE CLOCK</text>'%MONO)
    yyy=436
    for k,v in Otc:
        lines = textwrap.wrap(v, 33)
        for i,ln in enumerate(lines):
            if i==0:
                e.append('<text x="760" y="%d" font-family="%s" font-size="13" fill="#0f0f0f"><tspan fill="#6d6a63">%s</tspan>  %s</text>'%(yyy,SANS,k,ln))
            else:
                e.append('<text x="848" y="%d" font-family="%s" font-size="13" fill="#0f0f0f">%s</text>'%(yyy,SANS,ln))
            yyy+=19
        yyy+=7
    out=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d">'%(W,H,W,H)] + e + ['</svg>']
    return ''.join(out)

def bento():
    W=1200; M=24; G=16; e=[]
    e.append('<rect width="%d" height="660" fill="#0d1117"/>'%W)
    def card(x,y,w,h):
        e.append('<rect x="%d" y="%d" width="%d" height="%d" rx="16" fill="#161b22" stroke="#30363d"/>'%(x,y,w,h))
    def label(x,y,t,c):
        e.append('<text x="%d" y="%d" font-family="%s" font-size="11" letter-spacing="2.5" fill="%s">%s</text>'%(x,y,MONO,c,t.upper()))
    c1w=int((W-2*M-2*G)*0.42); c2w=W-2*M-2*G-c1w
    card(M,M,c1w,150); card(M+c1w+G,M,c2w,150)
    e.append('<text x="%d" y="%d" font-family="%s" font-weight="800" font-size="40" fill="#f0f6fc">AKANE</text>'%(M+24,M+64,SANS))
    e.append('<text x="%d" y="%d" font-family="%s" font-size="14.5" fill="#8b949e">backend developer · AI models &amp; agents</text>'%(M+24,M+98,SANS))
    e.append('<text x="%d" y="%d" font-family="%s" font-size="14.5" fill="#8b949e">DevOps · self-hoster</text>'%(M+24,M+120,SANS))
    x2=M+c1w+G
    label(x2+24,M+40,"currently","#7ee787")
    e.append('<text x="%d" y="%d" font-family="%s" font-size="16" fill="#f0f6fc">handing routine ops to AI agents</text>'%(x2+24,M+70,SANS))
    e.append('<text x="%d" y="%d" font-family="%s" font-size="16" fill="#f0f6fc">and supervising the results</text>'%(x2+24,M+94,SANS))
    e.append('<text x="%d" y="%d" font-family="%s" font-size="12.5" fill="#58a6ff">● status → monitor.akaneri.tech</text>'%(x2+24,M+122,MONO))
    y2=M+150+G
    card(M,y2,W-2*M,196)
    label(M+24,y2+36,"things i self-host","#a78bfa")
    chips=[("Immich","photos"),("Pocket ID","SSO"),("Beszel","monitoring"),("Miniflux","RSS"),("Open WebUI","LLM chat"),("Arcane","Docker mgmt")]
    cx=M+24; cy=y2+56
    for n,d in chips:
        wch=int(len(n)*9+len(d)*7.6+44)
        e.append('<rect x="%d" y="%d" width="%d" height="34" rx="8" fill="#0d1117" stroke="#30363d"/>'%(cx,cy,wch))
        e.append('<text x="%d" y="%d" font-family="%s" font-size="13" fill="#f0f6fc">%s <tspan fill="#8b949e">· %s</tspan></text>'%(cx+16,cy+22,SANS,n,d))
        cx+=wch+10
        if cx>W-M-280: cx=M+24; cy+=44
    e.append('<text x="%d" y="%d" font-family="%s" font-size="13" fill="#8b949e">identity by Pocket ID · containers by Arcane · watched by Beszel — the stack watches itself</text>'%(M+24,y2+168,SANS))
    y3=y2+196+G; i_w=int((W-2*M-G)*0.46); o_w=W-2*M-G-i_w
    card(M,y3,i_w,200); card(M+i_w+G,y3,o_w,200)
    label(M+24,y3+36,"interests","#79c0ff")
    yy=y3+64
    for t in INTERESTS:
        e.append('<text x="%d" y="%d" font-family="%s" font-size="14" fill="#c9d1d9">· %s</text>'%(M+24,yy,SANS,t))
        yy+=24
    xo=M+i_w+G
    label(xo+24,y3+36,"off the clock","#ffa657")
    yy=y3+66
    for k,v in Otc:
        e.append('<text x="%d" y="%d" font-family="%s" font-size="12" fill="#8b949e">%s</text><text x="%d" y="%d" font-family="%s" font-size="14" fill="#c9d1d9">%s</text>'%(xo+24,yy,MONO,k,xo+112,yy,SANS,v))
        yy+=30
    out=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d 660" width="%d" height="660">'%(W,W)] + e + ['</svg>']
    return ''.join(out)

if __name__ == "__main__":
    import xml.dom.minidom as md
    import sys, os
    os.chdir(os.path.expanduser("~/Project/chat/profile-styles"))
    for name, svg in [("terminal",terminal("dark")),("terminal-light",terminal("light")),("editorial",editorial()),("swiss",swiss()),("bento",bento())]:
        md.parseString(svg)
        open(name+".svg","w").write(svg)
        print(name, "OK")
