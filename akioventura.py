Clock.bpm=130
Scale.default= "minor"
Root.default= 0

print(SynthDefs)

b1 >> dbass([0,2,5,7]+[0,4,8], dur=PDur(3,8), tremolo=1, amp=3)

b3 >> scatter([0,2,5,7]+[0,4,8], dur=PDur(3,8), amp=3)

b3.stop()

p1 >> play("h ")

p1.stop()

p2 >> play("vs", dur=1/2, amp=4)

p3 >> play("fff f ff f ff", sample=1, dur=1/4, amp=2)

b2 >> gong([0,2,5,7], dur=1/2, fmod=6, amp=4).every(6, "stutter", 4)
b2.stop()

b3 >> sinepad([0,2,5,7]+[0,4,8], dur=PDur(3,8), amp=3)

b4 >> bass(dur=2, amp=2)

b5 >> bell([8,6,4,3], dur=1/4, blur=5, amp=1)

b4.stop()

