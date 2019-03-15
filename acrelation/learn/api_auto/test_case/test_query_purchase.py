from ..api_call.qipei import QipeiService
from ..api_call.xlc import XlcService
from ..public.Assert import Assertions

class TestQueryPurchase():

    def test_query_purchase(self):
        # 生成询价单并获取询价单id
        query = XlcService()
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
        resp = query.commit_query_order(data=data)
        body = resp.get("body")
        data = body.get("data")
        inquiryId = data.get("id")
        quotate = QipeiService()
        data = {
	"inquiryId": inquiryId,
	"quotationProducts": [{
		"productQuality": 1,
		"inquiryId": 1119022408092,
		"productName": "电瓶",
		"inquiryProductId": 1443,
		"productCode": "配件编码001",
		"productBrand": "宝马",
		"productModel": "规格型号1/0",
		"salePrice": "66",
		"arriveTime": 0,
		"activated": "",
		"warranty": "12"
	}, {
		"productQuality": 2,
		"inquiryId": 1119022403781,
		"productName": "电瓶",
		"inquiryProductId": 1443,
		"productCode": "配件编码002",
		"productBrand": "奔驰",
		"productModel": "规格型号2/0",
		"salePrice": "66",
		"arriveTime": 1,
		"activated": "",
		"warranty": "12"
	}],
	"garageId": 3802
}
        resp = quotate.quotation(data=data)



query={
	"serviceId": null,
	"brandId": 52,
	"brandName": "奔驰",
	"carModel": "C 200 L",
	"dealerIdList": [3987, 3975],
	"displacement": "2.0T",
	"expectArriveTime": "2019-02-28 00:00:00",
	"garageArea": "",
	"garageName": "",
	"inquiryProductList": [{
		"createTime": "2019-01-25 15:04:54",
		"inquiryQuantity": 3,
		"productBrand": "",
		"productId": 10107191,
		"productModel": "",
		"productName": "方向盘"
	}],
	"invoiceStatus": 0,
	"isQualityBrand": 1,
	"isQualityOriginal": 1,
	"lineName": "C级",
	"modelName": "C 200 L",
	"picList": ["/group1/M00/00/8A/wKgETFx2iEmAXXO1AAG8Xk9Ry_8025.jpg", "/group1/M00/00/8A/wKgETFx2iE2AQYXQAAFecipeOD8715.jpg", "/group1/M00/00/8A/wKgETFx2iFGAQG0yAAGLPMHVFPY414.jpg"],
	"remark": "这是填写的备注信息"
}
quotation={
	"inquiryId": 1119022708284,
	"quotationProducts": [{
		"productQuality": 1,
		"inquiryId": 1119022708284,
		"productName": "方向盘",
		"inquiryProductId": 1608,
		"productCode": "配件编码668",
		"productBrand": "奔驰",
		"productModel": "规格型号0-2",
		"salePrice": "889",
		"arriveTime": 0,
		"activated": true,
		"warranty": "12"
	}, {
		"productQuality": 2,
		"inquiryId": 1119022708284,
		"productName": "方向盘",
		"inquiryProductId": 1608,
		"productCode": "配件编码688",
		"productBrand": "奔驰轿跑",
		"productModel": "规格型号-3",
		"salePrice": "889",
		"arriveTime": 0,
		"activated": true,
		"warranty": "24"
	}],
	"garageId": 3802
}
purchase={
	"inquiryId": 1119022708284,
	"province": "上海市",
	"city": "市辖区",
	"district": "浦东新区",
	"address": "张江镇张东路玉兰香苑四期143号1201",
	"contactName": "syq",
	"contactPhone": "15638743707",
	"dealerQuationList": [{
		"demanderRemark": "采购单其他要求",
		"quotationDetail2PurchaseList": [{
			"quantity": 3,
			"quotationId": 1219022702592,
			"quotationProductId": 1199
		}]
	}]
}
jiedan='http://devapi.phc-dow.com/order/dealer/purchase/1319022708420/confirm'
deliver={
	"deliverCertificate": "/group1/M00/00/8A/wKgETFx2jXyAC4hfAAGLPMHVFPY555.jpg",
	"expectedArrivalTime": "2019-02-28 11:00:00",
	"freight": "80",
	"freightPaymentType": 2,
	"logisticsCompanyName": "顺丰",
	"logisticsPhone": "15638743707",
	"supplierDeliverRemark": "这里是发货备注",
	"expressDate": "2019-02-28",
	"expressTime": "11:00"
}
receive='http://api.testxlc.bakheet.cn/order/garage/purchase/1319022708420/receive'