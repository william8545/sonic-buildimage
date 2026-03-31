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
SONiC Platform API - Thermal class for NVIDIA AST2700 BMC

This module provides the Thermal class for NVIDIA AST2700 BMC platform.
Thermal sensors are exposed via the IIO-HWMON bridge from ADC channels.
"""

import os

try:
    from sonic_platform_base.thermal_base import ThermalBase
except ImportError as e:
    raise ImportError(str(e) + " - required module not found")


class Thermal(ThermalBase):
    """
    Thermal sensor class for NVIDIA AST2700 BMC platform

    Reads temperature/voltage values from ADC channels exposed via iio-hwmon.
    """

    # TODO: Update HWMON path for NVIDIA hardware
    HWMON_IIO_PATH = "/sys/class/hwmon/hwmon10"

    def __init__(self, thermal_index):
        """
        Initialize a Thermal object

        Args:
            thermal_index: 0-based index of the thermal sensor (0-15 for 16 ADC channels)
        """
        ThermalBase.__init__(self)

        self.index = thermal_index
        self.name = f"ADC{thermal_index + 1}"

        # ADC channel input file (1-based in sysfs)
        self.thermal_input_path = os.path.join(
            self.HWMON_IIO_PATH,
            f"in{thermal_index + 1}_input"
        )

    def _read_sysfs_file(self, path):
        """
        Read a value from a sysfs file

        Args:
            path: Path to the sysfs file

        Returns:
            String value from the file, or None if read fails
        """
        try:
            with open(path, 'r') as f:
                return f.read().strip()
        except (IOError, OSError):
            return None

    def get_name(self):
        """
        Retrieves the name of the thermal sensor

        Returns:
            String containing the name of the thermal sensor
        """
        return self.name

    def get_presence(self):
        """
        Retrieves the presence of the thermal sensor

        Returns:
            True if thermal sensor is present, False if not
        """
        return os.path.exists(self.thermal_input_path)

    def get_model(self):
        """
        Retrieves the model of the thermal sensor

        Returns:
            String containing the model of the thermal sensor
        """
        return "AST2700-ADC"

    def get_serial(self):
        """
        Retrieves the serial number of the thermal sensor

        Returns:
            String containing the serial number of the thermal sensor
        """
        return "N/A"

    def get_status(self):
        """
        Retrieves the operational status of the thermal sensor

        Returns:
            True if thermal sensor is operating properly, False if not
        """
        return self.get_presence() and self.get_temperature() is not None

    def get_temperature(self):
        """
        Retrieves current temperature reading from thermal sensor

        Returns:
            A float number of current temperature in Celsius up to nearest
            thousandth of one degree Celsius, e.g. 30.125, or None if unavailable
        """
        # TODO: Implement proper temperature conversion for NVIDIA hardware
        value_str = self._read_sysfs_file(self.thermal_input_path)
        if value_str is None:
            return None

        try:
            millivolts = float(value_str)
            return millivolts / 10.0
        except ValueError:
            return None

    def get_high_threshold(self):
        """
        Retrieves the high threshold temperature of thermal sensor

        Returns:
            A float number, the high threshold temperature in Celsius
        """
        return 85.0

    def get_low_threshold(self):
        """
        Retrieves the low threshold temperature of thermal sensor

        Returns:
            A float number, the low threshold temperature in Celsius
        """
        return 0.0

    def get_high_critical_threshold(self):
        """
        Retrieves the high critical threshold temperature of thermal sensor

        Returns:
            A float number, the high critical threshold temperature in Celsius
        """
        return 100.0

    def get_low_critical_threshold(self):
        """
        Retrieves the low critical threshold temperature of thermal sensor

        Returns:
            A float number, the low critical threshold temperature in Celsius
        """
        return -10.0

    def set_high_threshold(self, temperature):
        """
        Sets the high threshold temperature of thermal sensor

        Args:
            temperature: A float number, the high threshold temperature in Celsius

        Returns:
            A boolean, True if threshold is set successfully, False if not
        """
        return False

    def set_low_threshold(self, temperature):
        """
        Sets the low threshold temperature of thermal sensor

        Args:
            temperature: A float number, the low threshold temperature in Celsius

        Returns:
            A boolean, True if threshold is set successfully, False if not
        """
        return False
