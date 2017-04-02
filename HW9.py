#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 17:01:52 2017

@author: josephmiles
"""

import os
import collections
from prettytable import PrettyTable

class Repository:
    
    def __init__(self):
        self.student_list = list()
        self.instructor_list = list()
        
    def findUser(self, CWID):
        user_list = self.student_list + self.instructor_list
        for user in user_list:
            if user.CWID == CWID:
                return user
            
    
    def loadUserInfo(self, file_name, user_type):
        try:
            file = open(file_name, 'r')
        except FileNotFoundError:
            print('Can’t open,', file_name, 'current directory is', os.getcwd())
        else:
            for line in file:
                CWID, name, dept = line.strip().split('\t')  
                if user_type == 'S':
                    self.student_list.append(Student(CWID, name, dept))
                elif user_type == 'I':
                    self.instructor_list.append(Instructor(CWID, name, dept))
                
    def loadGrades(self, file_name):
        try:
            file = open(file_name, 'r')
        except FileNotFoundError:
            print('Can’t open,', file_name, 'current directory is', os.getcwd())
        else:
            for line in file:
                CWID, course_name, grade, i_CWID = line.strip().split('\t')
                self.findUser(CWID).classes_taken[course_name] = grade
                self.findUser(i_CWID).courses_taught[course_name] += 1
            
    def printRepo(self):
        print('Student Summary')
        table = PrettyTable()
        table.field_names = ['CWID', 'NAME', 'Completed Courses']
        table.align = 'l'
        for student in self.student_list:
            table.add_row([student.CWID, student.name, sorted((list(dict(student.classes_taken).keys())))])
        
        
        print('Instructor Summary')
        table2 = PrettyTable(['CWID', 'NAME', 'Dept', 'Courses', 'Students'])
        table2.align = 'l'
        for instructor in self.instructor_list:
            for course in instructor.courses_taught.keys():
                table2.add_row([instructor.CWID, instructor.name, instructor.dept, course, instructor.courses_taught[course]])
        print(table)
        print(table2)
                
            
class User:
    
    def __init__(self, _CWID, _name, _dept):
        self.CWID = _CWID
        self.name = _name
        self.dept = _dept
        
class Student(User):
    '''An extension of the User Class to create student objects'''
    def __init__(self, _CWID, _name, _dept):
        super(Student, self).__init__(_CWID, _name, _dept)
        self.classes_taken = collections.defaultdict(str)

class Instructor(User):
    '''An extension of the User Class to create instructor objects'''
    def __init__(self, _CWID, _name, _dept):
        super(Instructor,self).__init__(_CWID, _name, _dept)
        self.courses_taught = collections.defaultdict(int)

def main():
    repo = Repository()
    repo.loadUserInfo('instructors.txt', 'I');
    repo.loadUserInfo('students.txt', 'S');
    repo.loadGrades('grades.txt')
    repo.printRepo()
    
    
main()  
    
    