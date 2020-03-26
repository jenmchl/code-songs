Clock.bpm=130
Scale.default= "major"
Root.default= 0

var.chords = var([1,4,5,9,2])

b7 >> play("xoxx", dur=1, sample=b7.degree.map({"x":6,"o":3}))

b1 >> play("x xv +V ", sample=b1.degree.map({"x":5,"v":2,"+":2,"V":4}), amp=1, dur=1/2)

b2 >> pluck([var.chords]+[1,4,3], dur=1/2, oct=6, room=4).every(16, "stutter", 4)

b2.stop()

b3 >> play("  [---------------------------]     ", sample=7)

b3.stop()

b4 >> dbass([var.chords]+[2,4,3], dur=1/2, oct=8, amp=0.3, coarse=2, room=2)

b4.stop()

b5 >> dirt([var.chords], dur=PDur(3,8), oct=6, blur=3, amp=0.5)

b5.stop()

b6 >> play("-- ---- -- - -- --", amp=3, sample=6)

b6.stop()
