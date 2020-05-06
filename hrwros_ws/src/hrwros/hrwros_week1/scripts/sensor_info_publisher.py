#!/usr/bin/env python

# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Node to publish sensor information topic.

import rospy
from hrwros_msgs.msg import SensorInformation
from hrwros_utilities.sim_sensor_data import distSensorData as getSensorData

def sensorInfoPublisher():
    si_publisher = rospy.Publisher('sensor_info', SensorInformation, queue_size = 10)
    rospy.init_node('sensor_info_publisher', anonymous=False)
    rate = rospy.Rate(1)

    # Create a new SensorInformation objeect and fill in its contents
    sensor_info = SensorInformation()
    # Fill in the header information
    sensor_info.sensor_data.header.stamp = rospy.Time.now()
    sensor_info.sensor_data.header.frame_id = 'distance_sensor_frame'
    # Fill in the sensor data information
    sensor_info.sensor_data.radiation_type = sensor_info.sensor_data.ULTRASOUND
    

    # Fill in the manufacturer and part information
    sensor_info.maker_name = 'The Ultrasound Company'
    sensor_info.part_number = 123456

    while not rospy.is_shutdown():
	# read the sensor data from a simulated sensor
	sensor_info.sensor_data.range = 1
        si_publisher.publish(sensor_info)
	# Print log message to indicate it is happening
	rospy.loginfo ('All went well. Publishing topic')
        rate.sleep()

if __name__ == '__main__':
    try:
        sensorInfoPublisher()
    except rospy.ROSInterruptException:
        pass
