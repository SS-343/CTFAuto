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
	print("Bandit4 Password ->", nextLevelPass)
	s.close()
	return nextLevelPass

def solve_bandit4(pwd):
	s = ssh(host=banditHost, user='bandit4', password=pwd, port=banditPort)
	shell = s.run('cd inhere && find ./ -type f -exec file {} \; | grep ASCII | cut -d: -f1 | xargs cat')
	nextLevelPass = shell.recvall().decode()
	print("Bandit5 Password ->", nextLevelPass)
	s.close()
	return nextLevelPass

def solve_bandit5(pwd):
	s = ssh(host=banditHost, user='bandit5', password=pwd, port=banditPort)
	shell = s.run('cd inhere && find ./ -type f -size 1033c -not -executable | cut -d: -f1 | xargs cat')
	nextLevelPass = shell.recvall().decode()
	print("Bandit6 Password ->", nextLevelPass)
	s.close()
	return nextLevelPass

def solve_bandit6(pwd):
        s = ssh(host=banditHost, user='bandit6', password=pwd, port=banditPort)
        shell = s.run('cd ../ && find / -group bandit6 -user bandit7 2>/dev/null | cut -d: -f1 | xargs cat')
        nextLevelPass = shell.recvall().decode()
        print("Bandit7 Password ->", nextLevelPass)
        s.close()
        return nextLevelPass

def solve_bandit7(pwd):
        s = ssh(host=banditHost, user='bandit7', password=pwd, port=banditPort)
        shell = s.run('cat data.txt | grep millionth | sed \'s/^[ \t]*//;s/[ \t]*$//;s/\bmillionth\b//\'')
        nextLevelPass = shell.recvall().decode()
        print("Bandit8 Password ->", nextLevelPass)
        s.close()
        return nextLevelPass



def solve_allBandits():
	password=["bandit0"] #mutable list to add passwords
	password.append(str(solve_bandit0(password[0]).strip()))
	password.append(str(solve_bandit1(password[1]).strip()))
	password.append(str(solve_bandit2(password[2]).strip()))
	password.append(str(solve_bandit3(password[3]).strip()))
	password.append(str(solve_bandit4(password[4]).strip()))
	password.append(str(solve_bandit5(password[5]).strip()))
	password.append(str(solve_bandit6(password[6]).strip()))
	password.append(str(solve_bandit7(password[7]).strip()))

solve_allBandits()
