# Introduction to `matplotlib`
## Line Graphs Quiz I

#### What is the command to create a figure with 3 rows and 2 columns, and a subplot in the second row and the first column?

<img src="https://content.codecademy.com/courses/matplotlib/Figure_1.png"  width="40%" height="40%">

 - [x] plt.subplot(3, 2, 3)
 - [ ] plt.plot(3, 2, [2, 1])
 - [ ] plt.figure(3, 2, subplot=3)
 - [ ] plt.subplot(3, 2, 2)

 #### Which line of code will set the y-axis ticks to be at 0, 1, 2, 4, and 9?

 - [ ] ax.yticks([0, 1, 2, 4, 9])
 - [ ] ax.ticks(x, [0, 1, 2, 4, 9])
 - [x] ax.set_yticks([0, 1, 2, 4, 9])
 - [ ] plt.plot(x, [0, 1, 2, 4, 9])

#### What is the command to set the horizontal spacing of subplots within a figure to 0.35?

 - [ ] plt.figure_adjust(space=0.35)
 - [ ] plt.subplot(1, 1, 1, left=0.35)
 - [ ] plt.adjust(hspace=0.35)
 - [x] plt.subplots_adjust(wspace=0.35)

 #### What is the command to plot a line graph in Matplotlib?

 - [ ] plt.show
 - [x] plt.plot
 - [ ] plt.graph
 - [ ] plt.line

#### Which line of code will create a figure with a height of 7 inches and a width of 6 inches?

 - [x] plt.figure(figsize=(6, 7))
 - [ ] plt.set_size([7,6])
 - [ ] plt.figsize(7, 6)
 - [ ] plt.plot(x, y, size=(6, 7))

#### Which line of code will set the x-axis labels to be ["Monday", "Tuesday", "Wednesday"]?

 - [ ] ax.label(x=["Monday", "Tuesday", "Wednesday"])
 - [ ] ax.xlabel(["Monday", "Tuesday", "Wednesday"])
 - [ ] plt.plot(["Monday", "Tuesday", "Wednesday"], y)
 - [x] ax.set_xticklabels(["Monday", "Tuesday", "Wednesday"])

#### What is the command to label the x-axis with the label 'Time'?

 - [ ] plt.set_xlabel('Time')
 - [ ] plt.plot(x, y, label='Time')
 - [x] plt.xlabel('Time')
 - [ ] plt.label(x='Time')

#### What is the command to add a legend to a plot with the labels ['Cats', 'Dogs']?

 - [x] plt.legend(['Cats', 'Dogs'])
 - [ ] plt.legend(loc=['Cats', 'Dogs'])
 - [ ] plt.plot(x, y, legend=['Cats', 'Dogs'])
 - [ ] plt.plot(x, y, labels=['Cats', 'Dogs'])

#### What is the command to set the linestyle of a line to be dashed?

 - [ ] plt.plot(x, y, linestyle='d--')
 - [ ] plt.style('dashed')
 - [ ] plt.linestyle('--')
 - [x] plt.plot(x, y, linestyle='--')

#### What are the inputs to the plt.plot function, in order?

 - [x] x values (list of numbers), y values (list of numbers)
 - [ ] x value (number), y value (number)
 - [ ] x values (list of numbers), scale of axes
 - [ ] y values (list of numbers), x values (list of numbers)

#### What is the command to clear all existing plots?

 - [ ] plt.close_all()
 - [x] plt.close('all')
 - [ ] plt.clear('all')
 - [ ] plt.clear_all()

#### What is the command to set a plot to display from x=-5 to x=5 and from y=0 to y=10?

 - [ ] plt.axis(-5, 0, 5, 10)
 - [ ] plt.set_axis([-5, 0, 5, 10])
 - [ ] plt.plot(x, y, axis=[-5, 5, 0, 10])
 - [x] plt.axis([-5, 5, 0, 10])

#### Which line of code will get the axes object of a plot and store it in a variable ax?

 - [ ] ax = plt.get_axis()
 - [ ] ax = plt.plot()
 - [ ] ax = plt.axes()
 - [x] ax = plt.subplot()

#### What is the command to save a figure to a file called 'it_figures.png'?

 - [ ] `plt.save_figure('it_figures', type='png')`
 - [ ] `plt.save('it_figures.png')`
 - [x] `plt.savefig('it_figures.png')`
 - [ ] `plt.save('it_figures', type='png')`

#### What is the command to set the color of a line to be 'green'?

 - [ ] `plt.plot(x, y, line_color='green')`
 - [x] `plt.plot(x, y, color='green')`
 - [ ] `plt.color('green')`
 - [ ] `plt.line_color('green')`

