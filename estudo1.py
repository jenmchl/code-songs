Clock.bpm=115
Scale.default = "major"


a1 >> donk(([0,3,6,9]), dur=1/2, oct=5, amp=1, coarse=1).every(4, 'stutter', dur=1/2)

a2 >> play(("-+-", " x "), amp=3, dur=1/2, pan=[1,-1], hpf=var([0,100],[16,2]))

a3 >> play(PZip ("Vv", "  s "), amp=2, dur=1/2, hpf=var([0,4000],[16,4])).every(8, 'stutter',dur=1/2)

a4 >> pluck([0,6/1,9,2,1/6]+[0,1,8], dur=1/2, oct=8, amp=0.8)

a5 >> play("x+{--[++]}", dur=1/2, amp=2)


b1 >> space([2,4,8,6]+[2,4,8], amp=1, dur=(1/2,1/2,2,6), oct=3, pan=[1,-1])

b2 >> bell((0,2,4,6), dur=4, amp=0.30, oct=4).every(8, 'stutter',dur=1/2)

b3 >> play("v-", amp=0.8, sample=8)

b4 >> viola([2,4,6,2,8,6]+[0,2,8], dur=PDur(1,8), oct=6, amp=0.8)


c1 >> creep([0,-2,-6,2]+[1,-2,-4], dur=1, amp=0.3, blur=2).every(8, 'stutter',1)


print(SynthDefs)
