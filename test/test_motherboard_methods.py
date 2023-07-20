import unittest
from parts_modules import Motherboard
from computer_parts_db import MOTHERBOARDS


class TestMotherboard(unittest.TestCase):
    def test_get_brand(self) -> None:
        test_cpu = Motherboard(part_type="CPU Cooler", part_data=MOTHERBOARDS[2])
        self.assertEqual(test_cpu.get_brand(), "MSI")

    def test_get_ram_slots(self) -> None:
        test_cpu = Motherboard(part_type="CPU Cooler", part_data=MOTHERBOARDS[2])
        self.assertEqual(test_cpu.get_ram_slots(), 4)
