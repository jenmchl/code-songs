ch = var([0,6,8,4])

p1 >> pluck([-10,-6,8], dur=1/2) + (0,8)

#p2 >> play("lambda", amp=1) + (0,2)

z1 >> zap([3,2,0], sus=1/2,dur=1/4, amp=4)

v1 >> viola(ch, dur=ch.dur, oct=(1,4)) + (0,2,4) + var([(0,2),(2,4)])

c1 >> crunch(dur=1/4)

p3 >> play ("xxox")

be >> bell ([2,4,0,2,0], dur=PSum(5,4), oct=(5,6))




