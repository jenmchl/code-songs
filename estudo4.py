Clock.bpm = 115
Scale.default = "minor"
Root.default = -4

var.chords = var([-2,1,-6,2])

b1 >> blip([var.chords,2,[2,8],4], dur=PDur(3,8), sus=2, fmod=2, coarse=4, blur=2, amp=0.)

p1 >> play("xs", sample=([1,8]))

b1.stop()

b2 >> bell([var.chords,4,[8,4],6], amp=0.5, fmod=2, tremolo=4)
b2.stop()

p2 >> play("-- - -- - -- --- [---]", sample=7, dur=PDur(2,8), amp=2)
p2.stop()


b3 >> star([var.chords], dur=12, amp=1)








print (SynthDefs)
