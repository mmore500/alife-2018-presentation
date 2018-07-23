from subprocess import call

for i in range(2,10):

    t = None

    with open('script/recursive/main.tex','U') as f:

        t = f.read()

        while '{{{}}}' in t:
            t=t.replace('{{{}}}',str(i-1))

    with open('script/recursive/main-'+str(i)+'.tex','w') as f:

        f.write(t)

    call(['latexmk', '-pdf', '-silent',
        '-jobname=level-'+str(i),
        '-pdflatex=pdflatex',
        'script/recursive/main-'+str(i)+'.tex'])

    call(['mv','level-'+str(i)+'.pdf', 'img/recursive'])
    call(['rm','level-'+str(i)+'.log'])
    call(['rm','script/recursive/main-'+str(i)+'.tex'])
