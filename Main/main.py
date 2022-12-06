from Position import Axis, homing, placing, axis_1, axis_2
from Micro import microswitch

axis1_pos1 = Axis(axis_1, 50)
axis2_pos1 = Axis(axis_2, 50)
axes_pos1 = [axis1_pos1, axis2_pos1]

homing()
placing(axes_pos1)

microswitch()
#fire_signal('test', 'Transmission')


