'''4. A kindly teacher wishes to distribute a tub of sweets between her pupils. She will
 first count the sweets and then divide them according to how many pupils attend
 that day. Write a program that will tell the teacher how many sweets to give to each
 pupil, and how many she will have le over.'''

total_sweets = int(input("How many sweets? "))
total_pupils = int(input("How many pupils? "))
sweets_per_pupil = total_sweets // total_pupils
leftover = total_sweets % total_pupils
print("Each pupil will get", sweets_per_pupil, "sweets.")
print("There will be", leftover, "sweets left over.")