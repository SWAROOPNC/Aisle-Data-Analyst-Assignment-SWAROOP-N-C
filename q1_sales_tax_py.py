class Constant(object):
    PARSE_DESCRIPTION_PATTERN = "(\d+)\s((imported\s)?\w+(\s\w+)*)\sat\s(\d+\.\d+)"
    COUNT_INDEX = 1
    NAME_INDEX = 2
    PRICE_INDEX = 5
    BOOK = ["book"]
    FOOD = ["chocolate bar", "box of chocolates"]
    MEDICAL = ["packet of headache pills"]
    BASE_TAXES = 0.1
    IMPORTED_TAXES = 0.05
    TAX_RATE_MIN_RANGE = 0.05
    IMPORTED_TEXT_IDENTIFY = "imported"
    SALES_TAXES_TEXT_IDENTIFY = "Sales Taxes: "
    TOTAL_TEXT_IDENTIFY = "Total: "

class NoTax:
    
    def __init__(self):
        pass

    def tax_rate(self, name):
        return 0

class BaseTax(NoTax):
    def tax_rate(self, name):
        return Constant.BASE_TAXES

class ImportedTax(NoTax):
    def tax_rate(self, name):
        return Constant.IMPORTED_TAXES

class TaxFactory:
    @staticmethod
    def build(name):
        taxes = [NoTax()]
        if TaxFactory.__item_not_in_exemptions_list(name):
            taxes.append(BaseTax())
        if TaxFactory.__item_is_imported(name):
            taxes.append(ImportedTax())
        return taxes

    @staticmethod
    def __item_not_in_exemptions_list(name):
        item_name = name.replace("%s " % Constant.IMPORTED_TEXT_IDENTIFY, "")
        return item_name not in Constant.BOOK + Constant.FOOD + Constant.MEDICAL

    @staticmethod
    def __item_is_imported(name):
        return Constant.IMPORTED_TEXT_IDENTIFY in name

class TaxRate():
    def __init__(self):
        pass

    def tax_rate(self, name):
        taxes = TaxFactory.build(name)
        tax_rate = 0
        for tax in taxes:
            tax_rate += tax.tax_rate(name)
        return tax_rate

import re

class Item:
    def __init__(self, description):
        match = re.search(Constant.PARSE_DESCRIPTION_PATTERN, description)
        self.count = match.group(Constant.COUNT_INDEX)
        self.name = match.group(Constant.NAME_INDEX)
        self.source_price = float(match.group(Constant.PRICE_INDEX))

    def sale(self):
        return str("%s %s: %.2f" % (self.count, self.name, self.price()))

    def tax(self):
        price = round(self.source_price * TaxRate().tax_rate(self.name), 2)
        mod = price % Constant.TAX_RATE_MIN_RANGE
        return price if mod == 0 else price + (Constant.TAX_RATE_MIN_RANGE - mod)

    def price(self):
        return round(self.source_price + self.tax(), 2)

class Items:
    def __init__(self, items):
        self.items = items

    def tax(self):
        tax = 0
        for item in self.items:
            tax += item.tax()
        return str((Constant.SALES_TAXES_TEXT_IDENTIFY + "%.2f") % tax)

    def total(self):
        total = 0
        for item in self.items:
            total += item.price()
        return str((Constant.TOTAL_TEXT_IDENTIFY + "%.2f") % total)

class ItemTestCase():
    def __init__(self):
        print("-------------------------------------------------------")
        n=int(input(" Enter number of items in the order = "))
        print("-------------------------------------------------------")

        il=[]
        ol=[]

        ip=[]
        op=[]

        for i in range(n):
            item = Item(input("  Enter item : "))
            il.append(item)
            ip.append(item.price()-item.tax())
            result = item.sale()
            ol.append(result)
            op.append(item.price())
        print("                                                       ")
        print(" ----------------------------------------------------- ")
        print("                  AISLE SUPER MARKET                   ")
        print(" ----------------------------------------------------- ")
        print("  244, 6th Cross, IndiraNagar II Stage, Hoysala Nagar  ")
        print('       Indiranagar, Bengaluru, Karnataka 560038        ')
        print(" ----------------------------------------------------- ")
        print("                     TAX - INVOICE                     ")
        print(" ----------------------------------------------------- ")
        print("  GSTIN : 24AISLE1206D1ZM         FSSAI:1152209123343  ")
        print(" ----------------------------------------------------- ")
        for k in ip:
            k=float(k)
        for m in op:
            m=float(m)
        #get date and time
        from datetime import datetime
        import pytz
        IST = pytz.timezone('Asia/Kolkata')
        datetime_ist = datetime.now(IST)
        print("         Date & Time : ",datetime_ist.strftime('%d-%m-%Y %H:%M:%S'),'           ')
        print(" ----------------------------------------------------- ")
        print("                    Items Description                  ")
        print(" ----------------------------------------------------- ")
        for g in ol :
            print('  ',g)
        taxable_amount=round(sum(ip),2)
        
        total=round(sum(op),2)
        
        salestax=round(total-taxable_amount,2)
        print(" ----------------------------------------------------- ")
        print("  Taxable Bill Amount :",taxable_amount)
        print(" ----------------------------------------------------- ")
        print("  Sales tax Applicable: ",salestax)
        print(" ----------------------------------------------------- ")
        print("  Total Payable Amount:",total)
        print(" ----------------------------------------------------- ")
        print("                       CASH PAID                       ")
        print(" ----------------------------------------------------- ")
        print("    This is Computer generated Bill,No sign required   ")
        print(" ----------------------------------------------------- ")      
        print("               Thank You, Visit Us Again               ")
        print(" ----------------------------------------------------- ")

TestCase1 = ItemTestCase()
