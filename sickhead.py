Clock.bpm=115
Scale.default = "major"


d1 >> donk(([0,3,6,9]), dur=1/2, oct=5, amp=1, coarse=1).every(4, 'stutter', dur=1/2)

d2 >> play(("-+-", " x "), amp=3, dur=1/2, pan=[1,-1], hpf=var([0,100],[16,2]))

d3 >> play(PZip ("Vv", "  s "), amp=2, dur=1/2, hpf=var([0,4000],[16,4])).every(8, 'stutter',dur=1/2)

d4 >> pluck([0,6/1,9,2,1/6]+[0,1,8], dur=1/2, oct=8, amp=0.8)
d4.stop()



c1 >> creep([0,-2,-6,2]+[1,-2,-4], dur=1, amp=0.8, blur=2).every(8, 'stutter',1)

print(SynthDefs)
