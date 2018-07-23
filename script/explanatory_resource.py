import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from tqdm import tqdm
import matplotlib
import matplotlib.lines as mlines

# open-type fonts
matplotlib.rcParams['pdf.fonttype'] = 42

#
s_res = [0,  1,  2,  2,  2,  2,  2,  2,  2]
m_res = [0,  1,  5, 13, 13, 13, 13, 13, 13]
l_res = [0,  1,  5, 13,-47,-62,-62,-62,-62]

def draw(data,name):

    for i,d in enumerate(data):
        fig = plt.figure(figsize=(2,10))
        ax = plt.subplot(111)
        ax.set_ylim((-70,70))

        bars = ax.bar([0], [d], width=1, color='r' if d < 0 else 'g')
        ax.set_yscale('symlog')

        for rect in bars:
            height = rect.get_height()
            plt.text(rect.get_x() + rect.get_width()/2.0, height, ('' if height < 0 else '+')+'%d' % int(height), ha='center', va='bottom', size=36, color='w'if height<0 else 'g')

        plt.gca().get_xaxis().set_ticks([])
        plt.gca().get_yaxis().set_ticks([])
        plt.minorticks_off()
        # plt.majorticks_off()
        plt.ylabel('Net Resource',fontsize=36)

        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)
        plt.gca().spines['bottom'].set_visible(False)
        plt.gca().spines['left'].set_visible(False)
        ax.axhline(y=0, color='k')

        plt.tight_layout(pad=0.4)

        plt.savefig('img/explanatory_sep/'+name+'-'+str(i)+'.pdf')

draw(s_res,'rs')
draw(m_res,'rm')
draw(l_res,'rl')
