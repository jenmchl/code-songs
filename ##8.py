print(SynthDefs)

Clock.bpm= 0
Scale.default= "minor"

var.chords=var([0,2,0,6]+[4,4,3,1])

b1 >> feel([0,2,0,6]+[4,4,3,1], dur=1, amp=1).every(1,"stutter",4)

b2 >> sawbass([var.chords], dur=1/4, amp=0.6, oct=5, coarse=1)

p1 >> play("x", dur=PDur(3,8), amp=1.4, sample=1)

p2 >> play("--- -- --- -- -", sample=7, amp=1)

b3 >> spark([var.chords], dur=1, amp=0.7).every(1,"stutter",4)

p3 >> play("xxox", coarse=0)

