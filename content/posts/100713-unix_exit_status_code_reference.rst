Unix Exit Status Code Reference
###############################

:date: 2010-07-13 19:51
:category: Code


I always find myself constantly Googling the list of unix status
codes (typically defined in ``sysexits.h``). ::

    0 # successful termination 64 # base value for error messages
    64 # command line usage error
    65 # data format error
    66 # cannot open input
    67 # addressee unknown
    68 # host name unknown
    69 # service unavailable
    70 # internal software error
    71 # system error (e.g., can't fork)
    72 # critical OS file missing
    73 # can't create (user) output file
    74 # input/output error
    75 # temp failure; user is invited to retry
    76 # remote error in protocol
    77 # permission denied
    78 # configuration error
