Clock.bpm=120 
Scale.deafault = "minor"

p1 >> play("n", dur=1/4, sample=PRand(7)).every(7.5, "stutter", 12, pan=var([-1,1]))

p2 >> play("fX" "sX", amp=2, room=0.5, sample=1)
    
p3 >> play("mV {+[--]}").every(8, "stutter", 1/2)

p4 >> play("---,- +-", dur=1/4, sample=PRand(6), pan=var([-1,1]))

p5 >> play("P", dur=1/4, amp=1, sample=PRand(8)).every(8, "stutter", 1/2)

b1 >> dirt([2,4,5,], amp=0.8, dur=1/4).every(8, "stutter", dur=1/4)

b2 >> viola([2,4,5], amp=1, dur=1/4, coarse=1, echo=2, sample=2)
 
