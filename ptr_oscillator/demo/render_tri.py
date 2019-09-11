import numpy
import soundfile
from pathlib import Path

# yapf: disable
def PTRTri0(phi, T):
    n = phi / T
    return 4*T*n-1

def PTRTri1(phi, T):
    n = phi / T
    if n >= 0.0:
        return 4*T*n-2*T-1
    if 0.0 <= n and n < 1.0:
        return 4*T*n**2-4*T*n+2*T-1
    return 0  # Just in case.

def PTRTri2(phi, T):
    n = phi / T
    if n >= 1.0:
        return 4*T*n-4*T-1
    if 0.0 <= n and n < 1.0:
        return (4*T*n**3)/3-4*T*n+4*T-1
    if 1.0 <= n and n < 2.0:
        return -(4*T*n**3)/3+8*T*n**2-12*T*n+(20*T)/3-1
    return 0  # Just in case.

def PTRTri3(phi, T):
    n = phi / T
    if n >= 2.0:
        return 4*T*n-6*T-1
    if 0.0 <= n and n < 1.0:
        return (T*n**4)/3-4*T*n+6*T-1
    if 1.0 <= n and n < 2.0:
        return -(2*T*n**4)/3+4*T*n**3-6*T*n**2+5*T-1
    if 2.0 <= n and n < 3.0:
        return (T*n**4)/3-4*T*n**3+18*T*n**2-32*T*n+21*T-1
    return 0  # Just in case.

def PTRTri4(phi, T):
    n = phi / T
    if n >= 3.0:
        return 4*T*n-8*T-1
    if 0.0 <= n and n < 1.0:
        return (T*n**5)/15-4*T*n+8*T-1
    if 1.0 <= n and n < 2.0:
        return -(T*n**5)/5+(4*T*n**4)/3-(8*T*n**3)/3+(8*T*n**2)/3-(16*T*n)/3+(124*T)/15-1
    if 2.0 <= n and n < 3.0:
        return (T*n**5)/5-(8*T*n**4)/3+(40*T*n**3)/3-(88*T*n**2)/3+(80*T*n)/3-(68*T)/15-1
    if 3.0 <= n and n < 4.0:
        return -(T*n**5)/15+(4*T*n**4)/3-(32*T*n**3)/3+(128*T*n**2)/3-(244*T*n)/3+(904*T)/15-1
    return 0  # Just in case.

def PTRTri5(phi, T):
    n = phi / T
    if n >= 4.0:
        return 4*T*n-10*T-1
    if 0.0 <= n and n < 1.0:
        return (T*n**6)/90-4*T*n+10*T-1
    if 1.0 <= n and n < 2.0:
        return -(2*T*n**6)/45+(T*n**5)/3-(5*T*n**4)/6+(10*T*n**3)/9-(5*T*n**2)/6-(11*T*n)/3+(179*T)/18-1
    if 2.0 <= n and n < 3.0:
        return (T*n**6)/15-T*n**5+(35*T*n**4)/6-(50*T*n**3)/3+(155*T*n**2)/6-25*T*n+(307*T)/18-1
    if 3.0 <= n and n < 4.0:
        return -(2*T*n**6)/45+T*n**5-(55*T*n**4)/6+(130*T*n**3)/3-(655*T*n**2)/6+137*T*n-(1151*T)/18-1
    if 4.0 <= n and n < 5.0:
        return (T*n**6)/90-(T*n**5)/3+(25*T*n**4)/6-(250*T*n**3)/9+(625*T*n**2)/6-(613*T*n)/3+(2945*T)/18-1
    return 0  # Just in case.

def PTRTri6(phi, T):
    n = phi / T
    if n >= 5.0:
        return 4*T*n-12*T-1
    if 0.0 <= n and n < 1.0:
        return (T*n**7)/630-4*T*n+12*T-1
    if 1.0 <= n and n < 2.0:
        return -(T*n**7)/126+(T*n**6)/15-(T*n**5)/5+(T*n**4)/3-(T*n**3)/3+(T*n**2)/5-(61*T*n)/15+(1261*T)/105-1
    if 2.0 <= n and n < 3.0:
        return (T*n**7)/63-(4*T*n**6)/15+(9*T*n**5)/5-(19*T*n**4)/3+13*T*n**3-(79*T*n**2)/5+(33*T*n)/5+(941*T)/105-1
    if 3.0 <= n and n < 4.0:
        return -(T*n**7)/63+(2*T*n**6)/5-(21*T*n**5)/5+(71*T*n**4)/3-77*T*n**3+(731*T*n**2)/5-(777*T*n)/5+(8231*T)/105-1
    if 4.0 <= n and n < 5.0:
        return (T*n**7)/126-(4*T*n**6)/15+(19*T*n**5)/5-(89*T*n**4)/3+(409*T*n**3)/3-(1829*T*n**2)/5+(7909*T*n)/15-(32729*T)/105-1
    if 5.0 <= n and n < 6.0:
        return -(T*n**7)/630+(T*n**6)/15-(6*T*n**5)/5+12*T*n**4-72*T*n**3+(1296*T*n**2)/5-(2572*T*n)/5+(15132*T)/35-1
    return 0  # Just in case.

def PTRTri7(phi, T):
    n = phi / T
    if n >= 6.0:
        return 4*T*n-14*T-1
    if 0.0 <= n and n < 1.0:
        return (T*n**8)/5040-4*T*n+14*T-1
    if 1.0 <= n and n < 2.0:
        return -(T*n**8)/840+(T*n**7)/90-(7*T*n**6)/180+(7*T*n**5)/90-(7*T*n**4)/72+(7*T*n**3)/90-(7*T*n**2)/180-(359*T*n)/90+(10079*T)/720-1
    if 2.0 <= n and n < 3.0:
        return (T*n**8)/336-(T*n**7)/18+(77*T*n**6)/180-(161*T*n**5)/90+(329*T*n**4)/72-(133*T*n**3)/18+(1337*T*n**2)/180-(743*T*n)/90+(10847*T)/720-1
    if 3.0 <= n and n < 4.0:
        return -(T*n**8)/252+(T*n**7)/9-(119*T*n**6)/90+(392*T*n**5)/45-(1253*T*n**4)/36+(784*T*n**3)/9-(12089*T*n**2)/90+(5096*T*n)/45-(10979*T)/360-1
    if 4.0 <= n and n < 5.0:
        return (T*n**8)/336-(T*n**7)/9+(161*T*n**6)/90-(728*T*n**5)/45+(3227*T*n**4)/36-(2800*T*n**3)/9+(59591*T*n**2)/90-(35864*T*n)/45+(152861*T)/360-1
    if 5.0 <= n and n < 6.0:
        return -(T*n**8)/840+(T*n**7)/18-(203*T*n**6)/180+(1169*T*n**5)/90-(6671*T*n**4)/72+(7525*T*n**3)/18-(208943*T*n**2)/180+(162647*T*n)/90-(866153*T)/720-1
    if 6.0 <= n and n < 7.0:
        return (T*n**8)/5040-(T*n**7)/90+(49*T*n**6)/180-(343*T*n**5)/90+(2401*T*n**4)/72-(16807*T*n**3)/90+(117649*T*n**2)/180-(117289*T*n)/90+(813463*T)/720-1
    return 0  # Just in case.

def PTRTri8(phi, T):
    n = phi / T
    if n >= 7.0:
        return 4*T*n-16*T-1
    if 0.0 <= n and n < 1.0:
        return (T*n**9)/45360-4*T*n+16*T-1
    if 1.0 <= n and n < 2.0:
        return -(T*n**9)/6480+(T*n**8)/630-(2*T*n**7)/315+(2*T*n**6)/135-(T*n**5)/45+(T*n**4)/45-(2*T*n**3)/135+(2*T*n**2)/315-(2521*T*n)/630+(90721*T)/5670-1
    if 2.0 <= n and n < 3.0:
        return (T*n**9)/2160-(T*n**8)/105+(26*T*n**7)/315-(2*T*n**6)/5+(11*T*n**5)/9-(37*T*n**4)/15+(446*T*n**3)/135-(298*T*n**2)/105-(325*T*n)/126+(9881*T)/630-1
    if 3.0 <= n and n < 4.0:
        return -(T*n**9)/1296+(T*n**8)/42-(20*T*n**7)/63+(12*T*n**6)/5-(512*T*n**5)/45+(106*T*n**4)/3-(1952*T*n**3)/27+(9908*T*n**2)/105-(23776*T*n)/315+(2519*T)/63-1
    if 4.0 <= n and n < 5.0:
        return (T*n**9)/1296-(2*T*n**8)/63+(4*T*n**7)/7-(796*T*n**6)/135+(192*T*n**5)/5-(1474*T*n**4)/9+(1376*T*n**3)/3-(256996*T*n**2)/315+(29216*T*n)/35-(206705*T)/567-1
    if 5.0 <= n and n < 6.0:
        return -(T*n**9)/2160+(T*n**8)/42-(34*T*n**7)/63+(106*T*n**6)/15-(2647*T*n**5)/45+(967*T*n**4)/3-(31366*T*n**3)/27+(278918*T*n**2)/105-(2208487*T*n)/630+(257885*T)/126-1
    if 6.0 <= n and n < 7.0:
        return (T*n**9)/6480-(T*n**8)/105+(82*T*n**7)/315-(62*T*n**6)/15+(1889*T*n**5)/45-(4237*T*n**4)/15+(169762*T*n**3)/135-(374266*T*n**2)/105+(3670169*T*n)/630-(2629679*T)/630-1
    if 7.0 <= n and n < 8.0:
        return -(T*n**9)/45360+(T*n**8)/630-(16*T*n**7)/315+(128*T*n**6)/135-(512*T*n**5)/45+(4096*T*n**4)/45-(65536*T*n**3)/135+(524288*T*n**2)/315-(1047316*T*n)/315+(8343248*T)/2835-1
    return 0  # Just in case.

def PTRTri9(phi, T):
    n = phi / T
    if n >= 8.0:
        return 4*T*n-18*T-1
    if 0.0 <= n and n < 1.0:
        return (T*n**10)/453600-4*T*n+18*T-1
    if 1.0 <= n and n < 2.0:
        return -(T*n**10)/56700+(T*n**9)/5040-(T*n**8)/1120+(T*n**7)/420-(T*n**6)/240+(T*n**5)/200-(T*n**4)/240+(T*n**3)/420-(T*n**2)/1120-(20159*T*n)/5040+(907199*T)/50400-1
    if 2.0 <= n and n < 3.0:
        return (T*n**10)/16200-(T*n**9)/720+(3*T*n**8)/224-(31*T*n**7)/420+(21*T*n**6)/80-(127*T*n**5)/200+(17*T*n**4)/16-(73*T*n**3)/60+(1023*T*n**2)/1120-(22207*T*n)/5040+(2893*T)/160-1
    if 3.0 <= n and n < 4.0:
        return -(T*n**10)/8100+(T*n**9)/240-(69*T*n**8)/1120+(221*T*n**7)/420-(231*T*n**6)/80+(2141*T*n**5)/200-(2183*T*n**4)/80+(2843*T*n**3)/60-(60213*T*n**2)/1120+(161501*T*n)/5040+(5717*T)/800-1
    if 4.0 <= n and n < 5.0:
        return (T*n**10)/6480-(T*n**9)/144+(31*T*n**8)/224-(45*T*n**7)/28+(2891*T*n**6)/240-(2439*T*n**5)/40+(10159*T*n**4)/48-(1995*T*n**3)/4+(857291*T*n**2)/1120-(77967*T*n)/112+(429721*T)/1440-1
    if 5.0 <= n and n < 6.0:
        return -(T*n**10)/8100+(T*n**9)/144-(39*T*n**8)/224+(215*T*n**7)/84-(1953*T*n**6)/80+(6311*T*n**5)/40-(11197*T*n**4)/16+(25265*T*n**3)/12-(4611459*T*n**2)/1120+(4767047*T*n)/1008-(386281*T)/160-1
    if 6.0 <= n and n < 7.0:
        return (T*n**10)/16200-(T*n**9)/240+(141*T*n**8)/1120-(941*T*n**7)/420+(2079*T*n**6)/80-(41021*T*n**5)/200+(89167*T*n**4)/80-(246923*T*n**3)/60+(11064957*T*n**2)/1120-(70223261*T*n)/5040+(7026547*T)/800-1
    if 7.0 <= n and n < 8.0:
        return -(T*n**10)/56700+(T*n**9)/720-(11*T*n**8)/224+(431*T*n**7)/420-(3367*T*n**6)/240+(26207*T*n**5)/200-(40619*T*n**4)/48+(223673*T*n**3)/60-(11994247*T*n**2)/1120+(91191167*T*n)/5040-(19635101*T)/1440-1
    if 8.0 <= n and n < 9.0:
        return (T*n**10)/453600-(T*n**9)/5040+(9*T*n**8)/1120-(27*T*n**7)/140+(243*T*n**6)/80-(6561*T*n**5)/200+(19683*T*n**4)/80-(177147*T*n**3)/140+(4782969*T*n**2)/1120-(4780729*T*n)/560+(42945921*T)/5600-1
    return 0  # Just in case.

def PTRTri10(phi, T):
    n = phi / T
    if n >= 9.0:
        return 4*T*n-20*T-1
    if 0.0 <= n and n < 1.0:
        return (T*n**11)/4989600-4*T*n+20*T-1
    if 1.0 <= n and n < 2.0:
        return -(T*n**11)/554400+(T*n**10)/45360-(T*n**9)/9072+(T*n**8)/3024-(T*n**7)/1512+(T*n**6)/1080-(T*n**5)/1080+(T*n**4)/1512-(T*n**3)/3024+(T*n**2)/9072-(181441*T*n)/45360+(9979201*T)/498960-1
    if 2.0 <= n and n < 3.0:
        return (T*n**11)/138600-(T*n**10)/5670+(17*T*n**9)/9072-(5*T*n**8)/432+(71*T*n**7)/1512-(143*T*n**6)/1080+(287*T*n**5)/1080-(575*T*n**4)/1512+(1151*T*n**3)/3024-(329*T*n**2)/1296-(176833*T*n)/45360+(1993997*T)/99792-1
    if 3.0 <= n and n < 4.0:
        return -(T*n**11)/59400+(T*n**10)/1620-(13*T*n**9)/1296+(289*T*n**8)/3024-(901*T*n**7)/1512+(2773*T*n**6)/1080-(8461*T*n**5)/1080+(3667*T*n**4)/216-(11083*T*n**3)/432+(233893*T*n**2)/9072-(885421*T*n)/45360+(12095749*T)/498960-1
    if 4.0 <= n and n < 5.0:
        return (T*n**11)/39600-(T*n**10)/810+(35*T*n**9)/1296-(1055*T*n**8)/3024+(4475*T*n**7)/1512-(18731*T*n**6)/1080+(15511*T*n**5)/216-(45485*T*n**4)/216+(185525*T*n**3)/432-(5271131*T*n**2)/9072+(4226935*T*n)/9072-(15196927*T)/99792-1
    if 5.0 <= n and n < 6.0:
        return -(T*n**11)/39600+(T*n**10)/648-(55*T*n**9)/1296+(2095*T*n**8)/3024-(11275*T*n**7)/1512+(60019*T*n**6)/1080-(63239*T*n**5)/216+(235765*T*n**4)/216-(1220725*T*n**3)/432+(43947619*T*n**2)/9072-(44991815*T*n)/9072+(230896823*T)/99792-1
    if 6.0 <= n and n < 7.0:
        return (T*n**11)/59400-(T*n**10)/810+(53*T*n**9)/1296-(2441*T*n**8)/3024+(15941*T*n**7)/1512-(103277*T*n**6)/1080+(663581*T*n**5)/1080-(604043*T*n**4)/216+(3818123*T*n**3)/432-(167683997*T*n**2)/9072+(1044830621*T*n)/45360-(6464254061*T)/498960-1
    if 7.0 <= n and n < 8.0:
        return -(T*n**11)/138600+(T*n**10)/1620-(31*T*n**9)/1296+(1675*T*n**8)/3024-(12871*T*n**7)/1512+(98407*T*n**6)/1080-(748207*T*n**5)/1080+(807745*T*n**4)/216-(6064393*T*n**3)/432+(316559287*T*n**2)/9072-(2344872367*T*n)/45360+(3452733371*T)/99792-1
    if 8.0 <= n and n < 9.0:
        return (T*n**11)/554400-(T*n**10)/5670+(71*T*n**9)/9072-(629*T*n**8)/3024+(5561*T*n**7)/1512-(49049*T*n**6)/1080+(431441*T*n**5)/1080-(3782969*T*n**4)/1512+(33046721*T*n**3)/3024-(287420489*T*n**2)/9072+(2486965841*T*n)/45360-(3055862687*T)/71280-1
    if 9.0 <= n and n < 10.0:
        return -(T*n**11)/4989600+(T*n**10)/45360-(5*T*n**9)/4536+(25*T*n**8)/756-(125*T*n**7)/189+(250*T*n**6)/27-(2500*T*n**5)/27+(125000*T*n**4)/189-(625000*T*n**3)/189+(6250000*T*n**2)/567-(12497732*T*n)/567+(124875260*T)/6237-1
    return 0  # Just in case.
# yapf: enable

class PTROscillator:
    def __init__(self, ptr_func, samplerate, frequency):
        self.ptr_func = ptr_func
        self.samplerate = samplerate
        self.setFrequency(frequency)
        self.phi = 0.0

    def setFrequency(self, frequency):
        self.T = frequency / self.samplerate

    def setPhase(self, phi, T):
        self.phi = phi
        ratio = self.T / T
        self.h = ratio - numpy.floor(ratio)

    def process(self):
        self.phi += self.T
        if self.phi >= 1.0:
            self.phi -= 1.0
        if self.phi < 0.5:
            return self.ptr_func(self.phi, self.T)
        return -self.ptr_func(self.phi - 0.5, self.T)

def render():
    samplerate = 44100
    frequency = 1000

    for order in range(11):
        func = globals()[f"PTRTri{order}"]
        osc = PTROscillator(func, samplerate, frequency)

        wav = numpy.empty(samplerate)

        for i in range(len(wav)):
            wav[i] = osc.process()

        snd_dir = Path("snd")
        if not snd_dir.exists():
            snd_dir.mkdir(parents=True)

        soundfile.write(
            str(snd_dir / f"PTRTri{order:02d}.wav"),
            wav,
            samplerate,
            subtype="FLOAT",
        )

render()
