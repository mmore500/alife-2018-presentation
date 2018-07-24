import svgutils.compose as cg
from tqdm import tqdm


for c in tqdm([1,2,4,9,18]):

    wh = str(16*c/12)+"cm"
    cg.Figure(wh,wh,*[cg.SVG('img/cpu.svg').scale(3) for __ in range(c*c)]).tile(c,c).save("img/cpugrids/cpu1-"+str(c)+".svg")
