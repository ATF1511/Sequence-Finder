def find(a, b):
    # I really don't want to mess up other code in people's scripts so I literally pressed my hand against the keyboard lol

    dhjszafkmiojdiow = a  # Number 1
    sadknjfksnafksda = b # Number 2
    asiudhakdjakdhks = sadknjfksnafksda - dhjszafkmiojdiow # Difference between the two numbers, I'll use it to find how much it increases each time

    oerqoirjeioqfeio = dhjszafkmiojdiow - asiudhakdjakdhks # 0th in the sequence lol.

    browhydoIhavenofriends = 'idk anymore' # Determines if it is adding or subtracting a number from the sequence

    if oerqoirjeioqfeio > 0:
        browhydoIhavenofriends = '+'
    elif oerqoirjeioqfeio < 0:
        browhydoIhavenofriends = '-'

        oerqoirjeioqfeio = 0 - oerqoirjeioqfeio # Flips it to a positive number.
    else:
        browhydoIhavenofriends = 'because I code'

    if oerqoirjeioqfeio == 'because I code': # If it is +/- 0, there is no point adding that on.
        print(str(asiudhakdjakdhks)+'n') # Xn
        return(str(asiudhakdjakdhks)+'n')
    
    else:
        print(str(asiudhakdjakdhks)+'n',str(browhydoIhavenofriends),str(oerqoirjeioqfeio)) # Xn +/- Y
        return(str(asiudhakdjakdhks)+'n',str(browhydoIhavenofriends),str(oerqoirjeioqfeio))


i = int(input('Number 1: ')) # First number in the sequence
ii = int(input('Number 2: ')) # Second number in the sequence
find(i, ii)