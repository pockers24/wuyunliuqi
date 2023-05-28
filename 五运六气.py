import os

tiangan_list = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
dizhi_list = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']

sitian_zaiquan_table = {
    "子午": {
        "司天": "少阴君火",
        "在泉": "阳明燥金"
    },
    "丑未": {
        "司天": "太阴湿土",
        "在泉": "太阳寒水"
    },
    "寅申": {
        "司天": "少阳相火",
        "在泉": "厥阴风木"
    },
    "卯酉": {
        "司天": "阳明燥金",
        "在泉": "少阴君火"
    },
    "辰戌": {
        "司天": "太阳寒水",
        "在泉": "太阴湿土"
    },
    "已亥": {
        "司天": "厥阴风木",
        "在泉": "少阳相火"
    }
}

zhuqi_table = {
    "厥阴风木": "1月21日到3月20日",
    "少阴君火": "3月21日到5月20日",
    "少阳相火": "5月21日到7月20日",
    "太阴湿土": "7月21日到9月20日",
    "阳明燥金": "9月21日到11月20日",
    "太阳寒水": "11月21日到1月20日",

}


def caculate_ganzhi(year):
    special_tiangan_list = ['庚', '辛', '壬', '癸', '甲', '乙', '丙', '丁', '戊', '己']
    special_dizhi_list = ['申', '酉', '戌', '亥', '子', '丑', '寅', '卯', '辰', '巳', '午', '未', ]
    if year <= 0:
        raise Exception(f'year {year} not valid')
    gan_index = year % 10
    zhi_index = year % 12
    return "{}{}".format(special_tiangan_list[gan_index], special_dizhi_list[zhi_index])


def calulate_wuyun(ganzhi):
    tiangan = ganzhi[0]
    wuyun_list = ['土', '金', '水', '木', '火']
    index = tiangan_list.index(tiangan)
    wuyun_index = index % 5
    wuyun_info = wuyun_list[wuyun_index] + "运"
    wuyun_strengh = "太过" if index % 2 == 0 else "不及"
    return wuyun_info + wuyun_strengh


def caculate_keqi(ganzhi):
    dizhi = ganzhi[1]

    sitian = None
    zaiquan = None
    for key in sitian_zaiquan_table.keys():
        if dizhi in key:
            sitian = sitian_zaiquan_table[key]['司天']
            zaiquan = sitian_zaiquan_table[key]['在泉']
    if not sitian or not zaiquan:
        raise Exception(f"get keqi for {ganzhi} failed")

    keqi_list = ['厥阴风木', '少阴君火', '太阴湿土', '少阳相火', '阳明燥金', '太阳寒水']
    sitian_index = keqi_list.index(sitian)
    zaiquan_index = keqi_list.index(zaiquan)

    final_keqi_list = []
    keqi_start_index = sitian_index - 2
    if keqi_start_index < 0:
        keqi_start_index = len(keqi_list) + keqi_start_index

    for index in range(len(keqi_list)):
        if keqi_start_index >= len(keqi_list):
            keqi_start_index = keqi_start_index - len(keqi_list)
        final_keqi_list.append(keqi_list[keqi_start_index])
        keqi_start_index += 1

    return final_keqi_list


if __name__ == '__main__':
    test_year = 2023
    ganzhi = caculate_ganzhi(test_year)
    print(f"干支:{ganzhi}")
    ret_wuyun = calulate_wuyun(ganzhi)
    print(f"五运:{ret_wuyun}")
    print(f"主气: {zhuqi_table}")
    ret_keqi = caculate_keqi(ganzhi)
    print(f"客气:{ret_keqi}")
