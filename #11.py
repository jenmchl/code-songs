Clock.bpm=140
Scale.default="minor"
Root.default=0

p1 >> play("X ", amp=1.5)

p2 >> play(" -", sample=7, amp=3)

p3 >> play(" fff f fff f ff ", sample=2)

p3.stop()

b1 >> glass(dur=2, fmod=2, tremolo=3, blur=2, amp=0.3)

p4 >> play("Vv", dur=1)

b2 >> swell([0,5,3,2]+[0,1,3], oct=5, coarse=3, amp=0.3)

print(SynthDefs)
