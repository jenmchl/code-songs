Clock.bpm = 115
Scale.default = "minor"
Root.default = -4

var.chords = var([-2,1,-6,2])

b1 >> blip([var.chords,2,[2,8],4], dur=PDur(3,8), sus=2, fmod=2, coarse=4, blur=2, amp=0)

p3 >> play("xs", sample=([1,8]), amp=1.4)

p4 >> play("  + + ++", sample=4, dur=1/2, amp=0.6)
p4.stop()
p2.stop()

b2 >> bell([var.chords,4,[8,4],6], amp=0, fmod=2, tremolo=4)

p2 >> play("-- - -- - -- --- [---]", sample=7, dur=PDur(2,8), amp=2)

b3 >> star([var.chords,9,11,13]+[9,7], dur=PDur(3,8), amp=0.8, tremolo=4, coarse=0, blur=3)
b3.stop()

b3.stop()










print (SynthDefs)
