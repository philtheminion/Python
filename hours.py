#simple pay calculator, tax rate must be entered as decimal currently.

hrs = raw_input("Enter Hours:")
rate = raw_input("Enter Rate:")
tax = raw_input("Enter Tax Rate:")
earnings = float(hrs) * float(rate)
netpay = float(earnings) * float(tax)
takehome = float(earnings) - float(netpay)
print "Your expected take home pay is:" ,takehome
