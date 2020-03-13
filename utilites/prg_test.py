def time_to_seconds(hours, minutes, seconds):
    return (hours * 3600) + (minutes * 60) + seconds


sec_ttl = time_to_seconds(hours = int(input("Введите местное время \n   часы: ")), minutes = int(input(" минуты: ")), seconds = int(input("секунды: ")))

def utc_offset(utc_local, utc_foreign):
    return -utc_local + utc_foreign

utcOffset = utc_offset(utc_local = int(input("   местный часовой пояс: ")), utc_foreign = int(input("     пояс для сравнения: "))) 

def utc_dif(time, offset):
    return (time + (offset * 3600)) 
for_time = utc_dif(sec_ttl, utcOffset)

def to_24_hour_clock(hours):
    return hours % 24

def get_hours(seconds):
    return to_24_hour_clock(seconds // 3600)  
for_hours = get_hours(for_time)

def get_minutes(seconds):
   return (seconds // 60) % 60
for_minutes = get_minutes(for_time)

def get_seconds(seconds):
    return seconds // 1 % 60
for_seconds = get_seconds(for_time)

print("Время в выбранном поясе:",for_hours,"ч",for_minutes,"м",for_seconds,"с")