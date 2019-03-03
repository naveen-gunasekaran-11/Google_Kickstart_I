# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 15:36:59 2019

@author: Naveen Gunasekaran
"""
import itertools
#input_file = "C-small-practice.in";
input_file = "C-large-practice.in";
#input_file = "test.in";
output_file = "large_solution.txt";
file_in = open (input_file, "r");
file_out = open (output_file, "w");

line = file_in.readline();
no_test_cases = int(line);
test_case_no = 1;
while no_test_cases != 0:
    line = "";
    flight_list = [];
    flight_dict = {};
    ticket_dict = {};
    order_dict = {};
    source = "";
    destination = "";
    prob_list = [];
    line = file_in.readline();
    no_of_flights = int(line);
    
    for i in range (0, no_of_flights * 2):
        line = file_in.readline();
        for i in line.split():
            flight_list.append (i);
    
    ticket_dict = dict(itertools.zip_longest(*[iter(flight_list)] * 2, fillvalue=""));
    
    for items in flight_list:
        if items in flight_dict:
            flight_dict [items] = flight_dict [items] + 1;
        else:
            flight_dict[items] = 1;
    
    for flight_name in flight_dict.keys():
        if flight_dict[flight_name] == 1:
            prob_list.append(flight_name);

    if len(prob_list) == 2:
        if prob_list[0] in ticket_dict:
            source = prob_list[0];
            destination = prob_list[1];
        else:
            source = prob_list[1];
            destination = prob_list[0];  
    else:
        print ("something wrong occured");
    
    search_term = source;
    
    while search_term != destination:
        if search_term in ticket_dict:
            order_dict[search_term] = ticket_dict[search_term];
            search_term = ticket_dict[search_term];
    
    file_out.write("Case #" + str(test_case_no) + ": ");
    for keys,values in order_dict.items():
        file_out.write (keys + "-" + values);
        file_out.write (" ");
    file_out.write ("\n");
    test_case_no = test_case_no + 1;
    no_test_cases = no_test_cases - 1;
  

file_in.close();
file_out.close();
