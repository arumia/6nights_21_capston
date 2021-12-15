from .celery import app
import math
import json
from datetime import datetime, time, date
import requests
from pytz import timezone

def grid(lat, lng) :

    RE = 6371.00877 # 지구 반경(km)
    GRID = 5.0      # 격자 간격(km)
    SLAT1 = 30.0    # 투영 위도1(degree)
    SLAT2 = 60.0    # 투영 위도2(degree)
    OLON = 126.0    # 기준점 경도(degree)
    OLAT = 38.0     # 기준점 위도(degree)
    XO = 43         # 기준점 X좌표(GRID)
    YO = 136        # 기1준점 Y좌표(GRID)

    DEGRAD = math.pi / 180.0
    RADDEG = 180.0 / math.pi

    re = RE / GRID;
    slat1 = SLAT1 * DEGRAD
    slat2 = SLAT2 * DEGRAD
    olon = OLON * DEGRAD
    olat = OLAT * DEGRAD

    sn = math.tan(math.pi * 0.25 + slat2 * 0.5) / math.tan(math.pi * 0.25 + slat1 * 0.5)
    sn = math.log(math.cos(slat1) / math.cos(slat2)) / math.log(sn)
    sf = math.tan(math.pi * 0.25 + slat1 * 0.5)
    sf = math.pow(sf, sn) * math.cos(slat1) / sn
    ro = math.tan(math.pi * 0.25 + olat * 0.5)
    ro = re * sf / math.pow(ro, sn);
    rs = {};

    ra = math.tan(math.pi * 0.25 + (lat) * DEGRAD * 0.5)
    ra = re * sf / math.pow(ra, sn)

    theta = lng * DEGRAD - olon
    if theta > math.pi :
        theta -= 2.0 * math.pi
    if theta < -math.pi :
        theta += 2.0 * math.pi
    theta *= sn
    rs['x'] = math.floor(ra * math.sin(theta) + XO + 0.5)
    rs['y'] = math.floor(ro - ra * math.cos(theta) + YO + 0.5)

    return str(rs["x"]).split('.')[0], str(rs["y"]).split('.')[0]

def get_sky_info(data):
    try:
        URL = "http://127.0.0.1:8000/api/weather/"
        print(requests.post(URL+"delete_all/", data=""))
        weather_info = data['response']['body']['items']['item']
        basedate = weather_info[0]['baseDate']
        d = date.fromisoformat(basedate[:4] + '-' + basedate[4:6] + '-' + basedate[6:])
        baseTime = weather_info[0]['baseTime']
        t = time.fromisoformat(baseTime[:2] + ":" + baseTime[2:])
        base_time = datetime.combine(d, t)

        fcstdate = weather_info[0]['fcstDate']
        d = date.fromisoformat(fcstdate[:4] + '-' + fcstdate[4:6] + '-' + fcstdate[6:])
        fcstTime = weather_info[0]['fcstTime']
        t = time.fromisoformat(fcstTime[:2] + ":" + fcstTime[2:])
        fcst_time = datetime.combine(d, t)
        tmp = ''
        pop = ''
        for i in range(0,240):
            if fcstdate == weather_info[i]['fcstDate'] and fcstTime == weather_info[i]['fcstTime']:
                if weather_info[i]['category'] == 'TMP':
                    tmp = weather_info[i]['fcstValue']
                elif weather_info[i]['category'] == 'POP':
                    pop = weather_info[i]['fcstValue']
            else:
                json_object = {'basetime': base_time.strftime('%Y-%m-%dT%H:%M'),
                               'fcstTime': fcst_time.strftime('%Y-%m-%dT%H:%M'), 'temp': tmp, 'rain': int(pop)}
                send_data = json.dumps(json_object)
                print(send_data)
                print(requests.post(URL, data=json_object))

                fcstdate = weather_info[i]['fcstDate']
                d = date.fromisoformat(fcstdate[:4] + '-' + fcstdate[4:6] + '-' + fcstdate[6:])
                fcstTime = weather_info[i]['fcstTime']
                t = time.fromisoformat(fcstTime[:2] + ":" + fcstTime[2:])
                fcst_time = datetime.combine(d, t)
                if weather_info[i]['category'] == 'TMP':
                    tmp = weather_info[i]['fcstValue']
                    print(tmp)
                elif weather_info[i]['category'] == 'POP':
                    pop = weather_info[i]['fcstValue']
                    print(pop)
    except KeyError:
        print('API 호출 실패!')

    return "success!"

def get_base_time(hour):
    hour = int(hour)
    if hour < 3:
        temp_hour = '23'
    elif hour < 6:
        temp_hour = '02'
    elif hour < 9:
        temp_hour = '05'
    elif hour < 12:
        temp_hour = '08'
    elif hour < 15:
        temp_hour = '11'
    elif hour < 18:
        temp_hour = '14'
    elif hour < 21:
        temp_hour = '17'
    elif hour < 24:
        temp_hour = '20'

    return temp_hour + '00'

@app.task
def get_weather():
    service_key = 'pz9gPzY4v9gCNURAJcS9K%2BvxjzuNyizZ%2FE9%2B14mYgV3IauXIHkY71eIcK7d1zlwx3fP%2FG7uuxyU8FhS%2BX2vDTA%3D%3D'
    now = datetime.now(timezone('Asia/Seoul'))
    now_date = now.strftime('%Y%m%d')
    now_hour = int(now.strftime('%H'))

    if now_hour < 2:
        base_date = str(int(now_date) - 1)
    else:
        base_date = now_date
    base_hour = get_base_time(now_hour)

    num_of_rows = '240'
    base_date = base_date
    base_time = base_hour
    nx, ny = grid(35.893684953438736, 128.61327796269993)
    dataType = 'json'
    api_url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?serviceKey={}' \
              '&numOfRows={}&dataType={}&base_date={}&base_time={}&nx={}&ny={}'.format(
        service_key, num_of_rows, dataType, base_date, base_time, nx, ny)
    print(api_url)

    data = requests.get(api_url)
    json_data = data.json()
    sky = get_sky_info(json_data)
    return sky

@app.task
def rfid_read():
  rdr = RFID()

  error = True
  while error:
    rdr.wait_for_tag()
    (error, tag_type) = rdr.request()
    if not error:
      print("Tag detected")
      (error, uid) = rdr.anticoll()
      if not error:
        print("UID: " + str(uid))
        # Select Tag is required before Auth
        if not rdr.select_tag(uid):
          # Auth for block 10 (block 2 of sector 2) using default shipping key A
          if not rdr.card_auth(rdr.auth_a, 10, [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF], uid):
            # This will print something like (False, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
            print("Reading block 10: " + str(rdr.read(10)))
            # Always stop crypto1 when done working
            rdr.stop_crypto()

  # Calls GPIO cleanup
  rdr.cleanup()
  return str(uid)
