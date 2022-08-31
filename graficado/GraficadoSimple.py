import random
from bokeh.plotting import figure, output_file, show

if __name__ == '__main__':
    output_file('graficado_simple.html')
    fig = figure()
    
    total_valores = int(input('Cuantos valores quieres graficar?: '))
    x = list(range(total_valores))
    y = []

    for i in x:
        y.append(random.randint(0,100))
    
    fig.line(x, y, line_width = 1)
    show(fig)