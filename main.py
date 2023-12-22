import folium
import csv

def main():
    create_a_router_map()



# Переводим координаты из таблицы в формат кортажа
def convert_point_format(point_str):
    # Удаляем 'POINT (' и ')' из строки и разделяем оставшуюся часть по пробелу
    lon, lat = point_str.replace('POINT (', '').replace(')', '').split()
    # Конвертируем значения в float и возвращаем в правильном порядке
    return float(lat), float(lon)

def create_a_router_map():
    # Создаем карту с центром в определенной точке
    # Центр карты - город Тула
    map_center = (54.193122, 37.617348)
    my_map = folium.Map(location=map_center, zoom_start=10)


    # Список координат, которые мы хотим отметить на карте
    # coordinates = [
    #     (54.204617, 37.618886),  # 1 роутер (0648078a-9d45-4577-af14-12b49e8f017b)
    #     (54.1688958982062, 37.5826629190378),  # 2 роутер (6422a0a5-2c2d-4610-bebc-91722ea37827)
    #     # Другие координаты
    # ]

    coordinates = {

    }


    with open('wifi_routers.csv') as file_obj:
        header = next(file_obj)
        reader_obj = csv.reader(file_obj, delimiter=';')
        for row in reader_obj:
            point_guid = row[0]
            point_cor = row[1]
            print(row[1])
            point_tuple = convert_point_format(point_cor)
            coordinates[point_guid] = point_tuple

    print(coordinates)





    # Добавляем маркеры на карту
    for point_guid in coordinates:
        folium.Marker(
            location=coordinates[point_guid],
            popup=f'<b>{point_guid}</b>',  # HTML с описанием места
        ).add_to(my_map)

    # Сохраняем карту в HTML-файл
    my_map.save("my_interactive_map.html")




main()


