from   ROOT    import *
from   iminuit import Minuit
import numpy   as     np
from   math    import *

#Main

h  = TH1D("h","",20,0,10)
for line in open("exp.dat"):
    h.Fill(float(line))

h.Draw("E")

f = TF1("f","[1]/[0]*exp(-x/[0])",0,10)
f.SetParameter(0,1)
f.SetParameter(1,h.GetEntries()*h.GetBinWidth(1))
print(h.GetEntries()*h.GetBinWidth(1))
h.Fit("f","L")

gApplication.Run(True)

