"""
Лабораторна робота: Варіант 6
Студент: Поліщук Віктор
Група: EIP30 Група 2
"""

# Задача 1: Вибір джерела навігації (if/elif/else)
def select_nav_source(gps_avail: bool, gps_acc: float, ins_calib: bool) -> str:
    if gps_avail and gps_acc < 5.0:
        return "GPS"
    elif ins_calib: 
        return "INS"
    else: 
        return "Star Tracker"

# Задача 2: Аналіз температурних зон супутника (match-case)
def check_temp_zone(zone_data: list) -> str:
    """
    Приймає [zone_name, [t1, t2, t3]].
    - zone_name == "ENGINE" та середнє(t1,t2,t3) > 100 -> "Перегрів двигуна"
    - будь-яка інша зона -> "Зона {zone_name} в нормі"
    """
    ...

# Задача 3: Пошук подолання швидкості звуку (for / break)
def find_supersonic_second(speeds: list) -> int | None:
    """
    За допомогою циклу for знаходить першу секунду (індекс), коли швидкість > 340 м/с,
    і перериває цикл за допомогою break.
    """
    ...

# Задача 4: Зменшення частоти дискретизації (range)
def downsample_telemetry(data: list) -> list:
    """
    За допомогою range з кроком 3 відбирає кожен 3-й елемент списку data.
    """
    ...
