#SPEND part ------- number of functions returning diferent values and saves it to varaibles'''

print("Удобный юнит фильтр/бумага/табак (40gr - пачка) это 5/6/10")


def count_fltr(price, pc):
    return price * pc

fl_price = int(input("оптовая цена за упаковку фильтров 120шт: "))
fl_pc = int(input("закуп: "))
#total money charge for filters'''
x_fltr = count_fltr(fl_price, fl_pc) 


def count_ppr(price, pc):
    return price * pc

pp_price = int(input("оптовая цена за упаковку бумаг 50шт: "))
pp_pc = int(input("закуп: "))
#total money charge for paper'''
x_ppr = count_ppr(pp_price, pp_pc)


def count_tbc(price, pc):
    return price * pc

tbc_price = int(input("оптовая цена за кг табака: "))
x127 = input("закуп: ")
tbc_pc = float(x127)
#total money charge for tobaco'''
x_tbc = count_tbc(tbc_price, tbc_pc)


def count_csprice(x1, x2, x3, x4, x5, x6):
    return (x1 / (x2 * 120)) + (x3 / (x4 * 50)) + (x5 / ((x6 / 25) * 60))
#charged for 1 cig in your stack'''
cs_spnt = count_csprice(x_fltr, fl_pc, x_ppr, pp_pc, x_tbc, tbc_pc) 
#total money charged for your stack'''
ttl_spnt = x_fltr + x_ppr + x_tbc

#INCOME part'''

def countFilter(inf_pr, inf_pc):
    return inf_pr * inf_pc

inc_ra_fl = int(input("цена продажи за пачку фильтров: "))
y_fltr = countFilter(inc_ra_fl, fl_pc)
     

def countPapper(inf_pr, inf_pc):
    return inf_pr * inf_pc

inc_ra_pp = int(input("бумаги: "))
y_pp = countPapper(inc_ra_pp, pp_pc)


def countTobacco(inf_pr, inf_pc):
    return inf_pr * inf_pc

inc_ra_tbc = int(input("табака за пачку 40 гр: "))
y_tbc = countTobacco(inc_ra_tbc, tbc_pc)

#total income'''
ttl_inc = y_fltr + y_pp + y_tbc
Cln_inc = ttl_inc -ttl_spnt

cs_pr = (y_fltr / (fl_pc * 120)) + (y_pp / (pp_pc * 50)) + (y_tbc / ((tbc_pc / 25) * 60))

print("чистая прибыль:", Cln_inc, "\nстоимость 1 самокрутки для клиента:", cs_pr, "\nцена за 20 готовых самокруток:", cs_pr * 20)