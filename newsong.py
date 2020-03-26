Bpm=130
Scale.default="minor"

print(SynthDefs)

a1 >> play("q", dur=1, sample=1, hpf=linvar([0,4000],[32,0]))

a2 >> play("-", dur=1, amp=1, coarse=4, sample=1)

a3 >> play("xs", sample=1)
