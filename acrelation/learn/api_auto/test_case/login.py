import requests

url = 'http://devapi.phc-dow.com/order/dealer/quotation/create'
headers = {"content-type":"application/json","token":"c9798d7e580c6f739b364893e3a8983f220d9ebc","LW_uid":"j1N5x5W019p3H5V7Z3M7B2D2B0"}
# data = {
# 	"inquiryId": 1119022408092,
# 	"quotationProducts": [{
# 		"productQuality": 1,
# 		"inquiryId": 1119022408092,
# 		"productName": "电瓶",
# 		"inquiryProductId": 1443,
# 		"productCode": "配件编码001",
# 		"productBrand": "宝马",
# 		"productModel": "规格型号1/0",
# 		"salePrice": "66",
# 		"arriveTime": 0,
# 		"activated": "",
# 		"warranty": "12"
# 	}, {
# 		"productQuality": 2,
# 		"inquiryId": 1119022403781,
# 		"productName": "电瓶",
# 		"inquiryProductId": 1443,
# 		"productCode": "配件编码002",
# 		"productBrand": "奔驰",
# 		"productModel": "规格型号2/0",
# 		"salePrice": "66",
# 		"arriveTime": 1,
# 		"activated": "",
# 		"warranty": "12"
# 	}],
# 	"garageId": 3802
# }
# resp = requests.post(url,json=data,headers=headers)
# print(resp.json())



data = {
	'code': 200,
	'body': {
		'data': {
			'id': 1119022600547,
			'carModel': '宝马 5系 530Li 3.0L',
			'companySnapshotId': 1877,
			'companyId': 3802,
			'expectArriveTime': '2019-02-28 00:00:00',
			'isQualityBrand': 1,
			'isQualityOriginal': 1,
			'invoiceStatus': 0,
			'createTime': '2019-02-26 22:48:12',
			'status': 0,
			'brandName': '宝马',
			'lineName': '5系',
			'modelName': '530Li',
			'displacement': '3.0L',
			'brandId': 98,
			'luxuryType': 0
		},
		'result': 0
	},
	'text': '{"data":{"id":1119022600547,"carModel":"宝马 5系 530Li 3.0L","companySnapshotId":1877,"companyId":3802,"expectArriveTime":"2019-02-28 00:00:00","isQualityBrand":1,"isQualityOriginal":1,"invoiceStatus":0,"createTime":"2019-02-26 22:48:12","status":0,"brandName":"宝马","lineName":"5系","modelName":"530Li","displacement":"3.0L","brandId":98,"luxuryType":0},"result":0}',
	'time_consuming': 179.903,
	'time_total': 0.179903
}

body = data.get("body")
data = body.get("data")
print(data.get("id"))
