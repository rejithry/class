#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      rragha
#
# Created:     14/11/2012
# Copyright:   (c) rragha 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import copy

weight_dict = {'500 to 999 Lbs.' : '999', '100 Lbs. or more' : '999', '200 to 499 Lbs.':'499', '500 to 999 Lbs.':'999', '1000 Lbs. or more':'99999' }

def to_int(s):
    return int(s)

def weight_sort(weight_string):
    return float(weight_string.split(',')[0].replace('$',''))

def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text

def get_services(input_file):
    l_file = [i.replace('1,000','1000').replace(',','\t').replace('$','').replace('"','') for i in input_file]
    d_services = {}
    current_service = 'misc'
    d_services[current_service] = []
    l_services = []

    l_services.append(current_service)
    for i in range(len(l_file)):
        if 'UPS 3 Day Select Zones' in l_file[i]:
            service_name = 'UPS 3 Day Select'
            d_services[service_name] = [l_file[i].replace('UPS 3 Day Select','')]
            l_services.append(service_name)
            current_service = service_name
        elif 'UPS Ground Zones' in l_file[i]:
            service_name = 'UPS Ground'
            d_services[service_name] = [l_file[i].replace('UPS Ground','')]
            l_services.append(service_name)
            current_service = service_name
        elif 'UPS' in l_file[i] :
            d_services[l_file[i]] = []
            l_services.append(l_file[i])
            current_service = l_file[i]
        else:
            d_services[current_service].append(l_file[i])
    return d_services, l_services

def main():
    input_file = open('input.txt' , 'r')


    d_services, l_services = get_services(input_file)

    l_zones = []

    zone_charge= {}
    for service in l_services:
        if len(d_services[service]) > 0 and 'Zone'  in d_services[service][0]:
            pos = 0
            for i in d_services[service][0].split('\t'):
                if 'Zone' not in i:
                    charge =  [ d_services[service][j].split('\t')[0].strip() + '|' + d_services[service][j].split('\t')[pos].strip()  for j in range(len(d_services[service])) if j > 0 and d_services[service][j].split('\t')[pos].strip() ]
                    if len(charge) > 0:
                        if i.strip() not in zone_charge:
                            l_zones.append([i.strip(),service.strip().split('\t')[0]])
                            zone_charge[i.strip()] = {}
                        for l in charge:
                            zone_charge[i.strip()][l.split('|')[0]] = l.split('|')[1]
                pos += 1

    zone_charge_new  = copy.deepcopy(zone_charge)
    for i in zone_charge:
        if 'Minimum Charge' not in zone_charge[i]:
            zone_charge_new[i]['Minimum Charge'] = 0
    for z in range(len(l_zones)):
        i = l_zones[z]
        print i[1].strip() + ',' + i[0].strip() + ',' +  str(zone_charge_new[i[0]]['Minimum Charge']).strip()+ ',' +  ','.join(sorted([replace_all(j, weight_dict) + ',' + str(zone_charge_new[i[0]][j]) for j in zone_charge_new[i[0]] if j != 'Minimum Charge'], key=weight_sort))





if __name__ == '__main__':
    main()
