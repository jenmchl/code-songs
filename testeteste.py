d1 >> play(P["x--(-[--])o--o(-=)"].layer("mirror"),
      pan=(-1,1),
      dur=PDur(5,8),
      sample=-1,
      rate=var([1,4],[28,4]))
      
d2 >> play(PZip ("Vs", "  n "), sample=2, hpf=var([0,4000],[28,4])).every(3,'stutter', dur=1)
 
b1 >> dirt(var([0,2,-1,3]), dur=PDur(3,8), bits=4, lpf=40, fmod=(0,1))
