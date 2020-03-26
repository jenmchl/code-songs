print(SynthDefs)

Clock.bpm=130
Scale.default="minor"
Root.default=0

c4 >> play(" v vv V ", dur=1/4, sample=4, amp=1) 

p1 >> play("X ", dur=1/2, amp=2)

p4 >> play(" X", sample=1)

c1 >> play(" -", sample=7, amp=3)

c2 >> play(" -", sample=7, room=1, amp=3)

c3 >> play(" s", dur=1/2, sample=3)

p2 >> play(" fff f fff f ff ", dur=1/4, sample=2)

p2.stop()

p3 >> play("+", dur=PDur(4,7), sample=2, amp=0.5).every(16, "stutter", 8)

p3.stop()

b1 >> glass([9,3,2,0,-1,0,3,5,8]+[0,1,-3,8], 
    dur=1/2, 
    oct=4, 
    amp=2,
    fmod=4)
    
b1.stop()
    
b2 >> glass(dur=2, fmod=2, tremolo=3, blur=2, amp=1)




