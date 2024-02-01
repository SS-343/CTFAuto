#!/usr/bin/env python3
import sys
from pwn import *
banditHost = 'bandit.labs.overthewire.org'
banditPort = 2220


def solve_bandit0(banditPassword):
	s = ssh(host=banditHost, user='bandit0', password=banditPassword, port=banditPort)
	shell = s.run('cat readme')
	nextLevelPass = shell.recvall().decode()
	print("Bandit1 Password ->", nextLevelPass)
	s.close()
	return nextLevelPass

def solve_bandit1(pwd):
	s = ssh(host=banditHost, user='bandit1', password=pwd, port=banditPort)
	shell = s.run('cat ./-')
	nextLevelPass = shell.recvall().decode()
	print("Bandit2 Password ->",nextLevelPass)
	s.close()
	return nextLevelPass

def solve_bandit2(pwd):
	s = ssh(host=banditHost, user='bandit2', password=pwd, port=banditPort)
	shell = s.run('cat "spaces in this filename" ')
	nextLevelPass = shell.recvall().decode()
	print("Bandit3 Password ->", nextLevelPass)
	s.close()
	return nextLevelPass

def solve_bandit3(pwd):
	s = ssh(host=banditHost, user='bandit3', password=pwd, port=banditPort)
	shell = s.run('cd inhere && cat .hidden')
	nextLevelPass = shell.recvall().decode()
	print("Bandit3 Password ->", nextLevelPass)
	s.close()
	return nextLevelPass

def solve_allBandits():
	password=["bandit0"] #mutable list to add passwords
	password.append(str(solve_bandit0(password[0]).strip()))
	password.append(str(solve_bandit1(password[1]).strip()))
	password.append(str(solve_bandit2(password[2]).strip()))
	password.append(str(solve_bandit3(password[3]).strip()))

solve_allBandits()
