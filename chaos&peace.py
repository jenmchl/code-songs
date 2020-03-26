Clock.bpm=130
Scale.default="major"

print(SynthDefs)

print(Player.get_attributes())

print(Scale.names())


a1 >> play("w ww ww ", sample=1, dur=1/2, chop=0, amp=0.7)

a2 >> play(" x", sample=1, amplify=3)

a3 >> play("@",dur=1, sample=1, glide=0, amp=0.0)

a4 >> play("#",dur=1, sample=1, tremolo=4)

a5 >> play("s ",dur=1/2, sample=3, room=0, amplify=1) 

b1 >> pasha([-10,-4,8,2,4,1]+[0,3], hpf=linvar([0,4000],[32,0]), dur=1/4, scale=Scale.indian)

a6 >> play(" X")

b1.stop()
b2 >> 
