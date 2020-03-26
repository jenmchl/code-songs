Clock.bpm=115
Scale.default = "major"

a1 >> glass([1], amp=0.7, sus=4, reverb=2)

a2 >> space([1,5,3], dur=16, amp=0.7)

a3 >> sinepad([1], dur=16, oct=6, sus=2, echo=3, room=1, amp=0.7)

a4 >> ambi([(9,4,2,0),(3,5,2,7)], dur=8, sus=6, room=3, amp=0.5)


b1 >> charm([1,5,3,9], dur=2, room=7, sus=3, tremolo=2, echo=2)

b2 >> pads([(1,7),(1,7),(3,9),(5,9)], dur=4, fmod=2, amp=0.6, oct=4, room=6, coarse=2, blur=2)

b3 >> marimba([3,7,1,5,3], dur=[1,1,1,1/2,1/2], room=5, oct=5, amp=3).shuffle()

b4 >> donk((1,9), dur=PDur(3,8), amp=0.7).every(8, 'stutter')

