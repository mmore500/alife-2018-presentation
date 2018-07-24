from subprocess import call

call(['latexmk', '-pdf', '-silent',
    '-jobname=cpu-dots',
    '-pdflatex=pdflatex',
    'script/dots/cpu-dots.tex'])

call(['latexmk', '-pdf', '-silent',
    '-jobname=sub-dots',
    '-pdflatex=pdflatex',
    'script/dots/sub-dots.tex'])

call(['mv','cpu-dots.pdf', 'img/cpugrids'])
call(['mv','sub-dots.pdf', 'img/subgrids'])
