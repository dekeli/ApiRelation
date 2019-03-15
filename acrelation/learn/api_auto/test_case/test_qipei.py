from ..api_call.qipei import QipeiService

def test_quotation():
    base = QipeiService()
    data = {
	"inquiryId": 1119022408092,
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
    resp = base.quotation(data)
    print(resp)


    #
    # '{"inquiryId":1119022404161,"province":"上海市","city":"市辖区","district":"浦东新区","address":"张江镇张东路玉兰香苑四期143号1201","contactName":"syq","contactPhone":"15638743707","dealerQuationList":[{"quotationDetail2PurchaseList":[{"quantity":1,"quotationId":1219022409212,"quotationProductId":1173}]}]}'