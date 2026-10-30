"""
Лабораторна робота: Варіант 6
Студент: Поліщук Віктор
Група: EIP30 Група 2
"""

# Задача 1: Вибір джерела навігації (if/elif/else)
def select_nav_source(gps_avail: bool, gps_acc: float, ins_calib: bool) -> str:
    if gps_avail:
        if gps_acc < 5.0:
            return "GPS"
        elif ins_calib: 
            return "INS"
        else: 
            return "Star Tracker"
    elif ins_calib: 
        return "INS"
    else: 
        return "Star Tracker"

# Задача 2: Аналіз температурних зон супутника (match-case)
def check_temp_zone(zone_data: list) -> str:
    match zone_data:
        case [zone_name, [temp1, temp2, temp3]] if zone_name == "ENGINE" and (temp1 + temp2 + temp3)/3 > 100:
            return "Перегрів двигуна"
        case [zone_name, *_]:
            return f"Зона {zone_name} в нормі"
        case _:
            return 'INVALID INPUT'

# Задача 3: Пошук подолання швидкості звуку (for / break)
def find_supersonic_second(speeds: list) -> int | None:
    index = None
    for (index, speed) in enumerate(speeds):
        if speed > 340:
            break
    else: 
        index = None
    return index

# Задача 4: Зменшення частоти дискретизації (range)
def downsample_telemetry(data: list) -> list:
    downsampled_data = []
    for i in range(0, len(data), 3):
        downsampled_data.append(data[i])
    return downsampled_data

# Тести для задачі 1
print(f"Input: gps_avail = True, gps_acc = 4, ins_calib = False ==> select_nav_source = {select_nav_source(True, 4, False)}")
print(f"Input: gps_avail = False, gps_acc = 4.5, ins_calib = False ==> select_nav_source = {select_nav_source(False, 4, False)}")
print(f"Input: gps_avail = True, gps_acc = 7, ins_calib = True ==> select_nav_source = {select_nav_source(True, 7, True)}")
print(f"Input: gps_avail = True, gps_acc = 7.34, ins_calib = False ==> select_nav_source = {select_nav_source(True, 7, False)}")
print()

# Тести для задачі 2
print(f"Input: ['ENGINE', [140, 80, 200.5]] ==> check_temp_zone = {check_temp_zone(['ENGINE', [140, 80, 200.5]])}")
print(f"Input: ['Light', [140, 80, 200.5]] ==> check_temp_zone = {check_temp_zone(['Light', [140, 80, 200.5]])}")
print(f"Input: ['ENGINE', [140, ]] ==> check_temp_zone = {check_temp_zone(["ENGINE", [140, 200]])}")
print(f"Input: [] ==> check_temp_zone = {check_temp_zone([])}")
print()

# Тести для задачі 3
print(f"Input: [12, 120, 200, 341, 400, 645] ==> find_supersonic_second = {find_supersonic_second([12, 120, 200, 341, 400])}")
print(f"Input: [12, 120, 200, 231, 300, 320] ==> find_supersonic_second = {find_supersonic_second([12, 120, 200, 231, 300, 320])}")
print(f"Input: [] ==> find_supersonic_second = {find_supersonic_second([])}")
print()

# Тести для задачі 4
print(f"Input: [1, 2, 3, 4, 5, 6, 7, 8] ==> downsample_telemetry = {downsample_telemetry([1, 2, 3, 4, 5, 6, 7, 8])}")
print(f"Input: [{list(range(16))}] ==> downsample_telemetry = {downsample_telemetry(list(range(16)))}")
print(f"Input: [] ==> downsample_telemetry = {downsample_telemetry([])}")
print()