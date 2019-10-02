import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from IPython import display



def custom_3dplot( f, f_plot_param ):

	x1_min = f_plot_param["x1_min"]
	x1_max = f_plot_param["x1_max"]
	x2_min = f_plot_param["x2_min"]
	x2_max = f_plot_param["x2_max"]
	nb_points = f_plot_param["nb_points"]
	v_min = f_plot_param["v_min"]
	v_max = f_plot_param["v_max"]
	levels = f_plot_param["levels"]
	title = f_plot_param["title"]

	def f_no_vector(x1,x2):
		return f( np.array( [x1,x2] ) )

	x , y = np.meshgrid(np.linspace(x1_min,x1_max,nb_points),np.linspace(x2_min,x2_max,nb_points))
	z = f_no_vector(x,y)

	fig = plt.figure()
	ax = fig.gca(projection='3d')
	ax.plot_surface(x, y, z,   cmap=cm.hot , vmin = v_min, vmax =  v_max)
	ax.set_zlim(v_min, v_max)
	plt.show()


def level_plot( f, f_plot_param ):


	x1_min = f_plot_param["x1_min"]
	x1_max = f_plot_param["x1_max"]
	x2_min = f_plot_param["x2_min"]
	x2_max = f_plot_param["x2_max"]
	nb_points = f_plot_param["nb_points"]
	v_min = f_plot_param["v_min"]
	v_max = f_plot_param["v_max"]
	levels = f_plot_param["levels"]
	title = f_plot_param["title"]


	def f_no_vector(x1,x2):
		return f( np.array( [x1,x2] ) )

	x , y = np.meshgrid(np.linspace(x1_min,x1_max,nb_points),np.linspace(x2_min,x2_max,nb_points))
	z = f_no_vector(x,y)
	
	fig = plt.figure()
	graphe = plt.contour(x,y,z,levels)
	#plt.plot(3,1,'r*',markersize=15)
	#plt.clabel(graphe,  inline=1, fontsize=10,fmt='%3.2f')
	plt.title(title)
	plt.show()


def level_points_plot(f, x_tab, f_plot_param, show_path: bool = False):

	x1_min = f_plot_param["x1_min"]
	x1_max = f_plot_param["x1_max"]
	x2_min = f_plot_param["x2_min"]
	x2_max = f_plot_param["x2_max"]
	nb_points = f_plot_param["nb_points"]
	v_min = f_plot_param["v_min"]
	v_max = f_plot_param["v_max"]
	levels = f_plot_param["levels"]
	title = f_plot_param["title"]

	x, y = np.meshgrid(np.linspace(x1_min, x1_max, nb_points),
                       np.linspace(x2_min, x2_max, nb_points))

	z = f([x, y])

	for k in range(x_tab.shape[0]):
		plt.contour(x, y, z, levels)
		plt.plot(*x_tab[k], '*b', markersize=5)
		if show_path and k != 0:
			for i in range(k):
				plt.arrow(*x_tab[i],
                          *np.subtract(x_tab[i + 1], x_tab[i]),
                          width=0.0001)
		display.clear_output(wait=True)
		plt.pause(0.5)

	plt.show()


def level_2points_plot( f , x_tab , x_tab2 ,  f_plot_param ):

	x1_min = f_plot_param["x1_min"]
	x1_max = f_plot_param["x1_max"]
	x2_min = f_plot_param["x2_min"]
	x2_max = f_plot_param["x2_max"]
	nb_points = f_plot_param["nb_points"]
	v_min = f_plot_param["v_min"]
	v_max = f_plot_param["v_max"]
	levels = f_plot_param["levels"]
	title = f_plot_param["title"]

	def f_no_vector(x1,x2):
		return f( np.array( [x1,x2] ) )

	x , y = np.meshgrid(np.linspace(x1_min,x1_max,nb_points),np.linspace(x2_min,x2_max,nb_points))
	z = f_no_vector(x,y)

	fig = plt.figure()
	graphe = plt.contour(x,y,z,levels)
	#plt.plot(3,1,'r*',markersize=15)
	#plt.clabel(graphe,  inline=1, fontsize=10,fmt='%3.2f')
	plt.title(title)

	delay = 4.0/x_tab.shape[0]
	for k in range(x_tab.shape[0]):
		plt.plot(x_tab[k,0],x_tab[k,1],'*b',markersize=10)
		#plt.annotate(k,(x_tab[k,0],x_tab[k,1]))
		plt.draw()
		plt.pause(delay)

	delay = 4.0/x_tab2.shape[0]
	for k in range(x_tab2.shape[0]):
		plt.plot(x_tab2[k,0],x_tab2[k,1],'dg',markersize=8)
		#plt.annotate(k,(x_tab2[k,0],x_tab2[k,1]))
		plt.pause(delay)
		plt.draw()
	plt.show()
		


































