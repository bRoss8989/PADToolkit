# PAD-Toolkit
PrUn Adjusted Production Toolkit for the game prosperous universe.

Many modules for use in Jupyter or for other python apps.

PAD - adjusted production calculations for all combinations sourcing on-site or shipping in

Trade Finder - tests combinations of shipping requests to find the best route given a starting point, ending point, ship type, and days available.

Data source from FIO https://doc.fnar.net/#/

PIP torch, pymongo, pandas

pandas as pd, Pool as p, numpy as np

Update authexample and follow instructions inside file

Create file mongopw.py '/Modules/Storage/mongopw.py'
leave as below if you don't use auth or fill in if you are

mongopass = ''

db_addr = ''

Modules typically return full lists or dicts

natural_id's from in-game are used for nearly everything

for any unordered pair key the abc_gen is used to concat 2 inputs in abc order with _ between
