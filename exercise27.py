#!/usr/bin/env python

def print_bold(str):
    print '\033[1m' + str + '\033[0m'
    
def get_len(str):
   return (2 * (len(str))) 
    
def print_line(lenght):
    print "-" * lenght

def print_title(str, line_len):
   print_line(line_len)
   print_bold(str)
   print_line (line_len)
   
   
def print_truth_terms():
    list_truth_terms = """
    \t * and
    \t * or
    \t * not
    \t * != (not equal)
    \t * == (equal)
    \t * >= (greater-than-equal)
    \t * <= (less-than-equal)
    \t * True
    \t * False
    """
    print_bold ("The truth terms used in Python:")
    print list_truth_terms
    
def print_not_table():
    title = " \t THE 'NOT' TABLE "
    line_lenght = get_len(title)
    print_title(title, line_lenght)
    print "NOT       \t | \t True?"
    print_line(line_lenght)
    print "Not False \t | \t %s " % (not (False))
    print "Not True  \t | \t %s " % (not (True))
    print_line(line_lenght)
    print "\n"
    
def print_or_table():
    title = " \t THE 'OR' TABLE "
    line_lenght = get_len(title)
    print_title(title, line_lenght)
    print "OR             \t | \t True?"
    print_line (line_lenght)    
    print "True or False  \t | \t %s " % (True or False)
    print "True or True   \t | \t %s " % (True or True)
    print "False or True  \t | \t %s " % (False or True)
    print "False or False \t | \t %s " % (False or False)
    print_line(line_lenght)
    print "\n"
    
def print_nor_table():
    title = " \t THE 'NOR' TABLE "
    line_lenght = get_len(title)
    print_title(title, line_lenght)
    print "NOR             \t | \t True?"
    print_line (line_lenght)    
    print "not (True or False)  \t | \t %s " % (not (True or False))
    print "not (True or True)   \t | \t %s " % (not (True or True))
    print "not (False or True)  \t | \t %s " % (not (False or True))
    print "not (False or False) \t | \t %s " % (not (False or False))
    print_line(line_lenght)
    print "\n"
    
def print_and_table():
    title = " \t THE 'AND' TABLE "
    line_lenght = get_len(title)
    print_title(title, line_lenght)
    print "      AND       \t | \t True?"
    print_line (line_lenght)
    print "True and False  \t | \t %s " % (True and False)
    print "True and True   \t | \t %s " % (True and True)
    print "False and True  \t | \t %s " % (False and True)
    print "False and False \t | \t %s " % (False and False)
    print_line(line_lenght)
    print "\n"
    
def print_nand_table():
    title = " \t THE 'NAND' TABLE "
    line_lenght = get_len(title)
    print_title(title, line_lenght)
    print "      NOT AND       \t | \t True?"
    print_line (line_lenght)
    print "Not (True and False)  \t | \t %s " % (not (True and False))
    print "Not (True and True )  \t | \t %s " % (not (True and True))
    print "Not (False and True)  \t | \t %s " % (not (False and True))
    print "Not (False and False) \t | \t %s " % (not (False and False))
    print_line(line_lenght)
    print "\n"
    
def print_notequal_table():
    title = " \t THE '!=' TABLE "
    line_lenght = get_len(title)
    print_title(title, line_lenght)
    print "      !=       \t | \t True?"
    print_line (line_lenght)
    print "True != False  \t | \t %s " % (True != False)
    print "True != True   \t | \t %s " % (True != True)
    print "False != True  \t | \t %s " % (False != True)
    print "False != False \t | \t %s " % (False != False)
    print_line(line_lenght)
    print "\n"
    
def print_equal_table():
    title = " \t THE '==' TABLE "
    line_lenght = get_len(title)
    print_title(title, line_lenght)
    print "      ==       \t | \t True?"
    print_line (line_lenght)
    print "True == False  \t | \t %s " % (True == False)
    print "True == True   \t | \t %s " % (True == True)
    print "False == True  \t | \t %s " % (False == True)
    print "False == False \t | \t %s " % (False == False)
    print_line(line_lenght)
    print "\n"
    
def print_truth_tables():
    print_bold("The Truth Tables: \n")
    print_not_table()
    print_or_table()
    print_and_table()
    print_nand_table()
    print_nor_table()
    print_notequal_table()
    print_equal_table()
    
    
def main():
    print_truth_terms()
    print_truth_tables()
    

main()