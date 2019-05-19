# -*- coding:utf-8 -*-
"""
@author:goblinM
@date:2019-5-12
@describe:信息地域分布,颗粒度到市级，然后处理不是很好，有很多未识别的

"""
from collections import Counter

from app.web.db_utils.mongodb import MongoDBUtils

city_province = {

    "北京市": "北京",
    "上海市": "上海",
    "天津市": "天津",
    "重庆市": "重庆",
    "香港": "香港",
    "澳门": "澳门",
    "台湾": "台湾",

    "台北": "台湾",
    "高雄": "台湾",
    "台中": "台湾",
    "花莲": "台湾",
    "基隆": "台湾",
    "嘉义": "台湾",
    "金门": "台湾",
    "连江": "台湾",
    "苗栗": "台湾",
    "南投": "台湾",
    "澎湖": "台湾",
    "屏东": "台湾",
    "台东": "台湾",
    "台南": "台湾",
    "桃园": "台湾",
    "新竹": "台湾",
    "宜兰": "台湾",
    "云林": "台湾",
    "彰化": "台湾",

    "安徽": "安徽",
    "安庆市": "安徽",
    "蚌埠市": "安徽",
    "亳州市": "安徽",
    "巢湖市": "安徽",
    "池州市": "安徽",
    "滁州市": "安徽",
    "阜阳市": "安徽",
    "合肥市": "安徽",
    "淮北市": "安徽",
    "淮南市": "安徽",
    "黄山市": "安徽",
    "六安市": "安徽",
    "马鞍山市": "安徽",
    "铜陵市": "安徽",
    "芜湖市": "安徽",
    "宿州市": "安徽",
    "宣城市": "安徽",
    "福建": "福建",
    "福州市": "福建",
    "龙岩市": "福建",
    "南平市": "福建",
    "宁德市": "福建",
    "莆田市": "福建",
    "泉州市": "福建",
    "三明市": "福建",
    "厦门市": "福建",
    "漳州市": "福建",
    "甘肃": "甘肃",
    "白银市": "甘肃",
    "定西市": "甘肃",
    "甘南州": "甘肃",
    "嘉峪关市": "甘肃",
    "金昌市": "甘肃",
    "酒泉市": "甘肃",
    "兰州市": "甘肃",
    "临夏市": "甘肃",
    "陇南市": "甘肃",
    "平凉市": "甘肃",
    "庆阳市": "甘肃",
    "天水市": "甘肃",
    "武威市": "甘肃",
    "张掖市": "甘肃",
    "广东": "广东",
    "潮州市": "广东",
    "东莞市": "广东",
    "佛山市": "广东",
    "广州市": "广东",
    "河源市": "广东",
    "惠州市": "广东",
    "江门市": "广东",
    "揭阳市": "广东",
    "茂名市": "广东",
    "梅州市": "广东",
    "清远市": "广东",
    "汕头市": "广东",
    "汕尾市": "广东",
    "韶关市": "广东",
    "深圳市": "广东",
    "阳江市": "广东",
    "云浮市": "广东",
    "湛江市": "广东",
    "肇庆市": "广东",
    "中山市": "广东",
    "珠海市": "广东",
    "广西": "广西",
    "广西壮族自治区": "广西",
    "百色市": "广西",
    "北海市": "广西",
    "崇左市": "广西",
    "防城港市": "广西",
    "贵港市": "广西",
    "桂林市": "广西",
    "河池市": "广西",
    "贺州市": "广西",
    "来宾市": "广西",
    "柳州市": "广西",
    "南宁市": "广西",
    "钦州市": "广西",
    "梧州市": "广西",
    "玉林市": "广西",
    "贵州": "贵州",
    "安顺市": "贵州",
    "毕节地区": "贵州",
    "贵阳市": "贵州",
    "六盘水市": "贵州",
    "黔东南州": "贵州",
    "黔南州": "贵州",
    "黔西南州": "贵州",
    "铜仁地区": "贵州",
    "遵义市": "贵州",
    "海南": "海南",
    "澄迈市": "海南",
    "儋州市": "海南",
    "东方市": "海南",
    "海口市": "海南",
    "琼海市": "海南",
    "三亚市": "海南",
    "屯昌县": "海南",
    "万宁市": "海南",
    "文昌市": "海南",
    "五指山市": "海南",
    "河北": "河北",
    "保定市": "河北",
    "沧州市": "河北",
    "承德市": "河北",
    "邯郸市": "河北",
    "衡水市": "河北",
    "廊坊市": "河北",
    "秦皇岛市": "河北",
    "石家庄市": "河北",
    "唐山市": "河北",
    "邢台市": "河北",
    "张家口市": "河北",
    "河南": "河南",
    "安阳市": "河南",
    "鹤壁市": "河南",
    "焦作市": "河南",
    "开封市": "河南",
    "洛阳市": "河南",
    "漯河市": "河南",
    "南阳市": "河南",
    "平顶山市": "河南",
    "濮阳市": "河南",
    "三门峡市": "河南",
    "商丘市": "河南",
    "济源市": "河南",
    "新乡市": "河南",
    "信阳市": "河南",
    "许昌市": "河南",
    "郑州市": "河南",
    "周口市": "河南",
    "驻马店市": "河南",
    "黑龙江": "黑龙江",
    "大庆市": "黑龙江",
    "大兴安岭地区": "黑龙江",
    "哈尔滨市": "黑龙江",
    "鹤岗市": "黑龙江",
    "黑河市": "黑龙江",
    "鸡西市": "黑龙江",
    "佳木斯市": "黑龙江",
    "牡丹江市": "黑龙江",
    "齐齐哈尔市": "黑龙江",
    "七台河市": "黑龙江",
    "双鸭山市": "黑龙江",
    "绥化市": "黑龙江",
    "伊春市": "黑龙江",
    "湖北": "湖北",
    "鄂州市": "湖北",
    "恩施州": "湖北",
    "黄冈市": "湖北",
    "黄石市": "湖北",
    "荆门市": "湖北",
    "荆州市": "湖北",
    "潜江市": "湖北",
    "神农架林区": "湖北",
    "十堰市": "湖北",
    "随州市": "湖北",
    "武汉市": "湖北",
    "天门市": "湖北",
    "仙桃市": "湖北",
    "咸宁市": "湖北",
    "襄樊市": "湖北",
    "孝感市": "湖北",
    "宜昌市": "湖北",
    "湖南": "湖南",
    "常德市": "湖南",
    "长沙市": "湖南",
    "郴州市": "湖南",
    "衡阳市": "湖南",
    "怀化市": "湖南",
    "娄底市": "湖南",
    "邵阳市": "湖南",
    "湘潭市": "湖南",
    "湘西州": "湖南",
    "益阳市": "湖南",
    "永州市": "湖南",
    "岳阳市": "湖南",
    "张家界市": "湖南",
    "株洲市": "湖南",
    "吉林": "吉林",
    "白城市": "吉林",
    "白山市": "吉林",
    "长春市": "吉林",
    "吉林市": "吉林",
    "辽源市": "吉林",
    "四平市": "吉林",
    "松原市": "吉林",
    "通化市": "吉林",
    "延边州": "吉林",
    "江苏": "江苏",
    "常州市": "江苏",
    "淮安市": "江苏",
    "连云港市": "江苏",
    "南京市": "江苏",
    "南通市": "江苏",
    "苏州市": "江苏",
    "宿迁市": "江苏",
    "泰州市": "江苏",
    "无锡市": "江苏",
    "徐州市": "江苏",
    "盐城市": "江苏",
    "扬州市": "江苏",
    "镇江市": "江苏",
    "江西": "江西",
    "抚州市": "江西",
    "吉安市": "江西",
    "赣州市": "江西",
    "景德镇市": "江西",
    "九江市": "江西",
    "南昌市": "江西",
    "萍乡市": "江西",
    "上饶市": "江西",
    "新余市": "江西",
    "宜春市": "江西",
    "鹰潭市": "江西",
    "辽宁": "辽宁",
    "鞍山市": "辽宁",
    "本溪市": "辽宁",
    "朝阳市": "辽宁",
    "大连市": "辽宁",
    "丹东市": "辽宁",
    "抚顺市": "辽宁",
    "阜新市": "辽宁",
    "葫芦岛市": "辽宁",
    "锦州市": "辽宁",
    "辽阳市": "辽宁",
    "盘锦市": "辽宁",
    "沈阳市": "辽宁",
    "铁岭市": "辽宁",
    "营口市": "辽宁",
    "内蒙古": "内蒙古",
    "包头市": "内蒙古",
    "赤峰市": "内蒙古",
    "鄂尔多斯市": "内蒙古",
    "呼和浩特市": "内蒙古",
    "呼伦贝尔市": "内蒙古",
    "通辽市": "内蒙古",
    "乌海市": "内蒙古",
    "阿拉善盟": "内蒙古",
    "锡林郭勒盟": "内蒙古",
    "兴安盟": "内蒙古",
    "巴彦淖尔市": "内蒙古",
    "乌兰察布市": "内蒙古",
    "宁夏": "宁夏",
    "固原市": "宁夏",
    "石嘴山市": "宁夏",
    "吴忠市": "宁夏",
    "银川市": "宁夏",
    "中卫市": "宁夏",
    "青海": "青海",
    "果洛州": "青海",
    "海东地区": "青海",
    "海西州": "青海",
    "海北州": "青海",
    "海南州": "青海",
    "黄南州": "青海",
    "西宁市": "青海",
    "玉树州": "青海",
    "山东": "山东",
    "济南市": "山东",
    "滨州市": "山东",
    "德州市": "山东",
    "东营市": "山东",
    "菏泽市": "山东",
    "济宁市": "山东",
    "莱芜市": "山东",
    "聊城市": "山东",
    "临沂市": "山东",
    "青岛市": "山东",
    "日照市": "山东",
    "泰安市": "山东",
    "威海市": "山东",
    "潍坊市": "山东",
    "烟台市": "山东",
    "枣庄市": "山东",
    "淄博市": "山东",
    "山西": "山西",
    "长治市": "山西",
    "大同市": "山西",
    "晋城市": "山西",
    "晋中市": "山西",
    "临汾市": "山西",
    "吕梁市": "山西",
    "朔州市": "山西",
    "太原市": "山西",
    "忻州市": "山西",
    "阳泉市": "山西",
    "运城市": "山西",
    "陕西": "陕西",
    "安康市": "陕西",
    "宝鸡市": "陕西",
    "汉中市": "陕西",
    "商洛市": "陕西",
    "铜川市": "陕西",
    "渭南市": "陕西",
    "西安市": "陕西",
    "咸阳市": "陕西",
    "延安市": "陕西",
    "榆林市": "陕西",
    "四川": "四川",
    "阿坝州": "四川",
    "巴中市": "四川",
    "成都市": "四川",
    "达州市": "四川",
    "德阳市": "四川",
    "甘孜州": "四川",
    "广安市": "四川",
    "广元市": "四川",
    "乐山市": "四川",
    "凉山州": "四川",
    "泸州市": "四川",
    "眉山市": "四川",
    "绵阳市": "四川",
    "内江市": "四川",
    "南充市": "四川",
    "攀枝花市": "四川",
    "遂宁市": "四川",
    "雅安市": "四川",
    "宜宾市": "四川",
    "资阳市": "四川",
    "自贡市": "四川",
    "西藏": "西藏",
    "阿里地区": "西藏",
    "昌都地区": "西藏",
    "拉萨市": "西藏",
    "林芝地区": "西藏",
    "那曲地区": "西藏",
    "日喀则地区": "西藏",
    "山南地区": "西藏",
    "新疆": "新疆",
    "阿克苏地区": "新疆",
    "阿勒泰地区": "新疆",
    "巴音郭楞州": "新疆",
    "博尔塔拉州": "新疆",
    "昌吉州": "新疆",
    "哈密地区": "新疆",
    "和田地区": "新疆",
    "喀什地区": "新疆",
    "克拉玛依市": "新疆",
    "克孜勒苏柯州": "新疆",
    "塔城地区": "新疆",
    "吐鲁番地区": "新疆",
    "乌鲁木齐市": "新疆",
    "伊犁州": "新疆",
    "石河子市": "新疆",
    "阿拉尔市": "新疆",
    "云南": "云南",
    "保山市": "云南",
    "楚雄州": "云南",
    "大理州": "云南",
    "德宏州": "云南",
    "迪庆州": "云南",
    "红河州": "云南",
    "昆明市": "云南",
    "丽江市": "云南",
    "临沧市": "云南",
    "怒江州": "云南",
    "曲靖市": "云南",
    "思茅市": "云南",
    "文山州": "云南",
    "西双版纳州": "云南",
    "玉溪市": "云南",
    "昭通市": "云南",
    "浙江": "浙江",
    "杭州市": "浙江",
    "湖州市": "浙江",
    "嘉兴市": "浙江",
    "金华市": "浙江",
    "丽水市": "浙江",
    "宁波市": "浙江",
    "衢州市": "浙江",
    "绍兴市": "浙江",
    "台州市": "浙江",
    "温州市": "浙江",
    "舟山市": "浙江",

}

province_list = ["浙江", "云南", "新疆", "西藏", "四川", "陕西", "山西", "山东", "青海", "宁夏", "内蒙古", "辽宁", "江西", "江苏", "吉林", "湖南", "湖北",
                 "黑龙江", "河南", "河北", "海南", "贵州", "广西", "广东", "甘肃", "福建", "安徽", "台湾", "澳门", "香港", "重庆", "天津", "上海", "北京"]


class Location:
    def __init__(self, collectionName):
        self.mongo = MongoDBUtils(collectionName)

    def analysis(self):
        curInfo = self.mongo.distinctID("author.id")
        location_list = []
        local_mongo = MongoDBUtils("zhihu_user")
        for uid in curInfo:
            if uid != "0":
                curUser = local_mongo.searchByDoc({"_id": uid})[0]
                # 数据库有数据的
                if curUser:
                    if len(curUser.get("location")) == 0:
                        continue
                    else:
                        # location_list.extend([data.get("name") for data in curUser.get("location")])
                        for data in curUser.get("location"):
                            if data.get("name") in city_province.keys():
                                location_list.append(city_province.get(data.get("name")))
                            elif data.get("name") + "市" in city_province.keys():
                                location_list.append(city_province.get(data.get("name") + "市"))
                            # elif data.get("name")+"" in city_province.keys():
                            #     location_list.append(city_province.get(data.get("name")+""))
                            else:
                                # print(data.get("name"))
                                for reg in province_list:
                                    if reg in data.get("name"):
                                        location_list.append(reg + "")
                                location_list.append("其他")
                else:
                    # 数据库没有数据的记录下来
                    # with open('uid2.txt','a+',encoding='utf-8') as f:
                    #     f.write(uid + '\n')  # 加\n换行显示
                    pass

        location_dict = Counter(location_list)
        print(location_dict)
        location_data = []
        for k,v in dict(location_dict).items():
            location_data.append({
                "name":k,
                "value":v
            })
        return location_data


if __name__ == '__main__':
    obj = Location("zhihu_car")
    obj.analysis()
