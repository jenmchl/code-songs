d1 >> play(P["x--(-[--])o--o(-=)"].layer("mirror"),
      pan=(-1,1),
      dur=PDur(5,8),
      sample=-1,
      rate=var([1,4],[28,4])).every(5, 'stutter', 4, pan=[-1,1], rate=4)
      
d2 >> play(PZip ("Vs", "  n "), sample=2, hpf=var([0,4000],[28,4])).every(3,'stutter', dur=1)

d2.solo()

s1 >> swell((0,2,4,const(6)), dur=4) + var([0,[1,-1]],8)

Scale.default = Pvar([Scale.major, Scale.minor], 16)

d3 >> play("[--]")

b1 >> bass(var([0,[1,-1]],8), dur=PDur(3,8), bits=0, lpf=0) + [0,4,const(7)]

k1 >> karp(dur=1/4, oct=var([6,7]), sus=1, rate=P[:32]*(1,2), delay=(0,1/8), lpf=linvar([400,5000],12), pan=linvar([-1,1],8)) + var([0,-1,1,-7])

k1.stop()

p1 >> blip([var([0,-1,-1,0]),4,[7,10],9], dur=PDur(5,8), sus=2, oct=(6), chop=4)
