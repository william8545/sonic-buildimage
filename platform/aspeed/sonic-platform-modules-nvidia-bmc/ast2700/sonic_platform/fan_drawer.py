#!/usr/bin/env python3
# SPDX-FileCopyrightText: NVIDIA CORPORATION & AFFILIATES
# Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""
fan_drawer.py

Implementation of FanDrawer class for NVIDIA AST2700 BMC platform.
Since BMC platforms typically don't have physical fan drawers/trays,
we create virtual fan drawers with one fan each to satisfy SONiC's
thermalctld requirements.
"""

try:
    from sonic_platform_base.fan_drawer_base import FanDrawerBase
except ImportError as e:
    raise ImportError(str(e) + " - required module not found")


class FanDrawer(FanDrawerBase):
    """
    Platform-specific FanDrawer class for NVIDIA AST2700 BMC.

    Each FanDrawer represents a virtual drawer containing a single fan.
    """

    def __init__(self, drawer_index, fan):
        """
        Initialize a FanDrawer with a single fan.

        Args:
            drawer_index: 0-based index of this fan drawer
            fan: Fan object to be contained in this drawer
        """
        FanDrawerBase.__init__(self)
        self._drawer_index = drawer_index
        self._fan_list.append(fan)

    def get_name(self):
        """
        Retrieves the fan drawer name.

        Returns:
            string: The name of the fan drawer (e.g., "FanDrawer1")
        """
        return "FanDrawer{}".format(self._drawer_index + 1)

    def get_presence(self):
        """
        Retrieves the presence of the fan drawer.

        Returns:
            bool: True if fan drawer is present, False otherwise
        """
        return True

    def get_status(self):
        """
        Retrieves the operational status of the fan drawer.

        Returns:
            bool: True if fan drawer is operating properly, False otherwise
        """
        if len(self._fan_list) > 0:
            return self._fan_list[0].get_status()
        return False

    def get_model(self):
        """
        Retrieves the model number of the fan drawer.

        Returns:
            string: Model number of the fan drawer
        """
        return "N/A"

    def get_serial(self):
        """
        Retrieves the serial number of the fan drawer.

        Returns:
            string: Serial number of the fan drawer
        """
        return "N/A"

    def get_status_led(self):
        """
        Gets the state of the fan drawer LED.

        Returns:
            string: One of the STATUS_LED_COLOR_* strings
        """
        return "N/A"

    def set_status_led(self, color):
        """
        Sets the state of the fan drawer LED.

        Args:
            color: A string representing the color

        Returns:
            bool: True if LED state is set successfully, False otherwise
        """
        return False

    def get_maximum_consumed_power(self):
        """
        Retrieves the maximum power drawn by the fan drawer.

        Returns:
            float: Maximum power consumption in watts
        """
        return 5.0

    def is_replaceable(self):
        """
        Indicate whether this fan drawer is replaceable.

        Returns:
            bool: True if replaceable, False otherwise
        """
        return False

    def get_position_in_parent(self):
        """
        Retrieves the 1-based relative physical position in parent device.

        Returns:
            integer: The 1-based relative physical position in parent device
        """
        return self._drawer_index + 1
