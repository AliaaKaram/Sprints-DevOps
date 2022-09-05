def get_mean (*args):
   integers_list = []
   float_list = []
   No_Type = 0
   mean_value = 0
   even_number = 0
   max_number = 0
   sum_value = 0
   for i in args:
	   if (type(i)== type(1)):
		   integers_list.append(i)

	   elif (type(i)==type(1.5)):
		   float_list.append(i)

	   else:
		   No_Type = No_Type +1

   if (No_Type == len(args)):
       output_2 = "The List doesn't contain neither int nor float"
       return output_2

   for k in integers_list:
		  if k%2 == 0:
			  sum_value = sum_value + k
			  even_number = even_number +1
   for z in float_list:
		   if z >= max_number:
			   max_number = z
   mean_value = sum_value/even_number
   output = "The mean value of even integer numbers = " + str(mean_value) + '\n'+\
            " and The max number of float point numbers = " + str(max_number) + '\n'

   return output

print(get_mean(1,2,3,20,40,22,3.7,9.0,10.11))

