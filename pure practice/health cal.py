def health_cal(age,apples_ate,cig_smoked):
    answer=(100-age)+(apples_ate * 3.5 ) - (cig_smoked *2)
    print(answer)
bucky_data=[27,20,0]
health_cal(bucky_data[0],bucky_data[1],bucky_data[2])
health_cal(*bucky_data)