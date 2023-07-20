from abc import ABC, abstractmethod
from typing import Optional

from computer_parts_db import CPUS


class ComputerPartBlueprint(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_brand(self) -> str:
        pass

    @abstractmethod
    def get_price(self) -> float:
        pass

    @abstractmethod
    def get_part_details(self) -> None:
        pass


class ComputerPart(ComputerPartBlueprint):
    def __init__(self, part_type: str, part_data: dict) -> None:
        self.part_type = part_type
        self.part_data = part_data
        self.brand = part_data["brand"]
        self.name = part_data["name"]
        self.price = part_data["price"]

    def get_brand(self) -> str:
        return self.brand

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price

    def get_part_details(self) -> None:
        print(f"{self.part_type}:")
        print(self.part_data)
        for key, value in self.part_data.items():
            print(f"{key}: {value};")


class Cpu(ComputerPart):
    def __init__(self, part_type: str, part_data: dict) -> None:
        super().__init__(part_type=part_type, part_data=part_data)
        self.core_count = part_data["core_count"]
        self.performance_core_clock = part_data["performance_core_clock"]
        self.performance_boost_clock = part_data["performance_boost_clock"]
        self.integrated_graphics = part_data["integrated_graphics"]

    def get_core_count(self) -> int:
        return self.core_count

    def get_performance_core_clock(self) -> float:
        return self.performance_core_clock

    def get_performance_boost_clock(self) -> float:
        return self.performance_boost_clock

    def get_integrated_graphics(self) -> Optional[str]:
        return self.integrated_graphics


class CpuCooler(ComputerPart):
    def __init__(self, part_type: str, part_data: dict) -> None:
        super().__init__(part_type=part_type, part_data=part_data)
        self.fan_rpm = part_data["fan_rpm"]
        self.noise_level = part_data["noise_level"]

    def get_fan_rpm(self) -> str:
        return self.fan_rpm

    def get_noise_level(self) -> str:
        return self.noise_level


class Motherboard(ComputerPart):
    def __init__(self, part_type: str, part_data: dict) -> None:
        super().__init__(part_type=part_type, part_data=part_data)
        self.socket = part_data["socket"]
        self.form_factor = part_data["form_factor"]
        self.ram_slots = part_data["ram_slots"]
        self.max_ram = part_data["max_ram"]

    def get_socket(self) -> str:
        return self.socket

    def get_form_factor(self) -> str:
        return self.form_factor

    def get_ram_slots(self) -> int:
        return self.ram_slots

    def get_max_ram(self) -> int:
        return self.max_ram


class MemoryRAM(ComputerPart):
    def __init__(self, part_type: str, part_data: dict) -> None:
        super().__init__(part_type=part_type, part_data=part_data)
        self.ram_type = part_data["ram_type"]
        self.ram_speed = part_data["ram_speed"]
        self.ram_modules = part_data["ram_modules"]

    def get_ram_type(self) -> str:
        return self.ram_type

    def get_ram_speed(self) -> int:
        return self.ram_speed

    def get_ram_modules(self) -> str:
        return self.ram_modules


class Storage(ComputerPart):
    def __init__(self, part_type: str, part_data: dict) -> None:
        super().__init__(part_type=part_type, part_data=part_data)
        self.storage_type = part_data["storage_type"]
        self.storage_capacity = part_data["storage_capacity"]
        self.storage_cache = part_data["storage_cache"]
        self.storage_form_factor = part_data["storage_form_factor"]
        self.storage_interface = part_data["storage_interface"]

    def get_storage_type(self) -> str:
        return self.storage_type

    def get_storage_capacity(self) -> int:
        return self.storage_capacity

    def get_storage_cache(self) -> int:
        return self.storage_cache

    def get_storage_form_factor(self) -> str:
        return self.storage_form_factor

    def get_storage_interface(self) -> str:
        return self.storage_interface


class VideoCard(ComputerPart):
    def __init__(self, part_type: str, part_data: dict) -> None:
        super().__init__(part_type=part_type, part_data=part_data)
        self.video_chipset = part_data["video_chipset"]
        self.video_memory = part_data["video_memory"]
        self.video_core_clock = part_data["video_core_clock"]
        self.video_boost_clock = part_data["video_boost_clock"]

    def get_video_chipset(self) -> str:
        return self.video_chipset

    def get_video_memory(self) -> int:
        return self.video_memory

    def get_video_core_clock(self) -> int:
        return self.video_core_clock

    def get_video_boost_clock(self) -> int:
        return self.video_boost_clock


class Case(ComputerPart):
    def __init__(self, part_type: str, part_data: dict) -> None:
        super().__init__(part_type=part_type, part_data=part_data)
        self.case_type = part_data["case_type"]
        self.case_color = part_data["case_color"]

    def get_case_type(self) -> str:
        return self.case_type

    def get_case_color(self) -> str:
        return self.case_color


class PowerSuply(ComputerPart):
    def __init__(self, part_type: str, part_data: dict) -> None:
        super().__init__(part_type=part_type, part_data=part_data)
        self.power_suply_type = part_data["power_suply_type"]
        self.wattage = part_data["wattage"]
        self.modular = part_data["modular"]

    def get_power_suply_type(self) -> str:
        return self.power_suply_type

    def get_wattage(self) -> int:
        return self.wattage

    def get_modular(self) -> str:
        return self.modular


class OperatingSystem(ComputerPart):
    def __init__(self, part_type: str, part_data: dict) -> None:
        super().__init__(part_type=part_type, part_data=part_data)
        self.mode = part_data["mode"]
        self.max_supported_memory = part_data["max_supported_memory"]

    def get_mode(self) -> str:
        return self.mode

    def get_max_supported_memory(self) -> int:
        return self.max_supported_memory


class Monitor(ComputerPart):
    def __init__(self, part_type: str, part_data: dict) -> None:
        super().__init__(part_type=part_type, part_data=part_data)
        self.screen_size = part_data["screen_size"]
        self.resolution = part_data["resolution"]
        self.refresh_rate = part_data["refresh_rate"]
        self.response_time = part_data["response_time"]
        self.panel_type = part_data["panel_type"]
        self.aspect_ratio = part_data["aspect_ratio"]

    def get_screen_size(self) -> float:
        return self.screen_size

    def get_resolution(self) -> str:
        return self.resolution

    def get_refresh_rate(self) -> int:
        return self.refresh_rate

    def get_response_time(self) -> float:
        return self.response_time

    def get_panel_type(self) -> str:
        return self.panel_type

    def get_aspect_ratio(self) -> str:
        return self.aspect_ratio


if __name__ == "__main__":
    cpu = CPUS[1]

    new_cpu = Cpu("CPU", cpu)

    # print(repr(new_cpu))

    print(new_cpu.get_brand())
    print(new_cpu.get_name())
    print(new_cpu.get_price())
    new_cpu.get_part_details()
