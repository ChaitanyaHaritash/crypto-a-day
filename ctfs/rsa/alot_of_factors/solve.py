#!/full/path/to/sage -python

from sage.all import *


e = 65537

n = 638660878087472358996570905277645893464713278579202478657573523144175081073102094406933450365370825406374546644491443938977915437597703423308605854881003722273326558998045782346994957619537814664832385201010153776018661445863260915187696275569780167937886360244626397901640694539229287761690847276298273

c = 571583761312452626717249726031229278368217682192904641677766966237627700353724664817014070551016728110390656899885008845974176384109748345150417016203031937173045328442575013421607805990567637476353855484034654085940253974502605169327217314099449181792303176762731136118965578030800816734805718988658861

phi = (2148685727 -1)*(2158008403 -1)*(2314216241 -1)*(2333217269 -1)*(2335487009 -1)*(2376496607 -1)*(2407617371 -1)*(2443146737 -1)*(2485953859 -1)*(2512580639 -1)*(2547022057 -1)*(2644542223 -1)*(2705949637 -1)*(2768113367 -1)*(2775843583 -1)*(2778924943 -1)*(2783508671 -1)*(2829162143 -1)*(2845776001 -1)*(2957112023 -1)*(3096006647 -1)*(3130498457 -1)*(3263232293 -1)*(3296048869 -1)*(3436811437 -1)*(3577456139 -1)*(3603161741 -1)*(3813438169 -1)*(3931129519 -1)*(3994187501 -1)*(4147229587 -1)*(4229134831-1)

if gcd(e, phi) == 1:
	print "[+] Works well"

d = inverse_mod(e, phi)
intz = pow(c,d,n)
intz = int(intz)
plain = hex(intz)
flag = plain[2:-1].decode('hex')
print flag
# picoCTF{p_&_q_n0_r_$_t!!_1251830}
