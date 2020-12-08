#loop over list
#parse data into set?
#check if amount > $1000 - add to flagged array
#check time from previous transaction if current time - 60 >= previous time

def invalidTransactions(transactions):
    # first = transactions[0].split(',')
    # second = transactions[1].split(',')
    # print(first)
    name = []
    time = []
    amount = []
    city = []
    flagged = []
    for transaction in transactions:
        split_trans = transaction.split(',')
        name.append(split_trans[0])
        time.append(int(split_trans[1]))
        amount.append(int(split_trans[2]))
        city.append(split_trans[3])
    
    for idx_1, name_1 in enumerate(name):
        for idx_2, name_2 in enumerate(name):
            if name[idx_1] == name[idx_2]:
                if amount[idx_1] > 1000:
                    flagged.append(transactions[idx_1])
                    print('Flagged - amount!', transactions[idx_1])
                elif city[idx_1] != city[idx_2] and (time[idx_2] - time[idx_1] < 60):
                    flagged.append(transactions[idx_1])
                    print('Flagged - time!', transactions[idx_1])
    print(flagged)


invalidTransactions(["alice,20,800,mtv", "alice,50,100,beijing"])