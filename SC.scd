Quarks.install("FoxDot")

FoxDot.start

Platform.userExtensionDir

{
        var x = SinOsc.ar(MouseX.kr(1, 100));
	var y = SinOsc.ar(MouseY.kr(1, 100));
        SinOsc.ar(300 * x + 800, 0, 0.1)
        +
        PinkNoise.ar(0.1 * y + 0.1)
}.play;