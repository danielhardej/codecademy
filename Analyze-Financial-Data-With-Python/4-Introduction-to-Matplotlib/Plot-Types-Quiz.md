# Introduction to `matplotlib`

## Plot Types Quiz

#### What type of graph would work best to display the change in temperature in a city over time?

 - [ ] Pie
 - [x] Line
 - [ ] Bar
 - [ ] Histogram

#### What does it mean to normalize a histogram?

 - [ ] Normalizing is changing the transparency of the histogram bars so that multiple histograms can be seen on the same plot.
 - [x] Normalizing is dividing the height of each column by a constant such that the area under the curve sums to 1.
 - [ ] Normalizing is setting the range of the data to be 2 standard deviations above and below the mean.
 - [ ] Normalizing is removing outliers from the data so that the range of the data is smaller.


#### Which line of code will create a bar graph with error bars displaying +/- 4 error, with caps of size 10?

 - [ ] plt.error_bars(4, csize=10)
 - [x] plt.bar(x, y, yerr=4, capsize=10)
 - [ ] plt.error_bars(4, 10)
 - [ ] plt.bar(x, y, yerr=8, caps=10)


#### In the following function call, what does the list [0, 2, 4, 6, 8] represent?

    `plt.fill_between(range(5), [0, 2, 4, 6, 8], [4, 6, 8, 10, 12], alpha=0.2)`
 
 - [ ] The upper-bound y-values to plot
 - [ ] The transparency value of each point
 - [ ] The x-values to plot
 - [x] The lower-bound y-values to plot


#### What is the command to set x-axis ticks to be "Carbohydrates", "Lipids", "Protein"?

 - [ ] ax.xlabel(["Carbohydrates", "Lipids", "Protein"])
 - [ ] ax.xticks(["Carbohydrates", "Lipids", "Protein"])
 - [ ] ax.set_xlabels("Carbohydrates", "Lipids", "Protein")
 - [x] ax.set_xticklabels(["Carbohydrates", "Lipids", "Protein"])



#### What is the result of adding autopct='%d%%' to a plt.pie function call?

 - [ ] The pie chart will automatically resize to the specified percentage of the figure.
 - [ ] The pie chart will now display percentages, rounded to one decimal point, on each slice of the pie.
 - [x] The pie chart will now display percentages, rounded to the nearest int, on each slice of the pie.
 - [ ] The axes of the pie chart will be equal.

#### What type of graph would work best to display the proportion of team members who own a cat, dog, bird, or no pet? (Assume each team member can only own one pet.)

 - [ ] Bar
 - [ ] Line
 - [ ] Histogram
 - [x] Pie


#### What is the command to plot a bar graph in Matplotlib?

 - [ ] plt.graph
 - [ ] plt.bar_graph
 - [x] plt.bar
 - [ ] plt.plot


#### What is the command to stack a set of bars representing y2 on top of the set of bars representing y1?

 - [ ] plt.stack(y1, y2)
 - [ ] plt.bar(range(len(y1)), y1, stack=y2)
 - [x] plt.bar(range(len(y2)), y2, bottom=y1)
 - [ ] plt.bar(bottom=y1, top=y2)


#### What is the command to divide the data in a histogram into 10 equally-sized bins?

 - [ ] plt.hist(data%10)
 - [ ] plt.hist(data, range=10)
 - [ ] plt.hist(data, binsize=10)
 - [x] plt.hist(data, bins=10)


#### What are the inputs to the plt.bar function, in order?

 - [x] x values (list of numbers), y values (list of numbers)
 - [ ] x categories (list of strings), y values (list of numbers)
 - [ ] y values (list of numbers), x values (list of numbers)
 - [ ] x categories (list of strings), y categories (list of strings)


