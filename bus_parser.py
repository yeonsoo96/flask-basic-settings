import requests
from bs4 import BeautifulSoup


class Bus_list(object):
    def __init__(self):  # 버스 객체를 담을 리스트 생성
        self.bus_list = []

    def insert_bus(self, bus):  # 버스를 리스트로 저장함
        self.bus_list.append(bus)

    class Bus(object):  # 리스트에 저장할 버스 객체
        def __init__(self):  # 초기 버스 상태
            self.time = None  # 버스 출발 시간
            self.company = None  # 버스 회사명
            self.type = None  # 버스 프라이드(우등같은거)
            self.seats = None  # 잔여좌석

        def search_bus(self):  # 출발지와 도착지를 선택해 크롤링을 해온다.
            try:
                with requests.Session() as s:

                    URL = 'https://www.kobus.co.kr/mrs/alcnSrch.do'

                    data = {'deprCd': '032',  # 출발치 코드
                            'arvlCd': '300',  # 도착지 코드
                            'pathDvs': 'sngl',
                            'pathStep': '1',
                            'pathStepRtn': '1',
                            'deprDtm': '20191231',  # 서치 날짜
                            'busClsCd': '0',
                            }

                    response = s.post(URL, data)  # 크롤링해온 통짜 데이터
                    bus_info = self.parser(response.text)  # 통짜 데이터를 파싱하기위해 넘긴다

                    return bus_info  # 파싱이 완료된 최종 데이터를 리턴한다
            except:
                raise('fail')

        def parser(self, response):  # 크롤링한 통짜 데이터를 받아와서 필요한 정보만 파싱
            parser = BeautifulSoup(response, 'html.parser')  # 뷰티풀숲을 이용해 파싱
            bus_info = parser.findAll('span', {'class': {'start_time',
                                                         'bus_com',
                                                         'grade_mo',
                                                         'remain'}})  # 버스정보만 가져온다
            return bus_info  # 파싱한 데이터를 넘겨준다


if __name__ == '__main__':
    arr = Bus_list()  # 버스 객체를 담을 객체 생성
    obj = arr.Bus()  # 버스 정보를 담을 객체 생성
    bus_info = obj.search_bus()  # 파싱을 마친 데이터

    for index, value in enumerate(bus_info):  # 데이터를 객체에 담아주는 반복문
        if index < 3:  # 필요없는 데이터는 건너뜀
            continue

        if index % 4 == 3:
            obj = arr.Bus()
            obj.time = str(value.text)
        elif index % 4 == 0:
            obj.type = str(value.text)
        elif index % 4 == 1:
            obj.company = str(value.text)
        elif index % 4 == 2:
            obj.seats = str(value.text)
            arr.insert_bus(obj)

    for i in arr.bus_list:  # 출력 테스트용
        print(i.__dict__)