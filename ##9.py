print(SynthDefs)

Clock.bpm=120
Scale.default="major"
Root.default= 0

p4 >> play("Vs")


b1 >> blip([0,4,3,-2,4]+[1,1,4], dur=1/2, oct=5)


p1 >> play("x", sample=1, dur=PDur(3,8), amp=0.8)

p1.stop()

p2 >> play("ppp pp p pp", sample=1, amp=1)

p2.stop()

p3 >> play("P", sample=1, dur=1/2, amp=1.2, pan=[1,-1]).every(2,"stutter", 2)

p3.stop()

b2 >> dbass([0,4,3,-2,4]+[1,1,4], dur=1/4, oct=5, amp=0.5, tremolo=2)

b2.stop()

p4 >> play("Vs")

p4.stop()

