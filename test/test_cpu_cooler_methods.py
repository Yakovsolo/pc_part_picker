import unittest
from parts_modules import CpuCooler
from computer_parts_db import CPU_COOLERS


class TestCpuCooler(unittest.TestCase):
    def test_get_brand(self) -> None:
        test_cpu = CpuCooler(part_type="CPU Cooler", part_data=CPU_COOLERS[2])
        self.assertEqual(test_cpu.get_brand(), "Cooler Master")

    def test_get_fan_rpm(self) -> None:
        test_cpu = CpuCooler(part_type="CPU Cooler", part_data=CPU_COOLERS[2])
        self.assertEqual(test_cpu.get_fan_rpm(), "650-1800 RPM")
