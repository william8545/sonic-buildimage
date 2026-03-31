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
# chassis.py
#
# Chassis implementation for NVIDIA AST2700 BMC
#

try:
    from sonic_platform_base.chassis_base import ChassisBase
    from sonic_platform.thermal import Thermal
    from sonic_platform.watchdog import Watchdog
    from sonic_py_common.device_info import get_platform_json_data
except ImportError as e:
    raise ImportError(str(e) + " - required module not found")


class Chassis(ChassisBase):
    """
    Platform-specific Chassis class for NVIDIA AST2700 BMC

    Hardware Configuration:
    - TODO: Update fan/thermal counts for NVIDIA hardware
    - Currently uses empty inventories (skeleton)
    """

    NUM_FANS = 0
    NUM_THERMAL_SENSORS = 0

    def __init__(self):
        """
        Initialize NVIDIA chassis with hardware-specific configuration
        """
        super().__init__()

        self._platform_data = get_platform_json_data() or {}

        # Empty fan and thermal lists for skeleton
        self._fan_list = []
        self._fan_drawer_list = []
        self._thermal_list = []

    def get_reboot_cause(self):
        """
        Retrieves the cause of the previous reboot

        Returns:
            A tuple (string, string) where the first element is a reboot cause
            string from ChassisBase and the second is an optional description.
        """
        # TODO: Implement hardware-specific reboot cause detection
        return (self.REBOOT_CAUSE_NON_HARDWARE, None)

    def get_name(self):
        """
        Retrieves the name of the chassis

        Returns:
            String containing the name of the chassis
        """
        return self._platform_data.get('chassis', {}).get('name', 'N/A')

    def get_model(self):
        """
        Retrieves the model number (or part number) of the chassis

        Returns:
            String containing the model number of the chassis
        """
        return self._platform_data.get('chassis', {}).get('model', 'N/A')

    def get_serial(self):
        """
        Retrieves the serial number of the chassis

        Returns:
            String containing the serial number of the chassis
        """
        return "N/A"

    def get_num_thermals(self):
        """
        Retrieves the number of thermal sensors available on this chassis

        Returns:
            An integer, the number of thermal sensors available on this chassis
        """
        return len(self._thermal_list)

    def get_all_thermals(self):
        """
        Retrieves all thermal sensors available on this chassis

        Returns:
            A list of objects derived from ThermalBase representing all thermal
            sensors available on this chassis
        """
        return self._thermal_list

    def get_thermal(self, index):
        """
        Retrieves thermal sensor represented by (0-based) index

        Args:
            index: An integer, the index (0-based) of the thermal sensor to retrieve

        Returns:
            An object derived from ThermalBase representing the specified thermal
            sensor, or None if index is out of range
        """
        if index < 0 or index >= len(self._thermal_list):
            return None
        return self._thermal_list[index]

    def get_num_fans(self):
        """
        Retrieves the number of fans available on this chassis

        Returns:
            An integer, the number of fans available on this chassis
        """
        return len(self._fan_list)

    def get_all_fans(self):
        """
        Retrieves all fan modules available on this chassis

        Returns:
            A list of objects derived from FanBase representing all fan
            modules available on this chassis
        """
        return self._fan_list

    def get_fan(self, index):
        """
        Retrieves fan module represented by (0-based) index

        Args:
            index: An integer, the index (0-based) of the fan module to retrieve

        Returns:
            An object derived from FanBase representing the specified fan
            module, or None if index is out of range
        """
        if index < 0 or index >= len(self._fan_list):
            return None
        return self._fan_list[index]

    def _detect_card_revision(self):
        """
        Detect the BMC card revision from hardware

        Returns:
            str: Card revision identifier (e.g., 'r0', 'r1')
        """
        # TODO: Implement revision detection from EEPROM or device tree
        return 'r0'
