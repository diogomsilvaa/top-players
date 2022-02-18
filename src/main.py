import dataCollection as dc

transferMarkt = dc.TransferMarkt()
transferMarkt.init_browser()
print(transferMarkt.top200())
