
Clock.bpm=130
Scale.default = "minor"
Root.default= 0


d1 >> play("[V-]", dur=1, amp=1)

d2 >> play("q", sample=1 , dur=PDur(3,8), amp=1)

b1 >> viola([0,2.4,2,0.2], dur=1, fmod=2, room=1, tremolo=3, amp=1)

b2 >> bass([0,2.4,2], fmod=4, dur=1/2, amp=0.7)

b3 >> lazer([2,4.8,4,2,0,4,2], var=[2,0,4], oct=4, dur=1/2, amp=2)

print(SynthDefs)
