import pymysql

def insert_data(item):
    conn = pymysql.connect(host='localhost', user='af372', password='12sqec34',
                           db='af372', charset='utf8')

    curs = conn.cursor()
    sql = """insert into batter_stats1(G)
             values (%s)"""


    print(item[0])
    # print(item[1])

    # roster_id
    # season
    game = int(item[0])
    # pa
    # ab


    curs.execute(sql, (game))
    # curs.execute(sql, ('2', '이연수', '서울'))
    conn.commit()

    conn.close()