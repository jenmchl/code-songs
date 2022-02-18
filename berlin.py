Clock.bpm = 120
Root.default = 0
Scale.default = Scale.chromatic

var.keys = var([-4,-8,-4,-2])

#intro

b1 >> bell(chop=8, dur=4, fmod=8, amp=2, spin=6)

#pt1

a1 >> ambi([1], oct=2, amp=6, output=P[2,4,8,12,14,16,20,22,24])

b4.stop()

b2 >> bell(chop=8, dur=2, fmod=8, amp=2, spin=6)

p1 >> play(("<x-x->"), amp=6)

#pt2

b3 >> bass(P[var.keys, 0], dur=1/4, fmod=8, amp=3, pan=[1,-1])

p4 >> play (" ccc", dur=1/4, amp=1, pan=[-1,1])

b4 >> snick(P[var.keys, 2], oct=4, amp=2)

p3 >> play('r',dur=PDur(3,8), amp=1)


print(SynthDefs)
