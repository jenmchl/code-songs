print(SynthDefs)

Clock.bpm=130
Scale.default="minor"
Root.default=-4

b1 >> karp([-4,0,-2,3,6,7,2,3,1]+[0,0,2,1,3,5,0,0,6,4], coarse=0, oct=5, dur=1/2, amp=0.2).every(16,"stutter", 4)

p1 >> play(" v vv V ", dur=1/4, sample=4, amp=1) 

p2 >> play("- ",dur=1/2, sample=7, room=1, amp=1.5)

p3 >> play(" s", dur=1/2, sample=1)

p4 >> play("vs")

b1.stop()
p2.stop()
p3.stop()





