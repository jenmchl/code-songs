Clock.bpm=115
Scale.default = "major"

a1 >> play("x", dur=1,amp=0.5, sample=3)
a1.stop()

a2 >> donk((1,9))
a2.stop()

a3 >> play("vv[tt]+", amp=0.50, dur=2, pan=[1,-1])
a3.stop()

a4 >> play("--,- --", amp=2)
a4.stop()


a5 >> glass([2,3,4,5] + [0,2,8], amp=0.8)
a5.stop()

a6 >> bass([2,1,3,8] + [0,9,8], dur=1/2, amp=0.45) + (2)
a6.stop()

a7 >> play("xxox")
a7.stop()
