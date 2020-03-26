Clock.bpm = 135
Scale.default = "minor"
Root.default = 1

var.chords = var[0,1,4,2,7,9,7,6,5,8,2,1,9]

b1 >> karp([0,1,4,2,7,9,7,6,5,8,2,1,9]+[11,2,8], amp=1.2, dur=1/4, hpf=var([0,2000],[16,4])).every(8, "stutter", 3)

p1 >> play("Vs")

p2 >> play("q+", dur=2)

b2 >> dbass([0,1,4,2,7,9,7,6,5,8,2,1,9], dur=1/4, amp=0.5)

print(SynthDefs)
