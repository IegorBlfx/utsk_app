M1 = 1
M2 = 2
M3 = 3
M4 = 4
M5 = 5
M6 = 6
M7 = 7
M8 = 8
M9 = 9
M10 = 10
M11 = 11
M12 = 12

LENGTH = (
    (M1, '1'),
    (M2, '2'),
    (M3, '3'),
    (M4, '4'),
    (M5, '5'),
    (M6, '6'),
    (M7, '7'),
    (M8, '8'),
    (M9, '9'),
    (M10, '10'),
    (M11, '11'),
    (M12, '12'),
    )

######################################################3

TN = 1
M = 2
POSL = 3

UNITS = (
    (TN, 'tn'),
    (M, 'm'),
    (POSL, 'posluga')
)
###############################################################

GOST_8732 = 1
GOST_8734 = 2
GOST_10705 = 3
GOST_10706 = 4
TU_UV_ON_Profile = 5

STANDARDS = (
    (GOST_8732, 'GOST 8732'),
    (GOST_8734, 'GOST 8734'),
    (GOST_10705, 'GOST 10705'),
    (GOST_10706, 'GOST 10706'),
    (TU_UV_ON_Profile, 'TU UV  2.7 , 2.4.45')
)

############################################################

st20 = 1
st35 = 2
st45 = 3
st09G2S = 4

STEEL = (
    (st20 , 'steel 20'),
    (st35 , 'steel 35'),
    (st09G2S,'steel 09G2S'),
)

####################################################
TOV = 1
FOP = 2
PP = 3
ZAT = 4

OWNERSHIP = (
    (TOV,'TOV'),
    (FOP, 'FOP'),
    (PP, 'PP'),
    (ZAT, 'ZAT')
)

######################################################################################
CONTRACT_SUPPLY = 1
CONTRACT_SELL = 2

CONTRACT = (
    (CONTRACT_SUPPLY, 'Supply'),
    (CONTRACT_SELL, 'Sells'),
)
############################################################################################
UTSK = 1
PIF = 2
FPST = 3

COMPANY = (
    (UTSK, 'Ugtransstroycompect'),
    (PIF, 'Pifagor'),
    (FPST, 'Forpost'),
)

###############################################################################################
NDS_20 = 1
NDS_5 = 2
NDS_0 = 3

NDS = (
    (NDS_20, '20%'),
    (NDS_5, '5%'),
    (NDS_0 , '0%')
)

############################################################################################
UAH = 1
USD = 2
EUR = 3

CURRENCY = (
    (UAH, 'UAH'),
    (USD, 'USD'),
    (EUR, 'EUR')
)

#########################################################################################
SAT = 1
DELIVERY = 2
CAR = 3

TRANSPORT_TYPE = (
    (SAT, ' Sat'),
    (DELIVERY, 'Delivery'),
    (CAR, 'Car')
)

MERSEDES = 1
ZIL = 2
MAZ = 3
GAZEL = 4

TRANSPORT_MARK = (
    (MERSEDES, 'Mers'),
    (ZIL, 'Zil'),
    (MAZ, 'Maz'),
    (GAZEL, 'Gazel')
)