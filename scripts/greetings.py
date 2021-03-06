#! /usr/bin/env python
#
# This file is part of the Robot Learning Lab stack
#
# Copyright (C) 2018 Wolfgang Wiedmeyer <wolfgang.wiedmeyer@kit.edu>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import rospy
from rll_move_client.client import RLLDefaultMoveClient


def greetings(move_client):
    joint_1 = 0.6
    joint_2 = 1.6
    joint_3 = -0.3
    joint_4 = 2.01
    joint_5 = -2.0
    joint_6 = 0.0
    joint_7 = 1.4835

    success = move_client.move_joints(joint_1, joint_2, joint_3, joint_4,
                                      joint_5, joint_6, joint_7)

    if not success:
        rospy.logerr("moving to first joint pos failed")
        return False

    joint_3 = 0.3
    joint_5 = -0.7
    success = move_client.move_joints(joint_1, joint_2, joint_3, joint_4,
                                      joint_5, joint_6, joint_7)

    if not success:
        rospy.logerr("moving to second joint pos failed")
        return False

    return True


def execute(move_client):
    num_greetings = 5

    for num in range(0, num_greetings):
        rospy.loginfo("greetings back and forth rotation %d/%d",
                      num + 1, num_greetings)
        success = greetings(move_client)
        if not success:
            return False

    return True


def main():
    rospy.init_node('greetings')
    client = RLLDefaultMoveClient(execute)
    client.spin()


if __name__ == '__main__':
    main()
