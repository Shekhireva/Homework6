# Working with dictionaries
my_dict= {'Denis': 2001, "Max": 2000, 'Anna': 1998, 'Egor': 1992}
print('Dict:',(my_dict))
print("Existing value:",(my_dict['Max']))
print('Not existing value:',(my_dict.get('Anton')))
my_dict.update({'Boris':1993, 'Sveta':2001})
a = my_dict.pop('Max')
print('Deleted value:',(a))
print('Modified dictonary:',(my_dict))


# Working with sets
my_set= {78,13,1,2,8,8,2,1,'Hi',True,8,2,78,8,'Hi',(3,4,6,7),False, 0,-1}
print('Set:',my_set)
my_set.add(-3)
my_set.add('Bye')
my_set.discard(78)
print('Modified set:', (my_set))

