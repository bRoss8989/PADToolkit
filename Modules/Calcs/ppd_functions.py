
# takes the moria DW PPD and the inflation adjusted price from the game and prices all the PPD values given. can be 1 or numpy array 
def dw_model_fromppd(mor_dw_ppd, item_ppd, dw_price):
    priced = mor_dw_ppd / item_ppd
    return priced * dw_price

# does the opposite of the above given the same moria dw starting values
def ppd_from_dw_model(mor_dw_ppd, prices, dw_price):
    ppd = dw_price / prices
    return ppd * mor_dw_ppd

# takes ppd values and the quantities and returns the total days needed to provide
def days_from_ppd(ppd, quant):
    days = 1 / ppd
    return days * quant