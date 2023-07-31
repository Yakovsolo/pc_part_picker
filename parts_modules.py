from abc import ABC, abstractmethod
import json
from typing import List, Dict, Any, Optional
from logger import console_logger, file_logger


class PCPartsBaseBlueprint(ABC):
    @abstractmethod
    def get_all_parts(self) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    def get_parts_by_brand(self) -> Optional[List[Dict[str, Any]]]:
        pass

    @abstractmethod
    def get_part_by_name(self) -> Optional[Dict[str, Any]]:
        pass

    @abstractmethod
    def get_part_price(self) -> Optional[float]:
        pass


class PCPartsBase(PCPartsBaseBlueprint):
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.parts_base = self.__load_parts()

    def __load_parts(self) -> Dict[str, Any]:
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            console_logger.warning(
                f"PC parts database file '{self.file_path}' not found. Creating an empty parts base."
            )
            file_logger.warning(
                f"PC parts database file '{self.file_path}' not found. Creating an empty parts base."
            )
            return {}
        except json.JSONDecodeError as e:
            console_logger.error(f"Error while parsing JSON in '{self.file_path}'")
            file_logger.error(f"Error while parsing JSON in '{self.file_path}': {e}")
            return {}

    def __save_parts(self) -> None:
        try:
            with open(self.file_path, "w") as file:
                json.dump(self.parts_base, file)
        except Exception as e:
            console_logger.error(f"Error while saving parts base to '{self.file_path}'")
            file_logger.error(
                f"Error while saving parts base to '{self.file_path}': {e}"
            )

    def get_all_parts(self) -> Dict[str, Any]:
        return self.parts_base

    def get_parts_by_brand(self, brand: str) -> Optional[List[Dict[str, Any]]]:
        filtered_parts = [part for part in self.parts_base if part["brand"] == brand]
        if filtered_parts != []:
            return filtered_parts
        else:
            console_logger.info(
                f"There are no brand, named '{brand}' in the parts base."
            )
            return None

    def get_part_by_name(self, part_name: str) -> Optional[Dict[str, Any]]:
        part = [part for part in self.parts_base if part["name"] == part_name]
        if part:
            return part
        else:
            console_logger.info(
                f"There are no part, named '{part_name}' in the parts base."
            )
            return None

    def get_part_price(self, part_name: str) -> Optional[float]:
        part = [part for part in self.parts_base if part["name"] == part_name]
        if part:
            return part["price"]
        else:
            console_logger.info(
                f"There are no part, named '{part_name}' in the parts base."
            )
            return None

    def change_part_price(self, part_name: str, new_price: float) -> Optional[float]:
        part = self.get_part_by_name(part_name)
        if part:
            file_logger.info(
                f"Changing part's {part_name} price from ${part['price']} to ${new_price}"
            )
            part["price"] = new_price
            self.__save_parts()
            console_logger.info(
                f"Part's {part_name} price have been changed to ${new_price}"
            )
            file_logger.info(
                f"Part's {part_name} price have been changed to ${new_price}"
            )
            return part
        else:
            console_logger.info(
                f"Part with name '{part_name}' not found in the parts base."
            )
            return None

    def delete_part(self, part_name: str) -> Optional[Dict[str, Any]]:
        part = self.get_part_by_name(part_name)
        if part:
            self.parts_base.remove(part)
            self.__save_parts()
            console_logger.info(
                f"Part {part_name} have been deleted from parts database"
            )
            file_logger.info(f"Part {part_name} have been deleted from parts database")
            return part
        else:
            console_logger.info(
                f"Part with name '{part_name}' not found in the parts base."
            )
            return None

    def add_part(self, new_part: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        new_name = new_part["name"]
        for part in self.parts_base:
            if part["name"] == new_name:
                console_logger.info(
                    f"Part with name '{new_name}' already exist in the parts base."
                )
                return None
        self.parts_base.append(new_part)
        self.__save_parts()
        console_logger.info(f"Part {new_name} have been added to parts database")
        file_logger.info(f"Part {new_name} have been added to parts database")
        return new_part


class Cpus(PCPartsBase):
    def __init__(self, file_path: str = "parts_db\cpus.json") -> None:
        super().__init__(file_path=file_path)

    def get_core_count(self, part_name: str) -> Optional[int]:
        part = self.get_part_by_name(part_name)
        if part:
            return part["core_count"]
        else:
            console_logger.info(
                f"Part with name '{part_name}' not found in the parts base."
            )
            return None

    def get_performance_core_clock(self, part_name: str) -> Optional[float]:
        part = self.get_part_by_name(part_name)
        if part:
            return part["performance_core_clock"]
        else:
            console_logger.info(
                f"Part with name '{part_name}' not found in the parts base."
            )
            return None

    def get_performance_boost_clock(self, part_name: str) -> Optional[float]:
        part = self.get_part_by_name(part_name)
        if part:
            return part["performance_boost_clock"]
        else:
            console_logger.info(
                f"Part with name '{part_name}' not found in the parts base."
            )
            return None

    def get_integrated_graphics(self, part_name: str) -> Optional[str]:
        part = self.get_part_by_name(part_name)
        if part:
            return part["integrated_graphics"]
        else:
            console_logger.info(
                f"Part with name '{part_name}' not found in the parts base."
            )
            return None


class CpuCoolers(PCPartsBase):
    def __init__(self, file_path: str = "parts_db\cpu_coolers.json") -> None:
        super().__init__(file_path=file_path)

    def get_fan_rpm(self, part_name: str) -> Optional[str]:
        part = self.get_part_by_name(part_name)
        if part:
            return part["fan_rpm"]
        else:
            console_logger.info(
                f"Part with name '{part_name}' not found in the parts base."
            )
            return None

    def get_noise_level(self, part_name: str) -> Optional[str]:
        part = self.get_part_by_name(part_name)
        if part:
            return part["noise_level"]
        else:
            console_logger.info(
                f"Part with name '{part_name}' not found in the parts base."
            )
            return None


class Motherboards(PCPartsBase):
    def __init__(self, file_path: str = "parts_db\motherboards.json") -> None:
        super().__init__(file_path=file_path)

    def get_socket(self, part_name: str) -> Optional[str]:
        part = self.get_part_by_name(part_name)
        if part:
            return part["socket"]
        else:
            console_logger.info(
                f"Part with name '{part_name}' not found in the parts base."
            )
            return None

    def get_form_factor(self, part_name: str) -> Optional[str]:
        part = self.get_part_by_name(part_name)
        if part:
            return part["form_factor"]
        else:
            console_logger.info(
                f"Part with name '{part_name}' not found in the parts base."
            )
            return None

    def get_ram_slots(self, part_name: str) -> Optional[int]:
        part = self.get_part_by_name(part_name)
        if part:
            return part["ram_slots"]
        else:
            console_logger.info(
                f"Part with name '{part_name}' not found in the parts base."
            )
            return None

    def get_max_ram(self, part_name: str) -> Optional[int]:
        part = self.get_part_by_name(part_name)
        if part:
            return part["max_ram"]
        else:
            console_logger.info(
                f"Part with name '{part_name}' not found in the parts base."
            )
            return None


class MemoryRAM(PCPartsBase):
    def __init__(self, file_path: str = "parts_db\memory_ram.json") -> None:
        super().__init__(file_path=file_path)

    def get_ram_type(self, part_name: str) -> Optional[str]:
        part = self.get_part_by_name(part_name)
        if part:
            return part["ram_type"]
        else:
            console_logger.info(
                f"Part with name '{part_name}' not found in the parts base."
            )
            return None

    def get_ram_speed(self, part_name: str) -> Optional[int]:
        part = self.get_part_by_name(part_name)
        if part:
            return part["ram_speed"]
        else:
            console_logger.info(
                f"Part with name '{part_name}' not found in the parts base."
            )
            return None

    def get_ram_modules(self, part_name: str) -> Optional[str]:
        part = self.get_part_by_name(part_name)
        if part:
            return part["ram_modules"]
        else:
            console_logger.info(
                f"Part with name '{part_name}' not found in the parts base."
            )
            return None


class Storages(PCPartsBase):
    def __init__(self, file_path: str = "parts_db\storages.json") -> None:
        super().__init__(file_path=file_path)

    def get_storage_type(self, part_name: str) -> Optional[str]:
        part = self.get_part_by_name(part_name)
        if part:
            return part["storage_type"]
        else:
            console_logger.info(
                f"Part with name '{part_name}' not found in the parts base."
            )
            return None

    def get_storage_capacity(self, part_name: str) -> Optional[int]:
        part = self.get_part_by_name(part_name)
        if part:
            return part["storage_capacity"]
        else:
            console_logger.info(
                f"Part with name '{part_name}' not found in the parts base."
            )
            return None

    def get_storage_cache(self, part_name: str) -> Optional[int]:
        part = self.get_part_by_name(part_name)
        if part:
            return part["storage_cache"]
        else:
            console_logger.info(
                f"Part with name '{part_name}' not found in the parts base."
            )
            return None

    def get_storage_form_factor(self, part_name: str) -> Optional[str]:
        part = self.get_part_by_name(part_name)
        if part:
            return part["storage_form_factor"]
        else:
            console_logger.info(
                f"Part with name '{part_name}' not found in the parts base."
            )
            return None

    def get_storage_interface(self, part_name: str) -> Optional[str]:
        part = self.get_part_by_name(part_name)
        if part:
            return part["storage_interface"]
        else:
            console_logger.info(
                f"Part with name '{part_name}' not found in the parts base."
            )
            return None


class VideoCards(PCPartsBase):
    def __init__(self, file_path: str = "parts_db\video_cards.json") -> None:
        super().__init__(file_path=file_path)

    def get_video_chipset(self, part_name: str) -> Optional[str]:
        part = self.get_part_by_name(part_name)
        if part:
            return part["video_chipset"]
        else:
            console_logger.info(
                f"Part with name '{part_name}' not found in the parts base."
            )
            return None

    def get_video_memory(self, part_name: str) -> Optional[int]:
        part = self.get_part_by_name(part_name)
        if part:
            return part["video_memory"]
        else:
            console_logger.info(
                f"Part with name '{part_name}' not found in the parts base."
            )
            return None

    def get_video_core_clock(self, part_name: str) -> Optional[int]:
        part = self.get_part_by_name(part_name)
        if part:
            return part["video_core_clock"]
        else:
            console_logger.info(
                f"Part with name '{part_name}' not found in the parts base."
            )
            return None

    def get_video_boost_clock(self, part_name: str) -> Optional[int]:
        part = self.get_part_by_name(part_name)
        if part:
            return part["video_boost_clock"]
        else:
            console_logger.info(
                f"Part with name '{part_name}' not found in the parts base."
            )
            return None


class Cases(PCPartsBase):
    def __init__(self, file_path: str = "parts_db\cases.json") -> None:
        super().__init__(file_path=file_path)

    def get_case_type(self, part_name: str) -> Optional[str]:
        part = self.get_part_by_name(part_name)
        if part:
            return part["case_type"]
        else:
            console_logger.info(
                f"Part with name '{part_name}' not found in the parts base."
            )
            return None

    def get_case_color(self, part_name: str) -> Optional[str]:
        part = self.get_part_by_name(part_name)
        if part:
            return part["case_color"]
        else:
            console_logger.info(
                f"Part with name '{part_name}' not found in the parts base."
            )
            return None


class PowerSuplyes(PCPartsBase):
    def __init__(self, file_path: str = "parts_db\power_suplyes.json") -> None:
        super().__init__(file_path=file_path)

    def get_power_suply_type(self, part_name: str) -> Optional[str]:
        part = self.get_part_by_name(part_name)
        if part:
            return part["power_suply_type"]
        else:
            console_logger.info(
                f"Part with name '{part_name}' not found in the parts base."
            )
            return None

    def get_wattage(self, part_name: str) -> Optional[int]:
        part = self.get_part_by_name(part_name)
        if part:
            return part["wattage"]
        else:
            console_logger.info(
                f"Part with name '{part_name}' not found in the parts base."
            )
            return None

    def get_modular(self, part_name: str) -> Optional[str]:
        part = self.get_part_by_name(part_name)
        if part:
            return part["modular"]
        else:
            console_logger.info(
                f"Part with name '{part_name}' not found in the parts base."
            )
            return None


class OperatingSystems(PCPartsBase):
    def __init__(self, file_path: str = "parts_db\operating_systems.json") -> None:
        super().__init__(file_path=file_path)

    def get_mode(self, part_name: str) -> Optional[str]:
        part = self.get_part_by_name(part_name)
        if part:
            return part["mode"]
        else:
            console_logger.info(
                f"Part with name '{part_name}' not found in the parts base."
            )
            return None

    def get_max_supported_memory(self, part_name: str) -> Optional[int]:
        part = self.get_part_by_name(part_name)
        if part:
            return part["max_supported_memory"]
        else:
            console_logger.info(
                f"Part with name '{part_name}' not found in the parts base."
            )
            return None


class Monitors(PCPartsBase):
    def __init__(self, file_path: str = "parts_db\monitors.json") -> None:
        super().__init__(file_path=file_path)

    def get_screen_size(self, part_name: str) -> Optional[float]:
        part = self.get_part_by_name(part_name)
        if part:
            return part["screen_size"]
        else:
            console_logger.info(
                f"Part with name '{part_name}' not found in the parts base."
            )
            return None

    def get_resolution(self, part_name: str) -> Optional[str]:
        part = self.get_part_by_name(part_name)
        if part:
            return part["resolution"]
        else:
            console_logger.info(
                f"Part with name '{part_name}' not found in the parts base."
            )
            return None

    def get_refresh_rate(self, part_name: str) -> Optional[int]:
        part = self.get_part_by_name(part_name)
        if part:
            return part["refresh_rate"]
        else:
            console_logger.info(
                f"Part with name '{part_name}' not found in the parts base."
            )
            return None

    def get_response_time(self, part_name: str) -> Optional[float]:
        part = self.get_part_by_name(part_name)
        if part:
            return part["response_time"]
        else:
            console_logger.info(
                f"Part with name '{part_name}' not found in the parts base."
            )
            return None

    def get_panel_type(self, part_name: str) -> Optional[str]:
        part = self.get_part_by_name(part_name)
        if part:
            return part["panel_type"]
        else:
            console_logger.info(
                f"Part with name '{part_name}' not found in the parts base."
            )
            return None

    def get_aspect_ratio(self, part_name: str) -> Optional[str]:
        part = self.get_part_by_name(part_name)
        if part:
            return part["aspect_ratio"]
        else:
            console_logger.info(
                f"Part with name '{part_name}' not found in the parts base."
            )
            return None
