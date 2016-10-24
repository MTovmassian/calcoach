#!/usr/bin/env python3

import random, readline, sys

def prompt_f(string, sep=' ', gap=4, end=''):
	return (sep * gap) + end + string

def start():
	print(prompt_f("type A for addition"))
	print(prompt_f("type S for substraction"))
	print(prompt_f("type M for multiplication"))
	print(prompt_f("type Q for quit"))
	
	reader = readline.get_line_buffer()
	user_choice = input(prompt_f('', '>', 3, ' ') + reader).upper()
	if user_choice == 'A':
		train_add()
	elif user_choice == 'S':
		train_substract()
	elif user_choice == 'M':
		train_multiply()
	elif user_choice == 'Q':
		sys.exit(0)
	else:
		start()

def get_user_result(callback, i1, i2):
	reader = readline.get_line_buffer()
	user_result = input(prompt_f('', '>', 3, ' ') + reader)
	if user_result.upper() == 'Q':
		start()
	else:
		try:
			user_result = int(user_result)
			return user_result
		except ValueError:
			print(prompt_f('Please type a number...'))
			callback(i1, i2)

def check(math_result, user_result):
	if user_result == math_result:
		print(prompt_f(':) True!'))
	else:
		print(prompt_f(':( False...{0}'.format(math_result)))

def train_add(*args):

	while True:
		if len(args) == 0:
			i1, i2 = random.randrange(10, 100), random.randrange(10, 100)
		elif len(args) == 2:
			i1, i2 = args[0], args[1]
			args = ()
		
		print("-"*20)
		print(prompt_f("{0} + {1} =".format(i1, i2)))
		
		user_result = get_user_result(train_add, i1, i2)
		math_result = i1 + i2
		check(math_result, user_result)

def train_substract(*args):

	while True:
		if len(args) == 0:
			i1 = random.randrange(11, 100)
			i2 = random.randrange(10, i1)
		elif len(args) == 2:
			i1, i2 = args[0], args[1]
			args = ()
		
		print(prompt_f("{0} - {1} =".format(i1, i2)))
		
		user_result = get_user_result(train_substract, i1, i2)
		math_result = i1 - i2
		check(math_result, user_result)

def train_multiply(*args):

	while True:
		if len(args) == 0:
			i1, i2 = random.randrange(10, 100), random.randrange(2, 10)
		elif len(args) == 2:
			i1, i2 = args[0], args[1]
			args = ()
		
		print(prompt_f("{0} x {1} =".format(i1, i2)))
		
		user_result = get_user_result(train_multiply, i1, i2)
		math_result = i1 * i2
		check(math_result, user_result)


if __name__ == '__main__':
	start()

