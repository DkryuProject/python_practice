import pymysql
from openpyxl import Workbook
from openpyxl import load_workbook
from datetime import datetime
from send_email import send_po_list

today = datetime.today().strftime("%Y-%m-%d")

print('PO List start ('+today+')')
#1. 커넥터로부터 커넥션을 받는다.
db = pymysql.connect(host="13.250.231.108", user="brandpo", password="@U5x2#tpv8@", db="brandpo", charset="utf8")

try:
    print('DB connection success')
    db_info = db.get_server_info()
 
    #2. 커서를 가져온다
    cursor = db.cursor()
 
    #3. 우리가 원하는거 실행 가능
    query = '''select
               b2.name as 'buyer'
              ,bb.name as 'brand'
              ,bm.designNumber as 'designNo'
              ,CONCAT(tsp.name ,' ',bm.seasonYear ) as 'season'
              ,spo.`number` as 'poNo'
              ,ttp.name as 'payment'
              ,s2.name as 'supplier'
              ,case when spoi.materialFabricMetaId is not null then 'FABRIC' else'SUBSIDIARY' end as 'category'
              ,IFNULL(mfm.millArticle,msm.millArticle) as 'millArticle'
              ,case when spoi.materialFabricMetaId is not null then
              concat((select GROUP_CONCAT(concat(mfc.rate,'% ',
              (select name from type_fabric_content tfc where tfc.id=mfc.typeFabricContentId)) SEPARATOR ', ')
              from material_fabric_content mfc where mfc.materialFabricMetaId=mfm.id), ' ', (select tgc2.name from type_material_color tgc2 where tgc2.id=spoi.typeMaterialColorId))
               else '' end 'fabricDetails'
              ,case when spoi.materialSubsidiaryMetaId is not null then (select tsis.name from type_subsidiary_item_size tsis where tsis.id=spoi.typeSubsidiaryItemSizeId ) else '' end 'size'
              ,spoi.purchaseQuantity as 'qty'
              ,(select tc.name from type_currency tc where tc.id = spo.typeCurrencyId) as 'currency'
              ,spoi.price as 'unitPrice'
              ,spoi.purchaseQuantity*spoi.price as 'amount'
              ,spo.dateExMill as 'exmill'
              ,spo.deliveryStartDate as 'deliveryDate'
              ,spo.dateInHouse as 'dateInHouse'
              ,spoi.status as 'status'
              ,CONCAT(m2.firstName,' ',m2.lastName) as 'createdBy'
              ,IFNULL(spo.releaseTimestamp, spo.`timestamp`) as 'timeStamp'
              ,(select mla.code from member_location_address mla, scl_material_fabric smf where mla.id=smf.memberLocationAddressId and smf.sclId=s.id limit 1) as 'factory'
        from supplier_purchase_order_item spoi
        inner join supplier_purchase_order spo on spoi.supplierPurchaseOrderId=spo.id
        inner join supplier_purchase_order_published spop on spop.id=spo.supplierPurchaseOrderPublishedId
        inner join member2 m2 on spo.memberId = m2.id
        inner join supplier s2 on spo.supplierId = s2.id
        inner join type_term_payment ttp on spo.typeTermPaymentId = ttp.id
        inner join scl s on spoi.sclId = s.id
        inner join bom_meta bm on s.bomMetaId = bm.id
        inner join buyer_brand bb on bb.id = bm.buyerBrandId
        inner join buyer b2 on bb.buyerId = b2.id
        inner join type_season_prefix tsp on bm.typeSeasonPrefixId = tsp.id
        left outer join material_fabric_meta mfm on spoi.materialFabricMetaId = mfm.id
        left outer join material_subsidiary_meta msm on spoi.materialSubsidiaryMetaId = msm.id
        where DATE(IFNULL(spop.releaseTimestamp, spop.`timestamp`))>=DATE_SUB(NOW(), INTERVAL 7 DAY)
        order by spo.id desc;'''  
    cursor.execute(query)
    # db.commit() 
    # 셀렉트에는 커밋이 없다.
    record = cursor.fetchall()
    
    #엑셀 생성
    wb = Workbook()
    ws = wb.active
    
    #엑셀 첫행
    ws.append(("BUYER", "BRAND", "DESIGN#", "SEASON+YEAR", "PO#", "PAYMENT",
                "SUPPLIER", "CATEGORY", "MILL ARTICLE#", "FABRIC DETAILS", "SIZE",
                "QTY", "CURRENCY", "UNIT PRICE", "AMOUNT", "EXMILL DATE", "DELIVERY START DATE",
                "DATE IN HOUSE", "STATUS", "Created By", "Time Stamp", "FACTORY ALLOCATION"))
    #DB 데이터 엑셀 저장
    for row in record:
        ws.append(row)
    #wb.save('test.xlsx')
    
    #DB 데이터 출력    
    # for data in record:
    #     print(data)    

    send_po_list(wb)
    
except Exception as e:
    print('error: ',e)
    
finally :
    #5. 커넥션을 모두 닫아줌.
    db.close()
    wb.close()
    print('PO List end ('+today+')')