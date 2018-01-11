###A
#annual_salary = float(input("Enter annual salary: "));
#portion_saved = float(input("Enter percent of salary to save, as a decimal: "));
#monthly_salary = annual_salary/12;
#total_cost = float(input("Enter cost of dream home: "));
#portion_down_payment = .25;
#current_savings = 0;
#r = 0.04;
#
#months = 0;
#while current_savings < total_cost*.25:
#    current_savings += current_savings*r/12;
#    current_savings += monthly_salary*portion_saved;
#    months += 1;
#print("Number of months:", months)



###B
#annual_salary = float(input("Enter annual salary: "));
#portion_saved = float(input("Enter percent of salary to save, as a decimal: "));
#monthly_salary = annual_salary/12;
#total_cost = float(input("Enter cost of dream home: "));
#portion_down_payment = .25;
#current_savings = 0;
#r = 0.04;
#semi_annual_raise = float(input("Enter semiannual raise: "))
#
#months = 0;
#while current_savings < total_cost*.25:
#    current_savings += current_savings*r/12;
#    current_savings += monthly_salary*portion_saved;
#    months += 1;
#    if months%6 == 0:
#        annual_salary += annual_salary*semi_annual_raise;
#        monthly_salary = annual_salary/12;
#print("Number of months:", months)



###C
salary = float(input("Enter annual salary: "));
annual_salary = salary;
monthly_salary = annual_salary/12;
total_cost = 1000000;
portion_down_payment = .25;
r = 0.04;
semi_annual_raise = .07;

portion_saved = .5;
search_steps = 0;
target = False;

while not target:
    current_savings = 0;
    annual_salary = salary;
    monthly_salary = annual_salary/12;
    search_steps += 1;
    months = 0;
    #print(portion_saved, search_steps);
    while current_savings < (total_cost*.25)-100 and months <= 40:
        current_savings += current_savings*r/12;
        current_savings += monthly_salary*portion_saved;
        months += 1;
        if months%6 == 0:
            annual_salary += annual_salary*semi_annual_raise;
            monthly_salary = annual_salary/12;
    #print(current_savings < (total_cost*.25)-100, months);
    if portion_saved > 2:
        print("Not possible");
        break;
    if months > 36:
        portion_saved += portion_saved/2;
        #print("too little")
    elif months < 36:
        portion_saved -= portion_saved/2;
        #print("too much")
    else:
        target = True;
        print("Rate:", portion_saved);
        print("Steps:", search_steps)
    portion_saved = int(round(portion_saved*10000))/10000;

#salary = float(input("Enter annual salary: "));
#annual_salary = salary;
#monthly_salary = annual_salary/12;
#total_cost = 1000000;
#portion_down_payment = .25;
#r = 0.04;
#semi_annual_raise = .07;
#
#portion_saved = float(input("Saved"));
#search_steps = 0;
#target = False;
#current_savings = 0;
#months = 0;
#
#while current_savings < (total_cost*.25)-100:
#        current_savings += current_savings*r/12;
#        current_savings += monthly_salary*portion_saved;
#        months += 1;
#        if months%6 == 0:
#            annual_salary += annual_salary*semi_annual_raise;
#            monthly_salary = annual_salary/12;
#print(current_savings < (total_cost*.25)-100, months);
