import matplotlib.pyplot as plt
import numpy as np
import functions as func


class Plotter:
    def __init__(self, x):
        self.x = x
        self.min_x = min(self.x)
        self.max_x = max(self.x)

        self.fig1 = plt.figure()
        self.ax1 = self.fig1.add_subplot(211)
        self.ax2 = self.fig1.add_subplot(212)
        self.ax1.plot(self.x, func.function_char1(self.x), self.x, np.zeros(self.x.shape), "black")
        self.ax2.plot(self.x, func.function_char2(self.x), self.x, np.zeros(self.x.shape), "black")
        self.point = 0

        self.fig1.canvas.mpl_connect('motion_notify_event', self.on_move)
        self.fig1.canvas.mpl_connect('button_press_event', self.on_click)
        plt.show()

    def on_move(self, event):
        try:
            if event.xdata > max(self.x):
                self.x = np.arange(self.min_x, event.xdata, 0.1)
            elif event.xdata < min(self.x):
                self.x = np.arange(event.xdata, self.max_x, 0.1)


            self.redraw_plot()

            self.ax1.scatter(event.xdata, func.function_char1(event.xdata), c='red')
            self.ax2.scatter(event.xdata, func.function_char2(event.xdata), c='red')

            self.ax1.scatter(self.point, func.function_char1(self.point), c='green')
            self.ax2.scatter(self.point, func.function_char2(self.point), c='green')

            event.canvas.draw()
        except TypeError:
            pass

    def on_click(self, event):
        self.point = event.xdata

    def redraw_plot(self):
        self.ax1.cla()
        self.ax2.cla()
        self.ax1.plot(self.x, func.function_char1(self.x), self.x, np.zeros(self.x.shape), "black")
        self.ax2.plot(self.x, func.function_char2(self.x), self.x, np.zeros(self.x.shape), "black")


x = np.arange(-10, 10, 0.1)
Plotter(x)

