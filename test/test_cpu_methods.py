import unittest
from parts_modules import Cpus
from computer_parts_db import CPUS


class TestCpuBrand(unittest.TestCase):
    def test_get_brand(self) -> None:
        test_cpu = Cpu(part_type="CPU", part_data=CPUS[2])
        self.assertEqual(test_cpu.get_brand(), "AMD")

    def test_get_core_count(self) -> None:
        test_cpu = Cpu(part_type="CPU", part_data=CPUS[2])
        self.assertEqual(test_cpu.get_core_count(), 8)
