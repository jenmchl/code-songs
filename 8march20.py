Clock.bpm = 125
Scale.default = "minor"
Root.default = -2

print(SynthDefs)

a1 >> sinepad((8,3,4), bpm=125, dur=1, blur=3, amp=0.2)

a2 >> sinepad(([-8,3,4],[4,5,2,-8]+[2,0,0]), dur=1/4, fmod=var([-110,-400]+[-2,-32]), pan=(1,-1))

b1 >> play("x-")

b2 >> play(" s", sample=2)

a3 >> dbass(([-8,3,4],[4,5,2,-8]+[2,0,0]), dur=1/4, oct=4, amp=0.8, room=1)

b3 >> play("X ", sample=1)
