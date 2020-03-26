print (SynthDefs)

Clock.bpm=118
Root.default= -6
Scale.default = "minor"

a1 >> bug(([0,2,4,8]), dur=2, amp=0.5, pan=[1,-1])

a2 >> pluck([2,4,6,0]+[1,0,8], amp= 0.8, 
       dur=PDur(3,8), 
       blur=4, 
       tremolo=3, 
       oct=7).every(8, "stutter", 2)

a3 >> play("Vc (cv)", amp=0.8, dur=1/4, sample=(1), tremolo=4)

a4 >> play("s- [-+]", amp=2)
