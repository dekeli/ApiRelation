from ..api_call.xlc import XlcService
from ..public.Assert import Assertions




def test_commit_query_order():
    base = XlcService()
    data = {
	"serviceId": '',
	"brandId": 98,
	"brandName": "宝马",
	"carModel": "530Li",
	"dealerIdList": [3987],
	"displacement": "3.0L",
	"expectArriveTime": "2019-02-28 00:00:00",
	"garageArea": "",
	"garageName": "",
	"inquiryProductList": [{
		"createTime": "",
		"inquiryQuantity": 1,
		"productId": 10107184,
		"productModel": "",
		"productName": "电瓶"
	}],
	"invoiceStatus": 0,
	"isQualityBrand": 1,
	"isQualityOriginal": 1,
	"lineName": "5系",
	"modelName": "530Li"
}
    Assert_0 = Assertions()
    resp = base.commit_query_order(data=data)
    print(resp)
